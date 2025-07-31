"""Run `pip install globalgenie llama-api-client yfinance` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.models.meta import Llama
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=Llama(id="Llama-4-Maverick-17B-128E-Instruct-FP8"),
    tools=[YFinanceTools()],
    show_tool_calls=True,
)
agent.print_response("Tell me the price of AAPL stock", stream=True)
