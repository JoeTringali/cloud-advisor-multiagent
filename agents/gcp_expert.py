"""
agents/gcp_expert.py
---------------------
GCP specialist agent — recommends GCP services and best practices.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_model_client
from utils.prompts import GCP_EXPERT_SYSTEM_PROMPT


def create_gcp_expert() -> AssistantAgent:
    """Create and return the GCP Expert agent using 0.7+ syntax."""
    return AssistantAgent(
        name="GCP_Expert",
        model_client=get_model_client(),
        system_message=GCP_EXPERT_SYSTEM_PROMPT,
        description=(
            "Google Cloud Platform Architect specializing in the GCP Architecture Framework, "
            "data analytics, AI/ML with Vertex AI, and open-source-aligned cloud-native patterns."
        ),
    )