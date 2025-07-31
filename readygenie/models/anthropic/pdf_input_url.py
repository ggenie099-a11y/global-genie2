from globalgenie.agent import Agent
from globalgenie.media import File
from globalgenie.models.anthropic import Claude

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[
        File(url="https://globalgenie-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"),
    ],
)
