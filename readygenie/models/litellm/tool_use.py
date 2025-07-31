from globalgenie.agent import Agent
from globalgenie.models.litellm import LiteLLM
from globalgenie.tools.yfinance import YFinanceTools

openai_agent = Agent(
    model=LiteLLM(
        id="gpt-4o",
        name="LiteLLM",
    ),
    markdown=True,
    tools=[YFinanceTools()],
)

# Ask a question that would likely trigger tool use
openai_agent.print_response("How is TSLA stock doing right now?")
