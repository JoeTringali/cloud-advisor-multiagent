"""
agents/cost_analyst.py
-----------------------
Cost Analyst agent — provides FinOps and pricing estimates.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_llm_config
from utils.prompts import COST_ANALYST_SYSTEM_PROMPT


def create_cost_analyst() -> AssistantAgent:
    """Create and return the Cost Analyst agent."""
    return AssistantAgent(
        name="Cost_Analyst",
        system_message=COST_ANALYST_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "Cloud FinOps specialist who estimates monthly costs across providers, "
            "identifies optimization opportunities, and flags pricing gotchas."
        ),
    )
