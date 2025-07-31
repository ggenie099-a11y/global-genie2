from globalgenie.agent import Agent
from globalgenie.models.ollama import Ollama
from globalgenie.tools.yfinance import YFinanceTools

agent = Agent(
    model=Ollama(id="qwen3:8b"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables to display data.",
)

agent.print_response("Write a report on NVDA", stream=True, markdown=True)
