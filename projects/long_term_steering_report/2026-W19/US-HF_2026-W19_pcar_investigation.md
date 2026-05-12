# PCAR Investigation: US-HF 2026-W19

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.13% → 89.6% (-1.68%)  
**Volume:** 16,324 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined significantly from 91.13% to 89.60% (-1.53 pp) in US-HF during W19, continuing a downward trend observed over the past 3 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent decline since W17 | -3.32 pp from W12 baseline | ⚠️ |
| L1: Country Breakdown | US only market, no threshold breach | -1.68% | ✅ |
| L1: PaymentMethod | "Others" flagged with -16.22% change | Low volume (37 orders) | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | US remains in Medium AR tier | -0.4% volume, Stable | ✅ |

**Key Findings:**
- US-HF shows a sustained 3-week declining trend: W17 (92.67%) → W18 (91.13%) → W19 (89.60%), representing a cumulative -3.07 pp drop
- Credit Card payments experienced the largest volume impact with -1.79% change across 9,312 orders (57% of total volume)
- "Others" payment method showed a dramatic -16.22% decline, though volume is negligible (37 orders)
- Apple Pay declined -1.68% across 5,611 orders, mirroring the overall rate decline
- PayPal remained relatively stable at -0.14%, suggesting the issue may be concentrated in card-based payment processing

**Action:** **Investigate** — The sustained 3-week decline pattern and broad impact across Credit Card and Apple Pay methods warrants deeper investigation into payment processor performance and potential issuer-side rejection patterns.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 89.6% | 16,324 | -1.68% ← REPORTED CHANGE |
| 2026-W18 | 91.13% | 16,396 | -1.66% |
| 2026-W17 | 92.67% | 15,496 | -0.09% |
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,669 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.60% | 91.13% | -1.68% | 16,324 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 83.78% | 100.0% | -16.22% | 37 | ⚠️ |
| Credit Card | 88.95% | 90.58% | -1.79% | 9,312 |  |
| Apple Pay | 90.34% | 91.89% | -1.68% | 5,611 |  |
| Paypal | 91.2% | 91.33% | -0.14% | 1,364 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 16,396 | 16,324 | -0.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
