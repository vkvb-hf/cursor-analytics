# AR Overall Investigation: HF-NA 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 92.42% → 92.31% (-0.12%)  
**Volume:** 513,372 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for HF-NA remained stable in 2026-W15, showing a slight improvement of +0.28pp (92.16% → 92.42%) with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.38pp | ✅ |
| 2_PreDunningAR | Target Metric | +0.28pp | ✅ |
| 3_PostDunningAR | Downstream | -0.01pp | ✅ |
| 6_PaymentApprovalRate | Final | +0.11pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; both US (+0.33pp) and CA (+0.03pp) showed stable or slightly improved performance
- Apple Pay showed the largest improvement among payment methods (+0.56pp to 86.28%), though it remains the lowest-performing method
- The 8-week trend shows the metric operating within a narrow band (91.59% - 92.42%), indicating stable overall performance
- All payment providers remained stable with Braintree (385,047 orders, +0.32pp) and ProcessOut (83,802 orders, +0.26pp) showing slight improvements
- Mix shift analysis confirms stable volume distribution across AR tiers with no concerning movements

**Action:** Monitor — No investigation required. The metric change is not statistically significant, no dimensional breakdowns exceed alert thresholds, and the 8-week trend shows normal fluctuation within expected ranges.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.31% | 513,372 | -0.12% |
| 2026-W15 | 92.42% | 497,775 | +0.28% ← REPORTED CHANGE |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | -0.16% |
| 2026-W11 | 92.28% | 539,763 | +0.30% |
| 2026-W10 | 92.0% | 554,777 | +0.45% |
| 2026-W09 | 91.59% | 553,112 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.49% | 93.47% | +0.03% | 103,253 |  |
| US | 93.09% | 92.78% | +0.33% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.28% | 98.54% | -0.26% | 4,410 |  |
| Paypal | 95.59% | 95.4% | +0.20% | 60,610 |  |
| Credit Card | 92.93% | 92.72% | +0.23% | 366,511 |  |
| Apple Pay | 86.28% | 85.8% | +0.56% | 66,244 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 91.46% | 91.94% | -0.52% | 773 |  |
| Adyen | 93.12% | 93.17% | -0.06% | 24,575 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,578 |  |
| ProcessOut | 90.07% | 89.84% | +0.26% | 83,802 |  |
| Braintree | 92.82% | 92.52% | +0.32% | 385,047 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.29% | 90.95% | +0.38% | 497,775 | 507,189 |  |
| 2_PreDunningAR | 92.42% | 92.16% | +0.28% | 497,775 | 507,189 |  |
| 3_PostDunningAR | 93.5% | 93.51% | -0.01% | 497,775 | 507,189 |  |
| 6_PaymentApprovalRate | 94.1% | 93.99% | +0.11% | 497,775 | 507,189 |  |

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

*Report: 2026-04-22*
