from langchain_community.llms import Ollama
from langchain.evaluation import load_evaluator
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from models import check_if_model_is_available
from document_loader import load_documents
import argparse
import sys
import pandas as pd
from llm import getChatChain

TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def load_documents_into_database(model_name: str, documents_path: str, reload: bool) -> Chroma:
    """
    Loads documents from the specified directory into the Chroma database
    after splitting the text into chunks.

    Returns:
        Chroma: The Chroma database with loaded documents.
    """

    print("Loading documents")
    raw_documents = load_documents(documents_path)
    documents = TEXT_SPLITTER.split_documents(raw_documents)

    if reload:
        print("Creating embeddings and loading documents into Chroma")
        db = Chroma.from_documents(
            documents=documents,
            embedding=OllamaEmbeddings(model=model_name),
            persist_directory="../Embeddings",
        )
        db.persist()
    else:
        db = Chroma(persist_directory="../Embeddings", embedding_function=OllamaEmbeddings(model=model_name))
    
    return db

def evalute(llm_model_name: str, db: Chroma):
    accuracy_criteria = {
    "accuracy": """
        Score 1: The answer is completely unrelated to the reference.
        Score 3: The answer has minor relevance but does not align with the reference.
        Score 5: The answer has moderate relevance but contains inaccuracies.
        Score 7: The answer aligns with the reference but has minor errors or omissions.
        Score 10: The answer is completely accurate and aligns perfectly with the reference."""
    }

    evaluator = load_evaluator(
        "labeled_score_string",
        criteria=accuracy_criteria,
        llm=Ollama(model=llm_model_name),
    )

    chat = getChatChain(Ollama(model=llm_model_name), db)
    df = pd.read_csv("evaluate.csv")

    for index,row in df.iterrows():
        question = row['question']
        answer = row['answer']
        evaluation = evaluator.evaluate_strings(prediction=chat(question=question),reference=answer,input=question)
        print(evaluation)

def main(llm_model_name: str, embedding_model_name: str, documents_path: str) -> None:
    # Check to see if the models available, if not attempt to pull them
    try:
        check_if_model_is_available(llm_model_name)
        check_if_model_is_available(embedding_model_name)
    except Exception as e:
        print(e)
        sys.exit()

    # Creating database form documents
    try:
        db = load_documents_into_database(embedding_model_name, documents_path,True)
    except FileNotFoundError as e:
        print(e)
        sys.exit()

    # Initialize LLM and chat chain
    llm = Ollama(model=llm_model_name)
    chat = getChatChain(llm, db)

    #evalute(llm_model_name,db)

    # Start the conversation loop
    while True:
        try:
            user_input = input("\n\nPlease enter your question (or type 'exit' to end): ")
            if user_input.lower() == "exit":
                break

            chat(user_input)
        except KeyboardInterrupt:
            break

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local LLM with RAG with Ollama.")
    parser.add_argument(
        "-m",
        "--model",
        default="mistral",
        help="The name of the LLM model to use.",
    )
    parser.add_argument(
        "-e",
        "--embedding_model",
        default="nomic-embed-text",
        help="The name of the embedding model to use.",
    )
    parser.add_argument(
        "-p",
        "--path",
        default="../Final PDF Files",
        help="The path to the directory containing documents to load.",
    )
    parser.add_argument(
        "-r",
        "--reload",
        action="store_true",
        default=False,
        help="If provided, Embeddings will be reloaded. Otherwise(default), they are read from the Vector Database.",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    main(args.model, args.embedding_model, args.path)