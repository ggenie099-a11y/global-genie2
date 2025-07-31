"""Run `pip install sqlalchemy` and ensure Postgres is running (`./readygenie/scripts/run_pgvector.sh`)."""

from globalgenie.agent import Agent
from globalgenie.models.vllm import vLLM
from globalgenie.storage.postgres import PostgresStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=vLLM(id="Qwen/Qwen2.5-7B-Instruct"),
    storage=PostgresStorage(table_name="agent_sessions", db_url=DB_URL),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)

agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
