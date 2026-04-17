# Reactivation Investigation: WL 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.67% → 89.29% (+0.70%)  
**Volume:** 9,277 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate improved slightly from 88.67% to 89.29% (+0.70% / +0.62pp) in W15, with volume increasing to 9,277 orders; the change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Overall Rate Change | +0.70% week-over-week | +0.62pp | ✅ |
| Statistical Significance | Not significant | N/A | ✅ |
| Country Threshold (±2.5%) | No countries exceeded | N/A | ✅ |
| Payment Method Anomalies | Others -66.67%, Apple Pay +3.99% | Low volume | ⚠️ |
| Mix Shift Impact | All segments stable | N/A | ✅ |

**Key Findings:**
- The +0.70% improvement continues a positive trend, with the rate now at its highest point (89.29%) in the 8-week window, up from 85.07% in W08
- All four countries showed improvement: AO led with +2.17%, followed by MR (+1.45%), ER (+1.23%), and GN (+1.07%) — none exceeded the ±2.5% threshold requiring investigation
- "Others" payment method showed a -66.67% decline but with only 3 orders, making it statistically irrelevant
- Apple Pay improved +3.99% (72.06% → 74.94%) on 794 orders, flagged but still performing below the overall average
- Volume increased 20.4% week-over-week (7,706 → 9,277), with mix shifts remaining stable across all country/tier segments

**Action:** Monitor — The improvement is not statistically significant, no countries exceeded investigation thresholds, and the 8-week trend shows healthy upward momentum. Continue standard monitoring.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.29% | 9,277 | +0.70% ← REPORTED CHANGE |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | +1.05% |
| 2026-W08 | 85.07% | 8,046 | - |

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
| Others | 33.33% | 100.0% | -66.67% | 3 | ⚠️ |
| Credit Card | 89.92% | 89.58% | +0.38% | 6,638 |  |
| Paypal | 93.27% | 92.9% | +0.39% | 1,842 |  |
| Apple Pay | 74.94% | 72.06% | +3.99% | 794 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

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

*Report: 2026-04-17*
