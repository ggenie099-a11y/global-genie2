"""Build a Web Search Agent using xAI."""

from globalgenie.agent import Agent
from globalgenie.models.vercel import v0
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=v0(id="v0-1.0-md"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
