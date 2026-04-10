# Fraud Investigation: US-HF 2026-W13

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 88.61% → 91.54% (+3.30%)  
**Volume:** 16,609 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by -1.41 percentage points from 89.88% (W12) to 88.61% (W13), representing a significant negative shift in fraud service performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR Trend | FAR dropped from 89.88% to 88.61% | -1.41 pp | ⚠️ |
| L1: Country Breakdown | US showed decline but within threshold | -1.41 pp | ✅ |
| L1: Channel - Paid | Minor decline, stable performance | -0.78 pp | ✅ |
| L1: Channel - Referral | Exceeded ±2.5% threshold | -4.26 pp | ⚠️ |

**Key Findings:**
- Referral channel FAR declined significantly from 62.44% to 59.79% (-4.26 pp), exceeding the ±2.5% threshold and flagged as a concern
- Pre-Fraud (PF) Block Rate increased notably from 2.72% (W12) to 3.60% (W13), a +0.88 pp increase that may be contributing to lower approvals
- Duplicate Rate increased slightly from 24.70% to 25.13% (+0.43 pp), continuing an upward trend over recent weeks
- Volume remained relatively stable at 17,575 customers (W13) vs 17,515 (W12)
- Paid channel maintained strong FAR at 96.17% despite slight decline of -0.78 pp

**Action:** Investigate — Focus investigation on the Referral channel's -4.26 pp FAR decline and the elevated Pre-Fraud Block Rate (+0.88 pp) to identify root causes driving reduced approvals.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 91.54% | 26.05% | 6.81% | 0.92% | 16,609 | +3.30% |
| 2026-W13 | 88.61% | 25.13% | 6.73% | 3.60% | 17,575 | -1.41% ← REPORTED CHANGE |
| 2026-W12 | 89.88% | 24.70% | 6.37% | 2.72% | 17,515 | +0.14% |
| 2026-W11 | 89.75% | 23.92% | 6.22% | 2.92% | 19,069 | -2.04% |
| 2026-W10 | 91.62% | 24.72% | 5.96% | 1.22% | 20,601 | -0.07% |
| 2026-W09 | 91.68% | 24.05% | 5.93% | 1.16% | 23,228 | +0.30% |
| 2026-W08 | 91.41% | 23.89% | 6.52% | 0.90% | 21,171 | -1.44% |
| 2026-W07 | 92.75% | 23.30% | 5.68% | 0.51% | 21,976 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W12 | 89.88% | - | 24.70% | - | 17,515 |  |
| US | 2026-W13 | 88.61% | -1.41% | 25.13% | +1.71% | 17,575 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W12 | 96.92% | - | 23.73% | - | 13,939 |  |
| Paid | 2026-W13 | 96.17% | -0.78% | 24.28% | +2.29% | 13,927 |  |
| Referral | 2026-W12 | 62.44% | - | 28.50% | - | 3,576 |  |
| Referral | 2026-W13 | 59.79% | -4.26% | 28.37% | -0.43% | 3,648 | ⚠️ |

---

*Report: 2026-04-10*
