from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIResponses
from globalgenie.tools.file import FileTools

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    tools=[{"type": "web_search_preview"}, FileTools()],
    instructions="Save the results to a file with a relevant name.",
    markdown=True,
)
agent.print_response("Whats happening in France?")
