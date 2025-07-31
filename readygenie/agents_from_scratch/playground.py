"""Your Agent Playground

Install dependencies: `pip install openai duckduckgo-search lancedb tantivy elevenlabs sqlalchemy 'fastapi[standard]' globalgenie`
"""

from agent_with_knowledge import agent_with_knowledge
from agent_with_storage import agent_with_storage
from agent_with_tools import agent_with_tools
from globalgenie.playground import Playground, serve_playground_app
from globalgenie_assist import globalgenie_assist
from simple_agent import simple_agent

# Create and configure the playground app
app = Playground(
    agents=[
        simple_agent,
        agent_with_tools,
        agent_with_knowledge,
        agent_with_storage,
        globalgenie_assist,
    ]
).get_app()

if __name__ == "__main__":
    # Run the playground app
    playground = Playground(
        agents=[
            simple_agent,
            agent_with_tools,
            agent_with_knowledge,
            agent_with_storage,
            globalgenie_assist,
        ],
        app_id="agents-from-scratch-playground-app",
        name="Agents from Scratch Playground",
    )
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(app="playground:app", reload=True)
