from typing import Optional

from globalgenie.agent import Agent
from globalgenie.eval.reliability import ReliabilityEval, ReliabilityResult
from globalgenie.models.openai import OpenAIChat
from globalgenie.run.team import TeamRunResponse
from globalgenie.team.team import Team
from globalgenie.tools.yfinance import YFinanceTools

team_member = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a stock.",
    tools=[YFinanceTools(stock_price=True)],
)

team = Team(
    name="Stock Research Team",
    model=OpenAIChat("gpt-4o"),
    members=[team_member],
    markdown=True,
    show_members_responses=True,
)

expected_tool_calls = [
    "transfer_task_to_member",  # Tool call used to transfer a task to a Team member
    "get_current_stock_price",  # Tool call used to get the current stock price of a stock
]


def evaluate_team_reliability():
    response: TeamRunResponse = team.run("What is the current stock price of NVDA?")
    evaluation = ReliabilityEval(
        name="Team Reliability Evaluation",
        team_response=response,
        expected_tool_calls=expected_tool_calls,
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    result.assert_passed()


if __name__ == "__main__":
    evaluate_team_reliability()
