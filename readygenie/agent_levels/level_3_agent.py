from globalgenie.agent import Agent
from globalgenie.memory.v2.db.sqlite import SqliteMemoryDb
from globalgenie.memory.v2.memory import Memory
from globalgenie.models.anthropic import Claude
from globalgenie.tools.reasoning import ReasoningTools
from globalgenie.tools.yfinance import YFinanceTools

memory = Memory(
    # Use any model for creating and managing memories
    model=Claude(id="claude-sonnet-4-20250514"),
    # Store memories in a SQLite database
    db=SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db"),
    # We disable deletion by default, enable it if needed
    delete_memories=True,
    clear_memories=True,
)

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    # User ID for storing memories, `default` if not provided
    user_id="ava",
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Only include the report in your response. No other text.",
    ],
    memory=memory,
    # Let the Agent manage its memories
    enable_agentic_memory=True,
    markdown=True,
)

if __name__ == "__main__":
    # This will create a memory that "ava's" favorite stocks are NVIDIA and TSLA
    agent.print_response(
        "My favorite stocks are NVIDIA and TSLA",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    # This will use the memory to answer the question
    agent.print_response(
        "Can you compare my favorite stocks?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
