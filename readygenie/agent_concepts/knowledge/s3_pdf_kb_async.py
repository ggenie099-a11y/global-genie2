import asyncio

from globalgenie.agent import Agent
from globalgenie.knowledge.s3.pdf import S3PDFKnowledgeBase
from globalgenie.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = S3PDFKnowledgeBase(
    bucket_name="globalgenie-public",
    key="recipes/ThaiRecipes.pdf",
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)


agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(agent.knowledge.aload(recreate=True))

    asyncio.run(agent.aprint_response("How to make Thai curry?", markdown=True))
