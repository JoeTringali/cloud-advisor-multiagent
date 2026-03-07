"""
agents/azure_expert.py
-----------------------
Azure specialist agent — recommends Azure services and best practices.
"""

import autogen
from config.llm_config import get_llm_config
from utils.prompts import AZURE_EXPERT_SYSTEM_PROMPT


def create_azure_expert() -> autogen.AssistantAgent:
    """Create and return the Azure Expert agent."""
    return autogen.AssistantAgent(
        name="Azure_Expert",
        system_message=AZURE_EXPERT_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "Azure Solutions Architect specializing in the Cloud Adoption Framework, "
            "Azure-native services, hybrid cloud, and Microsoft ecosystem integration."
        ),
    )
