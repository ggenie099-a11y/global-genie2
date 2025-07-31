"""Run `pip install duckduckgo-search openai` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.storage.json import JsonStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    storage=JsonStorage(dir_path="tmp/agent_sessions_json"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
