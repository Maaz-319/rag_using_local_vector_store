from config import VECTOR_DB_PATH, EMBEDDING_MODEL_NAME, RETRIEVER_K
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_retriever():
    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectordb = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedding_model)
    return vectordb.as_retriever(search_kwargs={"k": RETRIEVER_K})
