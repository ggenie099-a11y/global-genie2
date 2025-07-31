from globalgenie.agent import Agent
from globalgenie.media import File
from globalgenie.models.openai.responses import OpenAIResponses

agent = Agent(
    model=OpenAIResponses(id="gpt-4o-mini"),
    tools=[{"type": "file_search"}, {"type": "web_search_preview"}],
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file and search the web for more information.",
    files=[File(url="https://globalgenie-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
)

print("Citations:")
print(agent.run_response.citations)
