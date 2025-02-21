# Necessary Imports
import os
import json
import importlib
import pandas as pd
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Non-LLM Imports
import evaluate as hf_eval

# RAGAS Imports
from ragas import EvaluationDataset
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas import evaluate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Config File 
from config import LLM_METRICS, DATA_FILE, METRICS


### 1. Evaluation & Dataset Loaders ###

# OpenAI API
if LLM_METRICS['OpenAI_API']:
    os.environ["OPENAI_API_KEY"] = LLM_METRICS['OpenAI_API']
else:
    raise ValueError("OpenAI API key not found in LLM_BASED_METRICS.")

# Evaluator loaders
evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model=LLM_METRICS['OpenAI_Model']))
evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

# RAGAS evaluation library loaders
def ragas_evaluate_metric(dataset, metric):
    print(metric)
    ragas_metric = getattr(importlib.import_module('ragas.metrics'), metric)
    res = evaluate(dataset=dataset, metrics=[ragas_metric()], llm=evaluator_llm)
    return res

# Define RoBERTa NLI score function
def roberta_nli_score(sentence1, sentence2, model, tokenizer):
    # Tokenize the input
    inputs = tokenizer(sentence1, sentence2, return_tensors="pt", truncation=True)
    # Get model predictions
    with torch.no_grad():
        logits = model(**inputs).logits
    # Convert logits to probabilities (softmax)
    probs = torch.nn.functional.softmax(logits, dim=-1)
    # Extract probabilities for entailment, contradiction, and neutral
    entailment_prob = probs[:, 2].item()
    contradiction_prob = probs[:, 0].item()
    neutral_prob = probs[:, 1].item()
    return {
        "Entailment Score": entailment_prob,
        "Contradiction Score": contradiction_prob,
        "Neutral Score": neutral_prob
    }

# HuggingFace evaluation library loaders
def nonllm_evaluate_metric(data, metric):
    print(metric)
    scores = []
    if metric == 'roberta-nli':
        # Load the RoBERTa-large-mnli model and tokenizer once
        model_name = "roberta-large-mnli"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        for i in data:
            score = roberta_nli_score(i['reference'], i['response'], model, tokenizer)
            scores.append(score)
    else:
        eval_metric = hf_eval.load(metric)
        for i in data:
            score = eval_metric.compute(references=[[i['reference']]], predictions=[i['response']])
            scores.append(score)
    return scores


# Dataset Loaders 
# Datafile Loader
with open(DATA_FILE, mode='r', encoding='utf-8') as infile:
    data = json.load(infile)

# data = data[:10] 
dataset = EvaluationDataset.from_list(data) 




### 2. LLM Based Evaluation ###

evaluation_results = []

if LLM_METRICS:
    for metric, metric_class in LLM_METRICS.items():
        if metric_class is True:
            evaluation_results.append(ragas_evaluate_metric(dataset, metric))

if evaluation_results:
    # Scores Dataframe
    df = pd.DataFrame(evaluation_results)
    scores = df['scores']

    # Json file creation
    def create_json(scores):
        input_json = scores.values.tolist()
        transformed_result = {"scores": []}
        
        transposed = zip(*input_json)
        
        for group in transposed:
            score_entry = {}
            for item in group:
                score_entry.update(item) 
            transformed_result["scores"].append(score_entry)
        
        return transformed_result


    output_json = create_json(scores)

    # Write the transformed JSON to the file
    output_file = "ragas_scores.json"
    with open(output_file, 'w') as json_file:
        json.dump(output_json, json_file, indent=4)

    print(f"Metrics results saved to {output_file}")




### 3. Non-LLM Based Evaluation ###

metrics_results = []

if METRICS:
    for metric, metric_class in METRICS.items():
        if metric_class is True:
            metrics_results.append(nonllm_evaluate_metric(data, metric))

# Combining to form a json file
def combine_metrics_results(metrics_results):
    num_data_points = len(metrics_results[0])
    combined_data = []
    
    # Loop over each data point and combine the corresponding metrics from each metric set
    for i in range(num_data_points):
        combined_row = {}
        for metric_set in metrics_results:
            combined_row.update(metric_set[i])  # Merge corresponding data point's metrics
        combined_data.append(combined_row)
    
    return combined_data

if metrics_results:
    # Combine the metrics
    combined_data = combine_metrics_results(metrics_results)

    # Write to a JSON file
    output_file = "quant_scores.json"
    with open(output_file, "w") as f:
        json.dump(combined_data, f, indent=4)

    print(f"Metrics results saved to {output_file}")
