# PCAR Investigation: HF-NA 2026-W20

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 91.02% → 90.68% (-0.37%)  
**Volume:** 19,628 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined by -0.34pp (91.02% → 90.68%) on 19,628 orders in W20, continuing a 4-week downward trend from the W17 peak of 93.94%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Sustained decline since W17 | -3.26pp over 4 weeks | ⚠️ |
| Country Threshold (±2.5%) | No countries exceeded | US: -0.51%, CA: +0.25% | ✅ |
| Payment Method Threshold | Others flagged (+16.37%) | Low volume (40 orders) | ✅ |
| Volume Shift | Both countries declining | US: -4.8%, CA: -7.3% | ⚠️ |
| Statistical Significance | Not significant | - | ✅ |

**Key Findings:**
- PCAR has declined for 4 consecutive weeks, dropping from 93.94% (W17) to 90.68% (W20), a cumulative loss of -3.26pp
- US drives the majority of volume (15,543 orders, 79% of total) and declined -0.51pp to 89.15%
- Credit Card (90.0%, -0.63pp) and PayPal (91.46%, -0.67pp) showed the largest declines among high-volume payment methods
- Total order volume declined -5.3% WoW (20,734 → 19,628), with CA seeing a steeper -7.3% volume drop
- The "Others" payment method flag (+16.37%) is not actionable due to minimal volume (40 orders)

**Action:** Monitor — While the week-over-week change is not statistically significant, the sustained 4-week declining trend warrants continued observation. If PCAR drops below 90% or the trend continues through W21, escalate for deeper investigation into Credit Card and PayPal decline drivers in US.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 90.68% | 19,628 | -0.37% ← REPORTED CHANGE |
| 2026-W19 | 91.02% | 20,734 | -1.55% |
| 2026-W18 | 92.45% | 21,206 | -1.59% |
| 2026-W17 | 93.94% | 20,363 | +0.09% |
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,513 | -0.04% |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,788 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.15% | 89.61% | -0.51% | 15,543 |  |
| CA | 96.50% | 96.26% | +0.25% | 4,085 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 91.46% | 92.08% | -0.67% | 1,757 |  |
| Credit Card | 90.0% | 90.56% | -0.63% | 11,267 |  |
| Apple Pay | 91.59% | 91.6% | -0.01% | 6,564 |  |
| Others | 97.5% | 83.78% | +16.37% | 40 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 16,327 | 15,543 | -4.8% | Stable |
| CA | High (>92%) | 4,407 | 4,085 | -7.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
