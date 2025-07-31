import asyncio

from globalgenie.agent import Agent, RunResponse  # noqa
from globalgenie.models.vercel import v0

agent = Agent(model=v0(id="v0-1.0-md"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
