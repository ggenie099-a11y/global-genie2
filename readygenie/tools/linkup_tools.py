from globalgenie.agent import Agent
from globalgenie.tools.linkup import LinkupTools

agent = Agent(tools=[LinkupTools()], show_tool_calls=True)
agent.print_response("What's the latest news in French politics?", markdown=True)
