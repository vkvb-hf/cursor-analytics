# Reactivation Investigation: HF-NA 2026-W20

**Metric:** Reactivation Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 90.66% → 90.24% (-0.46%)  
**Volume:** 18,775 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation rate declined modestly from 90.66% to 90.24% (-0.42 pp) in W20, remaining within normal fluctuation range and statistically not significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate stable between 89.41%-90.95% | -0.42 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US: -0.59%, CA: +0.06% | ✅ |
| L1: Payment Method | Minor shifts across all methods | PayPal: -0.87%, Credit Card: -0.46% | ✅ |
| Mix Shift Analysis | Both countries stable despite volume decline | US: -15.2% vol, CA: -12.8% vol | ✅ |

**Key Findings:**
- The -0.42 pp decline is within the 8-week range (89.41%-90.95%) and marked as not statistically significant
- US drove the majority of the decline (-0.59 pp) on 78.8% of total volume (14,787 orders)
- Overall order volume decreased significantly from 22,007 to 18,775 (-14.7%), but this did not materially impact rates
- PayPal showed the largest payment method decline (-0.87 pp) but represents only 14.6% of volume
- No dimension flags were triggered across any L1 breakdown

**Action:** Monitor — Continue standard weekly monitoring. No investigation required as the change is not statistically significant and all metrics remain within normal operating ranges.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 90.24% | 18,775 | -0.46% ← REPORTED CHANGE |
| 2026-W19 | 90.66% | 22,007 | +0.20% |
| 2026-W18 | 90.48% | 19,213 | +0.14% |
| 2026-W17 | 90.35% | 20,799 | +1.05% |
| 2026-W16 | 89.41% | 23,973 | -0.92% |
| 2026-W15 | 90.24% | 26,178 | -0.78% |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.20% | 90.74% | -0.59% | 14,787 |  |
| CA | 90.40% | 90.34% | +0.06% | 3,988 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 60.0% | 0.0% | +nan% | 5 |  |
| Paypal | 92.78% | 93.59% | -0.87% | 2,741 |  |
| Credit Card | 90.33% | 90.75% | -0.46% | 13,122 |  |
| Apple Pay | 87.51% | 87.27% | +0.28% | 2,907 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 17,431 | 14,787 | -15.2% | Stable |
| CA | Medium (>85%) | 4,576 | 3,988 | -12.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
