from globalgenie.agent import Agent
from globalgenie.tools.website import WebsiteTools

agent = Agent(tools=[WebsiteTools()], show_tool_calls=True)

agent.print_response(
    "Search web page: 'https://docs.globalgenie.com/introduction'", markdown=True
)
