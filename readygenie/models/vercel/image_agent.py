from globalgenie.agent import Agent
from globalgenie.media import Image
from globalgenie.models.vercel import v0
from globalgenie.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=v0(id="v0-1.0-md"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)
