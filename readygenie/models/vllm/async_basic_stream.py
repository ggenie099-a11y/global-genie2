import asyncio

from globalgenie.agent import Agent
from globalgenie.models.vllm import vLLM

agent = Agent(model=vLLM(id="Qwen/Qwen2.5-7B-Instruct"), markdown=True)
asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
