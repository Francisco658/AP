import streamlit as st
import argparse
import base64
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

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local LLM with RAG with Ollama.")
    parser.add_argument(
        "-r",
        "--reload",
        action="store_true",
        default=False,
        help="If provided, Embeddings will be reloaded. Otherwise(default), they are read from the Vector Database.",
    )
    return parser.parse_args()

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
        .stApp{
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
        }
        [data-testid="stBottom"] > div {
            background: transparent;
        }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)

    input_style = """
    <style>
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  // This changes the text color inside the input box
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)
    return

def setup():
    st.set_page_config(page_title='FitBot', page_icon="📊", initial_sidebar_state="expanded", layout='wide')
    st.sidebar.image("../Images/fitbot2.png")

def main(reload: bool):
    setup()
    set_background_image("../Images/background.png")
    st.sidebar.header("Settings")
    reload_embedings = st.sidebar.checkbox("Reload Embeddings",True)
    llm_model_name = st.sidebar.selectbox("LLM Model Name", ["mistral","llama2","zephyr"],0)
    embedding_model_name = "nomic-embed-text"
    documents_path = "../Final PDF Files"

    # Check to see if the models available, if not attempt to pull them
    try:
        check_if_model_is_available(llm_model_name)
        check_if_model_is_available(embedding_model_name)
    except Exception as e:
        st.error(e)
        st.stop()

    if reload_embedings:
        try:
            db = load_documents_into_database(embedding_model_name, documents_path)
        except FileNotFoundError as e:
            st.error(e)
            st.stop()
    else:
        db = Chroma(persist_directory=documents_path, embedding_function=OllamaEmbeddings(model=llm_model_name))

    llm = Ollama(model=llm_model_name)
    chat = getChatChain(llm, db)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Message FitBot"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            response = chat(prompt)
            st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    args = parse_arguments()
    main(args.reload)