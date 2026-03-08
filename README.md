# ☁️ Cloud Advisor Multi-Agent System

A multi-agent AI system built with **Microsoft AutoGen** that helps organizations choose and design cloud computing solutions across AWS, Azure, and GCP, 
following each provider's best practices.

---

## 🧠 Architecture Overview

```
User Input
    │
    ▼
┌─────────────────────────────────────────────────┐
│              Orchestrator Agent                 │
│   (Routes queries, manages conversation flow)   │
└──────────┬──────────┬──────────┬────────────────┘
           │          │          │
           ▼          ▼          ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │  AWS     │ │  Azure   │ │  GCP     │
    │  Expert  │ │  Expert  │ │  Expert  │
    │  Agent   │ │  Agent   │ │  Agent   │
    └──────────┘ └──────────┘ └──────────┘
           │          │          │
           └──────────┴──────────┘
                      │
                      ▼
           ┌─────────────────────┐
           │  Architect Agent    │
           │ (Synthesizes &      │
           │  compares options)  │
           └─────────────────────┘
                      │
                      ▼
           ┌─────────────────────┐
           │  Cost Analyst Agent │
           │ (Estimates pricing  │
           │  & TCO)             │
           └─────────────────────┘
                      │
                      ▼
           ┌─────────────────────┐
           │  Summary Agent      │
           │ (Final report &     │
           │  recommendations)   │
           └─────────────────────┘
```

## 👥 Agents

| Agent | Role |
|-------|------|
| **Orchestrator** | Routes queries, manages clarification, drives the conversation |
| **AWS Expert** | Specializes in AWS services, Well-Architected Framework |
| **Azure Expert** | Specializes in Azure services, Cloud Adoption Framework |
| **GCP Expert** | Specializes in GCP services, Google Cloud Architecture Framework |
| **Cloud Architect** | Synthesizes recommendations, compares multi-cloud options |
| **Cost Analyst** | Estimates costs, TCO, and pricing comparisons |
| **Summary Agent** | Produces final structured reports and action plans |

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/cloud-advisor-multiagent.git
cd cloud-advisor-multiagent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Copy the example environment file and add your keys:
```bash
cp .env.example .env
```

Edit `.env`:
```
OPENAI_API_KEY=your_openai_key_here
# Optional: Use Azure OpenAI instead
AZURE_OPENAI_API_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

### 4. Run the System
```bash
python main.py
```

---

## 📁 Project Structure

```
cloud-advisor-multiagent/
├── main.py                    # Entry point
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
├── README.md                  # This file
│
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py        # Orchestrator agent
│   ├── aws_expert.py          # AWS specialist
│   ├── azure_expert.py        # Azure specialist
│   ├── gcp_expert.py          # GCP specialist
│   ├── architect.py           # Cloud architect synthesizer
│   ├── cost_analyst.py        # Cost estimation agent
│   └── summary.py             # Report/summary agent
│
├── config/
│   ├── __init__.py
│   ├── llm_config.py          # LLM configuration
│   └── agent_config.py        # Agent behavior settings
│
├── utils/
│   ├── __init__.py
│   ├── prompts.py             # System prompts and templates
│   └── report_generator.py    # Markdown report output
│
├── examples/
│   ├── startup_saas.py        # Example: SaaS startup scenario
│   ├── enterprise_migration.py # Example: Enterprise migration
│   └── data_platform.py       # Example: Data analytics platform
│
└── docs/
    ├── agent_design.md        # Detailed agent design notes
    └── best_practices.md      # Cloud best practices reference
```

---

## 💬 Example Interaction

```
╔══════════════════════════════════════════════════════╗
║        Cloud Advisor Multi-Agent System              ║
║     Powered by AutoGen | AWS · Azure · GCP           ║
╚══════════════════════════════════════════════════════╝

Hello! I'm your Cloud Advisor. I have specialists for AWS, 
Azure, and GCP ready to help you design the best cloud solution.

What cloud challenge can we help you with today?
> We're a healthcare startup needing HIPAA-compliant infrastructure 
  for a patient data platform with ML capabilities.

[Orchestrator] → Routing to all three cloud experts for parallel analysis...
[AWS Expert]   → Analyzing HIPAA-compliant architecture on AWS...
[Azure Expert] → Evaluating Azure Healthcare APIs and compliance tools...
[GCP Expert]   → Reviewing GCP Healthcare API and Vertex AI options...
[Architect]    → Synthesizing comparison across providers...
[Cost Analyst] → Estimating monthly costs for each option...
[Summary]      → Generating final recommendation report...
```

---

## ⚙️ Configuration Options

### LLM Backends Supported
- **OpenAI** (GPT-4o recommended)
- **Azure OpenAI**
- **Ollama** (local models — experimental)

Edit `config/llm_config.py` to switch backends.

### Conversation Modes
- `interactive` — Full back-and-forth with user clarifications (default)
- `batch` — Process a requirements doc and output a report directly

Set via `CONVERSATION_MODE` in `.env`.

---

## 📊 Sample Output

The system produces a structured Markdown report including:
- **Requirements summary**
- **Per-provider architecture recommendation**
- **Comparison matrix** (services, compliance, scalability, cost)
- **Best practices checklist** for each provider
- **Estimated monthly cost range**
- **Recommended next steps**

---

## 🤝 Contributing

Pull requests are welcome! See `docs/agent_design.md` for how to add new specialist agents.

---

## 📄 License

MIT License — see `LICENSE` for details.
