from globalgenie.agent import Agent
from globalgenie.models.openai.responses import OpenAIResponses

agent = Agent(model=OpenAIResponses(id="o3-mini"))
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
)
