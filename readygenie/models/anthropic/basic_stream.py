from typing import Iterator  # noqa
from globalgenie.agent import Agent, RunResponseEvent  # noqa
from globalgenie.models.anthropic import Claude

agent = Agent(model=Claude(id="claude-sonnet-4-20250514"), markdown=True)

# Get the response in a variable
# run_response: Iterator[RunResponseEvent] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
