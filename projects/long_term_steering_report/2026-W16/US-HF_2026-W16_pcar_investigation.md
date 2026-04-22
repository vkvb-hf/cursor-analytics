# PCAR Investigation: US-HF 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 93.02% → 92.75% (-0.29%)  
**Volume:** 18,142 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for US-HF declined by -0.29% (from 93.02% to 92.75%) in 2026-W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.57%-94.58%) | -0.29% | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | -0.29% | ✅ |
| L1: PaymentMethod Scan | No methods flagged; Others -2.34% but low volume (54) | N/A | ✅ |
| L1: PaymentProvider Scan | No data available | N/A | ✅ |
| Mix Shift Analysis | US High AR tier stable, volume +2.7% | N/A | ✅ |

**Key Findings:**
- The -0.29% decline is within normal weekly fluctuation range observed over the 8-week period (92.57% to 94.58%)
- Volume increased by 2.7% week-over-week (17,669 → 18,142 orders), indicating healthy transaction growth
- No payment methods exceeded the ±2.5% threshold; "Others" showed -2.34% decline but represents only 54 orders (0.3% of volume)
- Credit Card (55% of volume) declined -0.51% while Apple Pay (36% of volume) improved +0.29%, largely offsetting each other
- No countries or segments were flagged for deep-dive investigation

**Action:** Monitor — The decline is not statistically significant, falls within normal variance, and no dimensional breakdowns reveal concerning patterns. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.75% | 18,142 | -0.29% ← REPORTED CHANGE |
| 2026-W15 | 93.02% | 17,669 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | -0.09% |
| 2026-W11 | 93.0% | 16,952 | -1.67% |
| 2026-W10 | 94.58% | 17,681 | +1.54% |
| 2026-W09 | 93.15% | 21,474 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.75% | 93.02% | -0.29% | 18,142 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 94.44% | 96.7% | -2.34% | 54 |  |
| Paypal | 94.27% | 95.39% | -1.18% | 1,483 |  |
| Credit Card | 92.45% | 92.92% | -0.51% | 10,008 |  |
| Apple Pay | 92.85% | 92.58% | +0.29% | 6,597 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 17,669 | 18,142 | +2.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
