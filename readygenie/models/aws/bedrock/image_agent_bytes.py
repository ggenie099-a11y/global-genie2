from pathlib import Path

from globalgenie.agent import Agent
from globalgenie.media import Image
from globalgenie.models.aws import AwsBedrock
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from globalgenie.utils.media import download_image

agent = Agent(
    model=AwsBedrock(id="amazon.nova-pro-v1:0"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

download_image(
    url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg",
    output_path=str(image_path),
)

# Read the image file content as bytes
image_bytes = image_path.read_bytes()

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(content=image_bytes, format="jpeg"),
    ],
)
