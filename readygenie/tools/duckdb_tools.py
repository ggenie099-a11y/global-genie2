from globalgenie.agent import Agent
from globalgenie.tools.duckdb import DuckDbTools

agent = Agent(
    tools=[DuckDbTools()],
    show_tool_calls=True,
    instructions="Use this file for Movies data: https://globalgenie-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
)
agent.print_response(
    "What is the average rating of movies?", markdown=True, stream=False
)
