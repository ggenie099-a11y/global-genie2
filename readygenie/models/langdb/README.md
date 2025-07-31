# LangDB ReadyGenie

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `LANGDB_API_KEY` and `LANGDB_PROJECT_ID`

```shell
export LANGDB_API_KEY=***
export LANGDB_PROJECT_ID=***
```

### 3. Install libraries

```shell
pip install -U openai duckduckgo-search duckdb yfinance globalgenie
```

### 4. Run Agent without Tools

- Streaming on

```shell
python readygenie/models/langdb/basic_stream.py
```

- Streaming off

```shell
python readygenie/models/langdb/basic.py
```

### 5. Run Agent with Tools

- Yahoo Finance with streaming on

```shell
python readygenie/models/langdb/agent_stream.py
```

- Yahoo Finance without streaming

```shell
python readygenie/models/langdb/agent.py
```

- Web Search Agent

```shell
python readygenie/models/langdb/web_search.py
```

- Data Analyst

```shell
python readygenie/models/langdb/data_analyst.py
```

- Finance Agent

```shell
python readygenie/models/langdb/finance_agent.py
```

### 6. Run Agent that returns structured output

```shell
python readygenie/models/langdb/structured_output.py
```


