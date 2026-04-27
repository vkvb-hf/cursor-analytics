# PCAR Investigation: US-HF 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.75% → 92.67% (-0.09%)  
**Volume:** 15,496 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined slightly from 92.75% to 92.67% (-0.08 pp) in US-HF during 2026-W17, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.57%-94.58%) | -0.08 pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | -0.08 pp | ✅ |
| L1: PaymentMethod | "Others" flagged but minimal volume (60 orders) | +4.12 pp | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | High AR tier volume decreased but impact stable | -14.6% vol | ✅ |

**Key Findings:**
- The -0.08 pp decline is within normal weekly fluctuation observed over the 8-week period (range: 92.57% to 94.58%)
- PayPal showed the largest decline among major payment methods at -1.24 pp (1,202 orders), while Credit Card improved +0.38 pp (8,776 orders)
- "Others" payment method flagged with +4.12 pp change, but volume is negligible (60 orders) and not material to overall rate
- Order volume decreased 14.6% week-over-week (18,142 → 15,496), but mix shift impact remains stable
- No systemic issues identified across any dimension at threshold levels

**Action:** Monitor — No investigation required. The decline is not statistically significant and falls within normal operating variance. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.67% | 15,496 | -0.09% ← REPORTED CHANGE |
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,669 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | -0.09% |
| 2026-W11 | 93.0% | 16,952 | -1.67% |
| 2026-W10 | 94.58% | 17,681 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.67% | 92.75% | -0.08% | 15,496 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 93.09% | 94.27% | -1.24% | 1,202 |  |
| Apple Pay | 92.3% | 92.85% | -0.58% | 5,458 |  |
| Credit Card | 92.8% | 92.45% | +0.38% | 8,776 |  |
| Others | 98.33% | 94.44% | +4.12% | 60 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 18,142 | 15,496 | -14.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
