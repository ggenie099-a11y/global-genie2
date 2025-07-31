"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.xai import xAI
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-2"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
