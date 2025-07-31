"""
Async example using Claude with tool calls.
"""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.anthropic import Claude
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
