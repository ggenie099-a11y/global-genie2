"""
This example shows how to instrument your globalgenie agent with OpenInference and send traces to LangSmith.

1. Create a LangSmith account and get your API key: https://smith.langchain.com/
2. Set your LangSmith API key as an environment variable:
  - export LANGSMITH_API_KEY=<your-key>
  - export LANGSMITH_TRACING=true
  - export LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com or https://api.smith.langchain.com
  - export LANGSMITH_PROJECT=<your-project-name>
3. Install dependencies: pip install openai openinference-instrumentation-globalgenie opentelemetry-sdk opentelemetry-exporter-otlp
"""

import os

from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat
from globalgenie.tools.duckduckgo import DuckDuckGoTools
from openinference.instrumentation.globalgenie import GlobalGenieInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "https://eu.api.smith.langchain.com/otel/v1/traces"
headers = {
    "x-api-key": os.getenv("LANGSMITH_API_KEY"),
    "Langsmith-Project": os.getenv("LANGSMITH_PROJECT"),
}


tracer_provider = TracerProvider()
tracer_provider.add_span_processor(
    SimpleSpanProcessor(OTLPSpanExporter(endpoint=endpoint, headers=headers))
)
trace_api.set_tracer_provider(tracer_provider=tracer_provider)

# Start instrumenting globalgenie
GlobalGenieInstrumentor().instrument()

agent = Agent(
    name="Stock Market Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    debug_mode=True,
)

agent.print_response("What is news on the stock market?")
