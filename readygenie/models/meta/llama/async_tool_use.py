"""Run `pip install globalgenie llama-api-client yfinance` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.meta import Llama
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=Llama(id="Llama-4-Maverick-17B-128E-Instruct-FP8"),
    tools=[YFinanceTools()],
    debug_mode=True,
)
asyncio.run(agent.aprint_response("Whats the price of AAPL stock?"))
