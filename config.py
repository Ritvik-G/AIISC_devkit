# LLM-based metrics (RAGAS Only)
LLM_METRICS = {
    "OpenAI_Model" : "gpt-4o",
    "OpenAI_API" : "<Paste your API key here>",
    "LLMContextPrecisionWithoutReference" : False,
    "LLMContextPrecisionWithReference" : False,
    "LLMContextRecall" : True,
    "ContextEntityRecall" : False,
    "NoiseSensitivity" : False,
    "ResponseRelevancy" : True,
    "Faithfulness" : True,
}

# Quantitative metrics
METRICS = {
    "bleu" : True, 
    "rouge" : True, 
    "meteor" : True, 
    "nubia" : True,
}

# Data file path
DATA_FILE = "data.json"
