import asyncio

from globalgenie.agent import Agent
from globalgenie.models.nebius import Nebius
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Nebius(id="Qwen/Qwen3-30B-A3B"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
