# PAR Investigation: WL 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 91.65% → 91.69% (+0.04%)  
**Volume:** 164,785 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate showed a marginal improvement from 91.65% to 91.69% (+0.04 pp), a statistically non-significant change on volume of 164,785 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.92% | ✅ |
| 2_PreDunningAR | Within normal range | +0.87% | ✅ |
| 3_PostDunningAR | Within normal range | +0.61% | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.67% | ✅ |

**Key Findings:**
- All funnel steps show consistent improvement, with FirstRunAR contributing the largest gain (+0.92%), indicating upstream payment success drove the overall lift
- PaymentProvider "Unknown" flagged with +13.15% change, but represents minimal volume (664 orders) and does not materially impact overall rate
- No countries exceeded the ±2.5% threshold; AO showed the largest country-level improvement (+2.21 pp) but remained below threshold
- Volume declined 12.0% in AO and 8.5% in GN week-over-week, though mix shift impact remains stable across all segments
- ProcessOut provider improved +2.05 pp (17,676 orders), contributing positively to overall rate

**Action:** Monitor — The change is not statistically significant and all dimensions remain within normal operating ranges. No investigation or escalation required at this time.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.69% | 164,785 | +0.04% |
| 2026-W15 | 91.65% | 160,979 | +0.66% ← REPORTED CHANGE |
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,965 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 89.82% | 89.16% | +0.75% | 10,259 |  |
| ER | 91.36% | 90.56% | +0.87% | 68,811 |  |
| MR | 83.92% | 83.02% | +1.08% | 19,468 |  |
| AO | 93.21% | 91.20% | +2.21% | 13,883 |  |

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
| Adyen | 94.13% | 93.5% | +0.67% | 36,376 |  |
| ProcessOut | 82.67% | 81.01% | +2.05% | 17,676 |  |
| Unknown | 96.99% | 85.71% | +13.15% | 664 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.17% | 87.37% | +0.92% | 160,979 | 165,018 |  |
| 2_PreDunningAR | 90.1% | 89.32% | +0.87% | 160,979 | 165,018 |  |
| 3_PostDunningAR | 91.21% | 90.66% | +0.61% | 160,979 | 165,018 |  |
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

*Report: 2026-04-22*
