from globalgenie.agent import Agent
from globalgenie.embedder.openai import OpenAIEmbedder
from globalgenie.knowledge.url import UrlKnowledge
from globalgenie.models.openai import OpenAIChat
from globalgenie.storage.sqlite import SqliteStorage
from globalgenie.vectordb.lancedb import LanceDb, SearchType

globalgenie_assist = Agent(
    name="GlobalGenie Assist",
    model=OpenAIChat(id="gpt-4o"),
    description="You help answer questions about the GlobalGenie framework.",
    instructions="Search your knowledge before answering the question.",
    knowledge=UrlKnowledge(
        urls=["https://docs.globalgenie.com/llms-full.txt"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="globalgenie_assist_knowledge",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    ),
    storage=SqliteStorage(table_name="globalgenie_assist_sessions", db_file="tmp/agents.db"),
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    globalgenie_assist.knowledge.load()  # Load the knowledge base, comment after first run
    globalgenie_assist.print_response("What is GlobalGenie?")
