# Agent Design Notes

## Overview

This document describes the design decisions behind each agent in the Cloud Advisor system.

## Agent Interaction Flow

```
1. User submits requirements (interactive prompt or batch input)
2. Orchestrator gathers context via clarifying questions (interactive mode)
3. Orchestrator signals readiness → triggers specialist agents
4. AWS Expert, Azure Expert, GCP Expert each produce:
   - Recommended services
   - Architecture pattern
   - Best practices (Well-Architected / CAF / GCP Framework)
   - Compliance notes
5. Cloud Architect synthesizes a comparison matrix and primary recommendation
6. Cost Analyst adds pricing estimates and FinOps recommendations
7. Summary Agent produces the final Markdown report
8. UserProxy receives and displays the report; report is saved to disk
```

## Agent Roles

### Orchestrator
- **Type:** AssistantAgent
- **Trigger:** Always speaks first
- **Key behavior:** Asks clarifying questions (up to MAX_CLARIFICATION_ROUNDS), then hands off to specialists
- **Termination:** Does not terminate; defers to Summary Agent

### AWS / Azure / GCP Experts
- **Type:** AssistantAgent
- **Trigger:** After Orchestrator signals requirements are understood
- **Key behavior:** Each produces a structured analysis independently
- **Format:** Services → Architecture Pattern → Best Practices → Compliance

### Cloud Architect
- **Type:** AssistantAgent
- **Trigger:** After all three cloud experts have responded
- **Key behavior:** Builds comparison matrix, identifies best-fit provider(s)
- **Format:** Comparison table + primary recommendation + trade-off analysis

### Cost Analyst
- **Type:** AssistantAgent
- **Trigger:** After Cloud Architect's comparison
- **Key behavior:** Provides cost ranges (not precise quotes), flags egress fees and gotchas
- **Format:** Per-provider cost range + optimization tips + FinOps recommendations

### Summary Agent
- **Type:** AssistantAgent
- **Trigger:** After Cost Analyst, or when user requests a report
- **Key behavior:** Produces the full structured Markdown report
- **Termination:** Ends with `CLOUD_ADVISOR_COMPLETE` keyword

## Adding a New Specialist Agent

1. Create `agents/my_new_expert.py` following the pattern of existing experts.
2. Add a system prompt to `utils/prompts.py`.
3. Import and instantiate the agent in `main.py`'s `build_group_chat()` function.
4. Add it to the `agents` list in `build_group_chat()`.

## Extending for New Providers

To add Oracle Cloud Infrastructure (OCI) or IBM Cloud support:
1. Create a new expert agent file.
2. Add comprehensive service knowledge and best practices to the system prompt.
3. Update the Architect and Cost Analyst prompts to include the new provider.
4. Add the new agent to the group chat.

## Conversation Management

- **Max rounds:** Controlled by `MAX_CONVERSATION_ROUNDS` env var (default: 30)
- **Termination:** `CLOUD_ADVISOR_COMPLETE` in any message ends the GroupChat
- **Human input:** `ALWAYS` in interactive mode; `NEVER` in batch mode
- **Speaker selection:** `"auto"` — the GroupChatManager LLM decides who speaks next

## Known Limitations

- Agent communication is sequential (not truly parallel per-provider); AutoGen's GroupChat
  does not natively support parallel agent execution without custom implementations.
- Cost estimates are LLM-generated approximations, not real-time pricing API calls.
  For production use, integrate AWS Pricing API, Azure Retail Prices API, and GCP Price List.
- The system prompt for each agent is large; using a model with ≥ 128K context is recommended.
