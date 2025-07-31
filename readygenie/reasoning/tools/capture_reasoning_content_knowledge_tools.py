"""
ReadyGenie: Capturing reasoning_content with KnowledgeTools

This example demonstrates how to access and print the reasoning_content
when using KnowledgeTools with URL knowledge, in both streaming and non-streaming modes.
"""

from textwrap import dedent

from globalgenie.agent import Agent
from globalgenie.embedder.openai import OpenAIEmbedder
from globalgenie.knowledge.url import UrlKnowledge
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.knowledge import KnowledgeTools
from globalgenie.vectordb.lancedb import LanceDb, SearchType

# Create a knowledge base containing information from a URL
print("Setting up URL knowledge base...")
globalgenie_docs = UrlKnowledge(
    urls=["https://www.paulgraham.com/read.html"],
    # Use LanceDB as the vector database
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="readygenie_knowledge_tools",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

# Only load if needed
try:
    print("Loading knowledge base (skip if already exists)...")
    globalgenie_docs.load(recreate=False)
    print("Knowledge base loaded.")
except:
    print("Creating new knowledge base...")
    globalgenie_docs.load(recreate=True)
    print("Knowledge base created.")


print("\n=== Example 1: Using KnowledgeTools in non-streaming mode ===\n")

# Create agent with KnowledgeTools
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        KnowledgeTools(
            knowledge=globalgenie_docs,
            think=True,
            search=True,
            analyze=True,
            add_instructions=True,
        )
    ],
    instructions=dedent("""\
        You are an expert problem-solving assistant with strong analytical skills! 🧠
        Use the knowledge tools to organize your thoughts, search for information, 
        and analyze results step-by-step.
        \
    """),
    markdown=True,
    stream=False,
)

# Run the agent (non-streaming)
print("Running with KnowledgeTools (non-streaming)...")
agent.print_response(
    "What does Paul Graham explain here with respect to need to read?", stream=False
)

# Print the reasoning_content
print("\n--- reasoning_content from agent.run_response ---")
if (
    hasattr(agent, "run_response")
    and agent.run_response
    and hasattr(agent.run_response, "reasoning_content")
    and agent.run_response.reasoning_content
):
    print(agent.run_response.reasoning_content)
else:
    print("No reasoning_content found in agent.run_response")


print("\n\n=== Example 2: Using KnowledgeTools in streaming mode ===\n")

# Create a fresh agent for streaming
streaming_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        KnowledgeTools(
            knowledge=globalgenie_docs,
            think=True,
            search=True,
            analyze=True,
            add_instructions=True,
        )
    ],
    instructions=dedent("""\
        You are an expert problem-solving assistant with strong analytical skills! 🧠
        Use the knowledge tools to organize your thoughts, search for information, 
        and analyze results step-by-step.
        \
    """),
    markdown=True,
)

# Print response (which includes processing streaming responses)
print("Running with KnowledgeTools (streaming)...")
streaming_agent.print_response(
    "What does Paul Graham explain here with respect to need to read?",
    stream=True,
    stream_intermediate_steps=True,
    show_full_reasoning=True,
)

# Access reasoning_content from the agent's run_response after streaming
print("\n--- reasoning_content from agent.run_response after streaming ---")
if (
    hasattr(streaming_agent, "run_response")
    and streaming_agent.run_response
    and hasattr(streaming_agent.run_response, "reasoning_content")
    and streaming_agent.run_response.reasoning_content
):
    print(streaming_agent.run_response.reasoning_content)
else:
    print("No reasoning_content found in agent.run_response after streaming")
