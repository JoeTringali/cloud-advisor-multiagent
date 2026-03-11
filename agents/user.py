"""
agents/user.py
--------------------
User agent — Allows the user to provide feedback, answer questions, and guide the agents in interactive mode.
"""

# NEW: Standard import for 0.7+ UserProxyAgent
from autogen_agentchat.agents import UserProxyAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import USER_PROXY_PROMPT


def create_user() -> UserProxyAgent:
    """Create and return the User agent using 0.7+ syntax."""
    return UserProxyAgent(
        name="User",
        # NEW: Required parameter for the 0.7+ architecture
        system_message=USER_PROXY_PROMPT,
        # NOTE: human_input_mode is omitted as it is now handled by the 
        # Team orchestration layer or UserProxyAgent in this version.
        description=(
            "Allows the user to provide feedback, answer questions, and guide the agents in interactive mode. "
        ),
    )