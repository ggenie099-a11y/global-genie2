import asyncio

from globalgenie.agent import Agent
from globalgenie.models.portkey import Portkey
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Portkey(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

# Print the response in the terminal
asyncio.run(
    agent.aprint_response(
        "What are the latest developments in AI gateways?", stream=True
    )
)
