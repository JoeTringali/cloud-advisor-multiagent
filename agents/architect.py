"""
agents/architect.py
--------------------
Cloud Architect agent — synthesizes multi-cloud recommendations.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_llm_config
from utils.prompts import ARCHITECT_SYSTEM_PROMPT


def create_architect() -> AssistantAgent:
    """Create and return the Cloud Architect agent."""
    return AssistantAgent(
        name="Cloud_Architect",
        system_message=ARCHITECT_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "Senior multi-cloud architect who synthesizes recommendations from AWS, Azure, "
            "and GCP experts into a coherent comparison and primary recommendation."
        ),
    )
