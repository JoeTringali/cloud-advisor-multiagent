"""
agents/gcp_expert.py
---------------------
GCP specialist agent — recommends GCP services and best practices.
"""

# NEW: Standard import for 0.7+ AssistantAgent
from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import GCP_EXPERT_SYSTEM_PROMPT


def create_gcp_expert() -> AssistantAgent:
    """Create and return the GCP Expert agent using 0.7+ syntax."""
    return AssistantAgent(
        name="GCP_Expert",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=GCP_EXPERT_SYSTEM_PROMPT,
        # NOTE: human_input_mode is now primarily handled by UserProxyAgent 
        # or the Team orchestration layer in this version.
        description=(
            "Google Cloud Platform Architect specializing in the GCP Architecture Framework, "
            "data analytics, AI/ML with Vertex AI, and open-source-aligned cloud-native patterns."
        ),
    )