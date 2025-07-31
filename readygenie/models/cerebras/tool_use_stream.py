from globalgenie.agent import Agent
from globalgenie.models.cerebras import Cerebras
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cerebras(id="llama-3.3-70b"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Print the response in the terminal
agent.print_response("Whats happening in France?", stream=True)
