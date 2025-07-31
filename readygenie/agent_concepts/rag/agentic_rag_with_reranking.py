"""
1. Run: `pip install openai globalgenie cohere lancedb tantivy sqlalchemy` to install the dependencies
2. Export your OPENAI_API_KEY and CO_API_KEY
3. Run: `python readygenie/agent_concepts/rag/agentic_rag_with_reranking.py` to run the agent
"""

from globalgenie.agent import Agent
from globalgenie.embedder.openai import OpenAIEmbedder
from globalgenie.knowledge.url import UrlKnowledge
from globalgenie.models.openai import OpenAIChat
from globalgenie.reranker.cohere import CohereReranker
from globalgenie.vectordb.lancedb import LanceDb, SearchType

# Create a knowledge base containing information from a URL
knowledge_base = UrlKnowledge(
    urls=["https://docs.globalgenie.com/introduction.md"],
    # Use LanceDB as the vector database and store embeddings in the `globalgenie_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="globalgenie_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(
            id="text-embedding-3-small"
        ),  # Use OpenAI for embeddings
        reranker=CohereReranker(
            model="rerank-multilingual-v3.0"
        ),  # Use Cohere for reranking
    ),
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # Agentic RAG is enabled by default when `knowledge` is provided to the Agent.
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment after first run
    # agent.knowledge.load(recreate=True)
    agent.print_response("What are GlobalGenie's key features?")
