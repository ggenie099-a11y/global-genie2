"""
This recipe shows how to store agent sessions in a Firestore database.
Steps:
1. Ensure your gcloud project is enabled with Firestore. Reference https://cloud.google.com/firestore/docs/create-database-server-client-library ?
2. Run: `pip install openai google-cloud-firestore globalgenie` to install dependencies
3. Make sure your gcloud project is set up and you have the necessary permissions to access Firestore
4. Run: `python readygenie/storage/firestore_storage.py` to run the agent
"""

from globalgenie.agent import Agent
from globalgenie.storage.firestore import FirestoreStorage
from globalgenie.tools.duckduckgo import DuckDuckGoTools

# The only required argument is the collection name.
# Firestore will connect automatically using your google cloud credentials.
# The class uses the (default) database by default to allow free tier access to firestore.
# You can specify a project_id if you'd like to connect to firestore in a different GCP project


agent = Agent(
    storage=FirestoreStorage(
        db_name="memory",
        collection_name="agent_sessions",
    ),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
