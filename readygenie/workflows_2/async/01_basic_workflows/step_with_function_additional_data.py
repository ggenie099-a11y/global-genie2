import asyncio
from typing import AsyncIterator, Union

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.run.v2.workflow import WorkflowRunResponseEvent
from globalgenie.storage.sqlite import SqliteStorage
from globalgenie.team import Team
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from globalgenie.tools.hackernews import HackerNewsTools
from globalgenie.workflow.v2.step import Step, StepInput, StepOutput
from globalgenie.workflow.v2.workflow import Workflow

# Define agents
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[HackerNewsTools()],
    instructions="Extract key insights and content from Hackernews posts",
)

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Search the web for the latest news and trends",
)

# Define research team for complex analysis
research_team = Team(
    name="Research Team",
    mode="coordinate",
    members=[hackernews_agent, web_agent],
    instructions="Analyze content and create comprehensive social media strategy",
)

content_planner = Agent(
    name="Content Planner",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Plan a content schedule over 4 weeks for the provided topic and research content",
        "Ensure that I have posts for 3 posts per week",
    ],
)


async def custom_content_planning_function(
    step_input: StepInput,
) -> AsyncIterator[Union[WorkflowRunResponseEvent, StepOutput]]:
    """
    Custom function that does intelligent content planning with context awareness
    Now also uses additional_data for extra context
    """
    message = step_input.message
    previous_step_content = step_input.previous_step_content

    # Access additional_data that was passed with the workflow
    additional_data = step_input.additional_data or {}
    user_email = additional_data.get("user_email", "No email provided")
    priority = additional_data.get("priority", "normal")
    client_type = additional_data.get("client_type", "standard")

    # Create intelligent planning prompt
    planning_prompt = f"""
        STRATEGIC CONTENT PLANNING REQUEST:

        Core Topic: {message}

        Research Results: {previous_step_content[:500] if previous_step_content else "No research results"}

        Additional Context:
        - Client Type: {client_type}
        - Priority Level: {priority}
        - Contact Email: {user_email}

        Planning Requirements:
        1. Create a comprehensive content strategy based on the research
        2. Leverage the research findings effectively
        3. Identify content formats and channels
        4. Provide timeline and priority recommendations
        5. Include engagement and distribution strategies
        {"6. Mark as HIGH PRIORITY delivery" if priority == "high" else "6. Standard delivery timeline"}

        Please create a detailed, actionable content plan.
    """

    try:
        response_iterator = await content_planner.arun(
            planning_prompt, stream=True, stream_intermediate_steps=True
        )
        async for event in response_iterator:
            yield event
        response = content_planner.run_response

        enhanced_content = f"""
            ## Strategic Content Plan

            **Planning Topic:** {message}

            **Client Details:**
            - Type: {client_type}
            - Priority: {priority.upper()}
            - Contact: {user_email}

            **Research Integration:** {"✓ Research-based" if previous_step_content else "✗ No research foundation"}

            **Content Strategy:**
            {response.content}

            **Custom Planning Enhancements:**
            - Research Integration: {"High" if previous_step_content else "Baseline"}
            - Strategic Alignment: Optimized for multi-channel distribution
            - Execution Ready: Detailed action items included
            - Priority Level: {priority.upper()}
        """.strip()

        yield StepOutput(content=enhanced_content, response=response)

    except Exception as e:
        yield StepOutput(
            content=f"Custom content planning failed: {str(e)}",
            success=False,
        )


# Define steps using different executor types

research_step = Step(
    name="Research Step",
    team=research_team,
)

content_planning_step = Step(
    name="Content Planning Step",
    executor=custom_content_planning_function,
)


# Define and use examples
if __name__ == "__main__":
    content_creation_workflow = Workflow(
        name="Content Creation Workflow",
        description="Automated content creation with custom execution options",
        storage=SqliteStorage(
            table_name="workflow_v2",
            db_file="tmp/workflow_v2.db",
            mode="workflow_v2",
        ),
        steps=[research_step, content_planning_step],
    )

    # Run workflow with additional_data
    asyncio.run(
        content_creation_workflow.aprint_response(
            message="AI trends in 2024",
            additional_data={
                "user_email": "kaustubh@globalgenie.com",
                "priority": "high",
                "client_type": "enterprise",
            },
            markdown=True,
            stream=True,
            stream_intermediate_steps=True,
        )
    )

    print("\n" + "=" * 60 + "\n")
