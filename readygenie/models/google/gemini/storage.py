"""Run `pip install duckduckgo-search sqlalchemy google.genai` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.google import Gemini
from globalgenie.storage.postgres import PostgresStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
