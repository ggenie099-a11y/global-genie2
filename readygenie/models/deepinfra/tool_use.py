"""Run `pip install duckduckgo-search` to install dependencies."""

from globalgenie.agent import Agent  # noqa
from globalgenie.models.deepinfra import DeepInfra  # noqa
from globalgenie.tools.duckduckgo import DuckDuckGoTools  # noqa

agent = Agent(
    model=DeepInfra(id="meta-llama/Llama-2-70b-chat-hf"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
