# PCAR Investigation: US-HF 2026-W18

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 92.67% → 91.13% (-1.66%)  
**Volume:** 16,396 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined significantly from 92.67% to 91.13% (-1.54 pp) in US-HF during 2026-W18, representing the largest week-over-week drop in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -1.87 pp from W11 peak | ⚠️ |
| L1: Country Breakdown | US threshold check (±2.5%) | -1.66% | ✅ |
| L1: PaymentMethod | Credit Card threshold check | -2.40% | ⚠️ |
| L1: PaymentProvider | Data availability | No data | ⚠️ |
| Mix Shift | Volume tier stability | +5.8% volume, High tier | ✅ |

**Key Findings:**
- Credit Card payment method showed the steepest decline at -2.40%, affecting 9,210 orders (56% of total volume)
- PayPal also declined by -1.90% across 1,338 orders, suggesting a broader payment processing issue
- Apple Pay remained relatively stable at -0.45%, indicating the issue may be isolated to traditional card-based processors
- The 8-week trend shows a consistent downward pattern from 93.0% (W11) to 91.13% (W18), a cumulative loss of 1.87 pp
- Volume increased 5.8% WoW to 16,396 orders, ruling out low-volume anomaly

**Action:** **Investigate** – The Credit Card payment method decline approaching the 2.5% threshold warrants immediate investigation into card processor performance, decline codes, and any recent integration changes.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 91.13% | 16,396 | -1.66% ← REPORTED CHANGE |
| 2026-W17 | 92.67% | 15,496 | -0.09% |
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,669 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | -0.09% |
| 2026-W11 | 93.0% | 16,952 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 91.13% | 92.67% | -1.66% | 16,396 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 90.58% | 92.8% | -2.40% | 9,210 |  |
| Paypal | 91.33% | 93.09% | -1.90% | 1,338 |  |
| Apple Pay | 91.89% | 92.3% | -0.45% | 5,793 |  |
| Others | 100.0% | 98.33% | +1.69% | 55 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 15,496 | 16,396 | +5.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
