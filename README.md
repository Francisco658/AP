# Deep Learning - FitBot Project

The FitBot Project consists of developing a chatbot using Ollama LLM's and the integration of RAG to create a chatbot that creates Workout and Nutritional Plans based on Scientific Studies. It also gives tips to specific exercises and meals according to the user's goals.

## Team Members

- **PG50380** - Francisco Claudino
- **PG53597** - Afonso Bessa
- **PG54213** - Rui Silva

## Index of Contents

### `src`: Contains the Source Code of the Project

- **`app.py`**: Contains the core chatbot implementation using Ollama LLM's.
- **`document_loader.py`**: Contains the script for loading the PDF files to the database.
- **`evaluate.csv`**: Contains the Test Dataset for the evaluation of the LLM Models.
- **`evaluate.ipynb`**: Contains the Jupyter Notebook for evaluating the LLM Models.
- **`extract_pdfplumber.py`**: Contains the code for extracting raw text from PDF files using PDFPlumber.
- **`streamlit.py`**: Main script to run the chatbot on a Web Based Application.
- **`llm.py`**: Contains the prompts and the chain build with the RAG Framework.
- **`models.py`**: Contains code that verifies and downloads the LLM Models if not present in the local machine.
- **`py2pdf.py`**: Contains the code for extracting raw text from PDF files using Py2PDF.
- **`requirements.txt`**: Contains the tools necessary to run the project.
- **`Stats.csv`**: Contains the Dataset that aggregates the ratings of the models achieved in **`evaluate.ipynb`**.
- **`stats.py`**: Contains the script for visualizing the performance of the LLM models in a Streamlit Web Application.
- **`tesseract.py`**: Contains the code for extracting raw text from PDF files using Tesseract.
- **`txt_converter.py`**: Contains the code that applies lowercase to the txt file provided.
- **`txt_to_pdf.py`**: Contains the code that transforms a txt file to a PDF file.

#### `Embeddings`: Contains the vector embeddings of the LLM Models.

#### `Final PDF Files`: Contains the PDF files, converted from the txt files, that are loaded to the Database to be used by the LLM Models.

#### `Images`: Contains the images used to build the Web Application of the model.

#### `PDF Files`: Contains the initial PDF files, before the cleaning process.

#### `TXT Files`: Contains the txt files that were extracted from the PDF Files.

## Setup :
1. Create a virtual environment in python.
2. Install the required Python packages by running `pip install -r requirements.txt` on your virtual environment.

## Running the Project

**Note:** The first time you run the project, it will download the necessary models from Ollama for the LLM and embeddings. This is a one-time setup process and may take some time depending on your internet connection.

1. Ensure your virtual environment is activated.
2. Run the main script with `python app.py -m <model_name> -p <path_to_documents> - r <reload_embeddings>` to specify a model, the path to documents and if you want the vector embeddings to be processed oe not. If no model is specified, it defaults to [mistral](https://ollama.com/library/mistral). If no path is specified, it defaults to `Final PDF Files`. If no information about the reload of the embeddings is specified, it defaults to True and it will reload the embeddings.
3. Optionally, you can specify the embedding model to use with `-e <embedding_model_name>`. If not specified, it defaults to [nomic-embed-text](https://ollama.com/library/nomic-embed-text).
4. To run the web application simply run `streamlit run streamlit.py`.
5. To run the performance tests, run the Jupyter Notebook **`evaluate.ipynb`**.
6. To see the graphics made with the evaluation of the models, run `streamlit run stats.py`.


## Technologies Used

- [Langchain](https://github.com/langchain/langchain): A Python library for working with Large Language Model
- [Ollama](https://ollama.ai/): A platform for running Large Language models locally.
- [Chroma](https://docs.trychroma.com/): A vector database for storing and retrieving embeddings.
- [PDFPlumber](https://pypi.org/project/PyPDF2/](https://pypi.org/project/pdfplumber/0.1.2/)): A Python library for reading and manipulating PDF files.
- [Streamlit](https://streamlit.io): A Python Library to build Web Based Applications.
