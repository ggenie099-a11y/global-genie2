import asyncio

from globalgenie.agent import Agent, RunResponse  # noqa
from globalgenie.models.aws import AwsBedrock

agent = Agent(model=AwsBedrock(id="mistral.mistral-small-2402-v1:0"), markdown=True)

# Print the response in the terminal
asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
