from globalgenie.agent import Agent
from globalgenie.embedder.openai import OpenAIEmbedder
from globalgenie.knowledge.url import UrlKnowledge
from globalgenie.models.anthropic import Claude
from globalgenie.storage.sqlite import SqliteStorage
from globalgenie.vectordb.lancedb import LanceDb, SearchType

# Load GlobalGenie documentation in a knowledge base
# You can also use `https://docs.globalgenie.com/llms-full.txt` for the full documentation
knowledge = UrlKnowledge(
    urls=["https://docs.globalgenie.com/introduction.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="globalgenie_docs",
        search_type=SearchType.hybrid,
        # Use OpenAI for embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
    ),
)

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="GlobalGenie Assist",
    model=Claude(id="claude-sonnet-4-20250514"),
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    agent.print_response("What is GlobalGenie?", stream=True)
