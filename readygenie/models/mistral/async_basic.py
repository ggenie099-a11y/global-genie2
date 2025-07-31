"""
Basic async example using Mistral.
"""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.mistral.mistral import MistralChat

agent = Agent(
    model=MistralChat(id="mistral-large-latest"),
    markdown=True,
)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
