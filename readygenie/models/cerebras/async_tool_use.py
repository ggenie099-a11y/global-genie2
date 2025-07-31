import asyncio

from globalgenie.agent import Agent
from globalgenie.models.cerebras import Cerebras
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?"))
