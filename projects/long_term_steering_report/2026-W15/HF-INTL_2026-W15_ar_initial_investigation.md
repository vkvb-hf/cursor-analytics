# AR Initial (LL0) Investigation: HF-INTL 2026-W15

**Metric:** AR Initial (LL0)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.86% → 91.77% (+2.13%)  
**Volume:** 27,526 orders

## Executive Summary

**Overall:** AR Initial (LL0) for HF-INTL improved significantly from 89.86% to 91.77% (+2.13pp) in 2026-W15, recovering to levels last seen in W11-W12 after a multi-week decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate increased +2.13pp with declining volume (27,526 vs 30,893) | +2.13pp | ✅ |
| L1: Country Mix | 6 of 7 countries exceed ±2.5% threshold; mixed performance | Varied | ⚠️ |
| L1: Payment Method | All methods stable or improving; Credit Card +3.06pp | +0.83pp to +3.06pp | ✅ |
| L1: Payment Provider | ProcessOut +3.08pp, Braintree +2.34pp driving gains | +0.19pp to +3.08pp | ✅ |

**Key Findings:**
- DE showed the strongest recovery at +6.05pp (81.58% → 86.51%), contributing significantly to overall improvement with 11,038 orders (highest volume)
- SE and GB declined against the trend: SE dropped -6.63pp (87.74% → 81.92%) and GB fell -3.12pp (80.07% → 77.57%), with GB representing the largest volume at 10,285 orders
- ProcessOut (+3.08pp) and Braintree (+2.34pp) payment providers drove the improvement, together handling 23,093 orders (84% of volume)
- Volume continues declining trend: down 10.9% WoW (30,893 → 27,526) and down 40% since W10 peak (47,660)
- DK (+8.77pp) and AT (+10.34pp) showed dramatic improvements though at lower volumes (1,609 and 1,019 orders respectively)

**Action:** Investigate – While overall metric improved, GB's continued decline (-3.12pp) requires investigation given its high volume (37% of total). Also monitor SE's sharp -6.63pp drop and the persistent volume decline trend.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.77% | 27,526 | +2.13% ← REPORTED CHANGE |
| 2026-W14 | 89.86% | 30,893 | -0.43% |
| 2026-W13 | 90.25% | 34,621 | -1.03% |
| 2026-W12 | 91.19% | 39,244 | -0.44% |
| 2026-W11 | 91.59% | 42,865 | +1.28% |
| 2026-W10 | 90.43% | 47,660 | +2.64% |
| 2026-W09 | 88.1% | 46,653 | -2.35% |
| 2026-W08 | 90.22% | 46,385 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| SE | 81.92% | 87.74% | -6.63% | 1,549 | ⚠️ |
| GB | 77.57% | 80.07% | -3.12% | 10,285 | ⚠️ |
| FR | 86.18% | 84.43% | +2.07% | 9,933 |  |
| DE | 86.51% | 81.58% | +6.05% | 11,038 | ⚠️ |
| LU | 85.71% | 79.38% | +7.98% | 77 | ⚠️ |
| DK | 89.62% | 82.39% | +8.77% | 1,609 | ⚠️ |
| AT | 88.71% | 80.4% | +10.34% | 1,019 | ⚠️ |

**Countries exceeding ±2.5% threshold:** SE, GB, DE, LU, DK, AT

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 97.28% | 97.88% | -0.62% | 4,266 |
| PaymentMethod | Paypal | 96.63% | 95.83% | +0.83% | 5,723 |
| PaymentMethod | Apple Pay | 88.2% | 85.92% | +2.66% | 7,961 |
| PaymentMethod | Credit Card | 89.38% | 86.73% | +3.06% | 9,576 |
| PaymentProvider | Unknown | 96.08% | 98.13% | -2.09% | 1,889 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 69 |
| PaymentProvider | Adyen | 97.21% | 97.02% | +0.19% | 2,475 |
| PaymentProvider | Braintree | 92.94% | 90.81% | +2.34% | 12,688 |
| PaymentProvider | ProcessOut | 88.22% | 85.58% | +3.08% | 10,405 |

---

*Report: 2026-04-14*
