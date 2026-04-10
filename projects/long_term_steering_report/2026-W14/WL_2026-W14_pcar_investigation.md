# PCAR Investigation: WL 2026-W14

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 97.07% → 97.03% (-0.04%)  
**Volume:** 11,373 orders

## Executive Summary

**Overall:** PCAR declined marginally by -0.04 percentage points (97.07% → 97.03%) on a volume of 11,373 orders in W14, representing a minor fluctuation within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stability check | -0.04 pp | ✅ Within normal variance; rate stable between 96.86%-97.37% over 8 weeks |
| L1: Country | AO threshold (±2.5%) | -3.13 pp | ⚠️ AO flagged with significant decline |
| L1: Country | Other countries | -1.25 pp to +0.68 pp | ✅ GN, ER, CK, KN within threshold |
| L1: Payment Method | Dimension scan | -0.37 pp to +0.16 pp | ✅ All payment methods within normal range |

**Key Findings:**
- AO is the only country exceeding the ±2.5% threshold with a -3.13 pp decline (87.96% → 85.21%), representing the primary driver of the overall metric decline
- Volume decreased significantly from 13,604 (W13) to 11,373 (W14), a -16.4% reduction in order volume
- The 8-week trend shows overall recovery from a low of 94.85% in W07 to current 97.03%, indicating positive longer-term trajectory
- Payment methods show minimal variance: Apple Pay declined slightly (-0.37 pp) while Paypal improved (+0.16 pp)
- GN showed the second-largest country decline at -1.25 pp (93.5% → 92.33%) but remains within acceptable thresholds

**Action:** Investigate - Focus investigation on AO to identify root cause of -3.13 pp decline; monitor GN for potential emerging issues

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.03% | 11,373 | -0.04% ← REPORTED CHANGE |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | +0.50% |
| 2026-W08 | 96.86% | 16,585 | +2.12% |
| 2026-W07 | 94.85% | 16,452 | - |

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
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Apple Pay | 96.65% | 97.0% | -0.37% | 3,461 |
| PaymentMethod | Others | 100.0% | 100.0% | +0.00% | 3 |
| PaymentMethod | Credit Card | 97.0% | 96.91% | +0.09% | 6,574 |
| PaymentMethod | Paypal | 98.13% | 97.97% | +0.16% | 1,335 |

---

*Report: 2026-04-10*
