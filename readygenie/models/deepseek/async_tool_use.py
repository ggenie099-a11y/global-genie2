"""
Async example using DeepSeek with tool calls.
"""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.deepseek import DeepSeek
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=DeepSeek(id="deepseek-chat"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
