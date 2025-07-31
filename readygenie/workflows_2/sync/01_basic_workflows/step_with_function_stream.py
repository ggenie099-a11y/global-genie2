from typing import Iterator, Union

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


def custom_content_planning_function(
    step_input: StepInput,
) -> Iterator[Union[WorkflowRunResponseEvent, StepOutput]]:
    """
    Custom function that does intelligent content planning with context awareness
    """
    message = step_input.message
    previous_step_content = step_input.previous_step_content

    # Create intelligent planning prompt
    planning_prompt = f"""
        STRATEGIC CONTENT PLANNING REQUEST:
        
        Core Topic: {message}
        
        Research Results: {previous_step_content[:500] if previous_step_content else "No research results"}
        
        Planning Requirements:
        1. Create a comprehensive content strategy based on the research
        2. Leverage the research findings effectively
        3. Identify content formats and channels
        4. Provide timeline and priority recommendations
        5. Include engagement and distribution strategies
        
        Please create a detailed, actionable content plan.
    """

    try:
        response_iterator = content_planner.run(
            planning_prompt, stream=True, stream_intermediate_steps=True
        )
        for event in response_iterator:
            yield event

        response = content_planner.run_response

        enhanced_content = f"""
            ## Strategic Content Plan

            **Planning Topic:** {message}

            **Research Integration:** {"✓ Research-based" if previous_step_content else "✗ No research foundation"}

            **Content Strategy:**
            {response.content}

            **Custom Planning Enhancements:**
            - Research Integration: {"High" if previous_step_content else "Baseline"}
            - Strategic Alignment: Optimized for multi-channel distribution
            - Execution Ready: Detailed action items included
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
    streaming_content_workflow = Workflow(
        name="Streaming Content Creation Workflow",
        description="Automated content creation with streaming custom execution functions",
        storage=SqliteStorage(
            table_name="workflow_v2_streaming",
            db_file="tmp/workflow_v2_streaming.db",
            mode="workflow_v2",
        ),
        # Define the sequence of steps
        # First run the research_step, then the content_planning_step
        # You can mix and match agents, teams, and even regular python functions directly as steps
        steps=[
            research_step,
            content_planning_step,
        ],
    )

    streaming_content_workflow.print_response(
        message="AI trends in 2024",
        markdown=True,
        stream=True,
        stream_intermediate_steps=True,
    )
