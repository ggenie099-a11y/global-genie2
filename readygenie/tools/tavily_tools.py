from globalgenie.agent import Agent
from globalgenie.tools.tavily import TavilyTools

agent = Agent(tools=[TavilyTools()], show_tool_calls=True)
agent.print_response("Search tavily for 'language models'", markdown=True)
