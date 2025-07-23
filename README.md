# LlamaIndex: Data Indexing and Retrieval for RAG

This project demonstrates how to use LlamaIndex for building Retrieval-Augmented Generation (RAG) applications with both local and cloud-based vector stores. It includes:

- **Local Quickstart:** Index and chat with your own documents using OpenAI embeddings and LLMs, with persistent local storage.
- **Pinecone Integration:** Store and query document embeddings in Pinecone, leveraging Replicate-hosted LLMs for scalable RAG workflows.
- **Function Agent:** An advanced agent that can answer questions about your documents and perform calculations, using LlamaIndex's function-calling capabilities.

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