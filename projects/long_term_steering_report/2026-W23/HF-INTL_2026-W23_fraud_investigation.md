# Fraud Investigation: HF-INTL 2026-W23

**Metric:** Fraud Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 92.51% → 92.66% (+0.16%)  
**Volume:** 38,519 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL increased marginally from 92.51% to 92.66% (+0.15pp) in 2026-W23, a change that is not statistically significant, with volume at 38,519 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (91.16%-92.66%) | +0.16pp | ✅ |
| L1: Country Scan | CH exceeds ±2.5% threshold | CH +3.63pp | ⚠️ |
| L1: Channel Category | Referral channel decline vs Paid stable | Referral -1.22pp | ✅ |
| L2: Duplicate Rate | New dup detection launched (0% → 32.31%) | +32.31pp | ⚠️ |
| L2: Referral Channel | Multiple countries show Referral FAR drops >5pp | NO -9.09pp, DK -8.05pp, CH -7.17pp | ⚠️ |

**Key Findings:**
- A new duplicate detection system was deployed in W23, evidenced by Dup Rate jumping from 0.00% to 32.31% across all markets, with corresponding Dup Block rates emerging (5.86% at L0)
- CH shows the largest country-level FAR improvement (+3.63pp), driven by Paid channel gains (+2.54pp), though volumes are low (148 customers)
- Referral channel FAR declined across nearly all markets in L2 analysis, with NO (-9.09pp), DK (-8.05pp), and CH (-7.17pp) showing the steepest drops
- The Referral Dup Block rates are significantly higher than Paid (e.g., IE Referral 21.66% vs Paid 0.00%), suggesting duplicate detection is catching more fraud attempts in the Referral channel
- GB maintains the highest volume (10,803) with stable FAR performance (-0.26pp), indicating core market health

**Action:** **Monitor** - The overall FAR change is not significant and remains within historical range. The new duplicate detection system appears to be functioning as intended, blocking fraudulent duplicates primarily in the higher-risk Referral channel. Continue monitoring Referral channel FAR in subsequent weeks to confirm the dup blocking is appropriately calibrated.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W23 | 92.66% | 32.31% | 5.86% | 0.22% | 38,519 | +0.16% ← REPORTED CHANGE |
| 2026-W22 | 92.51% | 0.00% | 0.00% | 0.36% | 35,283 | +0.46% |
| 2026-W21 | 92.09% | 0.00% | 0.00% | 0.30% | 34,646 | +1.02% |
| 2026-W20 | 91.16% | 0.00% | 0.00% | 0.31% | 38,780 | -1.26% |
| 2026-W19 | 92.32% | 0.00% | 0.00% | 0.25% | 39,883 | +0.56% |
| 2026-W18 | 91.81% | 0.00% | 0.00% | 0.53% | 41,059 | -0.32% |
| 2026-W17 | 92.11% | 0.00% | 0.00% | 0.31% | 41,733 | +0.11% |
| 2026-W16 | 92.00% | 0.00% | 0.00% | 0.23% | 44,964 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| AU | 2026-W22 | 91.40% | - | 0.00% | - | 3,628 |  |
| AU | 2026-W23 | 93.11% | +1.87% | 36.00% | - | 3,222 |  |
| DE | 2026-W22 | 92.84% | - | 0.00% | - | 6,191 |  |
| DE | 2026-W23 | 93.35% | +0.55% | 30.33% | - | 6,723 |  |
| IE | 2026-W22 | 94.72% | - | 0.00% | - | 2,008 |  |
| IE | 2026-W23 | 92.89% | -1.94% | 24.27% | - | 1,504 |  |
| GB | 2026-W22 | 93.79% | - | 0.00% | - | 8,988 |  |
| GB | 2026-W23 | 93.55% | -0.26% | 43.32% | - | 10,803 |  |
| NZ | 2026-W22 | 88.28% | - | 0.00% | - | 887 |  |
| NZ | 2026-W23 | 89.57% | +1.47% | 34.89% | - | 940 |  |
| CH | 2026-W22 | 84.11% | - | 0.00% | - | 151 |  |
| CH | 2026-W23 | 87.16% | +3.63% | 9.46% | - | 148 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CH

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 97.54% | - | 0.00% | - | 27,537 |  |
| Paid | 2026-W23 | 97.86% | +0.32% | 32.53% | - | 30,230 |  |
| Referral | 2026-W22 | 74.63% | - | 0.00% | - | 7,746 |  |
| Referral | 2026-W23 | 73.72% | -1.22% | 31.51% | - | 8,289 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.32% | - | 0.00% | - | 0.00% | - | 0.00% | - | 298 |  |
| Paid | 2026-W23 | 97.64% | -0.69% | 19.53% | - | 1.01% | - | 0.00% | - | 297 |  |
| Referral | 2026-W22 | 67.48% | - | 0.00% | - | 0.00% | - | 0.00% | - | 123 |  |
| Referral | 2026-W23 | 62.86% | -6.85% | 22.86% | - | 21.90% | - | 0.95% | - | 105 | ⚠️ |

