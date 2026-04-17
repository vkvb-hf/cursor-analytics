# PAR Investigation: RTE 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 94.75% → 94.87% (+0.13%)  
**Volume:** 421,406 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate increased slightly from 94.75% to 94.87% (+0.13%) in W15, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable pattern, recovery from W10 low | +0.13% | ✅ |
| L1: Country Breakdown | 1 country (TK) exceeds ±2.5% threshold | +7.54% TK | ⚠️ |
| L1: Dimension Scan | Unknown provider shows -10.44% but tiny volume (131) | Minor | ✅ |
| L2: TK Deep-Dive | All payment methods improved significantly | +6.5% to +12.1% | ⚠️ |
| L3: Related Metrics | All funnel stages stable | +0.47% to -0.01% | ✅ |
| Mix Shift | No significant volume shifts impacting overall rate | Stable | ✅ |

**Key Findings:**
- TK showed exceptional improvement (+7.54%), driven by a 5.81pp reduction in "Insufficient Funds" declines (from 8.32% to 2.51%)
- TK improvements were broad-based: applepay +12.10%, credit_card +6.49%, paypal +5.41%
- Both TK payment providers improved: Braintree +10.60%, Adyen +6.49%
- Overall trend shows recovery from W10 trough (93.42%) toward W12 peak (95.18%)
- Unknown provider decline (-10.44%) is immaterial due to minimal volume (131 orders)

**Action:** Monitor - The +0.13% change is not statistically significant. TK improvement is positive but represents only 0.5% of total volume (1,950 orders). Continue standard monitoring.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.87% | 421,406 | +0.13% ← REPORTED CHANGE |
| 2026-W14 | 94.75% | 431,853 | -0.20% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | +0.20% |
| 2026-W08 | 93.07% | 462,049 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.14% | 93.41% | -1.37% | 1,895 |  |
| YE | 87.77% | 88.15% | -0.43% | 42,126 |  |
| FJ | 93.97% | 93.62% | +0.38% | 388,956 |  |
| CF | 94.14% | 93.47% | +0.72% | 51,881 |  |
| TZ | 91.69% | 90.11% | +1.76% | 2,660 |  |
| TO | 86.67% | 84.89% | +2.11% | 3,204 |  |
| TK | 95.33% | 88.65% | +7.54% | 1,950 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.26% | 99.05% | -0.80% | 5,340 |  |
| Paypal | 97.72% | 97.71% | +0.01% | 53,618 |  |
| Credit Card | 94.73% | 94.58% | +0.16% | 308,898 |  |
| Apple Pay | 92.51% | 92.35% | +0.17% | 53,550 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 70.99% | 79.27% | -10.44% | 131 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 510 |  |
| ProcessOut | 93.45% | 93.43% | +0.02% | 64,367 |  |
| Braintree | 95.66% | 95.51% | +0.15% | 282,047 |  |
| Adyen | 93.13% | 92.88% | +0.27% | 74,351 |  |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 10 | 7 |  |
| paypal | 97.46% | 92.45% | +5.41% | 118 | 106 | ⚠️ |
| credit_card | 95.81% | 89.97% | +6.49% | 1,359 | 1,256 | ⚠️ |
| applepay | 93.51% | 83.41% | +12.10% | 462 | 410 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 10 | 7 |  |
| Adyen | 95.81% | 89.97% | +6.49% | 1,359 | 1,256 | ⚠️ |
| Braintree | 94.31% | 85.27% | +10.60% | 580 | 516 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,859 | 1,577 | 95.33% | 88.65% | +6.69 |
| Insufficient Funds | 49 | 148 | 2.51% | 8.32% | -5.81 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 21 | 32 | 1.08% | 1.80% | -0.72 |
| Other reasons | 20 | 22 | 1.03% | 1.24% | -0.21 |
| Unknown | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** paypal + Adyen + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.25% | 90.82% | +0.47% | 421,406 | 431,853 |  |
| 2_PreDunningAR | 92.83% | 92.46% | +0.41% | 421,406 | 431,853 |  |
| 3_PostDunningAR | 94.21% | 94.22% | -0.01% | 421,406 | 431,853 |  |
| 6_PaymentApprovalRate | 94.87% | 94.75% | +0.12% | 421,406 | 431,853 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 397,332 | 388,956 | -2.1% | Stable |
| CF | High (>92%) | 52,140 | 51,881 | -0.5% | Stable |
| YE | Medium (>85%) | 45,214 | 42,126 | -6.8% | Stable |
| TT | High (>92%) | 4,924 | 4,617 | -6.2% | Stable |
| TO | Low (>85%) | 3,480 | 3,204 | -7.9% | Stable |
| TZ | Medium (>85%) | 3,013 | 2,660 | -11.7% | Stable |
| TV | High (>92%) | 2,065 | 1,895 | -8.2% | Stable |
| TK | Medium (>85%) | 1,779 | 1,950 | +9.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↑ +7.54% | paypal +5.4% | Adyen +6.5% | Insufficient Funds -5.81pp | paypal + Adyen + Insufficient |

---

*Report: 2026-04-17*
