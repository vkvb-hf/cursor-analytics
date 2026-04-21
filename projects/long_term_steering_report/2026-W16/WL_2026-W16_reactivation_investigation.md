# Reactivation Investigation: WL 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.29% → 86.81% (-2.78%)  
**Volume:** 8,022 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate declined from 89.29% to 86.81% (-2.48 pp) in W16, representing a significant drop that breaks a three-week period of relative stability.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Metric dropped below recent range (85.86%-89.29%) | -2.48 pp | ⚠️ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | Max: -1.06 pp (KN) | ✅ |
| L1: PaymentMethod | Credit Card showed notable decline | -3.24 pp | ⚠️ |
| L1: PaymentProvider | No data available for analysis | N/A | ✅ |
| Mix Shift Analysis | All countries show stable impact | No shifts | ✅ |

**Key Findings:**
- Credit Card payment method declined -3.24 pp (89.92% → 87.01%) and represents 71% of volume (5,690 of 8,022 orders), making it the primary driver of the overall decline
- No single country exceeded the ±2.5% threshold; KN showed the largest decline at -1.06 pp
- Volume decreased 13.5% week-over-week (9,277 → 8,022 orders), which may amplify rate volatility
- GN showed strong volume growth (+17.8%) while maintaining high performance (94.19%), partially offsetting declines
- The "Others" payment method flagged (+200%) is not actionable due to minimal volume (1 order)

**Action:** Investigate — Focus on Credit Card payment method performance, as it accounts for the majority of volume and shows the largest rate decline. Review for potential technical issues, authorization failures, or processor-specific problems.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 86.81% | 8,022 | -2.78% ← REPORTED CHANGE |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.81% | 88.75% | -1.06% | 11,057 |  |
| MR | 80.82% | 81.37% | -0.68% | 18,584 |  |
| CK | 93.32% | 93.91% | -0.63% | 43,017 |  |
| AO | 87.79% | 87.06% | +0.83% | 14,640 |  |
| GN | 94.19% | 93.32% | +0.94% | 15,445 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 87.01% | 89.92% | -3.24% | 5,690 | ⚠️ |
| Paypal | 92.02% | 93.27% | -1.34% | 1,591 |  |
| Apple Pay | 74.05% | 74.94% | -1.18% | 740 |  |
| Others | 100.0% | 33.33% | +200.00% | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 68,811 | 69,808 | +1.4% | Stable |
| CG | High (>92%) | 43,937 | 42,996 | -2.1% | Stable |
| CK | High (>92%) | 42,398 | 43,017 | +1.5% | Stable |
| MR | Low (>85%) | 19,468 | 18,584 | -4.5% | Stable |
| AO | Medium (>85%) | 13,883 | 14,640 | +5.5% | Stable |
| GN | High (>92%) | 13,110 | 15,445 | +17.8% | Stable |
| KN | Medium (>85%) | 10,259 | 11,057 | +7.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
