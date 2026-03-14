"""
agents/user.py
--------------------
User agent — Allows the user to provide feedback, answer questions, and guide the agents in interactive mode.
"""

from autogen_agentchat.agents import UserProxyAgent
from utils.prompts import USER_PROXY_PROMPT


def create_user() -> UserProxyAgent:
    """Create and return the User agent using 0.7+ syntax."""
    return UserProxyAgent(
        name="User",
        description=(
            "Allows the user to provide feedback, answer questions, and guide the agents in interactive mode. "
        ),
    )