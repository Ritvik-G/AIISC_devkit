# Toggle any of the boolean values to True for activation of the metric's run on your dataset

# LLM-based metrics (RAGAS Only)
LLM_METRICS = {
    "OpenAI_API" : "<Paste your API key here>",
    "OpenAI_Model" : "gpt-4o",
    "LLMContextPrecisionWithoutReference" : False,
    "LLMContextPrecisionWithReference" : True,
    "LLMContextRecall" : True,
    "ContextEntityRecall" : False,
    "NoiseSensitivity" : False,
    "ResponseRelevancy" : True,
    "Faithfulness" : True,
}

# Non-LLM-based metrics
METRICS = {
    "bleu" : True, 
    "rouge" : True, 
    "meteor" : True, 
    "nubia" : True,
}

# Data file path
DATA_FILE = "data.json"
