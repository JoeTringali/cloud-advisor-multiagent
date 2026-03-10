"""
agents/summary.py
------------------
Summary agent — produces the final structured advisory report.
"""

from autogen_agentchat.agents import AssistantAgent
from config.llm_config import get_llm_config
from utils.prompts import SUMMARY_SYSTEM_PROMPT


def create_summary_agent() -> AssistantAgent:
    """Create and return the Summary / Report agent."""
    return AssistantAgent(
        name="Summary_Agent",
        system_message=SUMMARY_SYSTEM_PROMPT,
        llm_config=get_llm_config(),
        human_input_mode="NEVER",
        description=(
            "Produces the final structured Markdown advisory report, including comparison matrix, "
            "best practices checklist, cost summary, and recommended next steps."
        ),
    )
