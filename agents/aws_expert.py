"""
agents/aws_expert.py
---------------------
AWS specialist agent — recommends AWS services and best practices.
"""

from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import AWS_EXPERT_SYSTEM_PROMPT


def create_aws_expert() -> AssistantAgent:
    """Create and return the AWS Expert agent using 0.7+ syntax."""
    return AssistantAgent(
        name="AWS_Expert",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=AWS_EXPERT_SYSTEM_PROMPT,
        # NOTE: human_input_mode is omitted here as it is managed by the 
        # UserProxyAgent or the Team orchestration layer in this version.
        description=(
            "AWS Solutions Architect specializing in Well-Architected Framework, "
            "AWS-native services, and cloud-native patterns on Amazon Web Services."
        ),
    )