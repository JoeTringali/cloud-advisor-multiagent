"""
agents/summary.py
------------------
Summary agent — produces the final structured advisory report.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_model_client
from utils.prompts import SUMMARY_SYSTEM_PROMPT


def create_summary_agent() -> AssistantAgent:
    """Create and return the Summary / Report agent using 0.7+ syntax."""
    return AssistantAgent(
        name="Summary_Agent",
        model_client=get_model_client(),
        system_message=SUMMARY_SYSTEM_PROMPT,
        description=(
            "Produces the final structured Markdown advisory report, including comparison matrix, "
            "best practices checklist, cost summary, and recommended next steps."
        ),
    )