"""
agents/orchestrator.py
-----------------------
Orchestrator agent — manages conversation flow and coordinates specialists.
"""
# NEW: Standard import for 0.7+ AssistantAgent
from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import ORCHESTRATOR_SYSTEM_PROMPT


def create_orchestrator() -> AssistantAgent:
    """Create and return the Orchestrator agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Orchestrator",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=ORCHESTRATOR_SYSTEM_PROMPT,
        # NOTE: human_input_mode is now primarily handled by UserProxyAgent 
        # or the Team orchestration layer in this version.
        description=(
            "Manages conversation flow, gathers requirements from the user, "
            "and coordinates the specialist agents."
        ),
    )