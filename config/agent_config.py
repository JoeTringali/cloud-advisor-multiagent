"""
config/agent_config.py
----------------------
Shared agent behavior settings and constants.
"""

# Termination keyword used by agents to signal conversation end
TERMINATION_KEYWORD = "CLOUD_ADVISOR_COMPLETE"

# Token used by orchestrator to request clarification from the user
CLARIFICATION_TOKEN = "NEEDS_CLARIFICATION"

# Token used to trigger final summary generation
SUMMARIZE_TOKEN = "GENERATE_SUMMARY"

# Maximum number of clarification rounds before proceeding
MAX_CLARIFICATION_ROUNDS = 3

# Cloud providers covered
CLOUD_PROVIDERS = ["AWS", "Azure", "GCP"]

# Well-known compliance frameworks agents should be aware of
COMPLIANCE_FRAMEWORKS = [
    "HIPAA", "SOC 2", "PCI-DSS", "ISO 27001", "GDPR",
    "FedRAMP", "HITRUST", "NIST", "CIS Benchmarks",
]
