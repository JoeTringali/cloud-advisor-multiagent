"""
agents/aws_expert.py
---------------------
AWS specialist agent — recommends AWS services and best practices.
"""

import autogen
from config.llm_config import get_llm_config
from utils.prompts import AWS_EXPERT_SYSTEM_PROMPT


def create_aws_expert() -> autogen.AssistantAgent:
    """Create and return the AWS Expert agent."""
    return autogen.AssistantAgent(
        name="AWS_Expert",
        system_message=AWS_EXPERT_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "AWS Solutions Architect specializing in Well-Architected Framework, "
            "AWS-native services, and cloud-native patterns on Amazon Web Services."
        ),
    )
