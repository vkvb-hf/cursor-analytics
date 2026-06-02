# PAR Investigation: HF-NA 2026-W22

**Metric:** Payment Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 93.64% → 93.43% (-0.22%)  
**Volume:** 452,722 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined slightly from 93.64% to 93.43% (-0.21 pp) in W22, representing a non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Largest drop in funnel | -0.28 pp | ⚠️ |
| 2_PreDunningAR | Slight decline | -0.13 pp | ✅ |
| 3_PostDunningAR | Notable decline | -0.40 pp | ⚠️ |
| 6_PaymentApprovalRate | Final metric | -0.22 pp | ✅ |

**Key Findings:**
- PostDunningAR shows the largest decline in the funnel at -0.40 pp (92.90% → 92.52%), suggesting dunning recovery effectiveness decreased
- US drove the overall decline with -0.31 pp (94.24% → 93.95%) on 455K orders, while CA remained stable (+0.01 pp)
- PaymentProvider "Unknown" flagged with -9.78 pp decline (62.78% → 56.64%), though volume is minimal at 482 orders
- 8-week trend shows gradual decline from 94.09% (W15) to 93.43% (W22), a cumulative -0.66 pp over the period
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — The decline is not statistically significant and no dimensions exceeded alert thresholds. Continue tracking the gradual downward trend; if W23 continues below 93.5%, consider investigating PostDunningAR performance and the persistent decline pattern.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 93.43% | 452,722 | -0.22% ← REPORTED CHANGE |
| 2026-W21 | 93.64% | 468,983 | -0.23% |
| 2026-W20 | 93.86% | 487,754 | +0.20% |
| 2026-W19 | 93.67% | 508,009 | -0.27% |
| 2026-W18 | 93.92% | 506,464 | -0.11% |
| 2026-W17 | 94.02% | 510,064 | -0.11% |
| 2026-W16 | 94.12% | 513,373 | +0.03% |
| 2026-W15 | 94.09% | 497,777 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.95% | 94.24% | -0.31% | 455,505 |  |
| CA | 95.90% | 95.89% | +0.01% | 97,516 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 94.65% | 95.29% | -0.68% | 4,015 |  |
| Paypal | 96.01% | 96.33% | -0.33% | 54,714 |  |
| Apple Pay | 87.94% | 88.18% | -0.28% | 60,250 |  |
| Credit Card | 93.98% | 94.16% | -0.19% | 333,743 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 56.64% | 62.78% | -9.78% | 482 | ⚠️ |
| ProcessOut | 91.27% | 91.65% | -0.42% | 94,707 |  |
| Braintree | 93.81% | 94.0% | -0.20% | 329,966 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,120 |  |
| Adyen | 96.47% | 96.17% | +0.31% | 24,447 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.44% | 90.69% | -0.28% | 452,722 | 468,983 |  |
| 2_PreDunningAR | 91.72% | 91.84% | -0.13% | 452,722 | 468,983 |  |
| 3_PostDunningAR | 92.52% | 92.9% | -0.40% | 452,722 | 468,983 |  |
| 6_PaymentApprovalRate | 93.43% | 93.64% | -0.22% | 452,722 | 468,983 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 478,645 | 455,505 | -4.8% | Stable |
| CA | High (>92%) | 95,083 | 97,516 | +2.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
