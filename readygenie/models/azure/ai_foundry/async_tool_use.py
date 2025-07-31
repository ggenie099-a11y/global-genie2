"""
Async example using Claude with tool calls.
"""

import asyncio
from pprint import pprint

from globalgenie.agent import Agent
from globalgenie.models.azure import AzureAIFoundry
from globalgenie.run.response import RunResponse
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AzureAIFoundry(id="Cohere-command-r-08-2024"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?"))
