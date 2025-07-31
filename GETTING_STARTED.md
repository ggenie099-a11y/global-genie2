# Getting Started with GlobalGenie

Welcome to GlobalGenie! This guide will take you from installation to building your first intelligent AI agent in just a few minutes.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Basic Configuration](#basic-configuration)
4. [Your First Agent](#your-first-agent)
5. [Adding Tools](#adding-tools)
6. [Memory and Persistence](#memory-and-persistence)
7. [Knowledge Integration](#knowledge-integration)
8. [Multi-Agent Systems](#multi-agent-systems)
9. [Next Steps](#next-steps)

## Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed on your system
- **pip** package manager
- An **API key** from at least one AI provider (OpenAI, Anthropic, etc.)
- Basic familiarity with Python programming

### Checking Your Python Version

```bash
python --version
# Should output Python 3.8.x or higher
```

## Installation

### Basic Installation

Install GlobalGenie using pip:

```bash
pip install globalgenie
```

### Installation with Optional Dependencies

For specific features, install with optional dependencies:

```bash
# Web search and scraping capabilities
pip install globalgenie[web]

# Document processing (PDF, Word, etc.)
pip install globalgenie[docs]

# Vector database integrations
pip install globalgenie[vector]

# All optional dependencies
pip install globalgenie[all]
```

### Verify Installation

Test that GlobalGenie is installed correctly:

```python
import globalgenie
print(f"GlobalGenie version: {globalgenie.__version__}")
```

## Basic Configuration

### Environment Variables

Set up your API keys as environment variables:

```bash
# For OpenAI
export OPENAI_API_KEY="your-openai-api-key"

# For Anthropic
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# For Google
export GOOGLE_API_KEY="your-google-api-key"
```

### Configuration File (Optional)

Create a `globalgenie_config.py` file for advanced configuration:

```python
from globalgenie.config import GlobalGenieConfig
import os

config = GlobalGenieConfig(
    # API Keys
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    
    # Default Settings
    default_model="gpt-4",
    max_tokens=2000,
    temperature=0.7,
    
    # Memory Settings
    memory_backend="sqlite",
    memory_db_path="./agent_memory.db",
    
    # Vector Store Settings
    vector_store="chroma",
    vector_store_path="./vector_store",
    
    # Logging
    log_level="INFO",
    log_file="globalgenie.log"
)
```

## Your First Agent

Let's create a simple conversational agent:

### Step 1: Basic Agent

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

# Create a basic agent
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    instructions="You are a helpful AI assistant. Be concise and friendly."
)

# Have a conversation
response = agent.run("Hello! What can you help me with?")
print(response.content)
```

### Step 2: Interactive Chat

Create an interactive chat session:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

def chat_with_agent():
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        instructions="""
        You are a knowledgeable AI assistant. You should:
        - Be helpful and informative
        - Ask clarifying questions when needed
        - Provide step-by-step explanations for complex topics
        - Admit when you don't know something
        """
    )
    
    print("GlobalGenie Agent is ready! Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Agent: Goodbye! Have a great day!")
            break
        
        try:
            response = agent.run(user_input)
            print(f"Agent: {response.content}")
        except Exception as e:
            print(f"Error: {e}")

# Run the chat
chat_with_agent()
```

## Adding Tools

Tools extend your agent's capabilities beyond text generation. Let's add some useful tools:

### Step 1: Web Search Tool

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools

# Agent with web search capabilities
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    tools=[WebSearchTools()],
    instructions="""
    You are a research assistant with access to web search.
    Always search for current information when asked about:
    - Recent events or news
    - Current prices or statistics
    - Latest developments in any field
    
    Cite your sources when providing information.
    """
)

# Test the web search capability
response = agent.run("What are the latest developments in artificial intelligence this week?")
print(response.content)
```

### Step 2: Multiple Tools

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools
from globalgenie.tools.calculator import CalculatorTools
from globalgenie.tools.python import PythonTools

# Multi-tool agent
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    tools=[
        WebSearchTools(),
        CalculatorTools(),
        PythonTools()
    ],
    instructions="""
    You are a versatile AI assistant with multiple capabilities:
    
    1. Web Search: Use for current information, news, and research
    2. Calculator: Use for mathematical calculations
    3. Python: Use for data analysis, programming, and complex computations
    
    Choose the appropriate tool for each task and explain your reasoning.
    """
)

# Test multiple capabilities
test_queries = [
    "What's the current price of Bitcoin and calculate what $1000 would be worth?",
    "Find information about Python pandas library and show me a code example",
    "Calculate the compound interest on $5000 at 7% annual rate for 10 years"
]

for query in test_queries:
    print(f"\nQuery: {query}")
    response = agent.run(query)
    print(f"Response: {response.content}")
    print("-" * 50)
```

## Memory and Persistence

Add memory to your agents so they remember previous conversations:

### Step 1: Basic Memory

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.memory import SqliteMemory

# Agent with memory
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    memory=SqliteMemory(
        table_name="chat_history",
        db_file="agent_memory.db"
    ),
    instructions="""
    You are a personal AI assistant with memory.
    Remember important details about the user and reference them in future conversations.
    Build rapport by recalling previous interactions.
    """
)

# Have a conversation with memory
conversations = [
    "Hi, my name is Alex and I'm a software developer working on machine learning projects.",
    "What programming languages do you think I should focus on?",
    "I'm particularly interested in computer vision applications.",
    "Can you recommend some good resources for learning about neural networks?"
]

for message in conversations:
    print(f"\nUser: {message}")
    response = agent.run(message)
    print(f"Agent: {response.content}")
```

### Step 2: Advanced Memory with Sessions

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.memory import SqliteMemory

def create_agent_with_session(user_id: str):
    return Agent(
        model=OpenAIChat(id="gpt-4"),
        memory=SqliteMemory(
            table_name=f"user_{user_id}_memory",
            db_file="multi_user_memory.db"
        ),
        instructions=f"""
        You are a personal AI assistant for user {user_id}.
        Remember their preferences, interests, and previous conversations.
        Provide personalized responses based on their history.
        """
    )

# Simulate multiple users
users = ["alice", "bob", "charlie"]

for user in users:
    agent = create_agent_with_session(user)
    
    print(f"\n=== Conversation with {user.title()} ===")
    
    # Each user has different interests
    if user == "alice":
        response = agent.run("I love cooking and trying new recipes. What's a good dish for beginners?")
    elif user == "bob":
        response = agent.run("I'm into fitness and bodybuilding. Can you suggest a workout routine?")
    else:
        response = agent.run("I enjoy reading science fiction novels. Any recommendations?")
    
    print(f"Agent: {response.content}")
```

## Knowledge Integration

Add knowledge bases to your agents for domain-specific expertise:

### Step 1: Document Knowledge Base

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.knowledge import PDFKnowledgeBase
from globalgenie.tools.web import WebSearchTools

# Create a knowledge base from PDF documents
knowledge_base = PDFKnowledgeBase(
    path="./documents/",  # Directory containing PDF files
    vector_db="chroma",
    chunk_size=1000,
    chunk_overlap=200
)

# Agent with document knowledge
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    knowledge=knowledge_base,
    tools=[WebSearchTools()],
    instructions="""
    You are a knowledgeable assistant with access to a document library.
    
    When answering questions:
    1. First check your knowledge base for relevant information
    2. If needed, search the web for additional current information
    3. Combine both sources to provide comprehensive answers
    4. Always cite your sources
    """
)

# Query the knowledge base
response = agent.run("What are the key findings from the research papers about machine learning?")
print(response.content)
```

### Step 2: Web Knowledge Base

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.knowledge import WebKnowledgeBase

# Create knowledge base from websites
knowledge_base = WebKnowledgeBase(
    urls=[
        "https://docs.python.org/3/tutorial/",
        "https://pandas.pydata.org/docs/user_guide/",
        "https://scikit-learn.org/stable/user_guide.html"
    ],
    max_depth=2,  # How deep to crawl
    chunk_size=1000
)

# Python expert agent
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    knowledge=knowledge_base,
    instructions="""
    You are a Python programming expert with access to official documentation.
    
    Provide accurate, up-to-date information about:
    - Python language features
    - Pandas data manipulation
    - Scikit-learn machine learning
    
    Include code examples and best practices in your responses.
    """
)

# Ask Python questions
questions = [
    "How do I handle missing data in pandas DataFrames?",
    "What's the difference between lists and tuples in Python?",
    "How do I create a simple machine learning model with scikit-learn?"
]

for question in questions:
    print(f"\nQuestion: {question}")
    response = agent.run(question)
    print(f"Answer: {response.content}")
    print("-" * 80)
```

## Multi-Agent Systems

Create teams of specialized agents that work together:

### Step 1: Simple Agent Team

```python
from globalgenie.team import AgentTeam
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools
from globalgenie.tools.python import PythonTools

# Create specialized agents
researcher = Agent(
    name="researcher",
    model=OpenAIChat(id="gpt-4"),
    tools=[WebSearchTools()],
    instructions="""
    You are a research specialist. Your job is to:
    1. Gather comprehensive information on given topics
    2. Find current data and statistics
    3. Identify key trends and insights
    4. Provide well-sourced information to other team members
    """
)

analyst = Agent(
    name="analyst",
    model=OpenAIChat(id="gpt-4"),
    tools=[PythonTools()],
    instructions="""
    You are a data analyst. Your job is to:
    1. Process and analyze data provided by the researcher
    2. Create visualizations and statistical summaries
    3. Identify patterns and correlations
    4. Provide quantitative insights
    """
)

writer = Agent(
    name="writer",
    model=OpenAIChat(id="gpt-4"),
    instructions="""
    You are a technical writer. Your job is to:
    1. Synthesize information from researcher and analyst
    2. Create clear, well-structured reports
    3. Make complex information accessible
    4. Provide actionable recommendations
    """
)

# Create the team
team = AgentTeam(
    agents=[researcher, analyst, writer],
    workflow="sequential"  # researcher -> analyst -> writer
)

# Execute a complex task
task = "Create a comprehensive analysis of the electric vehicle market in 2025, including market size, key players, growth trends, and future projections."

result = team.run(task)
print("Team Result:")
print(result.content)
```

### Step 2: Collaborative Agent Team

```python
from globalgenie.team import AgentTeam
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools
from globalgenie.tools.calculator import CalculatorTools

# Create a collaborative team for financial analysis
market_researcher = Agent(
    name="market_researcher",
    model=OpenAIChat(id="gpt-4"),
    tools=[WebSearchTools()],
    instructions="""
    You specialize in market research and competitive analysis.
    Focus on market trends, competitor analysis, and industry insights.
    """
)

financial_analyst = Agent(
    name="financial_analyst", 
    model=OpenAIChat(id="gpt-4"),
    tools=[CalculatorTools(), WebSearchTools()],
    instructions="""
    You specialize in financial analysis and valuation.
    Focus on financial metrics, ratios, and quantitative analysis.
    """
)

risk_assessor = Agent(
    name="risk_assessor",
    model=OpenAIChat(id="gpt-4"),
    tools=[WebSearchTools()],
    instructions="""
    You specialize in risk assessment and regulatory analysis.
    Focus on identifying potential risks and compliance issues.
    """
)

# Collaborative team (agents can communicate with each other)
team = AgentTeam(
    agents=[market_researcher, financial_analyst, risk_assessor],
    workflow="collaborative",
    max_iterations=3
)

# Complex financial analysis task
task = """
Analyze Tesla (TSLA) as an investment opportunity. Consider:
1. Market position and competitive landscape
2. Financial performance and valuation metrics
3. Risk factors and regulatory challenges
4. Investment recommendation with rationale
"""

result = team.run(task)
print("Investment Analysis:")
print(result.content)
```

## Next Steps

Congratulations! You've learned the basics of GlobalGenie. Here's what to explore next:

### 1. Advanced Features
- **Custom Tools**: Build domain-specific tools for your use case
- **Advanced Memory**: Implement semantic and episodic memory systems
- **Workflow Orchestration**: Create complex multi-step processes
- **Model Fine-tuning**: Customize models for specific tasks

### 2. Production Deployment
- **API Integration**: Build REST APIs with your agents
- **Scaling**: Deploy agents in cloud environments
- **Monitoring**: Track agent performance and usage
- **Security**: Implement authentication and authorization

### 3. Specialized Use Cases
- **Customer Support**: Build intelligent chatbots
- **Content Creation**: Automate content generation workflows
- **Data Analysis**: Create automated reporting systems
- **Research Automation**: Build research and analysis pipelines

### 4. Community and Resources

- **📖 [Full Documentation](https://docs.globalgenie.com)** - Complete guides and API reference
- **💡 [Example Gallery](https://docs.globalgenie.com/examples)** - Real-world implementations
- **💬 [Discord Community](https://discord.gg/globalgenie)** - Get help and share ideas
- **🎓 [Tutorials](https://docs.globalgenie.com/tutorials)** - Step-by-step learning paths
- **📝 [Blog](https://blog.globalgenie.com)** - Latest updates and best practices

### 5. Contributing

Help improve GlobalGenie:
- **Report Issues**: Found a bug? Let us know!
- **Feature Requests**: Suggest new capabilities
- **Code Contributions**: Submit pull requests
- **Documentation**: Help improve our guides

---

**Ready to build something amazing?** Start with the [Example Gallery](https://docs.globalgenie.com/examples) or join our [Discord Community](https://discord.gg/globalgenie) to connect with other developers!