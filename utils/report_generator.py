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

    phrases_to_remove = [
        "Completion keyword: **completion**",
        "Completion keyword: completion",
        "CLOUD_ADVISOR_COMPLETE"
    ]
    clean_report = report_text
    for phrase in phrases_to_remove:
        clean_report = clean_report.replace(phrase, "")
    clean_report = clean_report.strip()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(clean_report)

    return filepath

def extract_report_from_chat(messages):
    """
    Extract the last message containing the report markers from chat history.
    """
    report_content = ""
    
    # Reverse the list to find the most recent summary/report
    for message in reversed(messages):
        # FIX: Check if the object has 'source' and 'content' 
        # (This skips the TaskResult object at the end of the stream)
        if not hasattr(message, "source") or not hasattr(message, "content"):
            continue

        if isinstance(message, TextMessage):
            content = message.content
            
            # Logic: Look for the Summary Agent's final output
            # or a specific Markdown header
            if message.source == "Summary_Agent" or "## " in content:
                report_content = content
                break # Stop once we find the final report
                
    return report_content