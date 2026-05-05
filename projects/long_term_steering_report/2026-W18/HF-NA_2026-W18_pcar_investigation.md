# PCAR Investigation: HF-NA 2026-W18

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 93.94% → 92.45% (-1.59%)  
**Volume:** 21,205 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined significantly from 93.94% to 92.45% (-1.59pp) in W18, representing the largest week-over-week drop in the 8-week trend period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | W18 vs W17 | -1.59pp | ⚠️ |
| L1: Country - US | Largest market | -1.66pp | ⚠️ |
| L1: Country - CA | Secondary market | -1.06pp | ⚠️ |
| L1: PaymentMethod - Credit Card | Highest volume method | -2.12pp | ⚠️ |
| L1: PaymentMethod - PayPal | Mid volume | -1.57pp | ⚠️ |
| L1: PaymentMethod - Apple Pay | Mid volume | -0.69pp | ✅ |
| Mix Shift | Volume distribution | Stable | ✅ |

**Key Findings:**
- Credit Card payments showed the steepest decline at -2.12pp (from 94.13% to 92.14%) with 12,224 orders, making it the primary driver of the overall rate drop
- US market declined -1.66pp (92.67% → 91.13%) on 16,396 orders, contributing the majority of the negative impact given its 77% volume share
- CA also declined -1.06pp (98.01% → 96.96%) indicating the issue is not isolated to a single country
- Mix shift analysis shows stable volume distribution between AR tiers, suggesting the decline is driven by within-segment performance degradation rather than volume shifts
- No individual country exceeded the ±2.5% threshold for automatic deep-dive escalation

**Action:** Investigate – The simultaneous decline across both countries and the pronounced Credit Card payment method drop (-2.12pp) warrants investigation into potential payment processor issues or fraud rule changes affecting Credit Card transactions, particularly in US.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 92.45% | 21,205 | -1.59% ← REPORTED CHANGE |
| 2026-W17 | 93.94% | 20,363 | +0.09% |
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,512 | -0.04% |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% |
| 2026-W11 | 94.16% | 22,919 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 91.13% | 92.67% | -1.66% | 16,396 |  |
| CA | 96.96% | 98.01% | -1.06% | 4,809 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 92.14% | 94.13% | -2.12% | 12,224 |  |
| Paypal | 92.41% | 93.89% | -1.57% | 1,831 |  |
| Apple Pay | 92.95% | 93.6% | -0.69% | 7,095 |  |
| Others | 100.0% | 98.33% | +1.69% | 55 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 15,496 | 16,396 | +5.8% | Stable |
| CA | High (>92%) | 4,867 | 4,809 | -1.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
