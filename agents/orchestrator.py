"""
agents/orchestrator.py
-----------------------
Orchestrator agent — manages conversation flow and coordinates specialists.
"""

import autogen
from config.llm_config import get_llm_config
from utils.prompts import ORCHESTRATOR_SYSTEM_PROMPT


def create_orchestrator() -> autogen.AssistantAgent:
    """Create and return the Orchestrator agent."""
    return autogen.AssistantAgent(
        name="Orchestrator",
        system_message=ORCHESTRATOR_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "Manages conversation flow, gathers requirements from the user, "
            "and coordinates the specialist agents."
        ),
    )
