# PCAR Investigation: HF-NA 2026-W22

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 92.33% → 91.9% (-0.47%)  
**Volume:** 17,468 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 92.33% to 91.9% (-0.43 pp) in W22, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal fluctuation range (90.68%-94.08%) | -0.43 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US: -0.38 pp, CA: -0.35 pp | ✅ |
| L1: Payment Method | "Others" flagged but low volume (58 orders) | +4.31 pp | ✅ |
| Mix Shift | Both US and CA volume declined but impact stable | US: -6.6%, CA: -10.3% | ✅ |

**Key Findings:**
- The -0.43 pp decline is within normal weekly variance and follows a +1.82 pp increase in W21, indicating typical fluctuation
- Overall volume decreased by 7.5% (17,468 vs 18,883 orders), continuing a downward trend from W15 peak of 23,513
- Both US (-0.38 pp) and CA (-0.35 pp) showed minor declines, with neither exceeding the ±2.5% investigation threshold
- Apple Pay showed the largest decline among major payment methods (-0.87 pp on 5,740 orders), though still below threshold
- 8-week trend shows gradual rate erosion from 94.08% (W15) to 91.9% (W22), a cumulative decline of 2.18 pp

**Action:** Monitor — No immediate investigation required. Continue tracking the gradual downward trend in both approval rate and volume over the 8-week period.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 91.9% | 17,468 | -0.47% ← REPORTED CHANGE |
| 2026-W21 | 92.33% | 18,883 | +1.82% |
| 2026-W20 | 90.68% | 19,628 | -0.37% |
| 2026-W19 | 91.02% | 20,734 | -1.55% |
| 2026-W18 | 92.45% | 21,206 | -1.59% |
| 2026-W17 | 93.94% | 20,363 | +0.09% |
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,513 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.37% | 90.75% | -0.43% | 13,412 |  |
| CA | 96.97% | 97.32% | -0.37% | 4,056 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 91.11% | 91.98% | -0.94% | 5,740 |  |
| Paypal | 92.1% | 92.74% | -0.69% | 1,544 |  |
| Credit Card | 92.3% | 92.46% | -0.17% | 10,126 |  |
| Others | 94.83% | 90.91% | +4.31% | 58 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 14,363 | 13,412 | -6.6% | Stable |
| CA | High (>92%) | 4,520 | 4,056 | -10.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
