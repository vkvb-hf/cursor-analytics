# PAR Investigation: WL 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.05% → 91.65% (+0.66%)  
**Volume:** 160,979 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate improved from 91.05% to 91.65% (+0.60 pp) in W15, representing a modest but statistically non-significant increase on 160,979 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.92% | ✅ |
| 2_PreDunningAR | Within normal range | +0.87% | ✅ |
| 3_PostDunningAR | Within normal range | +0.53% | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.67% | ✅ |

**Key Findings:**
- All funnel steps showed positive movement, with FirstRunAR contributing the largest improvement (+0.92%), indicating upstream payment success drove the PAR increase
- No countries exceeded the ±2.5% threshold; AO showed the largest country-level improvement (+2.17 pp) on 13,883 orders
- ProcessOut provider improved significantly (+2.05 pp) while Unknown provider showed anomalous +13.15% change on minimal volume (664 orders) - flagged as ⚠️
- Volume declined 2.4% week-over-week (165,018 → 160,979), with notable drops in AO (-12.0%) and GN (-8.5%)
- All major payment methods (Credit Card, PayPal, Apple Pay) showed stable, modest improvements under +0.70 pp

**Action:** Monitor — The improvement is not statistically significant and falls within normal weekly variance. Continue standard monitoring; no investigation required.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.65% | 160,979 | +0.66% ← REPORTED CHANGE |
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,965 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | +0.04% |
| 2026-W08 | 89.88% | 179,647 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.32% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.41% | 80.25% | +1.45% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.35% | 98.67% | -0.32% | 1,393 |  |
| Apple Pay | 87.44% | 87.06% | +0.43% | 20,488 |  |
| Paypal | 96.03% | 95.52% | +0.54% | 24,084 |  |
| Credit Card | 91.41% | 90.78% | +0.69% | 115,014 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 683 |  |
| Braintree | 92.22% | 91.8% | +0.45% | 105,580 |  |
| Adyen | 94.13% | 93.51% | +0.67% | 36,376 |  |
| ProcessOut | 82.67% | 81.01% | +2.05% | 17,676 |  |
| Unknown | 96.99% | 85.71% | +13.15% | 664 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.17% | 87.37% | +0.92% | 160,979 | 165,018 |  |
| 2_PreDunningAR | 90.1% | 89.33% | +0.87% | 160,979 | 165,018 |  |
| 3_PostDunningAR | 91.03% | 90.55% | +0.53% | 160,979 | 165,018 |  |
| 6_PaymentApprovalRate | 91.65% | 91.05% | +0.67% | 160,979 | 165,018 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 67,730 | 68,811 | +1.6% | Stable |
| CG | High (>92%) | 44,581 | 43,937 | -1.4% | Stable |
| CK | High (>92%) | 42,176 | 42,398 | +0.5% | Stable |
| MR | Low (>85%) | 20,784 | 19,468 | -6.3% | Stable |
| AO | Medium (>85%) | 15,776 | 13,883 | -12.0% | Stable |
| GN | High (>92%) | 14,333 | 13,110 | -8.5% | Stable |
| KN | Medium (>85%) | 11,048 | 10,259 | -7.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
