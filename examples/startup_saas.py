"""
examples/startup_saas.py
-------------------------
Example: SaaS startup needing a scalable multi-tenant web platform.

Run with:
    python examples/startup_saas.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import run_batch

REQUIREMENTS = """
We are a 10-person B2B SaaS startup building a project management tool.

Technical requirements:
- Multi-tenant web application (React frontend, Node.js + Python backend)
- PostgreSQL database with per-tenant row-level security
- Async background jobs (email notifications, report generation)
- File uploads (user documents, up to 100 MB each)
- REST API + WebSocket for real-time updates
- Expected scale: 500 tenants at launch, growing to 5,000 within 18 months

Non-functional requirements:
- 99.9% uptime SLA
- GDPR compliance (EU customers)
- Low-latency globally (US, EU, APAC)
- Monthly cloud budget: $2,000–$5,000 initially
- Small team (2 backend engineers) — prefer managed services to reduce ops burden

We have no existing cloud infrastructure. We are cloud-agnostic but lean toward
developer-friendly platforms. Please recommend the best cloud provider and architecture.
"""

if __name__ == "__main__":
    report = run_batch(REQUIREMENTS)
    if report:
        print("\n" + "=" * 60)
        print("FINAL REPORT PREVIEW (first 500 chars):")
        print("=" * 60)
        print(report[:500] + "...")
