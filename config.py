# LLM-based metrics (RAGAS Only)
LLM_METRICS = {
    "OpenAI_API" : "<Paste your API key here>",
    "OpenAI_Model" : "gpt-4o",
    "LLMContextPrecisionWithoutReference" : False,
    "LLMContextPrecisionWithReference" : False,
    "LLMContextRecall" : False,
    "ContextEntityRecall" : False,
    "NoiseSensitivity" : False,
    "ResponseRelevancy" : False,
    "Faithfulness" : False,
}

# Quantitative metrics
METRICS = {
    "bleu" : True, 
    "rouge" : True, 
    "meteor" : True, 
    "roberta-nli" : True,
}

# Data file path
DATA_FILE = "data.json"
