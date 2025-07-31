from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    add_location_to_instructions=True,
    tools=[DuckDuckGoTools(cache_results=True)],
)
agent.print_response("What is current news about my city?")
