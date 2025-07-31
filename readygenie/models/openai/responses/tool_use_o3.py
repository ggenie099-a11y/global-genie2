from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIResponses
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIResponses(id="o3"),
    tools=[YFinanceTools(cache_results=True)],
    show_tool_calls=True,
    markdown=True,
    telemetry=False,
    monitoring=False,
)

agent.print_response("What is the current price of TSLA?", stream=True)
