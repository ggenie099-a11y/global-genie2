# GlobalGenie ReadyGenies

## Getting Started

The getting started guide walks through the basics of building Agents with GlobalGenie. Recipes build on each other, introducing new concepts and capabilities.

## Agent Concepts

The concepts readygenie walks through the core concepts of GlobalGenie.

- [Async](./agent_concepts/async)
- [RAG](./agent_concepts/rag)
- [Knowledge](./agent_concepts/knowledge)
- [Memory](./agent_concepts/memory)
- [Storage](storage)
- [Tools](./tools)
- [Reasoning](./reasoning)
- [Vector DBs](./agent_concepts/knowledge/vector_dbs)
- [Multi-modal Agents](./agent_concepts/multimodal)
- [Agent Teams](./teams)
- [Other](./agent_concepts/other)

## Examples

The examples readygenie contains real world examples of building agents with GlobalGenie.

## Playground

The playground readygenie contains examples of interacting with agents using the GlobalGenie Agent UI.

## Workflows

The workflows readygenie contains examples of building workflows with GlobalGenie.

## Scripts

Just a place to store setup scripts like `run_pgvector.sh` etc

## Setup

### Create and activate a virtual environment

```shell
python3 -m venv .venv
source .venv/bin/activate
```

### Install libraries

```shell
pip install -U openai globalgenie  # And all other packages you might need
```

### Export your keys

```shell
export OPENAI_API_KEY=***
export GOOGLE_API_KEY=***
```

## Run a readygenie

```shell
python readygenie/.../example.py
```
