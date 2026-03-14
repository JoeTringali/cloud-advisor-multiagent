"""
agents/cost_analyst.py
-----------------------
Cost Analyst agent — provides FinOps and pricing estimates.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_model_client
from utils.prompts import COST_ANALYST_SYSTEM_PROMPT


def create_cost_analyst() -> AssistantAgent:
    """Create and return the Cost Analyst agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Cost_Analyst",
        model_client=get_model_client(),
        system_message=COST_ANALYST_SYSTEM_PROMPT,
        description=(
            "Cloud FinOps specialist who estimates monthly costs across providers, "
            "identifies optimization opportunities, and flags pricing gotchas."
        ),
    )