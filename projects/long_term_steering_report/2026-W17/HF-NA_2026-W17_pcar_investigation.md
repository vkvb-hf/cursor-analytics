# PCAR Investigation: HF-NA 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 93.86% → 93.94% (+0.09%)  
**Volume:** 20,363 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate showed a marginal improvement from 93.86% to 93.94% (+0.09pp) in W17, a statistically non-significant change on 20,363 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Overall Rate Change | Within normal range (+0.09pp) | +0.09pp | ✅ |
| Country Threshold (±2.5pp) | No countries exceeded threshold | US: -0.08pp, CA: +0.29pp | ✅ |
| Payment Method Threshold | "Others" exceeded threshold (+4.12pp) | Low volume (60 orders) | ⚠️ |
| Volume Trend | W17 volume decreased vs W16 | -12.9% (20,363 vs 23,369) | ⚠️ |
| 8-Week Trend | Rate below W10 peak (95.23%) | -1.29pp from peak | ⚠️ |

**Key Findings:**
- The +0.09pp improvement reverses the -0.23pp decline from W16, but the rate remains 1.29pp below the W10 peak of 95.23%
- US (76% of volume) showed a slight decline of -0.08pp to 92.67%, while CA improved +0.29pp to 98.01%
- "Others" payment method showed a +4.12pp increase but represents minimal volume (60 orders), making it statistically unreliable
- Credit Card (58% of volume) improved +0.33pp to 94.13%, while PayPal declined -0.91pp to 93.89%
- Overall order volume dropped 12.9% week-over-week (23,369 → 20,363), marking the lowest volume in the 8-week window

**Action:** Monitor — Continue standard tracking; no significant deviations warrant investigation. Watch for continued volume decline and whether the rate recovers toward the W10 baseline of 95.23%.

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

*Report: 2026-04-28*
