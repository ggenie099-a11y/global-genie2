from typing import Optional

from globalgenie.agent import Agent
from globalgenie.eval.accuracy import AccuracyEval, AccuracyResult
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.calculator import CalculatorTools

evaluation = AccuracyEval(
    name="Comparison Evaluation",
    model=OpenAIChat(id="o4-mini"),
    agent=Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[CalculatorTools(enable_all=True)],
        instructions="You must use the calculator tools for comparisons.",
    ),
    input="9.11 and 9.9 -- which is bigger?",
    expected_output="9.9",
    additional_guidelines="Its ok for the output to include additional text or information relevant to the comparison.",
)

result: Optional[AccuracyResult] = evaluation.run(print_results=True)
assert result is not None and result.avg_score >= 8
