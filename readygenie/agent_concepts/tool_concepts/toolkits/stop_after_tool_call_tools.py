from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.googlesearch import GoogleSearchTools

agent = Agent(
    model=OpenAIChat(id="gpt-4.5-preview"),
    tools=[
        GoogleSearchTools(
            stop_after_tool_call_tools=["google_search"],
            show_result_tools=["google_search"],
        )
    ],
    show_tool_calls=True,
)

agent.print_response("Whats the latest about gpt 4.5?", markdown=True)
