from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.storage.redis import RedisStorage
from globalgenie.team import Team
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from globalgenie.tools.hackernews import HackerNewsTools
from globalgenie.workflow.v2.step import Step
from globalgenie.workflow.v2.workflow import Workflow

# Define agents
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
)
web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    role="Search the web for the latest news and trends",
)

# Define research team for complex analysis
research_team = Team(
    name="Research Team",
    mode="coordinate",
    members=[hackernews_agent, web_agent],
    instructions="Research tech topics from Hackernews and the web",
)

content_planner = Agent(
    name="Content Planner",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Plan a content schedule over 4 weeks for the provided topic and research content",
        "Ensure that I have posts for 3 posts per week",
    ],
)

# Define steps
research_step = Step(
    name="Research Step",
    team=research_team,
)

content_planning_step = Step(
    name="Content Planning Step",
    agent=content_planner,
)

# Create and use workflow
if __name__ == "__main__":
    content_creation_workflow = Workflow(
        name="Content Creation Workflow",
        description="Automated content creation from blog posts to social media",
        storage=RedisStorage(
            prefix="globalgenie_test",
            host="localhost",
            port=6379,
        ),
        steps=[research_step, content_planning_step],
    )
    content_creation_workflow.print_response(
        message="AI trends in 2024",
        markdown=True,
    )
