# Weekly Steering Report Playbook

## Overview

The weekly steering report is automatically generated from Databricks and validated using Claude Opus 4.5 via AWS Bedrock. This playbook covers the workflow and troubleshooting steps.

## Output Location

**GitHub Repository:** https://github.com/vkvb-hf/cursor-databricks/tree/feature/long-term-steering-report/projects/long_term_steering_report

## Workflow

### 1. Automated Report Generation (Databricks)

The `generate_steering_report` notebook runs on Databricks and:
1. Queries metrics data from source tables
2. Generates the steering report in Markdown format
3. Validates the Key Insights section using Claude Opus 4.5 (AWS Bedrock)
4. Uploads the validated report to Git

**Notebook Location:** `/Workspace/Users/visal.kumar@hellofresh.com/generate_steering_report`

### 2. What the Validation Does

The Claude Opus 4.5 validation ensures:
- ✅ Uses proper Markdown bullet points (`-`) instead of bold labels
- ✅ Removes out-of-scope metrics (e.g., `3_PaymentProcessingFees%`)
- ✅ Replaces technical metric names with leadership-friendly names:
  - `5_DunningBadDebtRate_12wkCohort` → "Dunning Bad Debt Rate"
  - `6_TotalBadDebtRate_12wkCohort` → "Total Bad Debt Rate"
- ✅ Keeps Key Insights under 1000 characters
- ✅ Includes 4 categories: Critical Issues, Positive Trends, Risk Shifts, Emerging Concerns

---

## Troubleshooting: AWS Credentials Expired

### Symptom
The validation step fails with:
```
UnrecognizedClientException: The security token included in the request is invalid
```

### Cause
AWS SSO session tokens expire after 1-12 hours. The credentials stored in Databricks secrets need to be refreshed.

### Solution

#### Option A: Update Credentials (If You Have Access)

1. **Get fresh AWS credentials** from AWS SSO:
   - Go to: https://d-93677e566e.awsapps.com/start/#
   - Select account `bedrock1 (951719175506)` with role `bedrock-user`
   - Copy the credentials (access key, secret key, session token)

2. **Update Databricks secrets** using this prompt:

```
Update the AWS credentials in Databricks secrets (scope='aws') with these new credentials:

aws_access_key_id=<YOUR_NEW_ACCESS_KEY>
aws_secret_access_key=<YOUR_NEW_SECRET_KEY>
aws_session_token=<YOUR_NEW_SESSION_TOKEN>

Then run the steering report notebook.
```

#### Option B: Manual Validation (If Credentials Can't Be Updated)

If you cannot update the credentials, the report will still be generated but without AI validation. You can manually validate the Key Insights section using this prompt:

---

### Manual Validation Prompt

Copy and paste the following prompt to Claude/ChatGPT along with the generated Key Insights section:

```
You are a report validator. Fix the following Key Insights section to meet these requirements:

REQUIREMENTS:
1. Use proper Markdown bullet points (`-`) NOT bold labels on same line
2. Remove any mention of Payment Processing Fees (3_PaymentProcessingFees%) - it's out of scope
3. Replace technical metric names with leadership-friendly names:
   - Replace "5_DunningBadDebtRate_12wkCohort" with "Dunning Bad Debt Rate"
   - Replace "6_TotalBadDebtRate_12wkCohort" with "Total Bad Debt Rate"
4. Keep under 1000 characters
5. Include 4 categories: Critical Issues, Positive Trends, Risk Shifts, Emerging Concerns

CURRENT KEY INSIGHTS TO FIX:
[PASTE THE KEY INSIGHTS SECTION HERE]

Return ONLY the corrected Key Insights section using this format:

## Key Insights
- **Critical Issues:** [content]
- **Positive Trends:** [content]
- **Risk Shifts:** [content]
- **Emerging Concerns:** [content]
```

---

## Formatting Enhancement (Optional)

To make the report more readable for leadership, you can format business units and dimensions on separate lines:

### Before:
```
[5.0% - 19%] - Business Units: CA (↑7.06%), FR (↑10.96%), GB (↑5.63%), DE (↑5.16%)...
```

### After:
```
[5.0% - 19%] - Business Units:
  CA (↑7.06%)
  FR (↑10.96%)
  GB (↑5.63%)
  DE (↑5.16%)
  ...
```

### Prompt for Formatting:

```
Format the business units and dimensions in this steering report to be on separate lines for better readability. 

For any line like:
[5.0% - 19%] - Business Units: **CA** (↑7.06%), **FR** (↑10.96%), **GB** (↑5.63%)...

Convert to:
[5.0% - 19%] - Business Units:
  **CA** (↑7.06%)
  **FR** (↑10.96%)
  **GB** (↑5.63%)
  ...

Do the same for Dimensions lists.

[PASTE THE REPORT CONTENT HERE]
```

---

## Long-Term Solutions for AWS Credentials

The current SSO-based credentials expire frequently. Consider these alternatives:

### 1. IAM Instance Profile (Recommended)
Ask the platform team to attach an IAM role with Bedrock permissions to the Databricks cluster. This eliminates the need for manual credential management.

### 2. Databricks Foundation Model APIs
If available in your Databricks workspace, use Claude through Databricks AI Gateway instead of direct AWS Bedrock access.

### 3. Local Validation Workflow
- Generate report in Databricks (no credentials needed)
- Download report locally
- Validate using local AWS SSO credentials
- Push to Git

---

## Quick Reference

| Item | Location/Value |
|------|----------------|
| Notebook | `/Workspace/Users/visal.kumar@hellofresh.com/generate_steering_report` |
| Output Repo | https://github.com/vkvb-hf/cursor-databricks/tree/feature/long-term-steering-report/projects/long_term_steering_report |
| AWS SSO URL | https://d-93677e566e.awsapps.com/start/# |
| AWS Account | bedrock1 (951719175506) |
| AWS Role | bedrock-user |
| Databricks Secret Scope | `aws` |
| Bedrock Model | `eu.anthropic.claude-opus-4-5-20251101-v1:0` |
| Region | eu-west-1 |

---

## Contact

For issues with:
- **Databricks notebook**: Check the job run logs in Databricks
- **AWS credentials**: Refresh from AWS SSO portal
- **Report content**: Review against `REPORT_PROMPT_V2.md` and `Payments P0 Metrics.md`

