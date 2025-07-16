import os
from dotenv import load_dotenv

load_dotenv()

VECTOR_DB_PATH = "chroma_db"

WEB_URL = "YOUR_URL"

EMBEDDING_MODEL_NAME = "YOUR_MODEL_PATH"

GOOGLE_API_KEY = os.getenv("API_KEY")

RETRIEVER_K = 3

CHUNK_SIZE = 1500
CHUNK_OVERLAP = 150