**Analysis:** The W23 FAR performance for HF-INTL remains stable and within normal operating parameters despite the rollout of new duplicate detection capabilities. The observed Referral channel FAR declines across multiple markets (NO, DK, CH, AT, SE) are expected behavior as the duplicate blocking mechanism removes previously undetected fraud attempts, and the overall FAR improvement suggests the system is correctly approving legitimate customers while blocking duplicates. No immediate action is required, but the team should continue monitoring Referral channel metrics over the next 2-3 weeks to ensure the duplicate detection thresholds are optimally calibrated.

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 95.65% | - | 0.00% | - | 0.00% | - | 0.00% | - | 92 |  |
| Paid | 2026-W23 | 98.08% | +2.54% | 8.65% | - | 0.00% | - | 0.96% | - | 104 | ⚠️ |
| Referral | 2026-W22 | 66.10% | - | 0.00% | - | 0.00% | - | 0.00% | - | 59 |  |
| Referral | 2026-W23 | 61.36% | -7.17% | 11.36% | - | 9.09% | - | 0.00% | - | 44 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.74% | - | 0.00% | - | 0.00% | - | 0.13% | - | 792 |  |
| Paid | 2026-W23 | 99.49% | +0.77% | 28.79% | - | 0.13% | - | 0.13% | +0.00% | 792 |  |
| Referral | 2026-W22 | 80.71% | - | 0.00% | - | 0.00% | - | 0.00% | - | 254 |  |
| Referral | 2026-W23 | 74.21% | -8.05% | 28.42% | - | 17.37% | - | 0.53% | - | 190 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: IE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 99.20% | - | 0.00% | - | 0.00% | - | 0.06% | - | 1,622 |  |
| Paid | 2026-W23 | 99.20% | +0.01% | 24.16% | - | 0.00% | - | 0.18% | +187.08% | 1,130 |  |
| Referral | 2026-W22 | 75.91% | - | 0.00% | - | 0.00% | - | 0.00% | - | 386 |  |
| Referral | 2026-W23 | 73.80% | -2.78% | 24.60% | - | 21.66% | - | 0.27% | - | 374 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 100.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 108 |  |
| Paid | 2026-W23 | 100.00% | +0.00% | 10.91% | - | 0.00% | - | 0.00% | - | 110 |  |
| Referral | 2026-W22 | 30.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 20 |  |
| Referral | 2026-W23 | 31.58% | +5.26% | 15.79% | - | 10.53% | - | 0.00% | - | 19 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.96% | - | 0.00% | - | 0.00% | - | 0.00% | - | 575 |  |
| Paid | 2026-W23 | 99.39% | +0.44% | 21.86% | - | 0.20% | - | 0.00% | - | 494 |  |
| Referral | 2026-W22 | 84.62% | - | 0.00% | - | 0.00% | - | 0.00% | - | 169 |  |
| Referral | 2026-W23 | 76.92% | -9.09% | 23.93% | - | 11.11% | - | 0.00% | - | 117 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.79% | - | 0.00% | - | 0.00% | - | 0.76% | - | 660 |  |
| Paid | 2026-W23 | 98.20% | -0.59% | 33.15% | - | 0.14% | - | 0.55% | -27.07% | 724 |  |
| Referral | 2026-W22 | 57.71% | - | 0.00% | - | 0.00% | - | 0.44% | - | 227 |  |
| Referral | 2026-W23 | 60.65% | +5.09% | 40.74% | - | 32.87% | - | 0.00% | -100.00% | 216 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: SE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.57% | - | 0.00% | - | 0.00% | - | 0.00% | - | 840 |  |
| Paid | 2026-W23 | 98.61% | +0.04% | 35.37% | - | 0.42% | - | 0.14% | - | 721 |  |
| Referral | 2026-W22 | 87.11% | - | 0.00% | - | 0.00% | - | 0.35% | - | 287 |  |
| Referral | 2026-W23 | 83.03% | -4.68% | 23.85% | - | 8.26% | - | 0.00% | -100.00% | 218 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| CH | ↑ +3.63% | Paid ↑ +2.54%, Referral ↓ -7.17% | → - | → - | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-06-09*
