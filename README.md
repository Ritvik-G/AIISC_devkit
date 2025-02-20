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
### 2. Creating a Virtual Environment
Prior to installing the requirements, it is recommended to create a virtual environment to avoid any dependency clashes.

In your terminal or command prompt, run the following command to create a virtual environment:
```bash
python -m venv myenv
```

Activate the virtual environment using the following script
```bash
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
```

### 3. Install dependencies

This project requires the following python packages. Install them using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set up the configuration

1. **Prepare the dataset**:
   - The dataset is expected to be in the `data.json` format. Modify or create your own `data.json` file with a similar structure. You can refer to the example in the `data.json` file in the repository.
   - You can edit the location of the dataset file by just pasting the path of your data file in ``DATA_FILE`` line in ``Config.py``.

**NOTE** - There are two different types of metrics available and here's how you setup for both of them:
  
2. **RAGAS**
   - **Obtain your OpenAI API Key**: If you don’t have an OpenAI API key, you can get one from [OpenAI](https://beta.openai.com/signup/).
   - Open the `config.py` file and replace the placeholder in `LLM_METRICS['OpenAI_API']` with your actual OpenAI API key.
   - Set your desired model in `LLM_METRICS['OpenAI_Model']`, for example, `"gpt-4"`.
   - Toggle the metrics to either True or False depending on the necessity.
   - Please install `ragas` using the pip command given in section 2.
     
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
3. **Quantitative Metrics**
   - Toggle the metrics to either True or False depending on the necessity (similar to LLM_Metrics).
     
   ```python
   METRICS = {
       "bleu" : True, 
       "rouge" : True, 
       "meteor" : True, 
       "roberta-nli" : True,
   }
   ```
   

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
The results will be saved in two different files: 
1. `ragas_scores.json` : All RAGAS based scores would be available here.
2. `quant_scores.json` : All Quantitative based scores would be available here.

## Folder Structure

```plaintext
llm-evaluation/
│
├── main.py                # Main evaluation script
├── config.py              # Configuration file for setting up LLM-based metrics
├── data.json              # Input dataset for evaluation
├── ragas_scores.json      # RAGAS framework outputs
└── quant_scores.json      # Quantitative metrics outputs
```

## Troubleshooting

- **OpenAI API key not working**: Ensure that the OpenAI API key is correctly set in the `config.py` file. If you're using a proxy, verify the proxy settings.
- **Data format issues**: Ensure the `data.json` file follows the correct format with the necessary fields like `user_input`, `retrieved_contexts`, `response`, and `reference`.
- **Missing dependencies**: If there are missing dependencies, ensure you have correctly installed the packages using `pip`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
