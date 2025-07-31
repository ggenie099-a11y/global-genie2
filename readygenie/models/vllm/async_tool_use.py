"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from globalgenie.agent import Agent
from globalgenie.models.vllm import vLLM
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=vLLM(id="Qwen/Qwen2.5-7B-Instruct", top_k=20, enable_thinking=False),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
