# Marketing Secrets Podcast AI Chatbot

This script is designed to perform intelligent queries on a set of documents, particularly podcast episodes from Marketing Secrets by Russell Brunson. It utilizes machine learning models to generate summaries, topics, and titles for each document, and then allows you to run a query to retrieve relevant information.

## Prerequisites

- **Python 3.x**
- **LLamaCpp and HuggingFace Models:**: Ensure these models are downloaded and the paths are correctly set in the script.

## Dependencies

Before running the script, you need to install the required Python packages. You can do this using pip:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```
python main.py --query "your_question_here"
```

## Arguments

- --query or -q: The question you want to ask referring to the Marketing Secrets podcast. (Required)

## Notes

- Make sure the paths to the LLamaCpp and HuggingFace models are correctly set in the **MODEL_PATH** and **LLM_PATH** variables.
- The script will generate .pkl files for each document containing metadata like summaries and topics.
- The script uses Qdrant for vector storage and retrieval.

## Disclaimer

This script is intended for educational and research purposes. Always ensure you have the right to use and distribute the content you are querying.
