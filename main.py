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
import argparse
from dotenv import load_dotenv

load_dotenv()

import autogen
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from agents.orchestrator import create_orchestrator
from agents.aws_expert import create_aws_expert
from agents.azure_expert import create_azure_expert
from agents.gcp_expert import create_gcp_expert
from agents.architect import create_architect
from agents.cost_analyst import create_cost_analyst
from agents.summary import create_summary_agent
from config.llm_config import get_max_rounds
from config.agent_config import TERMINATION_KEYWORD
from utils.prompts import WELCOME_MESSAGE
from utils.report_generator import save_report, extract_report_from_chat

console = Console()


# ---------------------------------------------------------------------------
# Termination condition
# ---------------------------------------------------------------------------

def is_termination_message(message: dict) -> bool:
    """Return True when the Summary agent has finished its report."""
    content = message.get("content", "")
    return isinstance(content, str) and TERMINATION_KEYWORD in content


# ---------------------------------------------------------------------------
# Group chat builder
# ---------------------------------------------------------------------------

def build_group_chat(user_proxy: autogen.UserProxyAgent) -> autogen.GroupChat:
    """Instantiate all agents and wire them into a GroupChat."""

    orchestrator = create_orchestrator()
    aws_expert = create_aws_expert()
    azure_expert = create_azure_expert()
    gcp_expert = create_gcp_expert()
    architect = create_architect()
    cost_analyst = create_cost_analyst()
    summary_agent = create_summary_agent()

    # Ordered speaker list — GroupChat will follow this sequence loosely.
    # AutoGen's GroupChatManager will use the speaker_selection_method to decide
    # who speaks next; "auto" lets the LLM decide based on context.
    agents = [
        user_proxy,
        orchestrator,
        aws_expert,
        azure_expert,
        gcp_expert,
        architect,
        cost_analyst,
        summary_agent,
    ]

    group_chat = autogen.GroupChat(
        agents=agents,
        messages=[],
        max_round=get_max_rounds(),
        speaker_selection_method="auto",
        allow_repeat_speaker=True,
    )

    return group_chat


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def run_interactive() -> None:
    """Run the full interactive multi-agent conversation."""

    console.print(Panel(WELCOME_MESSAGE, style="bold cyan", expand=False))

    # UserProxyAgent acts as the human — it will prompt for input
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="ALWAYS",          # Always ask the user for input
        max_consecutive_auto_reply=0,        # Never auto-reply — always wait for human
        is_termination_msg=is_termination_message,
        code_execution_config=False,
        description="The human user seeking cloud architecture advice.",
    )

    group_chat = build_group_chat(user_proxy)

    manager = autogen.GroupChatManager(
        groupchat=group_chat,
        llm_config=None,                     # Manager uses round-robin / auto selection
        is_termination_msg=is_termination_message,
    )

    # Kick off the conversation — the Orchestrator will greet the user
    initial_message = (
        "Hello! Please greet the user, introduce the Cloud Advisor system and its specialists, "
        "and ask them what cloud computing challenge they need help with."
    )

    user_proxy.initiate_chat(
        manager,
        message=initial_message,
        clear_history=True,
    )

    # -----------------------------------------------------------------------
    # Post-conversation: save report
    # -----------------------------------------------------------------------
    if os.getenv("SAVE_REPORT", "true").lower() == "true":
        report_text = extract_report_from_chat(group_chat.messages)
        if report_text:
            output_dir = os.getenv("REPORT_OUTPUT_DIR", "./reports")
            filepath = save_report(report_text, output_dir)
            console.print(
                f"\n[bold green]✅ Report saved to:[/bold green] {filepath}"
            )
        else:
            console.print(
                "\n[yellow]ℹ️  No final report was generated in this session.[/yellow]"
            )

    console.print("\n[bold cyan]Thank you for using Cloud Advisor. Goodbye! ☁️[/bold cyan]\n")


# ---------------------------------------------------------------------------
# Batch mode
# ---------------------------------------------------------------------------

def run_batch(requirements: str, save: bool = True) -> str:
    """
    Non-interactive batch mode: submit requirements, get a report back.

    Args:
        requirements: Natural-language description of the cloud requirements.
        save: Whether to save the report to disk.

    Returns:
        The Markdown report string.
    """
    console.print("[bold cyan]Running in BATCH mode...[/bold cyan]")

    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",            # Never prompt — fully automated
        max_consecutive_auto_reply=0,
        is_termination_msg=is_termination_message,
        code_execution_config=False,
        description="Automated client submitting cloud requirements for analysis.",
    )

    group_chat = build_group_chat(user_proxy)

    manager = autogen.GroupChatManager(
        groupchat=group_chat,
        llm_config=None,
        is_termination_msg=is_termination_message,
    )

    batch_prompt = f"""
Please analyse the following cloud requirements and produce a complete advisory report.
Go through each specialist (AWS, Azure, GCP), synthesize with the Cloud Architect,
add cost estimates from the Cost Analyst, and finish with the Summary Agent's report.

REQUIREMENTS:
{requirements}
"""

    user_proxy.initiate_chat(
        manager,
        message=batch_prompt,
        clear_history=True,
    )

    report_text = extract_report_from_chat(group_chat.messages)

    if report_text and save:
        output_dir = os.getenv("REPORT_OUTPUT_DIR", "./reports")
        filepath = save_report(report_text, output_dir)
        console.print(f"\n[bold green]✅ Report saved to:[/bold green] {filepath}")

    return report_text


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

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

    mode = os.getenv("CONVERSATION_MODE", "interactive")

    if args.batch:
        run_batch(args.batch, save=not args.no_save)
    elif mode == "batch":
        # Batch mode via env var — read from stdin
        console.print("[yellow]Batch mode: paste your requirements and press Ctrl+D (or Ctrl+Z on Windows):[/yellow]")
        requirements = sys.stdin.read().strip()
        if not requirements:
            console.print("[red]Error: No requirements provided.[/red]")
            sys.exit(1)
        run_batch(requirements, save=not args.no_save)
    else:
        run_interactive()


if __name__ == "__main__":
    main()
