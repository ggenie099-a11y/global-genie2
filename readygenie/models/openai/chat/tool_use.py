"""Run `pip install duckduckgo-search` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?")
