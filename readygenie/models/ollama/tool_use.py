"""Run `pip install duckduckgo-search` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.ollama import Ollama
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Ollama(id="llama3.2:latest"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?")
