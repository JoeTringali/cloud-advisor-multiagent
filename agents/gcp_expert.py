"""
agents/gcp_expert.py
---------------------
GCP specialist agent — recommends GCP services and best practices.
"""

import autogen
from config.llm_config import get_llm_config
from utils.prompts import GCP_EXPERT_SYSTEM_PROMPT


def create_gcp_expert() -> autogen.AssistantAgent:
    """Create and return the GCP Expert agent."""
    return autogen.AssistantAgent(
        name="GCP_Expert",
        system_message=GCP_EXPERT_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "Google Cloud Platform Architect specializing in the GCP Architecture Framework, "
            "data analytics, AI/ML with Vertex AI, and open-source-aligned cloud-native patterns."
        ),
    )
