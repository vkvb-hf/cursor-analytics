# PAR Investigation: RTE 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 94.87% → 94.81% (-0.06%)  
**Volume:** 429,385 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate showed a minor decline of -0.06pp (94.87% → 94.81%) in W16, which is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Week-over-week change | +0.48% | ✅ |
| 2_PreDunningAR | Week-over-week change | +0.41% | ✅ |
| 3_PostDunningAR | Week-over-week change | +0.03% | ✅ |
| 6_PaymentApprovalRate | Week-over-week change | +0.12% | ✅ |
| Country Variance | TK exceeds ±2.5% threshold | +5.72% | ⚠️ |
| Provider Variance | Unknown exceeds threshold | -10.58% | ⚠️ |

**Key Findings:**
- TK showed significant improvement of +5.72pp (90.95% → 96.15%), driven by reduced "Insufficient Funds" declines (-4.63pp) across credit_card payments via Adyen
- Unknown PaymentProvider flagged with -10.58% change, but volume is negligible (130 orders) and not material to overall performance
- TV experienced the largest decline at -2.15pp (94.92% → 92.88%) with 1,895 orders, but low volume limits impact
- All payment methods stable: Credit Card +0.16%, Apple Pay +0.17%, Paypal +0.01%, Others -0.80%
- Mix shift analysis shows all countries stable despite volume fluctuations ranging from -11.7% (TZ) to +9.6% (TK)

**Action:** Monitor — The -0.06pp change is not significant, and the flagged TK country actually represents a positive improvement. No investigation or escalation required.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.81% | 429,385 | -0.06% |
| 2026-W15 | 94.87% | 421,406 | +0.13% ← REPORTED CHANGE |
| 2026-W14 | 94.75% | 431,856 | -0.20% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.88% | 94.92% | -2.15% | 1,895 |  |
| YE | 93.01% | 93.42% | -0.44% | 42,126 |  |
| FJ | 95.65% | 95.55% | +0.11% | 388,956 |  |
| CF | 95.33% | 94.86% | +0.50% | 51,881 |  |
| TO | 88.89% | 88.07% | +0.92% | 3,204 |  |
| TZ | 93.23% | 92.07% | +1.27% | 2,660 |  |
| TK | 96.15% | 90.95% | +5.72% | 1,950 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.26% | 99.05% | -0.80% | 5,339 |  |
| Paypal | 97.72% | 97.71% | +0.01% | 53,618 |  |
| Credit Card | 94.73% | 94.58% | +0.16% | 308,899 |  |
| Apple Pay | 92.51% | 92.35% | +0.17% | 53,550 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 71.54% | 80.0% | -10.58% | 130 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 510 |  |
| ProcessOut | 93.45% | 93.43% | +0.02% | 64,367 |  |
| Braintree | 95.65% | 95.51% | +0.15% | 282,048 |  |
| Adyen | 93.13% | 92.87% | +0.28% | 74,351 |  |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 10 | 7 |  |
| paypal | 97.46% | 95.28% | +2.28% | 118 | 106 |  |
| credit_card | 96.69% | 92.04% | +5.05% | 1,359 | 1,256 | ⚠️ |
| applepay | 94.37% | 86.34% | +9.30% | 462 | 410 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 10 | 7 |  |
| Adyen | 96.69% | 92.04% | +5.05% | 1,359 | 1,256 | ⚠️ |
| Braintree | 95.00% | 88.18% | +7.74% | 580 | 516 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,875 | 1,618 | 96.15% | 90.95% | +5.20 |
| Insufficient Funds | 38 | 117 | 1.95% | 6.58% | -4.63 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 20 | 25 | 1.03% | 1.41% | -0.38 |
| Other reasons | 16 | 19 | 0.82% | 1.07% | -0.25 |
| Unknown | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** credit_card + Adyen + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.25% | 90.82% | +0.48% | 421,406 | 431,856 |  |
| 2_PreDunningAR | 92.83% | 92.46% | +0.41% | 421,406 | 431,856 |  |
| 3_PostDunningAR | 94.33% | 94.3% | +0.03% | 421,406 | 431,856 |  |
| 6_PaymentApprovalRate | 94.87% | 94.75% | +0.12% | 421,406 | 431,856 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 397,332 | 388,956 | -2.1% | Stable |
| CF | High (>92%) | 52,140 | 51,881 | -0.5% | Stable |
| YE | High (>92%) | 45,217 | 42,126 | -6.8% | Stable |
| TT | High (>92%) | 4,924 | 4,617 | -6.2% | Stable |
| TO | Medium (>85%) | 3,480 | 3,204 | -7.9% | Stable |
| TZ | High (>92%) | 3,013 | 2,660 | -11.7% | Stable |
| TV | High (>92%) | 2,065 | 1,895 | -8.2% | Stable |
| TK | Medium (>85%) | 1,779 | 1,950 | +9.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↑ +5.72% | credit_card +5.0% | Adyen +5.0% | Insufficient Funds -4.63pp | credit_card + Adyen + Insufficient |

---

*Report: 2026-04-22*
