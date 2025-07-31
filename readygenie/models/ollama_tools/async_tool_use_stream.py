"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.ollama import OllamaTools
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OllamaTools(id="llama3.1:8b"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
