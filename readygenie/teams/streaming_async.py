import asyncio
from typing import Iterator  # noqa

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.team.team import Team
from globalgenie.tools.yfinance import YFinanceTools

stock_searcher = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a stock.",
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
        )
    ],
)

company_info_agent = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a stock.",
    tools=[
        YFinanceTools(
            stock_price=False,
            company_info=True,
            company_news=True,
        )
    ],
)


team = Team(
    name="Stock Research Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher, company_info_agent],
    markdown=True,
    show_members_responses=True,
)

if __name__ == "__main__":
    asyncio.run(
        team.aprint_response("What is the current stock price of NVDA?", stream=True)
    )
