import asyncio

from globalgenie.agent import Agent
from globalgenie.models.portkey import Portkey

agent = Agent(
    model=Portkey(id="gpt-4o-mini"),
    markdown=True,
)

# Print the response in the terminal
asyncio.run(
    agent.aprint_response("What is Portkey and why would I use it as an AI gateway?")
)
