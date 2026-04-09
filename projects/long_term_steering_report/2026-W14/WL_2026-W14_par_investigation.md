# PAR Investigation: WL 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.3% → 91.05% (-0.27%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** PAR declined by 0.27pp (91.3% → 91.05%) in W14, continuing a three-week downward trend from the W11 peak of 91.58%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 3-week consecutive decline (W12-W14) | -0.27pp | ⚠️ |
| L1: Country | AO exceeded ±2.5% threshold | -3.13pp | ⚠️ |
| L1: Payment Method | All methods declined, Apple Pay largest | -0.60pp | ✅ |
| L1: Payment Provider | Adyen showed notable decline | -0.87pp | ⚠️ |

**Key Findings:**
- **AO (Angola) is the primary driver:** AO declined -3.13pp (87.96% → 85.21%) with 15,776 orders, the only country exceeding the ±2.5% threshold
- **Adyen underperformance:** Adyen dropped -0.87pp (94.33% → 93.51%) across 38,117 orders, the largest decline among major payment providers
- **Volume contraction:** Order volume decreased from 169,667 to 165,018 (-2.7%), continuing a downward trend from W10's peak of 179,964
- **Broad-based decline:** All countries except KN (+0.68pp) showed negative movement, suggesting a systemic rather than isolated issue
- **Apple Pay weakness:** Apple Pay had the largest payment method decline at -0.60pp (87.59% → 87.06%)

**Action:** **Investigate** — Prioritize deep-dive into AO market performance and Adyen provider issues. Cross-reference AO x Adyen combination to determine if these factors are correlated or independent contributors.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.05% | 165,018 | -0.27% ← REPORTED CHANGE |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
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
| PaymentMethod | Apple Pay | 87.06% | 87.59% | -0.60% | 21,798 |
| PaymentMethod | Credit Card | 90.79% | 90.99% | -0.23% | 117,492 |
| PaymentMethod | Others | 98.67% | 98.87% | -0.20% | 826 |
| PaymentMethod | Paypal | 95.52% | 95.7% | -0.19% | 24,902 |
| PaymentProvider | Adyen | 93.51% | 94.33% | -0.87% | 38,117 |
| PaymentProvider | ProcessOut | 81.01% | 81.11% | -0.12% | 18,108 |
| PaymentProvider | Braintree | 91.8% | 91.85% | -0.06% | 108,008 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 750 |
| PaymentProvider | Unknown | 85.71% | 73.33% | +16.88% | 35 |

---

*Report: 2026-04-09*
