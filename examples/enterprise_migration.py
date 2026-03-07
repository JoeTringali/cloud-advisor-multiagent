"""
examples/enterprise_migration.py
---------------------------------
Example: Large enterprise migrating on-premises workloads to cloud.

Run with:
    python examples/enterprise_migration.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import run_batch

REQUIREMENTS = """
We are a 3,000-employee financial services company planning a 3-year cloud migration.

Current state:
- 400 VMs running Windows Server 2016/2019 and RHEL 8 in our own data centers
- SQL Server 2019 (Enterprise) — 40 instances, largest DB is 8 TB
- Active Directory on-premises with 3,000 users
- SAP ERP (SAP S/4HANA) — critical workload
- Legacy .NET Framework 4.x applications (60 apps, refactoring budget is limited)
- 100 Gbps dedicated WAN across 12 offices globally

Migration objectives:
- Lift-and-shift Phase 1 (12 months): Move VMs with minimal refactoring
- Modernize Phase 2 (12 months): Containerize stateless apps, managed databases
- Innovate Phase 3 (12 months): AI/analytics on migrated data
- Maintain existing Active Directory integration
- Zero disruption to SAP during migration

Compliance:
- PCI-DSS Level 1 (payment processing)
- SOC 2 Type II audit annually
- Data residency: US and EU only

We have an Enterprise Agreement with Microsoft. Evaluate Azure as primary, but
also assess if AWS or GCP should handle specific workloads (multi-cloud strategy).
"""

if __name__ == "__main__":
    report = run_batch(REQUIREMENTS)
    if report:
        print("\n" + "=" * 60)
        print("FINAL REPORT PREVIEW (first 500 chars):")
        print("=" * 60)
        print(report[:500] + "...")
