# AR Overall Investigation: HF-INTL 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

## Executive Summary

**Overall:** AR Overall performance declined from 94.16% to 93.64% (-0.52pp) in W14, continuing a 4-week downward trend from the peak of 94.9% in W11, with volume also decreasing to 784,389 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 4 consecutive weeks of decline | -0.55% | ⚠️ |
| L1 Country | DK -2.78pp, AT -2.50pp exceed threshold | -2.78pp max | ⚠️ |
| L1 PaymentMethod | Apple Pay lowest at 87.52% | -0.85pp | ⚠️ |
| L1 PaymentProvider | ProcessOut lowest at 91.13% | -0.83pp | ⚠️ |

**Key Findings:**
- Denmark (DK) experienced the largest country decline at -2.78pp (96.72% → 94.03%), exceeding the ±2.5% threshold with 30,036 orders affected
- Austria (AT) declined -2.50pp (95.19% → 92.81%), also at threshold level
- Apple Pay continues to underperform at 87.52% rate, representing 105,676 orders with the lowest acceptance among payment methods
- ProcessOut shows the weakest provider performance at 91.13% (-0.83pp), handling 226,595 orders
- Switzerland (CH) improved +2.98pp but on very low volume (2,174 orders), flagged as anomaly

**Action:** **Investigate** – Focus investigation on Denmark's -2.78pp decline and ProcessOut provider performance, particularly for Apple Pay transactions which show consistently low acceptance rates.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.64% | 784,389 | -0.55% ← REPORTED CHANGE |
| 2026-W13 | 94.16% | 842,480 | -0.47% |
| 2026-W12 | 94.6% | 877,187 | -0.32% |
| 2026-W11 | 94.9% | 897,106 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | -0.78% |
| 2026-W07 | 94.29% | 920,370 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DK | 94.03% | 96.72% | -2.78% | 30,036 | ⚠️ |
| AT | 92.81% | 95.19% | -2.50% | 12,458 |  |
| NO | 90.27% | 92.35% | -2.24% | 13,551 |  |
| BE | 94.01% | 95.31% | -1.37% | 74,093 |  |
| DE | 96.44% | 97.22% | -0.80% | 205,169 |  |
| FR | 92.95% | 93.7% | -0.80% | 158,170 |  |
| CH | 93.93% | 91.21% | +2.98% | 2,174 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DK, CH

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 87.52% | 88.27% | -0.85% | 105,676 |
| PaymentMethod | Credit Card | 91.6% | 92.31% | -0.77% | 354,933 |
| PaymentMethod | Paypal | 97.23% | 97.66% | -0.44% | 193,296 |
| PaymentMethod | Others | 98.85% | 97.61% | +1.27% | 130,484 |
| PaymentProvider | ProcessOut | 91.13% | 91.89% | -0.83% | 226,595 |
| PaymentProvider | Braintree | 94.19% | 94.69% | -0.53% | 292,920 |
| PaymentProvider | Adyen | 95.21% | 95.59% | -0.40% | 258,061 |
| PaymentProvider | No Payment | 100.0% | 99.94% | +0.06% | 4,352 |
| PaymentProvider | Unknown | 84.32% | 82.07% | +2.74% | 2,461 |

---

*Report: 2026-04-09*
