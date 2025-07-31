import asyncio

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.calculator import CalculatorTools
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        CalculatorTools(
            enable_all=True,
            exclude_tools=["exponentiate", "factorial", "is_prime", "square_root"],
        ),
        DuckDuckGoTools(include_tools=["duckduckgo_search"]),
    ],
    show_tool_calls=True,
)

asyncio.run(
    agent.aprint_response(
        "Search the web for a difficult sum that can be done with normal arithmetic and solve it.",
        markdown=True,
    )
)
