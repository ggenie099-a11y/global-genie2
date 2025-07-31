from globalgenie.agent import Agent
from globalgenie.tools.jina import JinaReaderTools

agent = Agent(tools=[JinaReaderTools()], show_tool_calls=True)
agent.print_response("Summarize: https://github.com/globalgenie-agi")
