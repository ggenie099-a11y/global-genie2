# GlobalGenie Troubleshooting Guide

This guide helps you resolve common issues when using GlobalGenie. If you can't find a solution here, please check our [FAQ](#frequently-asked-questions) or reach out to our [community support](#getting-help).

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [Configuration Problems](#configuration-problems)
3. [Model and API Issues](#model-and-api-issues)
4. [Memory and Storage Issues](#memory-and-storage-issues)
5. [Tool Integration Problems](#tool-integration-problems)
6. [Performance Issues](#performance-issues)
7. [Agent Behavior Issues](#agent-behavior-issues)
8. [Multi-Agent System Issues](#multi-agent-system-issues)
9. [Frequently Asked Questions](#frequently-asked-questions)
10. [Getting Help](#getting-help)

## Installation Issues

### Problem: pip install globalgenie fails

**Symptoms:**
- Package not found error
- Permission denied errors
- Dependency conflicts

**Solutions:**

1. **Update pip and try again:**
   ```bash
   pip install --upgrade pip
   pip install globalgenie
   ```

2. **Use virtual environment:**
   ```bash
   python -m venv globalgenie_env
   source globalgenie_env/bin/activate  # On Windows: globalgenie_env\Scripts\activate
   pip install globalgenie
   ```

3. **Install with user flag:**
   ```bash
   pip install --user globalgenie
   ```

4. **Clear pip cache:**
   ```bash
   pip cache purge
   pip install globalgenie
   ```

### Problem: Import errors after installation

**Symptoms:**
```python
ImportError: No module named 'globalgenie'
ModuleNotFoundError: No module named 'globalgenie.agent'
```

**Solutions:**

1. **Verify installation:**
   ```bash
   pip list | grep globalgenie
   python -c "import globalgenie; print(globalgenie.__version__)"
   ```

2. **Check Python path:**
   ```python
   import sys
   print(sys.path)
   ```

3. **Reinstall in correct environment:**
   ```bash
   pip uninstall globalgenie
   pip install globalgenie
   ```

### Problem: Optional dependencies not working

**Symptoms:**
- Web tools not available
- Vector database errors
- Document processing failures

**Solutions:**

1. **Install with all dependencies:**
   ```bash
   pip install globalgenie[all]
   ```

2. **Install specific feature sets:**
   ```bash
   pip install globalgenie[web]      # Web tools
   pip install globalgenie[docs]     # Document processing
   pip install globalgenie[vector]   # Vector databases
   ```

3. **Manual dependency installation:**
   ```bash
   pip install requests beautifulsoup4 selenium  # Web tools
   pip install PyPDF2 python-docx                # Document processing
   pip install chromadb pinecone-client          # Vector databases
   ```

## Configuration Problems

### Problem: API key not recognized

**Symptoms:**
```
AuthenticationError: Invalid API key
ConfigurationError: API key not found
```

**Solutions:**

1. **Set environment variables:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   export ANTHROPIC_API_KEY="your-anthropic-key-here"
   ```

2. **Verify environment variables:**
   ```bash
   echo $OPENAI_API_KEY
   ```

3. **Set in Python code:**
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key-here"
   
   from globalgenie.models.openai import OpenAIChat
   model = OpenAIChat(api_key="your-api-key-here")
   ```

4. **Use configuration file:**
   ```python
   from globalgenie.config import GlobalGenieConfig
   
   config = GlobalGenieConfig(
       openai_api_key="your-api-key-here",
       anthropic_api_key="your-anthropic-key-here"
   )
   ```

### Problem: Configuration not loading

**Symptoms:**
- Default settings not applied
- Custom configuration ignored

**Solutions:**

1. **Check configuration file location:**
   ```python
   from globalgenie.config import get_config_path
   print(get_config_path())
   ```

2. **Explicitly load configuration:**
   ```python
   from globalgenie.config import load_config
   config = load_config("path/to/your/config.py")
   ```

3. **Verify configuration syntax:**
   ```python
   from globalgenie.config import validate_config
   is_valid = validate_config(config)
   print(is_valid)
   ```

## Model and API Issues

### Problem: Model not responding

**Symptoms:**
- Timeout errors
- No response from agent
- Connection errors

**Solutions:**

1. **Check API status:**
   ```python
   from globalgenie.models.openai import OpenAIChat
   
   model = OpenAIChat(id="gpt-4")
   try:
       response = model.test_connection()
       print("Connection successful")
   except Exception as e:
       print(f"Connection failed: {e}")
   ```

2. **Increase timeout:**
   ```python
   model = OpenAIChat(id="gpt-4", timeout=60)
   ```

3. **Use fallback model:**
   ```python
   from globalgenie.agent import Agent
   
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       fallback_model=OpenAIChat(id="gpt-3.5-turbo")
   )
   ```

4. **Check rate limits:**
   ```python
   import time
   
   # Add delay between requests
   response1 = agent.run("Hello")
   time.sleep(1)
   response2 = agent.run("How are you?")
   ```

### Problem: Unexpected model responses

**Symptoms:**
- Inconsistent behavior
- Poor quality responses
- Hallucinations

**Solutions:**

1. **Adjust temperature:**
   ```python
   agent = Agent(
       model=OpenAIChat(id="gpt-4", temperature=0.1),  # More deterministic
       instructions="Be precise and factual."
   )
   ```

2. **Improve instructions:**
   ```python
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       instructions="""
       You are a helpful assistant. Follow these guidelines:
       1. Be accurate and factual
       2. If you're unsure, say so
       3. Provide step-by-step explanations
       4. Use tools when appropriate
       """
   )
   ```

3. **Add validation:**
   ```python
   def validate_response(response):
       # Add your validation logic
       if len(response.content) < 10:
           return False
       return True
   
   response = agent.run("Question")
   if not validate_response(response):
       response = agent.run("Please provide a more detailed answer")
   ```

## Memory and Storage Issues

### Problem: Memory not persisting

**Symptoms:**
- Agent doesn't remember previous conversations
- Memory database not created
- Data loss between sessions

**Solutions:**

1. **Check database file permissions:**
   ```bash
   ls -la agent_memory.db
   chmod 664 agent_memory.db
   ```

2. **Verify memory configuration:**
   ```python
   from globalgenie.memory import SqliteMemory
   
   memory = SqliteMemory(
       db_file="agent_memory.db",
       table_name="conversations"
   )
   
   # Test memory
   memory.add_memory("Test memory")
   memories = memory.get_memories()
   print(f"Stored memories: {len(memories)}")
   ```

3. **Use absolute paths:**
   ```python
   import os
   
   memory = SqliteMemory(
       db_file=os.path.abspath("agent_memory.db")
   )
   ```

4. **Check database connectivity:**
   ```python
   from globalgenie.memory import PostgresMemory
   
   try:
       memory = PostgresMemory(
           connection_string="postgresql://user:pass@localhost/db"
       )
       memory.test_connection()
   except Exception as e:
       print(f"Database connection failed: {e}")
   ```

### Problem: Vector database errors

**Symptoms:**
- ChromaDB connection errors
- Embedding failures
- Search not working

**Solutions:**

1. **Install vector database dependencies:**
   ```bash
   pip install chromadb
   pip install pinecone-client
   pip install weaviate-client
   ```

2. **Check vector store configuration:**
   ```python
   from globalgenie.knowledge import PDFKnowledgeBase
   
   try:
       kb = PDFKnowledgeBase(
           path="./documents",
           vector_db="chroma",
           collection_name="test_collection"
       )
       kb.test_connection()
   except Exception as e:
       print(f"Vector store error: {e}")
   ```

3. **Clear vector database:**
   ```python
   import shutil
   shutil.rmtree("./chroma_db")  # Remove ChromaDB directory
   ```

## Tool Integration Problems

### Problem: Tools not working

**Symptoms:**
- Tool execution failures
- Permission errors
- Import errors for tool dependencies

**Solutions:**

1. **Install tool dependencies:**
   ```bash
   pip install requests beautifulsoup4  # Web tools
   pip install selenium webdriver-manager  # Browser automation
   pip install pandas numpy matplotlib  # Data tools
   ```

2. **Check tool permissions:**
   ```python
   from globalgenie.tools.file import FileTools
   
   file_tools = FileTools(
       base_directory="./",
       allowed_extensions=[".txt", ".csv", ".json"]
   )
   
   # Test tool
   try:
       result = file_tools.read_file("test.txt")
       print("File tool working")
   except Exception as e:
       print(f"File tool error: {e}")
   ```

3. **Debug tool execution:**
   ```python
   from globalgenie.agent import Agent
   from globalgenie.models.openai import OpenAIChat
   from globalgenie.tools.web import WebSearchTools
   
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       tools=[WebSearchTools()],
       debug=True  # Enable debug logging
   )
   ```

### Problem: Custom tools not recognized

**Symptoms:**
- Custom tool not available to agent
- Tool execution errors

**Solutions:**

1. **Verify tool implementation:**
   ```python
   from globalgenie.tools import Tool
   
   class MyTool(Tool):
       def __init__(self):
           super().__init__(
               name="my_tool",
               description="My custom tool"
           )
       
       def run(self, **kwargs):
           return "Tool executed successfully"
   
   # Test tool
   tool = MyTool()
   result = tool.run()
   print(result)
   ```

2. **Register tool properly:**
   ```python
   from globalgenie.agent import Agent
   
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       tools=[MyTool()]
   )
   
   # Verify tool is registered
   print(f"Available tools: {[tool.name for tool in agent.tools]}")
   ```

## Performance Issues

### Problem: Slow response times

**Symptoms:**
- Long delays in agent responses
- Timeout errors
- High latency

**Solutions:**

1. **Optimize model selection:**
   ```python
   # Use faster models for simple tasks
   agent = Agent(
       model=OpenAIChat(id="gpt-3.5-turbo"),  # Faster than GPT-4
       max_tokens=500  # Limit response length
   )
   ```

2. **Implement caching:**
   ```python
   from globalgenie.cache import ResponseCache
   
   cache = ResponseCache(backend="redis")
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       cache=cache
   )
   ```

3. **Use async operations:**
   ```python
   import asyncio
   from globalgenie.agent import AsyncAgent
   
   async def process_multiple_queries():
       agent = AsyncAgent(model=OpenAIChat(id="gpt-4"))
       
       tasks = [
           agent.run("Query 1"),
           agent.run("Query 2"),
           agent.run("Query 3")
       ]
       
       results = await asyncio.gather(*tasks)
       return results
   ```

4. **Optimize knowledge base:**
   ```python
   from globalgenie.knowledge import PDFKnowledgeBase
   
   kb = PDFKnowledgeBase(
       path="./documents",
       chunk_size=500,  # Smaller chunks
       max_results=3    # Limit search results
   )
   ```

### Problem: High memory usage

**Symptoms:**
- Out of memory errors
- System slowdown
- Process killed

**Solutions:**

1. **Limit memory usage:**
   ```python
   from globalgenie.memory import SqliteMemory
   
   memory = SqliteMemory(
       max_memories=1000,  # Limit stored memories
       cleanup_interval=100  # Regular cleanup
   )
   ```

2. **Use streaming responses:**
   ```python
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       stream=True
   )
   
   for chunk in agent.run_stream("Long query"):
       print(chunk, end="")
   ```

3. **Implement memory cleanup:**
   ```python
   import gc
   
   # Periodic cleanup
   response = agent.run("Query")
   gc.collect()  # Force garbage collection
   ```

## Agent Behavior Issues

### Problem: Agent not following instructions

**Symptoms:**
- Ignoring system instructions
- Inconsistent behavior
- Not using tools appropriately

**Solutions:**

1. **Improve instruction clarity:**
   ```python
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       instructions="""
       IMPORTANT RULES:
       1. Always search the web for current information
       2. Use the calculator for any mathematical operations
       3. Be concise but thorough in your responses
       4. If you're unsure, ask for clarification
       
       NEVER:
       - Make up information
       - Ignore available tools
       - Provide outdated information
       """
   )
   ```

2. **Add validation and feedback:**
   ```python
   def validate_agent_response(response, expected_tools=None):
       if expected_tools:
           used_tools = [call.tool_name for call in response.tool_calls]
           if not any(tool in used_tools for tool in expected_tools):
               return False, "Expected tools not used"
       return True, "Valid response"
   
   response = agent.run("What's the current weather in New York?")
   is_valid, message = validate_agent_response(response, ["web_search"])
   
   if not is_valid:
       response = agent.run(f"Please use web search to find current weather. {message}")
   ```

3. **Use examples in instructions:**
   ```python
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       instructions="""
       You are a research assistant. Here are examples of good responses:
       
       User: "What's the latest news about AI?"
       Good response: *searches web* "Based on my search, here are the latest AI developments..."
       
       User: "Calculate 15% of 250"
       Good response: *uses calculator* "15% of 250 = 37.5"
       
       Always follow these patterns.
       """
   )
   ```

### Problem: Agent getting stuck in loops

**Symptoms:**
- Repeated tool calls
- Infinite reasoning loops
- No final answer

**Solutions:**

1. **Set iteration limits:**
   ```python
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       max_iterations=5,  # Limit tool use iterations
       tools=[WebSearchTools(), CalculatorTools()]
   )
   ```

2. **Add loop detection:**
   ```python
   class LoopDetectionAgent(Agent):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.tool_call_history = []
       
       def run(self, message, **kwargs):
           self.tool_call_history = []
           return super().run(message, **kwargs)
       
       def _execute_tool(self, tool_call):
           # Check for repeated tool calls
           if tool_call in self.tool_call_history[-3:]:
               raise Exception("Loop detected in tool calls")
           
           self.tool_call_history.append(tool_call)
           return super()._execute_tool(tool_call)
   ```

## Multi-Agent System Issues

### Problem: Agents not collaborating properly

**Symptoms:**
- Poor coordination between agents
- Duplicate work
- Communication failures

**Solutions:**

1. **Improve agent roles:**
   ```python
   from globalgenie.team import AgentTeam
   
   researcher = Agent(
       name="researcher",
       model=OpenAIChat(id="gpt-4"),
       instructions="""
       You are a researcher. Your ONLY job is to gather information.
       - Search for relevant data
       - Summarize findings
       - Pass information to the analyst
       - Do NOT analyze or draw conclusions
       """
   )
   
   analyst = Agent(
       name="analyst",
       model=OpenAIChat(id="gpt-4"),
       instructions="""
       You are an analyst. Your ONLY job is to analyze data.
       - Receive information from the researcher
       - Perform analysis and calculations
       - Identify patterns and insights
       - Pass results to the writer
       """
   )
   ```

2. **Add coordination mechanisms:**
   ```python
   team = AgentTeam(
       agents=[researcher, analyst, writer],
       workflow="sequential",
       coordination_prompt="""
       Each agent should:
       1. Clearly state what they received from the previous agent
       2. Explain what they're doing
       3. Clearly state what they're passing to the next agent
       """
   )
   ```

3. **Implement handoff validation:**
   ```python
   def validate_handoff(from_agent, to_agent, data):
       required_fields = {
           "researcher": ["sources", "data", "summary"],
           "analyst": ["analysis", "insights", "recommendations"],
           "writer": ["final_report"]
       }
       
       if to_agent.name in required_fields:
           missing = [field for field in required_fields[to_agent.name] 
                     if field not in data]
           if missing:
               raise ValueError(f"Missing required fields: {missing}")
   ```

## Frequently Asked Questions

### General Questions

**Q: What's the difference between GlobalGenie and other AI frameworks?**

A: GlobalGenie is specifically designed for building autonomous AI agents with advanced capabilities like persistent memory, knowledge integration, and multi-agent collaboration. Unlike simple chatbot frameworks, GlobalGenie agents can:
- Remember conversations across sessions
- Access and reason over large knowledge bases
- Use tools to interact with external systems
- Work together in teams to solve complex problems

**Q: Which AI models does GlobalGenie support?**

A: GlobalGenie supports 25+ AI models including:
- OpenAI: GPT-4, GPT-3.5 Turbo, GPT-4 Turbo
- Anthropic: Claude 3 (Opus, Sonnet, Haiku), Claude 2.1
- Google: Gemini Pro, Gemini Pro Vision
- Local models: Ollama, Hugging Face Transformers
- Cloud providers: AWS Bedrock, Azure OpenAI, Google Vertex AI

**Q: Can I use GlobalGenie without an internet connection?**

A: Partially. You can use local models (like Ollama) for offline operation, but many features require internet connectivity:
- Cloud-based AI models (OpenAI, Anthropic, Google)
- Web search tools
- Online knowledge bases
- Cloud vector databases

### Technical Questions

**Q: How do I handle rate limits from AI providers?**

A: GlobalGenie includes built-in rate limiting and retry mechanisms:

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(
        id="gpt-4",
        rate_limit=60,  # Requests per minute
        retry_attempts=3,
        retry_delay=1.0
    )
)
```

**Q: Can I use multiple AI models in the same agent?**

A: Yes, you can use fallback models and model switching:

```python
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    fallback_model=OpenAIChat(id="gpt-3.5-turbo"),
    model_selection_strategy="cost_optimized"
)
```

**Q: How do I secure my GlobalGenie application?**

A: Follow these security best practices:

```python
from globalgenie.config import GlobalGenieConfig

config = GlobalGenieConfig(
    # Use environment variables for API keys
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    
    # Enable sandbox mode for tool execution
    sandbox_mode=True,
    
    # Restrict allowed tools
    allowed_tools=["web_search", "calculator"],
    
    # Set resource limits
    max_tokens=1000,
    max_execution_time=30
)
```

**Q: How do I monitor agent performance?**

A: Use GlobalGenie's built-in monitoring:

```python
from globalgenie.monitoring import AgentMonitor

monitor = AgentMonitor(agent)
monitor.start()

# Get metrics
metrics = monitor.get_metrics()
print(f"Response time: {metrics['avg_response_time']}")
print(f"Token usage: {metrics['total_tokens']}")
print(f"Error rate: {metrics['error_rate']}")
```

### Deployment Questions

**Q: Can I deploy GlobalGenie agents in production?**

A: Yes, GlobalGenie is production-ready. Consider these deployment options:

1. **REST API deployment:**
```python
from fastapi import FastAPI
from globalgenie.agent import Agent

app = FastAPI()
agent = Agent(model=OpenAIChat(id="gpt-4"))

@app.post("/chat")
async def chat(message: str):
    response = await agent.run(message)
    return {"response": response.content}
```

2. **Docker deployment:**
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install globalgenie
CMD ["python", "app.py"]
```

**Q: How do I scale GlobalGenie for high traffic?**

A: Use these scaling strategies:

1. **Load balancing:**
```python
from globalgenie.scaling import LoadBalancer

balancer = LoadBalancer([
    Agent(model=OpenAIChat(id="gpt-4")),
    Agent(model=OpenAIChat(id="gpt-4")),
    Agent(model=OpenAIChat(id="gpt-4"))
])
```

2. **Async processing:**
```python
import asyncio
from globalgenie.agent import AsyncAgent

async def handle_requests(requests):
    agent = AsyncAgent(model=OpenAIChat(id="gpt-4"))
    tasks = [agent.run(req) for req in requests]
    return await asyncio.gather(*tasks)
```

**Q: What are the system requirements?**

A: Minimum requirements:
- Python 3.8+
- 4GB RAM (8GB+ recommended)
- 1GB disk space
- Internet connection (for cloud models)

For production:
- Python 3.9+
- 16GB+ RAM
- SSD storage
- Load balancer
- Monitoring system

## Getting Help

If you're still experiencing issues after trying these solutions:

### Community Support

- **💬 [Discord Community](https://discord.gg/globalgenie)** - Get help from other developers
- **📧 [Email Support](mailto:support@globalgenie.com)** - Direct support from our team
- **🐛 [GitHub Issues](https://github.com/globalgenie-agi/globalgenie/issues)** - Report bugs and request features

### Documentation

- **📖 [Complete Documentation](https://docs.globalgenie.com)** - Comprehensive guides
- **💡 [Examples Gallery](https://docs.globalgenie.com/examples)** - Working code examples
- **🛠️ [API Reference](https://docs.globalgenie.com/api)** - Detailed API documentation

### When Reporting Issues

Please include:

1. **GlobalGenie version:** `pip show globalgenie`
2. **Python version:** `python --version`
3. **Operating system:** Windows/macOS/Linux
4. **Error message:** Full error traceback
5. **Minimal code example:** Code that reproduces the issue
6. **Expected behavior:** What you expected to happen
7. **Actual behavior:** What actually happened

### Debug Information

Enable debug logging to get more information:

```python
import logging
from globalgenie.utils.logging import setup_logging

setup_logging(level="DEBUG")

# Your GlobalGenie code here
agent = Agent(model=OpenAIChat(id="gpt-4"), debug=True)
```

This will provide detailed logs that can help identify the issue.

---

**Still need help?** Don't hesitate to reach out to our community or support team. We're here to help you succeed with GlobalGenie!