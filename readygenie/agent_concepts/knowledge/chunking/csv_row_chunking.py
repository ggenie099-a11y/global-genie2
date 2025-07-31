from pathlib import Path

from globalgenie.agent import Agent
from globalgenie.document.chunking.row import RowChunking
from globalgenie.knowledge.csv_url import CSVUrlKnowledgeBase
from globalgenie.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = CSVUrlKnowledgeBase(
    urls=[
        "https://globalgenie-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
    ],
    vector_db=PgVector(
        table_name="imdb_movies_row_chunking",
        db_url=db_url,
    ),
    chunking_strategy=RowChunking(),
)
# Load the knowledge base
knowledge_base.load(recreate=False)

# Initialize the Agent with the knowledge_base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

# Use the agent
agent.print_response("Tell me about the movie Guardians of the Galaxy", markdown=True)
