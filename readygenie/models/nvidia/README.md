# Nvidia ReadyGenie

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `NVIDIA_API_KEY`

```shell
export NVIDIA_API_KEY=***
```

### 3. Install libraries

```shell
pip install -U openai globalgenie
```

### 4. Run basic Agent

- Streaming on

```shell
python readygenie/models/nvidia/basic_stream.py
```

- Streaming off

```shell
python readygenie/models/nvidia/basic.py
```

### 5. Run Agent with Tools


- DuckDuckGo search

```shell
python readygenie/models/nvidia/tool_use.py
```
