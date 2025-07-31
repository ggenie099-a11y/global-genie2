"""Run `pip install duckduckgo-search` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.azure import AzureAIFoundry
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AzureAIFoundry(id="Cohere-command-r-08-2024"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What is currently happening in France?", stream=True)
