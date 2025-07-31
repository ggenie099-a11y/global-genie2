import asyncio

from globalgenie.agent import Agent
from globalgenie.models.litellm import LiteLLM
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=LiteLLM(
        id="gpt-4o",
        name="LiteLLM",
    ),
    markdown=True,
    tools=[DuckDuckGoTools()],
)

# Ask a question that would likely trigger tool use
asyncio.run(agent.aprint_response("What is happening in France?"))
