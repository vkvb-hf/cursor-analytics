# PCAR Investigation: HF-NA 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 93.86% → 93.94% (+0.09%)  
**Volume:** 20,363 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-NA improved marginally from 93.86% to 93.94% (+0.08 pp) in W17, a change that is not statistically significant given the volume of 20,363 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (93.92%-95.23%) | +0.08 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US: -0.08 pp, CA: +0.29 pp | ✅ |
| L1: Payment Method | "Others" exceeded threshold but low volume | +4.12 pp (60 orders) | ⚠️ |
| Mix Shift | Volume declined but AR tiers stable | US: -14.6% vol, CA: -6.9% vol | ✅ |

**Key Findings:**
- The +0.08 pp increase represents a partial recovery from W16's -0.23 pp decline, but the rate remains below the W10 peak of 95.23% (-1.29 pp below peak)
- US approval rate declined slightly (-0.08 pp to 92.67%) while CA improved (+0.29 pp to 98.01%), with neither exceeding investigation thresholds
- "Others" payment method showed a +4.12 pp improvement flagged as ⚠️, but with only 60 orders this is not material to overall performance
- Credit Card (largest volume at 11,873 orders) improved +0.33 pp to 94.13%, contributing positively to the overall rate
- Overall volume decreased 12.9% week-over-week (23,369 → 20,363 orders)

**Action:** Monitor — The change is not statistically significant, no country or major payment method exceeded thresholds, and the flagged "Others" segment has insufficient volume to warrant investigation.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 93.94% | 20,363 | +0.09% ← REPORTED CHANGE |
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,512 | -0.04% |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% |
| 2026-W11 | 94.16% | 22,919 | -1.12% |
| 2026-W10 | 95.23% | 23,025 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.67% | 92.75% | -0.08% | 15,496 |  |
| CA | 98.01% | 97.72% | +0.29% | 4,867 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 93.89% | 94.75% | -0.91% | 1,685 |  |
| Apple Pay | 93.6% | 93.69% | -0.11% | 6,745 |  |
| Credit Card | 94.13% | 93.82% | +0.33% | 11,873 |  |
| Others | 98.33% | 94.44% | +4.12% | 60 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 18,142 | 15,496 | -14.6% | Stable |
| CA | High (>92%) | 5,227 | 4,867 | -6.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
