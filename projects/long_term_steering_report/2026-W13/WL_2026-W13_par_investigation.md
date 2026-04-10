# PAR Investigation: WL 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 91.3% → 91.05% (-0.27%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** PAR declined by -0.27 percentage points (pp) from 91.3% to 91.05% in 2026-W13, representing a continued downward trend from the recent peak of 91.58% in W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 3 consecutive weeks of decline (W12-W14) | -0.27 pp | ⚠️ |
| L1: Country | No country exceeds ±2.5% threshold | Max: +0.88 pp (CK) | ✅ |
| L1: PaymentMethod | Credit Card slight decline, Others anomaly | -0.32 pp / +12.46 pp | ⚠️ |
| L1: PaymentProvider | Unknown provider severe drop | -24.66 pp | ⚠️ |

**Key Findings:**
- **PaymentProvider "Unknown" dropped sharply by -24.66 pp** (from 97.33% to 73.33%), though volume is minimal at only 15 orders
- **Credit Card payments declined by -0.32 pp** (90.99% from 91.29%), impacting the largest volume segment at 120,798 orders
- **Braintree, the highest-volume provider (111,236 orders), declined by -0.33 pp** (from 92.15% to 91.85%), contributing significantly to overall PAR drop
- **PaymentMethod "Others" shows anomalous +12.46 pp increase** (87.92% to 98.87%) on very low volume (796 orders), suggesting data quality consideration
- **All countries performing within normal thresholds** with no individual country exceeding ±2.5% change

**Action:** **Monitor** - The -0.27 pp decline is modest and within normal fluctuation ranges. However, investigate the Braintree and Credit Card performance as they represent the largest volume contributors. The "Unknown" PaymentProvider anomaly should be reviewed for data quality but is not material given the 15-order volume.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% ← REPORTED CHANGE |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,964 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | +0.04% |
| 2026-W08 | 89.88% | 179,647 | -0.50% |
| 2026-W07 | 90.33% | 186,442 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.61% | 87.76% | -0.17% | 10,365 |  |
| CG | 96.76% | 96.84% | -0.08% | 44,477 |  |
| ER | 89.92% | 89.54% | +0.43% | 73,655 |  |
| AO | 87.96% | 87.38% | +0.66% | 16,249 |  |
| CK | 94.15% | 93.33% | +0.88% | 42,197 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 90.99% | 91.29% | -0.32% | 120,798 |
| PaymentMethod | Apple Pay | 87.59% | 87.46% | +0.15% | 22,237 |
| PaymentMethod | Paypal | 95.7% | 95.42% | +0.30% | 25,836 |
| PaymentMethod | Others | 98.87% | 87.92% | +12.46% | 796 |
| PaymentProvider | Unknown | 73.33% | 97.33% | -24.66% | 15 |
| PaymentProvider | Braintree | 91.85% | 92.15% | -0.33% | 111,236 |
| PaymentProvider | No Payment | 100.0% | 99.8% | +0.20% | 747 |
| PaymentProvider | Adyen | 94.33% | 93.76% | +0.61% | 39,337 |
| PaymentProvider | ProcessOut | 81.11% | 80.58% | +0.66% | 18,332 |

---

*Report: 2026-04-10*
