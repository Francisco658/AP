import streamlit as st
from models import check_if_model_is_available
from document_loader import load_documents
from llm import getChatChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from llm import getChatChain

TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def load_documents_into_database(model_name: str, documents_path: str) -> Chroma:
    print("Loading documents")
    raw_documents = load_documents(documents_path)
    documents = TEXT_SPLITTER.split_documents(raw_documents)

    print("Creating embeddings and loading documents into Chroma")
    db = Chroma.from_documents(
        documents,
        OllamaEmbeddings(model=model_name),
    )
    return db

def main(llm_model_name: str, embedding_model_name: str, documents_path: str) -> None:
    # Check to see if the models available, if not attempt to pull them
    try:
        check_if_model_is_available(llm_model_name)
        check_if_model_is_available(embedding_model_name)
    except Exception as e:
        st.error(e)
        st.stop()

    # Creating database from documents
    try:
        db = load_documents_into_database(embedding_model_name, documents_path)
    except FileNotFoundError as e:
        st.error(e)
        st.stop()

    llm = Ollama(model=llm_model_name)
    chat = getChatChain(llm, db)

    if "question_key" not in st.session_state:
        st.session_state.question_key = 0

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    def ask_question(question_key):
        user_input = st.text_input(
            f"Hello! How can I help you?",
            key=f"input_{question_key}"
        )

        if user_input.strip().lower() == "exit":
            st.stop()

        if st.button(f"Submit", key=f"button_{question_key}"):
            with st.spinner("Generating response..."):
                try:
                    response = chat(user_input.strip())
                    for message in st.session_state.consersation:
                        st.write(message)
                    st.write(response)
                    st.session_state.conversation.append((user_input.strip(), response))  # Save conversation
                    st.session_state.question_key += 1  # Update question key
                    ask_question(question_key + 1)  # Recursive call to ask the next question
                except KeyboardInterrupt:
                    st.stop()

    ask_question(st.session_state.question_key)

def main_streamlit():
    st.title("WorkoutWizard")

    st.sidebar.header("Settings")
    llm_model_name = st.sidebar.text_input("LLM Model Name", "mistral")

    main(llm_model_name, "nomic-embed-text", "../Final PDF Files")

if __name__ == "__main__":
    main_streamlit()