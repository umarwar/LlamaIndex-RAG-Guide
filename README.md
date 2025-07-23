# LlamaIndex: Data Indexing and Retrieval for RAG

This project demonstrates how to use LlamaIndex for building Retrieval-Augmented Generation (RAG) applications with both local and cloud-based vector stores. It includes:

- **Local Quickstart:** Index and chat with your own documents using OpenAI embeddings and LLMs, with persistent local storage.
- **Pinecone Integration:** Store and query document embeddings in Pinecone, leveraging Replicate-hosted LLMs for scalable RAG workflows.
- **Function Agent:** An advanced agent that can answer questions about your documents and perform calculations, using LlamaIndex's function-calling capabilities.

## Quick Start Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Before running the notebooks or scripts, set the following environment variables in your terminal or in a `.env` file:

- `PINECONE_API` – Your Pinecone API key
- `INDEX_HOST` – Your Pinecone index host URL
- `OPENAI_API_KEY` – Your OpenAI API key (if using OpenAI LLMs or embeddings)
- `REPLICATE_API_TOKEN` – Your Replicate API token (if using Replicate LLMs)
- (Optional) Any other LLM provider API keys you want to use


Create a `.env` file with the same variables.

## *Using Gemini API (Free Alternative)*

The provided examples use the Replicate API, but you can also use the free Gemini API from Google. To get started:

1. **Get your Gemini API key:** [Google Gemini API Key Page](https://aistudio.google.com/app/apikey)
2. **Install additional dependencies:**
   ```bash
   pip install llama-index-llms-gemini llama-index-embeddings-gemini
   ```
3. **Replace OpenAI config with Gemini:**
   ```python
   from llama_index.llms.gemini import Gemini
   from llama_index.embeddings.gemini import GeminiEmbedding

   embed_model = GeminiEmbedding(model_name="models/embedding-001")
   llm = Gemini()
   ```

Each notebook and script is self-contained and demonstrates a different aspect of LlamaIndex-powered RAG pipelines.