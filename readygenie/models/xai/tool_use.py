"""Build a Web Search Agent using xAI."""

from globalgenie.agent import Agent
from globalgenie.models.xai import xAI
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-2"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
