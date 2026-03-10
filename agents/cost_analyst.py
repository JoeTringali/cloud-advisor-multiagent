"""
agents/cost_analyst.py
-----------------------
Cost Analyst agent — provides FinOps and pricing estimates.
"""

# NEW: Standard import for 0.7+ AssistantAgent
from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import COST_ANALYST_SYSTEM_PROMPT


def create_cost_analyst() -> AssistantAgent:
    """Create and return the Cost Analyst agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Cost_Analyst",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=COST_ANALYST_SYSTEM_PROMPT,
        # NOTE: human_input_mode is omitted as it is now handled by the 
        # Team orchestration layer or UserProxyAgent in this version.
        description=(
            "Cloud FinOps specialist who estimates monthly costs across providers, "
            "identifies optimization opportunities, and flags pricing gotchas."
        ),
    )