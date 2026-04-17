# AR Overall Investigation: HF-NA 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 92.17% → 92.42% (+0.27%)  
**Volume:** 497,775 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Overall) for HF-NA improved slightly from 92.17% to 92.42% (+0.25 pp) in 2026-W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | +0.38 pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | +0.28 pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.04 pp | ✅ |
| 6_PaymentApprovalRate | Final approval | +0.11 pp | ✅ |

**Key Findings:**
- All funnel metrics remain stable with no significant changes; the overall rate of 92.42% continues an upward trend from 91.35% in W08
- No countries exceeded the ±2.5% threshold; US showed the largest improvement at +0.34 pp while CA remained flat at +0.02 pp
- Apple Pay showed the strongest improvement among payment methods (+0.56 pp to 86.28%), though it remains the lowest-performing method
- Volume declined by approximately 1.9% week-over-week (507,189 → 497,775 orders), consistent with the gradual downward volume trend observed over the 8-week period
- Mix shift analysis shows stable distribution with both US and CA maintaining High AR tier (>92%)

**Action:** Monitor — No intervention required. The metric shows normal fluctuation within expected ranges and continues a gradual positive trend over the 8-week period.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 92.42% | 497,775 | +0.27% ← REPORTED CHANGE |
| 2026-W14 | 92.17% | 507,189 | -0.07% |
| 2026-W13 | 92.23% | 517,599 | +0.10% |
| 2026-W12 | 92.14% | 526,516 | -0.15% |
| 2026-W11 | 92.28% | 539,763 | +0.30% |
| 2026-W10 | 92.0% | 554,777 | +0.45% |
| 2026-W09 | 91.59% | 553,112 | +0.26% |
| 2026-W08 | 91.35% | 548,921 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.51% | 93.49% | +0.02% | 103,253 |  |
| US | 93.09% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.23% | 98.54% | -0.31% | 4,412 |  |
| Paypal | 95.59% | 95.4% | +0.20% | 60,610 |  |
| Credit Card | 92.94% | 92.72% | +0.23% | 366,509 |  |
| Apple Pay | 86.28% | 85.8% | +0.56% | 66,244 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 91.23% | 91.94% | -0.78% | 775 |  |
| Adyen | 93.18% | 93.24% | -0.06% | 24,575 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,578 |  |
| ProcessOut | 90.07% | 89.84% | +0.26% | 83,802 |  |
| Braintree | 92.82% | 92.52% | +0.32% | 385,045 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.29% | 90.95% | +0.38% | 497,775 | 507,189 |  |
| 2_PreDunningAR | 92.42% | 92.17% | +0.28% | 497,775 | 507,189 |  |
| 3_PostDunningAR | 93.29% | 93.33% | -0.04% | 497,775 | 507,189 |  |
| 6_PaymentApprovalRate | 94.1% | 94.0% | +0.11% | 497,775 | 507,189 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 497,052 | 492,811 | -0.9% | Stable |
| CA | High (>92%) | 105,530 | 103,253 | -2.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-17*
