"""
Async example using Gemini with tool calls.
"""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.google import Gemini
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
