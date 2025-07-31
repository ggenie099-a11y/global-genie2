# Hackathon Resources

Thank you for using GlobalGenie to build your hackathon project! Here you'll find setup guides, examples, and resources to bring your multimodal agents to life.

> Read this documentation on [GlobalGenie Docs](https://docs.globalgenie.com)

## Environment Setup

Let's get your environment setup for the hackathon. Here are the steps:

1. Create a virtual environment
2. Install libraries
3. Export your API keys

### Create a virtual environment

You can use `python3 -m venv` or `uv` to create a virtual environment.

- Standard python

```shell
python3 -m venv .venv
source .venv/bin/activate
```

- Using uv

```shell
uv venv --python 3.12
source .venv/bin/activate
```

- for Windows

```shell
python -m venv venv
venv\scripts\activate
```

### Install libraries

Install the `globalgenie` python package along with the models and tools you want to use.

- Standard python

```shell
pip install -U globalgenie openai
```

- Using uv

```shell
uv pip install -U globalgenie openai
```

### Export your API keys

Export the API keys for the models and tools you want to use.

```shell
export OPENAI_API_KEY=***
export GOOGLE_API_KEY=***
export ELEVEN_LABS_API_KEY=***
```

for Windows

```shell
$env:OPENAI_API_KEY="your-api-key"
```

## Text Agents

Here are some examples of Text Agents built with GlobalGenie:

- [Simple Text Agent](readygenie/hackathon/examples/simple_text_agent.py)
- [Agent with Tools](readygenie/hackathon/examples/agent_with_tools.py)
- [Agent with Knowledge](readygenie/hackathon/examples/agent_with_knowledge.py)
- [Agent with Structured Outputs](readygenie/hackathon/examples/structured_output.py)
- [Research Agent](readygenie/hackathon/examples/research_agent.py)
- [Youtube Agent](readygenie/hackathon/examples/youtube_agent.py)

## Image Agents

- [Image Input + Tools](readygenie/hackathon/multimodal_examples/image_input_with_tools.py)
- [Image Generation](readygenie/hackathon/multimodal_examples/image_generate.py)
- [Image to Structured Output](readygenie/hackathon/multimodal_examples/image_to_structured_output.py)
- [Image to Audio](readygenie/hackathon/multimodal_examples/image_to_audio.py)
- [Image to Image](readygenie/hackathon/multimodal_examples/image_to_image.py)
- [Image Transcription](readygenie/hackathon/multimodal_examples/image_transcription.py)
- [Image Generation with Steps](readygenie/hackathon/multimodal_examples/image_generate_with_intermediate_steps.py)
- [Image Search with Giphy](readygenie/hackathon/multimodal_examples/image_gif_search.py)

## Audio Agents

- [Audio Input](readygenie/hackathon/multimodal_examples/audio_input.py)
- [Audio Input Output](readygenie/hackathon/multimodal_examples/audio_input_output.py)
- [Audio Multiturn](readygenie/hackathon/multimodal_examples/audio_multi_turn.py)
- [Audio Sentiment Analysis](readygenie/hackathon/multimodal_examples/audio_sentiment_analysis.py)
- [Audio Transcription](readygenie/hackathon/multimodal_examples/audio_transcription.py)
- [Audio Podcast](readygenie/hackathon/multimodal_examples/audio_podcast_generator.py)


