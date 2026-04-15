# Fraud Investigation: HF-NA 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.97% → 89.66% (-1.44%)  
**Volume:** 27,572 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) declined from 90.97% to 89.66% (-1.31pp) in 2026-W15, driven primarily by a significant drop in US Referral channel performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Overall | FAR 90.97% → 89.66% | -1.31pp | ⚠️ |
| L1: Country - US | FAR 91.59% → 89.20% | -2.61pp | ⚠️ |
| L1: Country - CA | FAR 89.46% → 90.87% | +1.41pp | ✅ |
| L1: Channel - Paid | FAR 96.24% → 95.63% | -0.61pp | ✅ |
| L1: Channel - Referral | FAR 67.80% → 63.00% | -4.80pp | ⚠️ |
| L2: US Referral | FAR 70.00% → 61.50% | -8.50pp | ⚠️ |
| L2: US Referral PF Block | 2.48% → 12.62% | +409.56% | ⚠️ |

**Key Findings:**
- US is the primary driver of FAR decline (-2.61pp), exceeding the ±2.5% threshold, while CA improved (+1.41pp)
- US Referral channel experienced severe FAR degradation (-12.15%), dropping from 70.00% to 61.50%
- PF Block rate in US Referral spiked dramatically from 2.48% to 12.62% (+409.56%), indicating a major policy or model change
- Overall volume increased significantly from 23,607 to 27,572 (+16.8%), with US volume growing from 16,726 to 20,057
- Duplicate Rate increased across both countries (US +3.60%, CA +3.30%) but Dup Block changes were moderate

**Action:** Investigate — Urgent review required of the PF Block rule/model changes affecting US Referral channel; the +409.56% increase in PF Block rate is the clear root cause of FAR decline.

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

**Analysis:** The 1.31pp decline in Fraud Approval Rate is attributable to a dramatic increase in PF (Policy/Fraud) Block rate within the US Referral channel, which surged from 2.48% to 12.62%. This isolated but severe impact on US Referral customers warrants immediate investigation into any policy changes, model updates, or fraud rule deployments that occurred between W14 and W15. CA performance improved during this period, confirming the issue is localized to US Referral traffic.

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


*Report: 2026-04-15*
