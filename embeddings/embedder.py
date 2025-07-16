from config import WEB_URL, CHUNK_SIZE, CHUNK_OVERLAP, VECTOR_DB_PATH, EMBEDDING_MODEL_NAME
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_vectorstore():
    loader = WebBaseLoader(WEB_URL)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    splits = splitter.split_documents(docs)

    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectordb = Chroma.from_documents(splits, embedding_model, persist_directory=VECTOR_DB_PATH)
    vectordb.persist()
    return vectordb
