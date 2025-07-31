# Anthropic Claude

[Models overview](https://docs.anthropic.com/claude/docs/models-overview)

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Set your `ANTHROPIC_API_KEY`

```shell
export ANTHROPIC_API_KEY=xxx
```

### 3. Install libraries

```shell
pip install -U anthropic duckduckgo-search duckdb yfinance globalgenie
```

### 4. Run basic Agent

- Streaming on

```shell
python readygenie/models/anthropic/basic_stream.py
```

- Streaming off

```shell
python readygenie/models/anthropic/basic.py
```

### 5. Run Agent with Tools

- DuckDuckGo Search

```shell
python readygenie/models/anthropic/tool_use.py
```

### 6. Run Agent that returns structured output

```shell
python readygenie/models/anthropic/structured_output.py
```

### 7. Run Agent that uses storage

```shell
python readygenie/models/anthropic/storage.py
```

### 8. Run Agent that uses knowledge

Take note that claude uses OpenAI embeddings under the hood, and you will need an OpenAI API Key
```shell
export OPENAI_API_KEY=***
```

```shell
python readygenie/models/anthropic/knowledge.py
```

### 9. Run Agent that uses memory   

```shell
python readygenie/models/anthropic/memory.py
```

### 10. Run Agent that analyzes an image

```shell
python readygenie/models/anthropic/image_agent.py
```
