"""
In this example, we upload a PDF file to Anthropic directly and then use it as an input to an agent.
"""

from pathlib import Path

from globalgenie.agent import Agent
from globalgenie.media import File
from globalgenie.models.anthropic import Claude
from globalgenie.utils.media import download_file
from anthropic import Anthropic

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

# Download the file using the download_file function
download_file(
    "https://globalgenie-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf", str(pdf_path)
)

# Initialize Anthropic client
client = Anthropic()

# Upload the file to Anthropic
uploaded_file = client.beta.files.upload(
    file=Path(pdf_path),
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
        "Summarize the contents of the attached file.",
        files=[File(external=uploaded_file)],
    )
