# PAR Investigation: HF-NA 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.13% → 94.03% (-0.11%)  
**Volume:** 510,064 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-NA declined marginally from 94.13% to 94.03% (-0.10 pp) in W17, a statistically non-significant change within normal weekly variation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.10 pp | ✅ |
| 2_PreDunningAR | Recovery | -0.13 pp | ✅ |
| 3_PostDunningAR | Dunning | -0.27 pp | ⚠️ |
| 6_PaymentApprovalRate | Final | -0.11 pp | ✅ |

**Key Findings:**
- The -0.11 pp decline is well within normal fluctuation; the 8-week trend shows the rate has steadily improved from 93.64% (W10) to 94.03% (W17), representing a +0.39 pp gain over the period
- CA experienced a -0.41 pp decline (95.75% → 95.35%) while US remained stable with a slight +0.03 pp improvement; neither country exceeded the ±2.5% threshold
- PostDunningAR showed the largest step decline at -0.27 pp, suggesting dunning recovery was slightly less effective this week
- "Others" payment method declined -0.79 pp (93.24% → 92.5%) and "Unknown" provider declined -0.80 pp (92.96% → 92.22%), the largest dimension-level drops observed
- Mix shift analysis shows stable volume distribution across both US and CA with minimal movement (<1% volume change)

**Action:** Monitor – No investigation required. The change is not statistically significant, no dimensions exceeded alert thresholds, and the overall 8-week trend remains positive.

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
| CA | 95.35% | 95.75% | -0.41% | 104,317 |  |
| US | 94.62% | 94.59% | +0.03% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.5% | 93.24% | -0.79% | 105,192 |  |
| Paypal | 96.53% | 96.52% | +0.01% | 62,032 |  |
| Apple Pay | 89.13% | 89.07% | +0.06% | 69,057 |  |
| Credit Card | 95.28% | 95.09% | +0.20% | 273,783 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 91.11% | +nan% | 0 |  |
| Unknown | 92.22% | 92.96% | -0.80% | 101,371 |  |
| Adyen | 95.41% | 95.72% | -0.33% | 25,715 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,500 |  |
| Braintree | 94.36% | 94.33% | +0.03% | 379,478 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.96% | 91.06% | -0.10% | 510,064 | 513,372 |  |
| 2_PreDunningAR | 92.19% | 92.31% | -0.13% | 510,064 | 513,372 |  |
| 3_PostDunningAR | 93.13% | 93.38% | -0.27% | 510,064 | 513,372 |  |
| 6_PaymentApprovalRate | 94.03% | 94.13% | -0.11% | 510,064 | 513,372 |  |

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

*Report: 2026-04-28*
