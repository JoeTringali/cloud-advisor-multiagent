"""
agents/orchestrator.py
-----------------------
Orchestrator agent — manages conversation flow and coordinates specialists.
"""
from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_model_client
from utils.prompts import ORCHESTRATOR_SYSTEM_PROMPT


def create_orchestrator() -> AssistantAgent:
    """Create and return the Orchestrator agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Orchestrator",
        model_client=get_model_client(),
        system_message=ORCHESTRATOR_SYSTEM_PROMPT,
        description=(
            "Manages conversation flow, gathers requirements from the user, "
            "and coordinates the specialist agents."
        ),
    )