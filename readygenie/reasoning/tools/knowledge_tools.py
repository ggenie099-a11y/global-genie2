"""
1. Run: `pip install openai globalgenie lancedb tantivy sqlalchemy` to install the dependencies
2. Export your OPENAI_API_KEY
3. Run: `python readygenie/reasoning/tools/knowledge_tools.py` to run the agent
"""

from globalgenie.agent import Agent
from globalgenie.embedder.openai import OpenAIEmbedder
from globalgenie.knowledge.url import UrlKnowledge
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.knowledge import KnowledgeTools
from globalgenie.vectordb.lancedb import LanceDb, SearchType

# Create a knowledge base containing information from a URL
globalgenie_docs = UrlKnowledge(
    urls=["https://docs.globalgenie.com/llms-full.txt"],
    # Use LanceDB as the vector database and store embeddings in the `globalgenie_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="globalgenie_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

knowledge_tools = KnowledgeTools(
    knowledge=globalgenie_docs,
    think=True,
    search=True,
    analyze=True,
    add_few_shot=True,
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[knowledge_tools],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment after first run
    globalgenie_docs.load(recreate=True)
    agent.print_response("How do I build multi-agent teams with GlobalGenie?", stream=True)
