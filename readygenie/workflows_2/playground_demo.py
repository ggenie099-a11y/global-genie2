"""
1. Install dependencies using: `pip install openai duckduckgo-search sqlalchemy 'fastapi[standard]' newspaper4k lxml_html_clean yfinance globalgenie`
2. Run the script using: `python readygenie/workflows/workflows_playground.py`
"""

from globalgenie.agent.agent import Agent
from globalgenie.models.openai.chat import OpenAIChat
from globalgenie.playground import Playground

# Import the workflows
from globalgenie.storage.sqlite import SqliteStorage
from globalgenie.tools.hackernews import HackerNewsTools
from globalgenie.workflow.v2.step import Step
from globalgenie.workflow.v2.workflow import Workflow
from blog_post_generator import blog_generator_workflow
from investment_report_generator import investment_workflow
from startup_idea_validator import startup_validation_workflow

# Define agents
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
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
    agent=hackernews_agent,
)

content_planning_step = Step(
    name="Content Planning Step",
    agent=content_planner,
)

content_creation_workflow = Workflow(
    name="Content Creation Workflow",
    description="Automated content creation from blog posts to social media",
    storage=SqliteStorage(
        table_name="workflow_v2",
        db_file="tmp/workflow_v2.db",
        mode="workflow_v2",
    ),
    steps=[research_step, content_planning_step],
)


# Initialize the Playground with the workflows
playground = Playground(
    workflows=[
        blog_generator_workflow,
        investment_workflow,
        startup_validation_workflow,
        content_creation_workflow,
    ],
    app_id="workflows-playground-app",
    name="Workflows Playground",
)
app = playground.get_app()

if __name__ == "__main__":
    # Start the playground server
    playground.serve(
        app="playground_demo:app",
        host="localhost",
        port=7777,
        reload=True,
    )
