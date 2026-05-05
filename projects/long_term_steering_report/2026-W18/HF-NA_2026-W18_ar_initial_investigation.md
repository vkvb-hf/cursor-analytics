# AR Initial (LL0) Investigation: HF-NA 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 90.11% → 89.35% (-0.84%)  
**Volume:** 16,003 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-NA declined from 90.11% to 89.35% (-0.76 pp) in 2026-W18, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | -0.81 pp | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.76 pp | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.71 pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.80 pp | ⚠️ |

**Key Findings:**
- The decline is consistent across the entire payment funnel, with all stages showing ~0.7-0.9 pp drops, indicating the issue originates at first payment attempt rather than recovery processes
- Both countries declined: CA dropped -1.24 pp (93.07% → 91.83%) and US dropped -0.71 pp (88.95% → 88.24%), with neither exceeding the ±2.5% investigation threshold
- Volume decreased 11.6% week-over-week (18,104 → 16,003 orders), primarily driven by US volume reduction of -14.7%
- No payment method or provider showed anomalous behavior exceeding thresholds; "Others" and "Unknown" provider showed the largest declines at -1.15 pp and -1.25 pp respectively
- The 8-week trend shows normal fluctuation within the 89.16%-90.82% range, with W18 near the lower bound but not unprecedented

**Action:** Monitor — The decline is not statistically significant, no dimensions exceed investigation thresholds, and the rate remains within normal 8-week variability. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 89.35% | 16,003 | -0.84% ← REPORTED CHANGE |
| 2026-W17 | 90.11% | 18,104 | +0.73% |
| 2026-W16 | 89.46% | 18,040 | -0.47% |
| 2026-W15 | 89.88% | 16,065 | +0.21% |
| 2026-W14 | 89.69% | 17,105 | +0.59% |
| 2026-W13 | 89.16% | 16,167 | -0.59% |
| 2026-W12 | 89.69% | 21,074 | -1.24% |
| 2026-W11 | 90.82% | 21,784 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 91.83% | 93.07% | -1.33% | 4,911 |  |
| US | 88.24% | 88.95% | -0.80% | 11,092 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 89.53% | 90.68% | -1.26% | 9,382 |  |
| Paypal | 89.77% | 90.68% | -1.00% | 1,280 |  |
| Apple Pay | 88.83% | 89.04% | -0.23% | 4,925 |  |
| Credit Card | 89.9% | 88.25% | +1.87% | 416 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 89.09% | 90.34% | -1.38% | 8,968 |  |
| Adyen | 96.2% | 96.96% | -0.78% | 579 |  |
| Braintree | 88.9% | 89.23% | -0.37% | 6,352 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 104 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.23% | 89.04% | -0.90% | 16,003 | 18,104 |  |
| 2_PreDunningAR | 89.35% | 90.11% | -0.85% | 16,003 | 18,104 |  |
| 3_PostDunningAR | 89.51% | 90.22% | -0.79% | 16,003 | 18,104 |  |
| 6_PaymentApprovalRate | 89.63% | 90.43% | -0.88% | 16,003 | 18,104 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 13,007 | 11,092 | -14.7% | Stable |
| CA | High (>92%) | 5,097 | 4,911 | -3.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
