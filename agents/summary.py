"""
agents/summary.py
------------------
Summary agent — produces the final structured advisory report.
"""

# NEW: Standard import for 0.7+ AssistantAgent
from autogen_agentchat.agents import AssistantAgent
# NEW: Import the updated function name from your config
from config.llm_config import get_model_client
from utils.prompts import SUMMARY_SYSTEM_PROMPT


def create_summary_agent() -> AssistantAgent:
    """Create and return the Summary / Report agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Summary_Agent",
        # NEW: Required parameter for the 0.7+ architecture
        model_client=get_model_client(),
        system_message=SUMMARY_SYSTEM_PROMPT,
        # NOTE: human_input_mode is omitted as it is now handled by the 
        # Team orchestration layer or UserProxyAgent in this version.
        description=(
            "Produces the final structured Markdown advisory report, including comparison matrix, "
            "best practices checklist, cost summary, and recommended next steps."
        ),
    )