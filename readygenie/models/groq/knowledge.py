"""Run `pip install duckduckgo-search sqlalchemy pgvector pypdf openai groq` to install dependencies."""

from globalgenie.agent import Agent
from globalgenie.knowledge.pdf_url import PDFUrlKnowledgeBase
from globalgenie.models.groq import Groq
from globalgenie.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://globalgenie-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    knowledge=knowledge_base,
    show_tool_calls=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
