"""
utils/report_generator.py
--------------------------
Saves the final advisory report to a Markdown file.
"""

import os
import re
from datetime import datetime
from autogen_agentchat.messages import TextMessage

from rich.console import Console
console = Console()

def save_report(report_text: str, output_dir: str = "./reports") -> str:
    """
    Save the generated report to a timestamped Markdown file.

    Args:
        report_text: The full Markdown report string.
        output_dir: Directory to write the file into.

    Returns:
        The path to the saved file.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cloud_advisory_report_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    # Strip the termination keyword if present
    # clean_report = report_text.replace("CLOUD_ADVISOR_COMPLETE", "").strip()
    clean_report = report_text

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(clean_report)

    return filepath


#def extract_report_from_chat(chat_history: list) -> str:
#    """
#    Extract the last message containing the report markers from chat history.
#
#    Args:
#        chat_history: List of AutoGen message dicts.
#
#    Returns:
#        The report text, or an empty string if not found.
#    """
#    for message in reversed(chat_history):
#        content = message.content
#        if isinstance(content, str) and "Cloud Architecture Advisory Report" in content:
#            return content
#    return ""

#=======================================================================
def extract_report_from_chat(messages):
    """
    Extract the last message containing the report markers from chat history.

    Args:
        messages: List of AutoGen messages.

    Returns:
        The report text, or an empty string if not found.
    """
    report_content = ""
    
    for message in reversed(messages):
        console.print(f"\n[bold]Debug:{message.source}:[/bold] {message.content}")
        if isinstance(message, TextMessage):
            content = message.content
#            
#            # Look for your summary agent or specific keywords
#            if message.source == "Summary_Agent" or "## Final Report" in content:
#                report_content = content

    report_content = content
                
    return report_content
#=======================================================================