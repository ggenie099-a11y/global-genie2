from globalgenie.agent import Agent
from globalgenie.models.google import Gemini
from globalgenie.playground import Playground, serve_playground_app
from globalgenie.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Finance Agent",
    agent_id="finance-agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[YFinanceTools(stock_price=True)],
    debug_mode=True,
)

playground = Playground(
    agents=[finance_agent],
    name="Gemini Agents",
    description="A playground for Gemini agents",
    app_id="gemini-agents",
)
app = playground.get_app(use_async=False)

if __name__ == "__main__":
    playground.serve(app="gemini_agents:app", reload=True)
