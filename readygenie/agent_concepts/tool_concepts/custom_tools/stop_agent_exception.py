from globalgenie.agent import Agent
from globalgenie.exceptions import StopAgentRun
from globalgenie.models.openai import OpenAIChat
from globalgenie.utils.log import logger


def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    agent.session_state["shopping_list"].append(item)
    len_shopping_list = len(agent.session_state["shopping_list"])
    if len_shopping_list < 3:
        raise StopAgentRun(
            f"Shopping list is: {agent.session_state['shopping_list']}. We must stop the agent."
        )

    logger.info(f"The shopping list is now: {agent.session_state.get('shopping_list')}")
    return f"The shopping list is now: {agent.session_state.get('shopping_list')}"


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with empty shopping list
    session_state={"shopping_list": []},
    tools=[add_item],
    markdown=True,
)
agent.print_response("Add milk", stream=True)
print(f"Final session state: {agent.session_state}")
