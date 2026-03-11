"""
agents/user.py
--------------------
User agent — Allows the user to provide feedback, answer questions, and guide the agents in interactive mode.
"""

# NEW: Standard import for 0.7+ UserProxyAgent
from autogen_agentchat.agents import UserProxyAgent
# NEW: Import the updated function name from your config
from utils.prompts import USER_PROXY_PROMPT


def create_user() -> UserProxyAgent:
    """Create and return the User agent using 0.7+ syntax."""
    return UserProxyAgent(
        name="User",
        # Use description to help the SelectorGroupChat identify the human turn
        description=(
            "Allows the user to provide feedback, answer questions, and guide the agents in interactive mode. "
        ),
    )