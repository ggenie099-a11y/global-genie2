from globalgenie.playground import Playground, serve_playground_app
from globalgenie_assist import globalgenie_support
from globalgenie_assist_voice import globalgenie_assist_voice
from fastapi import FastAPI

# Create and configure the playground app
playground_app = Playground(
    agents=[globalgenie_support, globalgenie_assist_voice],
    name="Playground-hackathon",
    app_id="playground-hackathon",
    description="A playground for testing and playing with GlobalGenie",
)

app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve(app="playground:app", reload=True)
