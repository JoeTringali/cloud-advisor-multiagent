# Cloud Best Practices Reference

Quick reference for the frameworks each specialist agent draws from.

## AWS Well-Architected Framework (6 Pillars)

| Pillar | Key Principles |
|--------|---------------|
| Operational Excellence | IaC, observability, runbooks, safe deployments |
| Security | IAM least-privilege, KMS encryption, GuardDuty, zero-trust |
| Reliability | Multi-AZ, auto-scaling, backup/restore, chaos engineering |
| Performance Efficiency | Right-sizing, serverless, caching, Graviton |
| Cost Optimization | Savings Plans, Reserved Instances, cost tagging, Trusted Advisor |
| Sustainability | Graviton instances, efficient architectures, managed services |

Reference: https://aws.amazon.com/architecture/well-architected/

---

## Azure Cloud Adoption Framework (CAF)

| Phase | Key Activities |
|-------|---------------|
| Strategy | Define motivations, business outcomes, financial model |
| Plan | Digital estate assessment, skills readiness |
| Ready | Landing Zone deployment, Azure Policy, naming standards |
| Adopt (Migrate) | Assess, replicate, optimize, decommission |
| Adopt (Innovate) | Build MVPs, measure, iterate |
| Govern | Cost Management, Security Baseline, Resource Consistency |
| Manage | Inventory, operational compliance, enhanced baseline |

Also references: Azure Well-Architected Framework (5 pillars: Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency)

Reference: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/

---

## Google Cloud Architecture Framework

| Pillar | Key Principles |
|--------|---------------|
| System Design | Microservices, GKE, Cloud Run, event-driven patterns |
| Operational Excellence | Cloud Operations Suite, SLO/SLA design, SRE practices |
| Security, Privacy & Compliance | BeyondCorp, VPC Service Controls, CMEK, Assured Workloads |
| Reliability | Multi-region, global load balancing, Spanner for consistency |
| Cost Optimization | Committed Use Discounts, rightsizing, Spot VMs, BigQuery slots |
| Performance Optimization | Premium Network Tier, global CDN, Vertex AI acceleration |

Reference: https://cloud.google.com/architecture/framework

---

## Cloud-Agnostic Best Practices

### Infrastructure as Code
- **Multi-cloud:** Terraform (recommended)
- **AWS-native:** AWS CDK, CloudFormation
- **Azure-native:** Bicep, ARM Templates
- **GCP-native:** Deployment Manager, Config Connector

### Security (Universal)
- Enforce MFA on all accounts
- Use secrets managers (never hardcode credentials)
- Encrypt all data at rest and in transit
- Implement network segmentation (VPC / subnets / NSGs)
- Enable audit logging everywhere
- Regular penetration testing

### Cost Management
- Tag every resource (owner, environment, project, cost-center)
- Set budget alerts at 50%, 80%, 100% of monthly budget
- Review and right-size monthly
- Use spot/preemptible/spot instances for fault-tolerant workloads
- Delete unused resources (snapshots, unattached disks, idle LBs)

### Reliability
- Design for failure — assume any component can fail at any time
- Use multi-AZ or multi-region for production
- Implement health checks and auto-healing
- Define and test RTO/RPO targets
- Practice game days and chaos engineering

### Observability
- Metrics: CPU, memory, latency, error rate, saturation (USE method)
- Logs: Centralized, structured (JSON), retention policy
- Traces: Distributed tracing for microservices (OpenTelemetry recommended)
- Alerts: Alert on symptoms (not just causes), avoid alert fatigue
