import asyncio

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.run.base import RunStatus
from globalgenie.run.v2.workflow import WorkflowRunResponse
from globalgenie.storage.sqlite import SqliteStorage
from globalgenie.team import Team
from globalgenie.tools.googlesearch import GoogleSearchTools
from globalgenie.tools.hackernews import HackerNewsTools
from globalgenie.utils.pprint import pprint_run_response
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
    tools=[GoogleSearchTools()],
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

content_creation_workflow = Workflow(
    name="Content Creation Workflow",
    description="Automated content creation from blog posts to social media",
    storage=SqliteStorage(
        table_name="workflow_v2_bg",
        db_file="tmp/workflow_v2_bg.db",
        mode="workflow_v2",
    ),
    steps=[research_step, content_planning_step],
)


async def main():
    print(" Starting Async Background Workflow Test")

    # Start background execution (async)
    bg_response = await content_creation_workflow.arun(
        message="AI trends in 2024", background=True
    )
    print(f" Initial Response: {bg_response.status} - {bg_response.content}")
    print(f" Run ID: {bg_response.run_id}")

    # Poll every 5 seconds until completion
    poll_count = 0

    while True:
        poll_count += 1
        print(f"\n Poll #{poll_count} (every 5s)")

        result = content_creation_workflow.get_run(bg_response.run_id)

        if result is None:
            print(" Workflow not found yet, still waiting...")
            if poll_count > 50:
                print(f"⏰ Timeout after {poll_count} attempts")
                break
            await asyncio.sleep(5)
            continue

        if result.has_completed():
            break

        if poll_count > 200:
            print(f"⏰ Timeout after {poll_count} attempts")
            break

        await asyncio.sleep(5)

    final_result = content_creation_workflow.get_run(bg_response.run_id)

    print(f"\n Final Result:")
    print("=" * 50)
    pprint_run_response(final_result, markdown=True)


if __name__ == "__main__":
    asyncio.run(main())
