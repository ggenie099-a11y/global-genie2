"""🔧 Example: Using the GeminiTools Toolkit for Video Generation

An Agent using the Gemini video generation tool.

Video generation only works with Vertex AI.
Make sure you have set the GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION environment variables.

Example prompts to try:
- "Generate a 5-second video of a kitten playing a piano"
- "Create a short looping animation of a neon city skyline at dusk"

Run `pip install google-genai globalgenie` to install the necessary dependencies.
"""

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.models.gemini import GeminiTools
from globalgenie.utils.media import save_base64_data

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[GeminiTools(vertexai=True)],  # Video Generation only works on VertexAI mode
    show_tool_calls=True,
    debug_mode=True,
)

agent.print_response(
    "create a video of a cat driving at top speed",
)
response = agent.run_response
if response.videos:
    for video in response.videos:
        save_base64_data(video.content, f"tmp/cat_driving_{video.id}.mp4")
