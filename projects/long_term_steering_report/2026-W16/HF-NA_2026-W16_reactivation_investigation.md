# Reactivation Investigation: HF-NA 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.24% → 89.41% (-0.92%)  
**Volume:** 23,973 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined by -0.83pp (90.24% → 89.41%) in W16, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal fluctuation range (86.89%-91.02%) | -0.83pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US: -0.13pp, CA: +0.09pp | ✅ |
| L1: PaymentMethod | Credit Card showed largest decline | -1.60pp | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift Analysis | Volume stable across tiers | US: +3.7%, CA: +1.3% | ✅ |

**Key Findings:**
- The -0.83pp decline is within the 8-week range (86.89%-91.02%) and follows a similar -0.78pp decline in W15
- Credit Card payment method showed the largest decline at -1.60pp (90.17% → 88.73%) with significant volume (16,661 orders)
- Both US and CA remained in high-performing tier (>92%) with stable volume growth
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation
- "Others" payment method flagged (⚠️) but represents only 2 orders, making it statistically irrelevant

**Action:** Monitor – Continue tracking Credit Card payment method performance over the next 1-2 weeks to determine if the -1.60pp decline represents a trend or normal fluctuation.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.41% | 23,973 | -0.92% ← REPORTED CHANGE |
| 2026-W15 | 90.24% | 26,178 | -0.78% |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | +1.54% |
| 2026-W09 | 86.89% | 23,884 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.97% | 93.09% | -0.13% | 511,272 |  |
| CA | 93.58% | 93.49% | +0.09% | 104,640 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.73% | 90.17% | -1.60% | 16,661 |  |
| Paypal | 92.99% | 92.78% | +0.23% | 3,767 |  |
| Apple Pay | 88.85% | 87.98% | +0.99% | 3,543 |  |
| Others | 50.0% | 28.57% | +75.00% | 2 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,811 | 511,272 | +3.7% | Stable |
| CA | High (>92%) | 103,253 | 104,640 | +1.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
