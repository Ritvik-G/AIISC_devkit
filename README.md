# LLM Evaluation Using RAGAS

## Overview
This project evaluates language model responses using the RAGAS (RAG and NLP Evaluation Metrics) framework. 
The evaluation process involves loading a dataset from a JSON file, evaluating various metrics, and then saving the results in a `scores.json` file.

## Requirements

- Python 3.7+
- Git
- OpenAI API Key (for LLM-based metrics)

## Installation

### 1. Clone the repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/Ritvik-G/AIISC_devkit.git
cd AIISC_devkit
```

### 2. Install dependencies

This project requires the following python packages. Install them using `pip`:

```bash
pip install ragas pandas evaluate nubia-score rouge_score
```

### 3. Set up the configuration

1. **Obtain your OpenAI API Key**:
   - If you don’t have an OpenAI API key, you can get one from [OpenAI](https://beta.openai.com/signup/).

2. **Configure your metrics**:
   - Open the `config.py` file and replace the placeholder in `LLM_METRICS['OpenAI_API']` with your actual OpenAI API key.
   - Set your desired model in `LLM_METRICS['OpenAI_Model']`, for example, `"gpt-4"`.
   - Toggle the metrics to either True or False depending on the necessity.
   - **NOTE** - Generic Metrics (Bleu, Rouge) are still under development. 

   Example:

   ```python
   LLM_METRICS = {
       "OpenAI_API": "your-openai-api-key",
       "OpenAI_Model": "gpt-4",
       "LLMContextPrecisionWithoutReference": False,
       "LLMContextPrecisionWithReference": True,
       "LLMContextRecall": False,
       "ContextEntityRecall": True,
       "NoiseSensitivity": True,
       "ResponseRelevancy": False,
       "Faithfulness": True,
   }
   ```

3. **Prepare the dataset**:
   - The dataset is expected to be in the `data.json` format. Modify or create your own `data.json` file with a similar structure. You can refer to the example in the `data.json` file in the repository.
   - You can edit the location of the dataset file by just pasting the path of your data file in ``DATA_FILE`` line in ``Config.py``.

## Running the Evaluation

After configuring your API key and the `config.py` file, you can run the `main.py` script to evaluate the LLM using the specified metrics.

### 1. Run the script

To start the evaluation, simply execute the `main.py` file:

```bash
python main.py
```

This will:

- Load the data from `data.json`.
- Load the LLM-based and non-LLM-based evaluation metrics as specified in `config.py`.
- Perform evaluation based on the active metrics.
- Save the results in a new `scores.json` file in the current directory.

### 2. Output

The results will be saved to a `scores.json` file. The results are structured as a list of metrics with their corresponding scores.

## Folder Structure

```plaintext
llm-evaluation/
│
├── main.py              # Main evaluation script
├── config.py            # Configuration file for setting up LLM-based metrics
├── data.json            # Input dataset for evaluation
└── scores.json          # Output results file 
```

## Troubleshooting

- **OpenAI API key not working**: Ensure that the OpenAI API key is correctly set in the `config.py` file. If you're using a proxy, verify the proxy settings.
- **Data format issues**: Ensure the `data.json` file follows the correct format with the necessary fields like `user_input`, `retrieved_contexts`, `response`, and `reference`.
- **Missing dependencies**: If there are missing dependencies, ensure you have correctly installed the packages using `pip`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
