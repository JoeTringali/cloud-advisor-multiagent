"""
agents/architect.py
--------------------
Cloud Architect agent — synthesizes multi-cloud recommendations.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_model_client
from utils.prompts import ARCHITECT_SYSTEM_PROMPT


def create_architect() -> AssistantAgent:
    """Create and return the Cloud Architect agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Cloud_Architect",
        model_client=get_model_client(),
        system_message=ARCHITECT_SYSTEM_PROMPT,
        description=(
            "Senior multi-cloud architect who synthesizes recommendations from AWS, Azure, "
            "and GCP experts into a coherent comparison and primary recommendation."
        ),
    )