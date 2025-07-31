# OpenAI ReadyGenie

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `OPENAI_API_KEY`

```shell
export OPENAI_API_KEY=***
```

### 3. Install libraries

```shell
pip install -U openai duckduckgo-search duckdb yfinance globalgenie
```

### 4. Run basic Agent

- Streaming on

```shell
python readygenie/models/openai/basic_stream.py
```

- Streaming off

```shell
python readygenie/models/openai/basic.py
```

### 5. Run Agent with Tools

- DuckDuckGo Search

```shell
python readygenie/models/openai/tool_use.py
```

### 6. Run Agent that returns structured output

```shell
python readygenie/models/openai/structured_output.py
```

### 7. Run Agent uses memory

```shell
python readygenie/models/openai/memory.py
```

### 8. Run Agent that uses storage

```shell
python readygenie/models/openai/storage.py
```

### 9. Run Agent that uses knowledge

```shell
python readygenie/models/openai/knowledge.py
```

### 10. Run Agent that generates an image using Dall-E

```shell
python readygenie/models/openai/generate_images.py
```

### 11. Run Agent that analyzes an image

```shell
python readygenie/models/openai/image_agent.py
```

or

```shell
python readygenie/models/openai/image_agent_with_memory.py
```

### 11. Run Agent that analyzes audio

```shell
python readygenie/models/openai/audio_input_agent.py
```

### 12. Run Agent that generates audio

```shell
python readygenie/models/openai/audio_output_agent.py
```
