"""Run `pip install duckduckgo-search boto3 openai` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.storage.dynamodb import DynamoDbStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=DynamoDbStorage(table_name="agent_sessions", region_name="us-east-1"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
