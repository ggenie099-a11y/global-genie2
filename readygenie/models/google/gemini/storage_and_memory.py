"""Run `pip install duckduckgo-search pgvector google.genai` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.knowledge.pdf_url import PDFUrlKnowledgeBase
from globalgenie.memory.v2.db.postgres import PostgresMemoryDb
from globalgenie.memory.v2.memory import Memory
from globalgenie.models.google import Gemini
from globalgenie.storage.postgres import PostgresStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from globalgenie.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://globalgenie-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    tools=[DuckDuckGoTools()],
    knowledge=knowledge_base,
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    # Store the memories and summary in a database
    memory=Memory(
        db=PostgresMemoryDb(table_name="agent_memory", db_url=db_url),
    ),
    enable_user_memories=True,
    enable_session_summaries=True,
    show_tool_calls=True,
    # This setting adds a tool to search the knowledge base for information
    search_knowledge=True,
    # This setting adds a tool to get chat history
    read_chat_history=True,
    # Add the previous chat history to the messages sent to the Model.
    add_history_to_messages=True,
    # This setting adds 6 previous messages from chat history to the messages sent to the LLM
    num_history_responses=6,
    markdown=True,
    debug_mode=True,
)
agent.print_response("Whats is the latest AI news?")
