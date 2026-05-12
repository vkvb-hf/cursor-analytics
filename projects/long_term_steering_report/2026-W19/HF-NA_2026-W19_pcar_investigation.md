# PCAR Investigation: HF-NA 2026-W19

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 92.45% → 91.02% (-1.55%)  
**Volume:** 20,728 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 92.45% to 91.02% (-1.43pp) in W19, continuing a two-week downward trend that has brought the rate below the 8-week baseline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consecutive declines W18-W19 | -1.55% WoW | ⚠️ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US -1.68%, CA -0.71% | ✅ |
| L1: PaymentMethod | "Others" segment flagged | -16.22% | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | CA volume declined 8.4% | Minor impact | ✅ |

**Key Findings:**
- The rate has declined for two consecutive weeks (W18: -1.59%, W19: -1.55%), dropping from 94.19% in W12 to 91.02% in W19
- US drives the majority of volume (16,324 of 20,728 orders, 79%) and experienced a -1.68% decline to 89.60%
- Credit Card payment method showed the largest absolute impact with -1.70% change on 12,140 orders
- "Others" payment method flagged with -16.22% change, but minimal volume (37 orders)
- CA high-approval volume decreased by 8.4% (4,809 → 4,404), reducing the positive mix contribution

**Action:** **Monitor** – No single country or dimension exceeded investigation thresholds, but the consecutive weekly declines warrant close observation. If the downward trend continues in W20, escalate for deeper PaymentMethod analysis focusing on Credit Card and Apple Pay performance.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 91.02% | 20,728 | -1.55% ← REPORTED CHANGE |
| 2026-W18 | 92.45% | 21,205 | -1.59% |
| 2026-W17 | 93.94% | 20,363 | +0.09% |
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,512 | -0.04% |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.60% | 91.13% | -1.68% | 16,324 |  |
| CA | 96.28% | 96.96% | -0.71% | 4,404 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 83.78% | 100.0% | -16.22% | 37 | ⚠️ |
| Credit Card | 90.57% | 92.14% | -1.70% | 12,140 |  |
| Apple Pay | 91.6% | 92.95% | -1.46% | 6,784 |  |
| Paypal | 92.08% | 92.41% | -0.36% | 1,767 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 16,396 | 16,324 | -0.4% | Stable |
| CA | High (>92%) | 4,809 | 4,404 | -8.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
