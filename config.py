# Configuration file for evaluation metrics in the RAGAS framework only for RAG and Natural Language Comparison metrics. Others, yet to apply.

# LLM-based metrics (RAGAS Only)
LLM_METRICS = {
    "OpenAI_API" : "<Paste your API key here>",
    "OpenAI_Model" : "gpt-4o",
    "LLMContextPrecisionWithoutReference" : False,
    "LLMContextPrecisionWithReference" : True,
    "LLMContextRecall" : False,
    "ContextEntityRecall" : True,
    "NoiseSensitivity" : True,
    "ResponseRelevancy" : False,
    "Faithfulness" : True,
}

# Non-LLM-based metrics
METRICS = {
    "NonLLMContextPrecisionWithReference" : False, # RAG
    "NonLLMContextRecall" : False, # RAG
    "NonLLMStringSimilarity" : True, # Traditional NLP Metrics (NLC)
    "BleuScore" : True, # Traditional NLP Metrics (NLC)
    "RougeScore" : True, # Traditional NLP Metrics (NLC)
    "ExactMatch" : True, # Traditional NLP Metrics (NLC)
    "StringPresence" : True,
}

# Data file path
DATA_FILE = "data.json"
