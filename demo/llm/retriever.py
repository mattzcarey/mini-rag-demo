import os
import tempfile

import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import BedrockEmbeddings, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from demo.constants.settings import SETTINGS


@st.cache_resource(ttl="1h")
def configure_retriever(uploaded_files, embeddings_provider):
    # Read documents
    docs = []
    temp_dir = tempfile.TemporaryDirectory()
    for file in uploaded_files:
        temp_filepath = os.path.join(temp_dir.name, file.name)
        with open(temp_filepath, "wb") as f:
            f.write(file.getvalue())
        loader = PyPDFLoader(temp_filepath)
        docs.extend(loader.load())

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # Embeddings
    if embeddings_provider == "openai":
        embeddings = OpenAIEmbeddings(openai_api_key=SETTINGS.openai_api_key.get_secret_value())
    elif embeddings_provider == "bedrock":
        embeddings = BedrockEmbeddings(region_name="us-east-1") # type: ignore
    else:
        raise ValueError(f"Unknown embeddings provider: {embeddings_provider}")

    # Store in vectordb
    vector_db = Chroma.from_documents(splits, embeddings)

    # Define retriever
    retriever = vector_db.as_retriever()

    return retriever