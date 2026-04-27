# PAR Investigation: HF-NA 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.13% → 94.03% (-0.11%)  
**Volume:** 510,064 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-NA declined slightly from 94.13% to 94.03% (-0.10pp) in W17, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline conversion | -0.10pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | -0.12pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.28pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.10pp | ✅ |

**Key Findings:**
- The -0.10pp decline is within normal weekly fluctuation; the 8-week trend shows PAR has steadily improved from 93.64% (W10) to 94.03% (W17), gaining +0.39pp overall
- CA showed the largest country-level movement at -0.39pp (95.75% → 95.37%), while US remained stable at +0.04pp
- Post-dunning recovery (3_PostDunningAR) showed the steepest funnel decline at -0.28pp, suggesting slightly reduced dunning effectiveness this week
- No payment method or provider exceeded the ±2.5% threshold; "Others" payment method showed the largest decline at -0.77pp but on moderate volume (105K orders)
- ProcessOut provider shows no volume in W17 (0 orders vs. prior week activity), though this represents minimal impact given historical low volume

**Action:** Monitor — No investigation required. The decline is not statistically significant, no dimensions exceeded alert thresholds, and the 8-week trend remains positive.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 94.03% | 510,064 | -0.11% ← REPORTED CHANGE |
| 2026-W16 | 94.13% | 513,372 | +0.03% |
| 2026-W15 | 94.1% | 497,776 | +0.12% |
| 2026-W14 | 93.99% | 507,189 | +0.03% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | -0.04% |
| 2026-W11 | 93.91% | 539,763 | +0.29% |
| 2026-W10 | 93.64% | 554,777 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 95.37% | 95.75% | -0.39% | 104,317 |  |
| US | 94.62% | 94.59% | +0.04% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.53% | 93.24% | -0.77% | 105,242 |  |
| Paypal | 96.53% | 96.52% | +0.01% | 62,032 |  |
| Apple Pay | 89.14% | 89.08% | +0.07% | 69,057 |  |
| Credit Card | 95.28% | 95.09% | +0.20% | 273,733 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 91.11% | +nan% | 0 |  |
| Unknown | 92.25% | 92.96% | -0.77% | 101,418 |  |
| Adyen | 95.41% | 95.72% | -0.32% | 25,697 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,500 |  |
| Braintree | 94.36% | 94.33% | +0.03% | 379,449 |  |

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
