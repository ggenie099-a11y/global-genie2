# GlobalGenie Examples

This document provides practical examples of building AI agents with GlobalGenie. Each example includes complete, runnable code and explanations.

## Table of Contents

1. [Basic Examples](#basic-examples)
2. [Tool Integration Examples](#tool-integration-examples)
3. [Memory and Knowledge Examples](#memory-and-knowledge-examples)
4. [Multi-Agent Examples](#multi-agent-examples)
5. [Real-World Applications](#real-world-applications)
6. [Advanced Patterns](#advanced-patterns)

## Basic Examples

### 1. Simple Conversational Agent

Create a basic agent for general conversation:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

def create_conversational_agent():
    """Create a friendly conversational agent"""
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        instructions="""
        You are a helpful and friendly AI assistant. 
        - Be conversational and engaging
        - Ask follow-up questions when appropriate
        - Provide helpful and accurate information
        - Maintain a positive and supportive tone
        """
    )
    return agent

# Usage
agent = create_conversational_agent()

# Single interaction
response = agent.run("Hello! I'm new to AI. Can you explain what you can help me with?")
print(response.content)

# Interactive chat loop
def chat_loop():
    print("GlobalGenie Agent ready! Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Agent: Goodbye! Have a great day!")
            break
        
        response = agent.run(user_input)
        print(f"Agent: {response.content}\n")

# Uncomment to run interactive chat
# chat_loop()
```

### 2. Research Agent with Web Search

Create an agent that can search the web for current information:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools

def create_research_agent():
    """Create a research agent with web search capabilities"""
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        tools=[WebSearchTools(max_results=5)],
        instructions="""
        You are a research assistant with access to web search.
        
        For any query requiring current information:
        1. Search the web for the most recent data
        2. Analyze multiple sources for accuracy
        3. Synthesize information into a comprehensive response
        4. Always cite your sources
        5. Indicate when information might be outdated
        
        Be thorough but concise in your research.
        """
    )
    return agent

# Usage
researcher = create_research_agent()

research_queries = [
    "What are the latest developments in quantum computing in 2024?",
    "What's the current status of renewable energy adoption globally?",
    "Who won the latest Nobel Prize in Physics and what was their contribution?"
]

for query in research_queries:
    print(f"\nResearching: {query}")
    response = researcher.run(query)
    print(f"Findings: {response.content}")
    print(f"Sources used: {len(response.tool_calls)} web searches")
    print("-" * 100)
```

### 3. Agent with Memory

Create an agent that remembers conversations:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.memory import SqliteMemory

def create_memory_agent(user_id="default_user"):
    """Create an agent with persistent memory"""
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        memory=SqliteMemory(
            db_file=f"memory_{user_id}.db",
            table_name="conversations",
            max_memories=1000
        ),
        instructions=f"""
        You are a personal AI assistant for {user_id} with persistent memory.
        
        Remember and reference:
        - User's name, preferences, and interests
        - Previous conversations and topics discussed
        - Important dates, events, and commitments
        - User's goals and projects
        
        Build rapport by:
        - Referencing previous conversations naturally
        - Showing interest in ongoing projects
        - Remembering personal details
        - Following up on previous discussions
        """
    )
    return agent

# Usage - Simulate multiple conversation sessions
def simulate_user_sessions():
    agent = create_memory_agent("Alice")
    
    # Session 1: Introduction
    print("=== Session 1: First Meeting ===")
    response = agent.run("""
    Hi! I'm Alice, a software developer working on machine learning projects. 
    I'm particularly interested in computer vision and I'm currently working 
    on a project to detect objects in satellite imagery.
    """)
    print(f"Agent: {response.content}\n")
    
    # Session 2: Follow-up (simulating next day)
    print("=== Session 2: Next Day ===")
    response = agent.run("""
    Good morning! I made some progress on that satellite imagery project 
    we discussed. I'm having trouble with the accuracy of my model though.
    """)
    print(f"Agent: {response.content}\n")

simulate_user_sessions()
```

## Tool Integration Examples

### 4. Multi-Tool Agent

Create an agent with multiple complementary tools:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools
from globalgenie.tools.calculator import CalculatorTools
from globalgenie.tools.python import PythonTools

def create_versatile_assistant():
    """Create a versatile assistant with multiple tools"""
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        tools=[
            WebSearchTools(),
            CalculatorTools(),
            PythonTools()
        ],
        instructions="""
        You are a versatile AI assistant with access to multiple tools:
        
        1. Web Search: For current information and research
        2. Calculator: For mathematical calculations
        3. Python: For data analysis, programming, and complex computations
        
        Choose the most appropriate tool(s) for each task and combine 
        multiple tools to solve complex problems.
        """
    )
    return agent

# Usage
assistant = create_versatile_assistant()

complex_tasks = [
    """
    I need to research the current Bitcoin price, calculate what my $5000 investment 
    from last year would be worth now (assuming I bought at $30,000), and create 
    a simple chart showing the potential profit/loss.
    """,
    
    """
    Find information about the top 5 programming languages in 2024, then create 
    a Python script that generates a bar chart comparing their popularity scores.
    """
]

for i, task in enumerate(complex_tasks, 1):
    print(f"\n{'='*20} Task {i} {'='*20}")
    print(f"Task: {task.strip()}")
    print("\nAssistant working...")
    
    response = assistant.run(task)
    print(f"\nResult: {response.content}")
    print(f"Tools used: {[call.tool_name for call in response.tool_calls]}")
    print("-" * 80)
```

## Multi-Agent Examples

### 5. Research Team

Create a team of specialized agents for comprehensive research:

```python
from globalgenie.team import AgentTeam
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools
from globalgenie.tools.python import PythonTools

def create_research_team():
    """Create a team of specialized research agents"""
    
    # Information Gatherer
    researcher = Agent(
        name="researcher",
        model=OpenAIChat(id="gpt-4"),
        tools=[WebSearchTools(max_results=10)],
        instructions="""
        You are a research specialist focused on information gathering.
        
        Your responsibilities:
        1. Search for comprehensive information on given topics
        2. Find multiple reliable sources
        3. Gather both current and historical data
        4. Collect quantitative data and statistics
        
        Always provide source URLs and assess data credibility.
        """
    )
    
    # Data Analyst
    analyst = Agent(
        name="analyst",
        model=OpenAIChat(id="gpt-4"),
        tools=[PythonTools()],
        instructions="""
        You are a data analyst who processes research findings.
        
        Your responsibilities:
        1. Analyze quantitative data from research
        2. Identify patterns and trends
        3. Create visualizations and charts
        4. Perform statistical analysis
        
        Always provide statistical summaries and data visualizations.
        """
    )
    
    # Report Writer
    writer = Agent(
        name="writer",
        model=OpenAIChat(id="gpt-4"),
        instructions="""
        You are a research synthesizer who creates comprehensive reports.
        
        Your responsibilities:
        1. Combine findings from researcher and analyst
        2. Identify key insights and implications
        3. Create structured, coherent reports
        4. Provide actionable recommendations
        
        Always provide executive summary and clear recommendations.
        """
    )
    
    team = AgentTeam(
        agents=[researcher, analyst, writer],
        workflow="sequential"
    )
    
    return team

# Usage
research_team = create_research_team()

research_topic = """
Research Topic: Electric Vehicle Market Analysis 2024

Please provide a comprehensive analysis covering:
1. Current market size and growth projections
2. Key players and market share
3. Technology trends and innovations
4. Consumer adoption patterns
5. Government policies and incentives
6. Future outlook and predictions
"""

print("Team working on research...")
result = research_team.run(research_topic)
print(f"\nFinal Report:\n{result.content}")
print(f"\nTeam Performance:")
print(f"- Total agents involved: {len(result.agent_responses)}")
print(f"- Total execution time: {result.execution_time:.2f} seconds")
```

## Real-World Applications

### 6. Customer Support Agent

Create an intelligent customer support system:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.memory import SqliteMemory
from globalgenie.knowledge import TextKnowledgeBase

def create_support_agent():
    """Create a customer support agent"""
    
    # Knowledge base with common support information
    support_kb = TextKnowledgeBase(
        texts=[
            """
            Product Information - GlobalGenie Pro:
            
            Features:
            - Advanced AI agent creation
            - Multi-model support (OpenAI, Anthropic, Google)
            - Persistent memory and knowledge bases
            - Tool integration (web search, calculators, file operations)
            - Multi-agent team collaboration
            
            Pricing:
            - Starter Plan: $29/month - Up to 5 agents, 10,000 API calls
            - Professional Plan: $99/month - Up to 25 agents, 100,000 API calls
            - Enterprise Plan: $299/month - Unlimited agents, 1M API calls
            """,
            
            """
            Common Issues and Solutions:
            
            Installation Problems:
            - Ensure Python 3.8+ is installed
            - Use virtual environments to avoid conflicts
            - Install with: pip install globalgenie
            
            API Key Issues:
            - Set environment variables: OPENAI_API_KEY, ANTHROPIC_API_KEY
            - Verify API keys are valid and have sufficient credits
            - Check for typos in API key configuration
            """
        ],
        vector_db="chroma",
        collection_name="support_knowledge"
    )
    
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        memory=SqliteMemory(
            db_file="support_conversations.db",
            table_name="customer_support"
        ),
        knowledge=support_kb,
        instructions="""
        You are a helpful customer support agent for GlobalGenie.
        
        Your approach:
        1. Greet customers warmly and professionally
        2. Listen carefully to understand their issue
        3. Search your knowledge base for relevant solutions
        4. Provide clear, step-by-step instructions
        5. Follow up to ensure the issue is resolved
        
        Always be patient, empathetic, and provide specific solutions.
        """
    )
    
    return agent

# Usage
support_agent = create_support_agent()

# Example support conversation
customer_message = """
Hi, I'm trying to install GlobalGenie but I keep getting an error that says 
"No module named 'globalgenie'" even after running pip install. I'm using 
Python 3.9 on Windows. Can you help?
"""

response = support_agent.run(customer_message, user_id="customer_001")
print(f"Customer: {customer_message.strip()}")
print(f"Support: {response.content}")
```

### 7. Financial Analysis Agent

Create an agent for financial analysis:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.web import WebSearchTools
from globalgenie.tools.calculator import CalculatorTools
from globalgenie.tools.python import PythonTools

def create_financial_analyst():
    """Create a financial analysis agent"""
    agent = Agent(
        model=OpenAIChat(id="gpt-4"),
        tools=[
            WebSearchTools(),
            CalculatorTools(),
            PythonTools()
        ],
        instructions="""
        You are a financial analyst with expertise in:
        - Financial statement analysis
        - Investment valuation
        - Risk assessment
        - Market analysis
        
        When conducting analysis:
        1. Gather current financial data and market information
        2. Perform quantitative analysis using appropriate metrics
        3. Create visualizations to illustrate findings
        4. Assess risks and opportunities
        5. Provide clear, actionable recommendations
        
        Always use current market data and show your calculations.
        """
    )
    return agent

# Usage
financial_analyst = create_financial_analyst()

analysis_request = """
Please analyze Apple Inc. (AAPL) as an investment opportunity. Include:
1. Current stock price and recent performance
2. Key financial metrics (P/E, P/B, ROE, etc.)
3. Revenue and earnings trends
4. Competitive position and market outlook
5. Risk factors and investment recommendation

Provide a comprehensive investment thesis with supporting data.
"""

print("Analyst working...")
response = financial_analyst.run(analysis_request)
print(f"\nAnalysis Report:\n{response.content}")
print(f"\nTools used: {[call.tool_name for call in response.tool_calls]}")
```

## Next Steps

These examples demonstrate the power and flexibility of GlobalGenie for building sophisticated AI agents. To continue learning:

1. **Experiment with the examples** - Modify the code to suit your specific needs
2. **Combine patterns** - Mix and match different approaches for complex applications
3. **Build custom tools** - Create domain-specific tools for your use cases
4. **Explore advanced features** - Try async operations, caching, and monitoring
5. **Join the community** - Share your creations and learn from others

### Resources

- **📖 [Complete Documentation](https://docs.globalgenie.com)** - Comprehensive guides and tutorials
- **🛠️ [API Reference](https://docs.globalgenie.com/api)** - Detailed API documentation
- **💬 [Discord Community](https://discord.gg/globalgenie)** - Connect with other developers
- **📝 [Blog](https://blog.globalgenie.com)** - Latest updates and advanced tutorials

Happy building with GlobalGenie! 🚀