import asyncio

from globalgenie.agent import Agent
from globalgenie.models.nebius import Nebius

agent = Agent(
    model=Nebius(),
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Print the response in the terminal
asyncio.run(agent.aprint_response("write a two sentence horror story", stream=True))
