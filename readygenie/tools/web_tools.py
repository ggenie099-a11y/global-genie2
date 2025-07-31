from globalgenie.agent import Agent
from globalgenie.tools.webtools import WebTools

agent = Agent(tools=[WebTools()], show_tool_calls=True)
agent.print_response("Tell me about https://tinyurl.com/57bmajz4")
