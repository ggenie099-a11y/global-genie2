"""Run `pip install duckduckgo-search` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.aimlapi import AIMLApi
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AIMLApi(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?")
