"""This example shows how to run a Reliability evaluation asynchronously."""

import asyncio
from typing import Optional

from globalgenie.agent import Agent
from globalgenie.eval.reliability import ReliabilityEval, ReliabilityResult
from globalgenie.models.openai import OpenAIChat
from globalgenie.run.response import RunResponse
from globalgenie.tools.calculator import CalculatorTools


def factorial():
    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[CalculatorTools(factorial=True)],
    )
    response: RunResponse = agent.run("What is 10!?")
    evaluation = ReliabilityEval(
        agent_response=response,
        expected_tool_calls=["factorial"],
    )

    # Run the evaluation calling the arun method.
    result: Optional[ReliabilityResult] = asyncio.run(
        evaluation.arun(print_results=True)
    )
    result.assert_passed()


if __name__ == "__main__":
    factorial()
