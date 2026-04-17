# Fraud Investigation: HF-NA 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.97% → 89.66% (-1.44%)  
**Volume:** 27,572 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-NA declined from 90.97% to 89.66% (-1.31 pp) in 2026-W15, a significant change affecting 27,572 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within 8-week range (89.11%-91.57%) | -1.31 pp | ✅ |
| L1: Country Scan | US exceeds ±2.5% threshold | -2.61% | ⚠️ |
| L1: Channel Scan | Referral exceeds threshold | -7.08% | ⚠️ |
| L2: US Referral | PF Block spike identified | +409.56% | ⚠️ |
| L2: CA Referral | FAR improved despite flag | +6.05% | ✅ |

**Key Findings:**
- US drove the regional decline with FAR dropping -2.61% (from 91.59% to 89.20%), while CA improved +1.57%
- US Referral channel experienced a severe FAR drop of -12.15% (from 70.00% to 61.50%) with volume increasing from 2,987 to 3,636 customers
- PF Block rate in US Referral spiked +409.56% (from 2.48% to 12.62%), indicating a significant change in fraud prevention rules or model behavior
- Dup Rate increased across the region (+0.88 pp) and Dup Block % rose from 6.49% to 6.71%, contributing to lower approvals
- Paid channels remained relatively stable with only -0.64% FAR change despite +6.29% increase in Dup Rate

**Action:** **Investigate** – The +409.56% spike in PF Block rate for US Referral requires immediate review of fraud prevention model changes or rule deployments that may have occurred between W14 and W15.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.66% | 26.94% | 6.71% | 2.84% | 27,572 | -1.44% ← REPORTED CHANGE |
| 2026-W14 | 90.97% | 26.06% | 6.49% | 1.37% | 23,607 | +2.09% |
| 2026-W13 | 89.11% | 25.99% | 6.26% | 3.32% | 24,581 | -1.32% |
| 2026-W12 | 90.30% | 25.55% | 6.04% | 2.49% | 24,839 | +0.03% |
| 2026-W11 | 90.27% | 24.97% | 5.89% | 2.65% | 26,804 | -1.36% |
| 2026-W10 | 91.51% | 25.47% | 5.84% | 1.40% | 27,719 | -0.06% |
| 2026-W09 | 91.57% | 24.88% | 5.81% | 1.27% | 30,555 | +0.03% |
| 2026-W08 | 91.54% | 24.93% | 6.13% | 1.08% | 28,183 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W14 | 91.59% | - | 25.49% | - | 16,726 |  |
| US | 2026-W15 | 89.20% | -2.61% | 26.41% | +3.60% | 20,057 | ⚠️ |
| CA | 2026-W14 | 89.46% | - | 27.44% | - | 6,881 |  |
| CA | 2026-W15 | 90.87% | +1.57% | 28.34% | +3.30% | 7,515 |  |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.24% | - | 24.28% | - | 19,231 |  |
| Paid | 2026-W15 | 95.63% | -0.64% | 25.81% | +6.29% | 22,526 |  |
| Referral | 2026-W14 | 67.80% | - | 33.89% | - | 4,376 |  |
| Referral | 2026-W15 | 63.00% | -7.08% | 31.99% | -5.62% | 5,046 | ⚠️ |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.14% | - | 24.65% | - | 0.53% | - | 2.04% | - | 5,492 |  |
| Paid | 2026-W15 | 96.41% | +0.28% | 26.14% | +6.04% | 0.64% | +20.98% | 2.06% | +1.20% | 6,105 |  |
| Referral | 2026-W14 | 63.07% | - | 38.44% | - | 30.02% | - | 4.90% | - | 1,389 |  |
| Referral | 2026-W15 | 66.88% | +6.05% | 37.87% | -1.49% | 28.37% | -5.51% | 3.48% | -29.01% | 1,410 | ⚠️ |

**Analysis:** The 1.31 pp decline in HF-NA Fraud Approval Rate is primarily driven by US performance, specifically within the Referral channel where a dramatic +409.56% increase in PF Block rate caused FAR to drop 12.15%. This suggests a potential fraud prevention model or rule change impacting US Referral traffic that warrants immediate investigation. The Paid channel and CA region remained stable, confirming the issue is isolated to US Referral fraud prevention blocking behavior.

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.28% | - | 24.13% | - | 2.20% | - | 0.50% | - | 13,739 |  |
| Paid | 2026-W15 | 95.34% | -0.98% | 25.68% | +6.43% | 3.01% | +36.86% | 0.90% | +79.46% | 16,421 |  |
| Referral | 2026-W14 | 70.00% | - | 31.77% | - | 26.21% | - | 2.48% | - | 2,987 |  |
| Referral | 2026-W15 | 61.50% | -12.15% | 29.70% | -6.51% | 25.22% | -3.79% | 12.62% | +409.56% | 3,636 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↓ -2.61% | Referral ↓ -12.15% | ↑ +3.60% | ↑ +8.45% | ↑ +253.98% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-17*
