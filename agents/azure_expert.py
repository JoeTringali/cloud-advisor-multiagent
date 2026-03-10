"""
agents/azure_expert.py
-----------------------
Azure specialist agent — recommends Azure services and best practices.
"""

# NEW: Standard import for 0.7+ AssistantAgent
from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import AZURE_EXPERT_SYSTEM_PROMPT


def create_azure_expert() -> AssistantAgent:
    """Create and return the Azure Expert agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Azure_Expert",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=AZURE_EXPERT_SYSTEM_PROMPT,
        # NOTE: human_input_mode is now primarily handled by UserProxyAgent 
        # or the Team orchestration layer in this version.
        description=(
            "Azure Solutions Architect specializing in the Cloud Adoption Framework, "
            "Azure-native services, hybrid cloud, and Microsoft ecosystem integration."
        ),
    )