# AR Initial (LL0) Investigation: HF-NA 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.64% → 89.98% (+0.38%)  
**Volume:** 17,332 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Initial Charges) for HF-NA improved slightly from 89.64% to 89.98% (+0.34 pp) in 2026-W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.64 pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.34 pp | ✅ |
| 3_PostDunningAR | Post-Dunning | +0.37 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.40 pp | ✅ |

**Key Findings:**
- All funnel stages show modest improvement (+0.34 to +0.64 pp), indicating consistent performance across the payment journey
- No countries exceeded the ±2.5% threshold; US improved +0.96 pp while CA declined -0.70 pp
- Volume decreased significantly from ~25K orders (W08-W10) to 17,332 orders in W15, a ~32% reduction over the 8-week period
- Credit Card (90.21%, +0.85 pp) and ProcessOut (90.36%, +0.87 pp) showed the strongest improvements among payment dimensions
- "Others" payment method and "Unknown" provider showed notable declines (-1.69 pp and -1.92 pp respectively), though both represent low volumes (<1,000 orders)

**Action:** Monitor — The metric remains stable within normal operating range with no significant deviations requiring investigation. Continue tracking volume trends given the sustained decline over recent weeks.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.98% | 17,332 | +0.38% ← REPORTED CHANGE |
| 2026-W14 | 89.64% | 17,052 | +0.46% |
| 2026-W13 | 89.23% | 16,205 | -0.47% |
| 2026-W12 | 89.65% | 21,103 | -1.29% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 90.74% | 91.38% | -0.70% | 5,170 |  |
| US | 89.66% | 88.81% | +0.96% | 12,162 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.16% | 98.83% | -1.69% | 810 |  |
| Paypal | 89.72% | 90.17% | -0.50% | 1,410 |  |
| Apple Pay | 88.57% | 88.36% | +0.24% | 5,417 |  |
| Credit Card | 90.21% | 89.45% | +0.85% | 9,695 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 96.49% | 98.38% | -1.92% | 655 |  |
| Adyen | 92.55% | 93.12% | -0.61% | 94 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 132 |  |
| Braintree | 88.64% | 88.61% | +0.03% | 6,970 |  |
| ProcessOut | 90.36% | 89.58% | +0.87% | 9,481 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.95% | 88.38% | +0.64% | 17,332 | 17,052 |  |
| 2_PreDunningAR | 89.98% | 89.64% | +0.38% | 17,332 | 17,052 |  |
| 3_PostDunningAR | 90.16% | 89.83% | +0.37% | 17,332 | 17,052 |  |
| 6_PaymentApprovalRate | 90.43% | 90.07% | +0.40% | 17,332 | 17,052 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 11,533 | 12,162 | +5.5% | Stable |
| CA | Medium (>85%) | 5,519 | 5,170 | -6.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-17*
