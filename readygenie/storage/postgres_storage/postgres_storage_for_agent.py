"""Run `pip install duckduckgo-search sqlalchemy openai` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.storage.postgres import PostgresStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    storage=PostgresStorage(
        table_name="agent_sessions", db_url=db_url, auto_upgrade_schema=True
    ),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
