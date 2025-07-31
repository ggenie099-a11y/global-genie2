"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.openrouter import OpenRouter
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenRouter(id="openai/gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
