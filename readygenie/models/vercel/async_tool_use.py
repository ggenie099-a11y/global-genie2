"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.vercel import v0
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=v0(id="v0-1.0-md"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
