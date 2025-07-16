# Practicing RAG Using Local Vector Store

A Retrieval-Augmented Generation (RAG) application that uses a local vector store to answer questions about the Milky Way Galaxy. Combines document retrieval with Google's Gemini language model to provide accurate, context-aware responses.

## Features

- **Local Vector Storage**: Uses ChromaDB for efficient document storage and retrieval
- **AI-Powered Q&A**: Integrates Google's Gemini 2.5 Flash model for intelligent responses
- **Web Document Loading**: Tried Automatic load and process web content
- **Interactive Chat Interface**: Tried Both command-line and GUI application
- **Context-Aware**: conversation history for better responses

## Project Structure

```
rag_using_local_vector_store/
├── app.py                  # Command-line chat application
├── chat_app.py            # GUI chat application using ttkbootstrap
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── chains/
│   └── qa_chain.py       # Question-answering chain implementation
├── embeddings/
│   └── embedder.py       # Document embedding and vector store creation
├── prompts/
│   └── prompt.py         # Custom prompt templates
├── retrieval/
│   └── retriever.py      # Document retrieval logic
└── utils/
    └── history.py        # Chat history formatting utilities
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Maaz-319/rag_using_local_vector_store.git
   cd rag_using_local_vector_store
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   API_KEY=your_google_api_key_here
   ```

4. **Configure the application**:
   Edit `config.py` to set your specific parameters:
   ```python
   WEB_URL = "YOUR_URL"  # URL of the content to load
   EMBEDDING_MODEL_NAME = "YOUR_MODEL_PATH"  # HuggingFace embedding model
   ```

## Configuration

The application uses several configurable parameters in `config.py`:

- `VECTOR_DB_PATH`: Directory for storing the ChromaDB vector database
- `WEB_URL`: Source URL for document loading
- `EMBEDDING_MODEL_NAME`: HuggingFace embedding model identifier
- `RETRIEVER_K`: Number of relevant documents to retrieve (default: 3)
- `CHUNK_SIZE`: Document chunk size for processing (default: 1500)
- `CHUNK_OVERLAP`: Overlap between document chunks (default: 150)

## Usage

### Command-Line Interface

Run the basic chat application:
```bash
python app.py
```

This will start an interactive session where you can ask questions about the Milky Way.

### GUI Application

Launch the graphical user interface:
```bash
python chat_app.py
```

## How It Works

1. **Document Loading**: Web content is loaded using LangChain's WebBaseLoader
2. **Text Splitting**: Documents are split into chunks using RecursiveCharacterTextSplitter
3. **Embedding Generation**: HuggingFace embeddings convert text chunks to vectors
4. **Vector Storage**: ChromaDB stores the embeddings locally for fast retrieval
5. **Query Processing**: User questions are embedded and matched against stored documents
6. **Response Generation**: Google Gemini generates responses using retrieved context

## Dependencies

- `langchain`: Framework for LLM applications
- `langchain-google-genai`: Google Gemini integration
- `langchain-huggingface`: HuggingFace embeddings
- `chromadb`: Vector database for document storage
- `ttkbootstrap`: Modern Tkinter UI framework
- `python-dotenv`: Environment variable management

## API Keys

You'll need a Google API key to use the Gemini language model:

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Add it to your `.env` file as `API_KEY=your_key_here`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Maaz Bin Asif** - [Maaz-319](https://github.com/Maaz-319)
**My Website** - [maaz.me](https://maaz.me)

---