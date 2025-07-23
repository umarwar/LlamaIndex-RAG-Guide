import os
import asyncio
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.core import settings
from llama_index.core.workflow import Context
from llama_index.embeddings.openai import OpenAIEmbedding


os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
settings.embed_model = OpenAIEmbedding(model="text-embedding-3-large", dimensions=1536)

storage_context = StorageContext.from_defaults(persist_dir="storage")
index = load_index_from_storage(storage_context)
chat_engine = index.as_chat_engine(chat_mode="context", verbose=True)


def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about GolfGuiders application manual."""
    response = await chat_engine.achat(query)
    return str(response)


# Create an enhanced workflow with both tools
agent = FunctionAgent(
    tools=[multiply, search_documents],
    llm=OpenAI(model="gpt-4o"),
    system_prompt="""You are a helpful assistant that can perform calculations
    and search through documents to answer questions.""",
)

# create context
ctx = Context(agent)


# Now we can ask questions about the documents or do calculations
async def main():
    while True:
        user_input = input("\nEnter your question: ")
        if user_input == "exit":
            break
        response = await agent.run(user_input, ctx=ctx)
        print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
