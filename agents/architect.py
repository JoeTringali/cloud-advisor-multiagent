"""
agents/architect.py
--------------------
Cloud Architect agent — synthesizes multi-cloud recommendations.
"""

# NEW: Standard import for 0.7+ AssistantAgent
from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import ARCHITECT_SYSTEM_PROMPT


def create_architect() -> AssistantAgent:
    """Create and return the Cloud Architect agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Cloud_Architect",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=ARCHITECT_SYSTEM_PROMPT,
        # NOTE: human_input_mode is omitted as it is now handled by the 
        # Team orchestration layer or UserProxyAgent in this version.
        description=(
            "Senior multi-cloud architect who synthesizes recommendations from AWS, Azure, "
            "and GCP experts into a coherent comparison and primary recommendation."
        ),
    )s