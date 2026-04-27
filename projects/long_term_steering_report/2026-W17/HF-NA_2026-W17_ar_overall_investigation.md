# AR Overall Investigation: HF-NA 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.31% → 92.19% (-0.13%)  
**Volume:** 510,064 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Overall) declined slightly from 92.31% to 92.19% (-0.12pp) in W17, a change that is **not statistically significant** with stable volume of 510,064 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.10pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.12pp | ✅ |
| 3_PostDunningAR | Recovery | -0.28pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.10pp | ✅ |

**Key Findings:**
- The -0.13pp decline is within normal weekly fluctuation; the 8-week trend shows rates oscillating between 92.0% and 92.41%
- CA showed the largest country-level decline at -0.47pp (93.58% → 93.13%), while US remained stable at +0.02pp
- No countries exceeded the ±2.5% investigation threshold
- "Others" payment method declined -1.08pp (91.34% → 90.36%) and "Unknown" payment provider declined -1.08pp (91.0% → 90.02%), suggesting potential data classification issues
- ProcessOut provider shows 0 volume in W17 (previously had activity at 88.38% rate), indicating possible provider discontinuation or data gap

**Action:** **Monitor** — No immediate investigation required. Continue tracking CA performance and the "Unknown" payment provider/method categories for potential data quality follow-up.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.19% | 510,064 | -0.13% ← REPORTED CHANGE |
| 2026-W16 | 92.31% | 513,372 | -0.11% |
| 2026-W15 | 92.41% | 497,776 | +0.27% |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | -0.15% |
| 2026-W11 | 92.27% | 539,763 | +0.29% |
| 2026-W10 | 92.0% | 554,777 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.13% | 93.58% | -0.47% | 104,317 |  |
| US | 92.99% | 92.97% | +0.02% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.36% | 91.34% | -1.08% | 105,242 |  |
| Paypal | 95.78% | 95.69% | +0.09% | 62,032 |  |
| Apple Pay | 86.58% | 86.44% | +0.17% | 69,057 |  |
| Credit Card | 93.5% | 93.27% | +0.24% | 273,733 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 88.38% | +nan% | 0 |  |
| Unknown | 90.02% | 91.0% | -1.08% | 101,418 |  |
| Adyen | 92.07% | 92.5% | -0.47% | 25,697 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,500 |  |
| Braintree | 92.71% | 92.65% | +0.07% | 379,449 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.96% | 91.06% | -0.10% | 510,064 | 513,372 |  |
| 2_PreDunningAR | 92.19% | 92.31% | -0.12% | 510,064 | 513,372 |  |
| 3_PostDunningAR | 93.09% | 93.35% | -0.28% | 510,064 | 513,372 |  |
| 6_PaymentApprovalRate | 94.03% | 94.13% | -0.10% | 510,064 | 513,372 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 511,272 | 508,019 | -0.6% | Stable |
| CA | High (>92%) | 104,640 | 104,317 | -0.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
