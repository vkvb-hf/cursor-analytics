# PCAR Investigation: US-HF 2026-W22

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 90.75% → 90.37% (-0.42%)  
**Volume:** 13,412 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** US-HF Payment Checkout Approval Rate declined by -0.42pp (90.75% → 90.37%) in 2026-W22, a change that is **not statistically significant** on volume of 13,412 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range | -0.42pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | -0.43pp (US) | ✅ |
| L1: PaymentMethod | "Others" exceeds threshold (+4.31%) | Low volume (58) | ✅ |
| L1: PaymentProvider | No data available | - | ✅ |
| Mix Shift | US Medium tier stable | -6.6% volume | ✅ |

**Key Findings:**
- The -0.42pp decline is within normal weekly fluctuation; W21 showed a +1.79pp increase, suggesting mean reversion
- 8-week trend shows gradual decline from 93.02% (W15) to 90.37% (W22), representing a -2.65pp erosion over 7 weeks
- "Others" payment method showed +4.31pp improvement but represents only 58 orders (0.4% of volume), making it non-material
- Apple Pay showed the largest decline among major payment methods at -1.08pp on 4,637 orders (35% of volume)
- Order volume continues to decline week-over-week (-6.6% from W21), down from 17,670 in W15

**Action:** **Monitor** - The weekly change is not significant and no dimensions exceeded thresholds. However, recommend tracking the longer-term downward trend in approval rate and declining order volumes over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 90.37% | 13,412 | -0.42% ← REPORTED CHANGE |
| 2026-W21 | 90.75% | 14,363 | +1.79% |
| 2026-W20 | 89.15% | 15,543 | -0.51% |
| 2026-W19 | 89.61% | 16,327 | -1.67% |
| 2026-W18 | 91.13% | 16,396 | -1.66% |
| 2026-W17 | 92.67% | 15,496 | -0.09% |
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,670 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.37% | 90.75% | -0.43% | 13,412 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 89.69% | 90.67% | -1.08% | 4,637 |  |
| Paypal | 90.79% | 91.01% | -0.25% | 1,075 |  |
| Credit Card | 90.68% | 90.76% | -0.09% | 7,642 |  |
| Others | 94.83% | 90.91% | +4.31% | 58 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 14,363 | 13,412 | -6.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
