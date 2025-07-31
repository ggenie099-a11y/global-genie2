# GlobalGenie API Reference

This document provides comprehensive API documentation for GlobalGenie, covering all classes, methods, and configuration options.

## Table of Contents

1. [Core Classes](#core-classes)
2. [Models](#models)
3. [Tools](#tools)
4. [Memory Systems](#memory-systems)
5. [Knowledge Bases](#knowledge-bases)
6. [Agent Teams](#agent-teams)
7. [Configuration](#configuration)
8. [Utilities](#utilities)

## Core Classes

### Agent

The main class for creating AI agents.

```python
from globalgenie.agent import Agent
```

#### Constructor

```python
Agent(
    model: BaseModel,
    tools: Optional[List[Tool]] = None,
    memory: Optional[BaseMemory] = None,
    knowledge: Optional[BaseKnowledge] = None,
    instructions: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    max_iterations: int = 10,
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
    stream: bool = False,
    debug: bool = False
)
```

**Parameters:**
- `model` (BaseModel): The AI model to use for the agent
- `tools` (List[Tool], optional): List of tools available to the agent
- `memory` (BaseMemory, optional): Memory system for the agent
- `knowledge` (BaseKnowledge, optional): Knowledge base for the agent
- `instructions` (str, optional): System instructions for the agent
- `name` (str, optional): Name identifier for the agent
- `description` (str, optional): Description of the agent's purpose
- `max_iterations` (int): Maximum number of tool use iterations
- `temperature` (float): Sampling temperature for model responses
- `max_tokens` (int, optional): Maximum tokens in response
- `stream` (bool): Whether to stream responses
- `debug` (bool): Enable debug logging

#### Methods

##### run()

Execute a single interaction with the agent.

```python
def run(
    self,
    message: str,
    session_id: Optional[str] = None,
    user_id: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None
) -> AgentResponse
```

**Parameters:**
- `message` (str): The input message or query
- `session_id` (str, optional): Session identifier for memory
- `user_id` (str, optional): User identifier for personalization
- `context` (Dict, optional): Additional context for the interaction

**Returns:**
- `AgentResponse`: Response object containing content, metadata, and tool usage

##### chat()

Start an interactive chat session.

```python
def chat(
    self,
    session_id: Optional[str] = None,
    user_id: Optional[str] = None
) -> None
```

##### add_tool()

Add a tool to the agent.

```python
def add_tool(self, tool: Tool) -> None
```

##### remove_tool()

Remove a tool from the agent.

```python
def remove_tool(self, tool_name: str) -> None
```

##### save_state()

Save the agent's current state.

```python
def save_state(self, filepath: str) -> None
```

##### load_state()

Load a previously saved agent state.

```python
def load_state(self, filepath: str) -> None
```

### AgentResponse

Response object returned by agent interactions.

```python
class AgentResponse:
    content: str                    # The main response content
    metadata: Dict[str, Any]        # Response metadata
    tool_calls: List[ToolCall]      # Tools used in the response
    tokens_used: int                # Number of tokens consumed
    response_time: float            # Response time in seconds
    session_id: Optional[str]       # Session identifier
    user_id: Optional[str]          # User identifier
```

## Models

### OpenAI Models

```python
from globalgenie.models.openai import OpenAIChat
```

#### OpenAIChat

```python
OpenAIChat(
    id: str = "gpt-4",
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
    top_p: float = 1.0,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    timeout: int = 30
)
```

**Supported Models:**
- `gpt-4` - GPT-4 (8K context)
- `gpt-4-32k` - GPT-4 (32K context)
- `gpt-4-turbo` - GPT-4 Turbo (128K context)
- `gpt-3.5-turbo` - GPT-3.5 Turbo (4K context)
- `gpt-3.5-turbo-16k` - GPT-3.5 Turbo (16K context)

### Anthropic Models

```python
from globalgenie.models.anthropic import Claude
```

#### Claude

```python
Claude(
    id: str = "claude-3-sonnet-20240229",
    api_key: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 4096,
    timeout: int = 30
)
```

**Supported Models:**
- `claude-3-opus-20240229` - Claude 3 Opus
- `claude-3-sonnet-20240229` - Claude 3 Sonnet
- `claude-3-haiku-20240307` - Claude 3 Haiku
- `claude-2.1` - Claude 2.1
- `claude-instant-1.2` - Claude Instant

### Google Models

```python
from globalgenie.models.google import Gemini
```

#### Gemini

```python
Gemini(
    id: str = "gemini-pro",
    api_key: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
    top_p: float = 1.0,
    top_k: int = 40
)
```

**Supported Models:**
- `gemini-pro` - Gemini Pro
- `gemini-pro-vision` - Gemini Pro Vision
- `gemini-ultra` - Gemini Ultra

### Local Models

```python
from globalgenie.models.ollama import Ollama
```

#### Ollama

```python
Ollama(
    id: str = "llama2",
    host: str = "http://localhost:11434",
    temperature: float = 0.7,
    timeout: int = 30
)
```

## Tools

### Base Tool Class

```python
from globalgenie.tools import Tool

class CustomTool(Tool):
    def __init__(self, name: str, description: str):
        super().__init__(name=name, description=description)
    
    def run(self, **kwargs) -> Any:
        # Tool implementation
        pass
```

### Web Tools

```python
from globalgenie.tools.web import WebSearchTools, WebScrapingTools
```

#### WebSearchTools

```python
WebSearchTools(
    provider: str = "duckduckgo",  # "duckduckgo", "google", "bing"
    max_results: int = 5,
    timeout: int = 10
)
```

**Methods:**
- `search(query: str, max_results: int = None) -> List[Dict]`
- `search_news(query: str, max_results: int = None) -> List[Dict]`
- `search_images(query: str, max_results: int = None) -> List[Dict]`

#### WebScrapingTools

```python
WebScrapingTools(
    timeout: int = 10,
    max_content_length: int = 100000
)
```

**Methods:**
- `scrape_url(url: str) -> Dict[str, Any]`
- `extract_text(url: str) -> str`
- `extract_links(url: str) -> List[str]`

### Calculator Tools

```python
from globalgenie.tools.calculator import CalculatorTools

CalculatorTools()
```

**Methods:**
- `calculate(expression: str) -> float`
- `solve_equation(equation: str) -> Dict[str, Any]`
- `plot_function(function: str, x_range: Tuple[float, float]) -> str`

### Python Tools

```python
from globalgenie.tools.python import PythonTools

PythonTools(
    timeout: int = 30,
    max_execution_time: int = 60,
    allowed_imports: Optional[List[str]] = None
)
```

**Methods:**
- `execute_code(code: str) -> Dict[str, Any]`
- `install_package(package: str) -> bool`
- `create_visualization(data: Any, chart_type: str) -> str`

### File Tools

```python
from globalgenie.tools.file import FileTools

FileTools(
    base_directory: str = "./",
    allowed_extensions: Optional[List[str]] = None
)
```

**Methods:**
- `read_file(filepath: str) -> str`
- `write_file(filepath: str, content: str) -> bool`
- `list_files(directory: str) -> List[str]`
- `delete_file(filepath: str) -> bool`

### Database Tools

```python
from globalgenie.tools.database import SQLTools

SQLTools(
    connection_string: str,
    max_results: int = 1000
)
```

**Methods:**
- `execute_query(query: str) -> List[Dict[str, Any]]`
- `describe_table(table_name: str) -> Dict[str, Any]`
- `list_tables() -> List[str]`

## Memory Systems

### Base Memory Class

```python
from globalgenie.memory import BaseMemory
```

### SQLite Memory

```python
from globalgenie.memory import SqliteMemory

SqliteMemory(
    db_file: str = "agent_memory.db",
    table_name: str = "conversations",
    max_memories: int = 1000
)
```

**Methods:**
- `add_memory(content: str, metadata: Dict = None) -> None`
- `get_memories(query: str = None, limit: int = 10) -> List[Dict]`
- `clear_memories(session_id: str = None) -> None`

### PostgreSQL Memory

```python
from globalgenie.memory import PostgresMemory

PostgresMemory(
    connection_string: str,
    table_name: str = "agent_memory",
    max_memories: int = 10000
)
```

### Redis Memory

```python
from globalgenie.memory import RedisMemory

RedisMemory(
    host: str = "localhost",
    port: int = 6379,
    db: int = 0,
    password: Optional[str] = None,
    ttl: int = 86400  # 24 hours
)
```

### Vector Memory

```python
from globalgenie.memory import VectorMemory

VectorMemory(
    vector_store: str = "chroma",
    collection_name: str = "agent_memories",
    embedding_model: str = "text-embedding-ada-002"
)
```

## Knowledge Bases

### Base Knowledge Class

```python
from globalgenie.knowledge import BaseKnowledge
```

### PDF Knowledge Base

```python
from globalgenie.knowledge import PDFKnowledgeBase

PDFKnowledgeBase(
    path: str,                      # Directory or file path
    vector_db: str = "chroma",      # Vector database
    chunk_size: int = 1000,         # Chunk size for splitting
    chunk_overlap: int = 200,       # Overlap between chunks
    embedding_model: str = "text-embedding-ada-002"
)
```

**Methods:**
- `load_documents() -> None`
- `search(query: str, limit: int = 5) -> List[Dict]`
- `add_document(filepath: str) -> None`
- `remove_document(filepath: str) -> None`

### Web Knowledge Base

```python
from globalgenie.knowledge import WebKnowledgeBase

WebKnowledgeBase(
    urls: List[str],
    max_depth: int = 1,
    vector_db: str = "chroma",
    chunk_size: int = 1000,
    chunk_overlap: int = 200
)
```

### Text Knowledge Base

```python
from globalgenie.knowledge import TextKnowledgeBase

TextKnowledgeBase(
    texts: List[str],
    vector_db: str = "chroma",
    chunk_size: int = 1000,
    embedding_model: str = "text-embedding-ada-002"
)
```

### Database Knowledge Base

```python
from globalgenie.knowledge import DatabaseKnowledgeBase

DatabaseKnowledgeBase(
    connection_string: str,
    tables: List[str],
    vector_db: str = "chroma"
)
```

## Agent Teams

### AgentTeam

```python
from globalgenie.team import AgentTeam

AgentTeam(
    agents: List[Agent],
    workflow: str = "sequential",    # "sequential", "parallel", "collaborative"
    max_iterations: int = 5,
    coordinator: Optional[Agent] = None
)
```

**Workflow Types:**
- `sequential`: Agents work one after another
- `parallel`: Agents work simultaneously
- `collaborative`: Agents can communicate and collaborate

**Methods:**
- `run(task: str) -> TeamResponse`
- `add_agent(agent: Agent) -> None`
- `remove_agent(agent_name: str) -> None`

### TeamResponse

```python
class TeamResponse:
    content: str                    # Final team output
    agent_responses: List[AgentResponse]  # Individual agent responses
    workflow_metadata: Dict[str, Any]     # Workflow execution data
    total_tokens: int               # Total tokens used
    execution_time: float           # Total execution time
```

## Configuration

### GlobalGenieConfig

```python
from globalgenie.config import GlobalGenieConfig

config = GlobalGenieConfig(
    # API Keys
    openai_api_key: Optional[str] = None,
    anthropic_api_key: Optional[str] = None,
    google_api_key: Optional[str] = None,
    
    # Default Model Settings
    default_model: str = "gpt-4",
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
    
    # Memory Settings
    memory_backend: str = "sqlite",
    memory_db_path: str = "./agent_memory.db",
    
    # Vector Store Settings
    vector_store: str = "chroma",
    vector_store_path: str = "./vector_store",
    embedding_model: str = "text-embedding-ada-002",
    
    # Logging
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    
    # Performance
    max_concurrent_requests: int = 10,
    request_timeout: int = 30,
    
    # Security
    allowed_tools: Optional[List[str]] = None,
    sandbox_mode: bool = False
)
```

### Environment Variables

GlobalGenie automatically reads these environment variables:

```bash
# API Keys
OPENAI_API_KEY
ANTHROPIC_API_KEY
GOOGLE_API_KEY
HUGGINGFACE_API_KEY

# Configuration
GLOBALGENIE_LOG_LEVEL
GLOBALGENIE_MEMORY_BACKEND
GLOBALGENIE_VECTOR_STORE
GLOBALGENIE_DEFAULT_MODEL

# Database URLs
GLOBALGENIE_DATABASE_URL
GLOBALGENIE_REDIS_URL
GLOBALGENIE_VECTOR_DB_URL
```

## Utilities

### Logging

```python
from globalgenie.utils.logging import setup_logging, get_logger

# Setup logging
setup_logging(level="INFO", file="globalgenie.log")

# Get logger
logger = get_logger(__name__)
logger.info("Agent started")
```

### Validation

```python
from globalgenie.utils.validation import validate_model, validate_tools

# Validate model configuration
is_valid = validate_model(model_config)

# Validate tools
valid_tools = validate_tools(tool_list)
```

### Serialization

```python
from globalgenie.utils.serialization import serialize_agent, deserialize_agent

# Serialize agent to JSON
agent_json = serialize_agent(agent)

# Deserialize agent from JSON
agent = deserialize_agent(agent_json)
```

### Metrics

```python
from globalgenie.utils.metrics import AgentMetrics

metrics = AgentMetrics(agent)

# Get performance metrics
stats = metrics.get_stats()
print(f"Total interactions: {stats['total_interactions']}")
print(f"Average response time: {stats['avg_response_time']}")
print(f"Token usage: {stats['total_tokens']}")
```

## Error Handling

### Common Exceptions

```python
from globalgenie.exceptions import (
    GlobalGenieError,
    ModelError,
    ToolError,
    MemoryError,
    KnowledgeError,
    ConfigurationError
)

try:
    response = agent.run("Hello")
except ModelError as e:
    print(f"Model error: {e}")
except ToolError as e:
    print(f"Tool error: {e}")
except GlobalGenieError as e:
    print(f"General error: {e}")
```

### Error Recovery

```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    retry_attempts=3,
    retry_delay=1.0,
    fallback_model=OpenAIChat(id="gpt-3.5-turbo")
)
```

## Best Practices

### 1. Resource Management

```python
# Use context managers for agents
with Agent(model=OpenAIChat(id="gpt-4")) as agent:
    response = agent.run("Hello")
# Agent resources are automatically cleaned up
```

### 2. Async Operations

```python
import asyncio
from globalgenie.agent import AsyncAgent

async def main():
    agent = AsyncAgent(model=OpenAIChat(id="gpt-4"))
    response = await agent.run("Hello")
    print(response.content)

asyncio.run(main())
```

### 3. Batch Processing

```python
from globalgenie.batch import BatchProcessor

processor = BatchProcessor(
    agent=agent,
    batch_size=10,
    max_workers=5
)

results = processor.process_batch([
    "Question 1",
    "Question 2", 
    "Question 3"
])
```

### 4. Monitoring and Observability

```python
from globalgenie.monitoring import AgentMonitor

monitor = AgentMonitor(agent)
monitor.start()

# Agent interactions are automatically tracked
response = agent.run("Hello")

# Get monitoring data
metrics = monitor.get_metrics()
```

---

For more detailed examples and advanced usage patterns, see the [Examples Gallery](https://docs.globalgenie.com/examples) and [Tutorials](https://docs.globalgenie.com/tutorials).