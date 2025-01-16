# Necessary Imports
import os
import json
import importlib
import pandas as pd

# RAGAS Imports
from ragas import EvaluationDataset
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas import evaluate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Config File 
from config import LLM_METRICS, DATA_FILE


### 1. Evaluation Loaders ###

# OpenAI API
if LLM_METRICS['OpenAI_API']:
    os.environ["OPENAI_API_KEY"] = LLM_METRICS['OpenAI_API']
else:
    raise ValueError("OpenAI API key not found in LLM_BASED_METRICS.")

#Evaluator loaders
evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model=LLM_METRICS['OpenAI_Model']))
evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

# Evaluation Libraries Loaders
def evaluate_metric(dataset, metric):
    print(metric)
    ragas_metric = getattr(importlib.import_module('ragas.metrics'),metric)
    res = evaluate(dataset=dataset,metrics = [ragas_metric()], llm = evaluator_llm)
    return res


### 2. Dataset Loaders ###

# Datafile Loader
with open(DATA_FILE, mode='r', encoding='utf-8') as infile:
    data = json.load(infile)

#data = data[:10] 
dataset = EvaluationDataset.from_list(data) 



### 3. LLM Based Evalutation ###

evaluation_results = []

if LLM_METRICS:
    for metric, metric_class in LLM_METRICS.items():
        if metric_class is True:
            evaluation_results.append(evaluate_metric(dataset, metric))
    


### 4. Saving Results in results.json file ###

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
with open('scores.json', 'w') as json_file:
    json.dump(output_json, json_file, indent=4)

print("Results saved to scores.json")

