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

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient # Ensure you use the Client now
from autogen_agentchat.messages import TextMessage, StopMessage, MultiModalMessage

from rich.console import Console
from rich.panel import Panel

from agents.orchestrator import create_orchestrator
from agents.aws_expert import create_aws_expert
from agents.azure_expert import create_azure_expert
from agents.gcp_expert import create_gcp_expert
from agents.architect import create_architect
from agents.cost_analyst import create_cost_analyst
from agents.summary import create_summary_agent
from agents.user import create_user
from config.agent_config import TERMINATION_KEYWORD
from utils.prompts import WELCOME_MESSAGE
from utils.report_generator import save_report, extract_report_from_chat

console = Console()

async def build_team(interactive: bool = True):
    """Instantiate agents and wire them into a SelectorGroupChat Team."""
    
    agents = [
        create_orchestrator(),
        create_aws_expert(),
        create_azure_expert(),
        create_gcp_expert(),
        create_architect(),
        create_cost_analyst(),
        create_summary_agent(),
    ]
    # Only add the human bridge if we are in interactive mode
    if interactive:
        agents.append(create_user())  # UserProxyAgent should be first to gather input early

    user_exit_condition = TextMentionTermination("quit") | TextMentionTermination("exit")
    system_completion_condition = TextMentionTermination(TERMINATION_KEYWORD)
    
    # Combined condition: Stop if user wants to quit OR if agents finish the task
    termination = user_exit_condition | system_completion_condition

    selector_model = OpenAIChatCompletionClient(model=os.getenv("LLM_MODEL", "gpt-4o"))

    team = SelectorGroupChat(
        participants=agents,
        model_client=selector_model,
        termination_condition=termination,
    )

    return team

async def run_interactive() -> None:
    console.print(Panel(WELCOME_MESSAGE, style="bold cyan", expand=False))

    team = await build_team()

    instruction = (
        "Orchestrator, please greet the user, introduce the team briefly, "
        "and ask: 'What cloud computing challenge can we help you with today?'"
    )

    is_first_message = True
    async for message in team.run_stream(task=instruction):
        # Skip printing the instruction itself
        if is_first_message:
            is_first_message = False
            continue
        
        # Handle TextMessage messages
        if isinstance(message, TextMessage):
            console.print(f"\n[bold]{message.source}:[/bold] {message.content}")
        
        # Handle multi-modal messages if your agents might send images/files
        elif isinstance(message, MultiModalMessage):
            console.print(f"\n[bold]{message.source}:[/bold] [Multi-modal content received]")

        elif isinstance(message, StopMessage):
            console.print("\n[italic yellow]Agents have reached a stopping point.[/italic yellow]")

    # Report saving logic remains similar, but you extract from team history
    # if os.getenv("SAVE_REPORT", "true").lower() == "true":
    #    ... (Logic to extract from team history)

async def run_batch(requirements: str, save: bool = True):
    console.print(f"[bold cyan]Running in BATCH mode...[/bold cyan]")

    team = await build_team(interactive=False)

#    batch_prompt = f"Analyze these requirements and produce a report: {requirements}"
    batch_prompt = (
        f"Orchestrator, please coordinate the team to analyze these requirements: {requirements}. "
        f"Once the analysis is complete, have the Summary Agent produce a final structured report. "
        f"End your final response with {TERMINATION_KEYWORD}."
    )

    result = await team.run(task=batch_prompt)

    # Iterate through the messages in the TaskResult to show the progress in the console
    for message in result.messages:
        if isinstance(message, TextMessage):
            console.print(f"\n[bold]{message.source}:[/bold] {message.content}")

    # Report saving logic
    if save:
        console.print("\n[bold green]Generating final report...[/bold green]")
        # extract_report_from_chat can now process result.messages directly
        report_content = extract_report_from_chat(result.messages)
        if report_content:
            file_path = save_report(report_content)
            console.print(f"\n[bold green]Report saved to:[/bold green] {file_path}")
        else:
            console.print("\n[bold red]Failed to extract report content from the conversation.[/bold red]")

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
    
    if args.batch:
        asyncio.run(run_batch(args.batch, save=not args.no_save))
    else:
        asyncio.run(run_interactive())

if __name__ == "__main__":
    main()