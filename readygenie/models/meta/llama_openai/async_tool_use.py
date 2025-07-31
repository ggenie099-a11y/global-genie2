"""Run `pip install openai yfinance` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.meta import LlamaOpenAI
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=LlamaOpenAI(id="Llama-4-Maverick-17B-128E-Instruct-FP8"),
    tools=[YFinanceTools()],
    show_tool_calls=True,
)
asyncio.run(agent.aprint_response("Whats the price of AAPL stock?"))
