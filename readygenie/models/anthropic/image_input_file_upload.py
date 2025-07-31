"""
In this example, we upload a PDF file to Anthropic directly and then use it as an input to an agent.
"""

from pathlib import Path

from globalgenie.agent import Agent
from globalgenie.media import Image
from globalgenie.models.anthropic import Claude
from globalgenie.utils.media import download_file
from anthropic import Anthropic

img_path = Path(__file__).parent.joinpath("globalgenie-intro.png")

# Download the file using the download_file function
download_file(
    "https://globalgenie-public.s3.us-east-1.amazonaws.com/images/globalgenie-intro.png",
    str(img_path),
)

# Initialize Anthropic client
client = Anthropic()

# Upload the file to Anthropic
uploaded_file = client.beta.files.upload(
    file=Path(img_path),
)

if uploaded_file is not None:
    agent = Agent(
        model=Claude(
            id="claude-opus-4-20250514",
            default_headers={"anthropic-beta": "files-api-2025-04-14"},
        ),
        markdown=True,
    )

    agent.print_response(
        "What does the attached image say.",
        images=[Image(content=uploaded_file)],
    )
