"""
main.py
-------
Entry point for the Cloud Advisor Multi-Agent System.

Usage:
    python main.py
    python main.py --batch "We need a HIPAA-compliant data platform on the cloud."
    python main.py --no-save  (disables report saving)
"""

import os
import sys
import asyncio
import argparse
from dotenv import load_dotenv

load_dotenv()

# NEW: v0.7+ Imports
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient # Ensure you use the Client now

from rich.console import Console
from rich.panel import Panel

# Local imports
from agents.orchestrator import create_orchestrator
from agents.aws_expert import create_aws_expert
from agents.azure_expert import create_azure_expert
from agents.gcp_expert import create_gcp_expert
from agents.architect import create_architect
from agents.cost_analyst import create_cost_analyst
from agents.summary import create_summary_agent
from config.agent_config import TERMINATION_KEYWORD
from utils.prompts import WELCOME_MESSAGE
from utils.report_generator import save_report, extract_report_from_chat

console = Console()

async def build_team():
    """Instantiate agents and wire them into a SelectorGroupChat Team."""
    
    # These creator functions MUST be updated to return 0.7+ Agents
    # and use the new OpenAIChatCompletionClient inside them.
    agents = [
        create_orchestrator(),
        create_aws_expert(),
        create_azure_expert(),
        create_gcp_expert(),
        create_architect(),
        create_cost_analyst(),
        create_summary_agent(),
    ]

    # The Termination condition replaces is_termination_message
    termination = TextMentionTermination(TERMINATION_KEYWORD)

    # NEW: SelectorGroupChat replaces GroupChat + GroupChatManager
    # You need to pass a model_client here for the 'selector' to think
    selector_model = OpenAIChatCompletionClient(model="gpt-4o")

    team = SelectorGroupChat(
        participants=agents,
        model_client=selector_model,
        termination_condition=termination,
    )

    return team

async def run_interactive() -> None:
    console.print(Panel(WELCOME_MESSAGE, style="bold cyan", expand=False))

    team = await build_team()

    initial_message = (
        "Hello! Please greet the user, introduce the Cloud Advisor system and its specialists, "
        "and ask them what cloud computing challenge they need help with."
    )

    # NEW: Run is now async and returns a TaskResult
    async for message in team.run_stream(task=initial_message):
        if message.content:
            console.print(f"[bold]{message.source}:[/bold] {message.content}")

    # Report saving logic remains similar, but you extract from team history
    # if os.getenv("SAVE_REPORT", "true").lower() == "true":
    #    ... (Logic to extract from team history)

async def run_batch(requirements: str, save: bool = True):
    console.print("[bold cyan]Running in BATCH mode...[/bold cyan]")
    team = await build_team()

    batch_prompt = f"Analyze these requirements and produce a report: {requirements}"

    # Use run() for batch if you don't need to stream the output
    result = await team.run(task=batch_prompt)
    
    # Process result.messages for your report generator
    return result

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="☁️ Cloud Advisor Multi-Agent System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py
  python main.py --batch "Healthcare startup needs HIPAA-compliant ML platform"
  python main.py --batch "Enterprise migrating 200 VMs from on-prem to cloud" --no-save
        """,
    )
    parser.add_argument(
        "--batch",
        metavar="REQUIREMENTS",
        type=str,
        default=None,
        help="Run in batch mode with the given requirements string (non-interactive).",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        default=False,
        help="Do not save the report to disk.",
    )
    return parser.parse_args()
    
def main() -> None:
    args = parse_args()
    
    # Use asyncio.run to kick off the async loop
    if args.batch:
        asyncio.run(run_batch(args.batch, save=not args.no_save))
    else:
        asyncio.run(run_interactive())

if __name__ == "__main__":
    main()