# Reactivation Investigation: HF-NA 2026-W18

**Metric:** Reactivation Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 90.35% → 90.48% (+0.14%)  
**Volume:** 19,213 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** HF-NA Reactivation Rate improved marginally from 90.35% to 90.48% (+0.14pp) in W18, a statistically non-significant change on 19,213 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (89.41%-91.02%) | +0.14pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | CA: -2.11pp, US: +1.04pp | ✅ |
| L1: PaymentMethod | "Others" flagged but negligible volume (3 orders) | -100.00% | ✅ |
| L1: PaymentProvider | No anomalies detected | - | ✅ |
| Mix Shift | Both segments stable despite volume decline | US: -9.5%, CA: -2.7% | ✅ |

**Key Findings:**
- The +0.14pp increase is within normal weekly fluctuation (8-week range: 89.41% to 91.02%) and not statistically significant
- CA declined -2.11pp (92.02% → 90.07%) but remains below the ±2.5% investigation threshold
- US improved +1.04pp (89.71% → 90.64%), offsetting CA's decline due to higher volume (13,634 vs 5,579 orders)
- Overall order volume decreased -7.6% WoW (20,799 → 19,213) but had no material impact on rate stability
- PaymentMethod "Others" shows -100% change but is statistically irrelevant (only 3 orders)

**Action:** Monitor — No investigation required. The change is not significant, no dimensions exceeded thresholds, and the metric remains stable within historical norms.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 90.48% | 19,213 | +0.14% ← REPORTED CHANGE |
| 2026-W17 | 90.35% | 20,799 | +1.05% |
| 2026-W16 | 89.41% | 23,973 | -0.92% |
| 2026-W15 | 90.24% | 26,178 | -0.78% |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 90.07% | 92.02% | -2.11% | 5,579 |  |
| US | 90.64% | 89.71% | +1.04% | 13,634 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 0.0% | 33.33% | -100.00% | 3 | ⚠️ |
| Apple Pay | 88.75% | 88.93% | -0.21% | 2,808 |  |
| Credit Card | 90.21% | 90.2% | +0.01% | 13,436 |  |
| Paypal | 93.43% | 92.31% | +1.21% | 2,966 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 15,063 | 13,634 | -9.5% | Stable |
| CA | High (>92%) | 5,736 | 5,579 | -2.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
