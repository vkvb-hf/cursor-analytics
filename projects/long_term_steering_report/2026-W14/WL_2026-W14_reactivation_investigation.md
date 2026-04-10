# Reactivation Investigation: WL 2026-W14

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 88.71% → 88.67% (-0.05%)  
**Volume:** 7,706 orders

## Executive Summary

**Overall:** Reactivation rate showed a minimal decline of -0.05 pp (from 88.71% to 88.67%) on volume of 7,706 orders, representing normal week-over-week fluctuation within an overall positive 8-week trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline? | -0.05 pp (single week) | ✅ No pattern - rate up +3.58 pp since W07 |
| L1: Country Breakdown | Any country > ±2.5%? | AO: -3.13 pp | ⚠️ AO flagged |
| L1: Dimension Scan | Payment method anomaly? | Apple Pay: -0.70 pp | ✅ Within normal range |

**Key Findings:**
- The -0.05 pp decline is negligible and occurs within a strong upward trend (85.09% in W07 → 88.67% in W14, +3.58 pp over 8 weeks)
- AO is the only country exceeding the ±2.5% threshold with a -3.13 pp drop (87.96% → 85.21%) on significant volume of 15,776 orders
- Apple Pay shows the lowest reactivation rate at 72.06% but remained relatively stable (-0.70 pp) with low volume (698 orders)
- Credit Card (5,441 orders, 70.6% of volume) showed slight improvement at +0.13 pp
- Volume decreased by 248 orders (7,954 → 7,706) compared to prior week

**Action:** Monitor — The overall metric change is within normal variance. Continue monitoring AO performance; if the -3.13 pp decline persists for a second consecutive week, escalate for country-specific investigation.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 88.67% | 7,706 | -0.05% ← REPORTED CHANGE |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | +1.05% |
| 2026-W08 | 85.07% | 8,046 | -0.02% |
| 2026-W07 | 85.09% | 8,553 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 85.21% | 87.96% | -3.13% | 15,776 | ⚠️ |
| GN | 92.33% | 93.5% | -1.25% | 14,333 |  |
| ER | 89.23% | 89.92% | -0.77% | 67,730 |  |
| CK | 93.82% | 94.15% | -0.35% | 42,176 |  |
| KN | 88.21% | 87.61% | +0.68% | 11,048 |  |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 72.06% | 72.57% | -0.70% | 698 |
| PaymentMethod | Others | 100.0% | 100.0% | +0.00% | 3 |
| PaymentMethod | Credit Card | 89.58% | 89.46% | +0.13% | 5,441 |
| PaymentMethod | Paypal | 92.9% | 92.37% | +0.58% | 1,564 |

---

*Report: 2026-04-10*
