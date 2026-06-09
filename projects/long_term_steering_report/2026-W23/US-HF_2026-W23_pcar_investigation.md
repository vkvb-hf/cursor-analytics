# PCAR Investigation: US-HF 2026-W23

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 90.39% → 91.56% (+1.29%)  
**Volume:** 15,371 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved significantly from 90.39% to 91.56% (+1.29%) in US-HF for 2026-W23, representing a positive recovery toward the 8-week high of 92.75% observed in W16.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate increasing from recent low | +1.29% vs W22 | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +1.29% (US only) | ✅ |
| L1: PaymentMethod | Others segment flagged (+3.68%) | Low volume (69 orders) | ⚠️ |
| L1: PaymentProvider | No data available | - | ✅ |
| Mix Shift | US Medium tier stable | +3.5% volume | ✅ |

**Key Findings:**
- US approval rate recovered +1.29% WoW, reversing the -0.40% decline from W22 and continuing the upward trend from W21's +1.79% gain
- The "Others" payment method showed the largest improvement at +3.68%, though with minimal volume impact (69 orders)
- Apple Pay showed strong improvement at +1.88% with significant volume (5,293 orders), contributing meaningfully to overall gains
- Credit Card, the highest volume segment (8,750 orders), improved +1.13%, driving the bulk of the rate increase
- PayPal was the only payment method to decline slightly (-0.28%), though the impact was minimal given its lower volume (1,259 orders)

**Action:** Monitor — The improvement is significant and broad-based across major payment methods. No deep-dive required as no countries exceeded the ±2.5% threshold. Continue monitoring to confirm the recovery trend sustains toward the W16-W17 baseline of ~92.7%.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 91.56% | 15,371 | +1.29% ← REPORTED CHANGE |
| 2026-W22 | 90.39% | 14,855 | -0.40% |
| 2026-W21 | 90.75% | 14,363 | +1.79% |
| 2026-W20 | 89.15% | 15,543 | -0.51% |
| 2026-W19 | 89.61% | 16,327 | -1.67% |
| 2026-W18 | 91.13% | 16,396 | -1.66% |
| 2026-W17 | 92.67% | 15,496 | -0.09% |
| 2026-W16 | 92.75% | 18,142 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 91.56% | 90.39% | +1.29% | 15,371 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 90.47% | 90.72% | -0.28% | 1,259 |  |
| Credit Card | 91.75% | 90.72% | +1.13% | 8,750 |  |
| Apple Pay | 91.42% | 89.74% | +1.88% | 5,293 |  |
| Others | 97.1% | 93.65% | +3.68% | 69 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 14,855 | 15,371 | +3.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
