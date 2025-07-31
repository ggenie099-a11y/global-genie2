"""
Async example using Fireworks with tool calls.
"""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.fireworks import Fireworks
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/llama-v3p1-405b-instruct"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
