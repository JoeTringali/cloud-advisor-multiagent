"""
examples/data_platform.py
--------------------------
Example: Retail company building a real-time data analytics and ML platform.

Run with:
    python examples/data_platform.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import run_batch

REQUIREMENTS = """
We are a mid-size retail company (500 stores, $2B annual revenue) building a
modern data and AI platform to replace our legacy data warehouse.

Data sources:
- Point-of-sale transactions: 2M events/day
- E-commerce clickstream: 50M events/day
- Inventory management system (Oracle DB)
- CRM (Salesforce)
- Supply chain ERP
- IoT sensors in warehouses (10,000 sensors, temperature/humidity)

Desired capabilities:
- Real-time dashboards for store managers (< 5 min latency)
- Demand forecasting ML model (retrain weekly, inference daily)
- Customer segmentation and personalization engine
- Unified data catalog and data governance (data lineage, access controls)
- Self-service analytics for 200 business analysts (SQL + no-code BI)
- Fraud detection for online payments (near real-time, < 500ms)

Scale:
- 5 TB new data per day at peak (holiday season)
- 10 PB total historical data to migrate from on-prem Hadoop cluster
- 200 concurrent analyst queries during business hours

Team: 8 data engineers, 4 ML engineers, 2 platform engineers. Strong Python skills,
some Spark experience, no Kubernetes expertise.

Budget: $80,000–$150,000/month cloud spend.

We are particularly interested in GCP's data capabilities but want an honest comparison.
"""

if __name__ == "__main__":
    report = run_batch(REQUIREMENTS)
    if report:
        print("\n" + "=" * 60)
        print("FINAL REPORT PREVIEW (first 500 chars):")
        print("=" * 60)
        print(report[:500] + "...")
