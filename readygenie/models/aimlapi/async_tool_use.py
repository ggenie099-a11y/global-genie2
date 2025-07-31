"""
Async example using AIMlAPI with tool calls.
"""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.aimlapi import AIMLApi
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AIMLApi(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
