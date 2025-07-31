"""Run `pip install requests` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.tools.models_labs import ModelsLabTools

# Create an Agent with the ModelsLabs tool
agent = Agent(tools=[ModelsLabTools()], name="ModelsLabs Agent")

agent.print_response(
    "Generate a video of a beautiful sunset over the ocean", markdown=True
)
