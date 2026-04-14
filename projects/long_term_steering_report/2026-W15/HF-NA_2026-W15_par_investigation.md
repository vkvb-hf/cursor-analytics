# PAR Investigation: HF-NA 2026-W15

**Metric:** PAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 94.0% → 94.11% (+0.12%)  
**Volume:** 497,775 orders

## Executive Summary

**Overall:** PAR improved by +0.12 percentage points (94.0% → 94.11%) on a volume of 497,775 orders, continuing a positive 8-week upward trend from 93.27% in W08 to 94.11% in W15.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent improvement over 8 weeks (+0.84 pp total) | +0.12 pp | ✅ |
| L1: Country | No country exceeded ±2.5% threshold | US +0.34 pp, CA +0.02 pp | ✅ |
| L1: PaymentMethod | "Others" declined but low volume | -0.75 pp (4,413 orders) | ✅ |
| L1: PaymentProvider | "Unknown" provider significant drop | -4.06 pp (776 orders) | ⚠️ |

**Key Findings:**
- US drove the majority of improvement with +0.34 pp on 492,811 orders, representing the largest volume segment
- PaymentProvider "Unknown" showed a significant decline of -4.06 pp (96.17% → 92.27%), though volume is minimal at 776 orders
- Braintree, the dominant payment provider (385,044 orders), improved slightly by +0.14 pp
- Apple Pay remains the lowest-performing payment method at 88.76%, though it improved +0.25 pp
- Volume has steadily decreased over 8 weeks (548,921 → 497,775), down ~9.3% while rate improved

**Action:** Monitor — The +0.12 pp improvement continues a healthy 8-week trend. The "Unknown" PaymentProvider decline warrants watching but has negligible volume impact. No escalation required.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.11% | 497,775 | +0.12% ← REPORTED CHANGE |
| 2026-W14 | 94.0% | 507,189 | +0.04% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | -0.04% |
| 2026-W11 | 93.91% | 539,763 | +0.29% |
| 2026-W10 | 93.64% | 554,777 | +0.30% |
| 2026-W09 | 93.36% | 553,112 | +0.10% |
| 2026-W08 | 93.27% | 548,921 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.52% | 93.5% | +0.02% | 103,253 |  |
| US | 93.1% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.53% | 99.27% | -0.75% | 4,413 |
| PaymentMethod | Credit Card | 94.65% | 94.57% | +0.08% | 366,508 |
| PaymentMethod | Paypal | 96.33% | 96.19% | +0.15% | 60,610 |
| PaymentMethod | Apple Pay | 88.76% | 88.54% | +0.25% | 66,244 |
| PaymentProvider | Unknown | 92.27% | 96.17% | -4.06% | 776 |
| PaymentProvider | Adyen | 95.76% | 95.86% | -0.10% | 24,575 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 3,578 |
| PaymentProvider | Braintree | 94.32% | 94.19% | +0.14% | 385,044 |
| PaymentProvider | ProcessOut | 92.38% | 92.24% | +0.15% | 83,802 |

---

*Report: 2026-04-14*
