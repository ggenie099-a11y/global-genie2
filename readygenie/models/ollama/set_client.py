"""Run `pip install yfinance` to install dependencies."""

from globalgenie.agent import Agent, RunResponse  # noqa
from globalgenie.models.ollama import Ollama
from ollama import Client as OllamaClient

agent = Agent(
    model=Ollama(id="llama3.1:8b", client=OllamaClient()),
    markdown=True,
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")
