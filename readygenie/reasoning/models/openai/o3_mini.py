from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="o3-mini"),
)
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
    stream_intermediate_steps=True,
)
