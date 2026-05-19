# AR Overall Investigation: RTE 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.0% → 92.73% (+0.79%)  
**Volume:** 414,676 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved from 92.0% to 92.73% (+0.79%) in W20, a positive but statistically not significant change across 414,676 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.45%-92.83%) | +0.79% | ✅ |
| L1: Country Breakdown | 1 country exceeding ±2.5% threshold (TK) | +2.93% | ⚠️ |
| L1: PaymentMethod | All methods within threshold | +0.27% to +0.90% | ✅ |
| L1: PaymentProvider | Unknown flagged but minimal volume (113) | +11.16% | ⚠️ |
| L2: TK Deep-Dive | applepay and Braintree flagged | +6.43%, +5.25% | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently | +0.55% to +0.79% | ✅ |
| Mix Shift | All countries stable, no significant volume shifts | - | ✅ |

**Key Findings:**
- TK showed the largest improvement (+2.93%) driven by applepay (+6.43%) and Braintree (+5.25%), with Insufficient Funds declines dropping by 2.35pp
- All payment methods improved globally, with Credit Card (+0.90%) showing the strongest gain at highest volume (303,503 orders)
- The entire payment funnel improved consistently: FirstRunAR (+0.75%), PreDunningAR (+0.79%), PostDunningAR (+0.55%), and PaymentApprovalRate (+0.68%)
- Volume declined 3.0% week-over-week (427,697 → 414,676), but mix shift analysis shows no material impact on rates
- Unknown PaymentProvider showed +11.16% improvement but represents negligible volume (113 orders)

**Action:** Monitor — The improvement is positive but not statistically significant. Continue tracking TK performance to confirm the applepay/Braintree improvement trend sustains.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 92.73% | 414,676 | +0.79% ← REPORTED CHANGE |
| 2026-W19 | 92.0% | 427,697 | -0.59% |
| 2026-W18 | 92.55% | 430,745 | -0.22% |
| 2026-W17 | 92.75% | 430,820 | +0.12% |
| 2026-W16 | 92.64% | 429,384 | -0.20% |
| 2026-W15 | 92.83% | 421,405 | +0.41% |
| 2026-W14 | 92.45% | 431,855 | -0.36% |
| 2026-W13 | 92.78% | 442,529 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CF | 93.87% | 93.63% | +0.26% | 52,629 |  |
| FJ | 93.70% | 93.21% | +0.52% | 375,016 |  |
| TT | 97.46% | 96.60% | +0.89% | 4,567 |  |
| YE | 88.88% | 86.82% | +2.37% | 44,478 |  |
| TO | 90.53% | 88.40% | +2.41% | 2,871 |  |
| TK | 94.66% | 91.97% | +2.93% | 1,949 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.52% | 96.26% | +0.27% | 53,613 |  |
| Apple Pay | 90.15% | 89.59% | +0.62% | 52,005 |  |
| Others | 98.36% | 97.66% | +0.72% | 5,555 |  |
| Credit Card | 92.4% | 91.57% | +0.90% | 303,503 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 597 |  |
| Braintree | 93.78% | 93.27% | +0.55% | 255,001 |  |
| ProcessOut | 91.63% | 90.56% | +1.18% | 83,380 |  |
| Adyen | 90.38% | 89.24% | +1.28% | 75,585 |  |
| Unknown | 62.83% | 56.52% | +11.16% | 113 | ⚠️ |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 8 | 15 |  |
| paypal | 95.76% | 94.49% | +1.35% | 118 | 127 |  |
| credit_card | 94.92% | 93.02% | +2.04% | 1,377 | 1,462 |  |
| applepay | 93.50% | 87.85% | +6.43% | 446 | 461 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 8 | 15 |  |
| Adyen | 94.92% | 93.02% | +2.04% | 1,377 | 1,462 |  |
| Braintree | 93.97% | 89.29% | +5.25% | 564 | 588 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,845 | 1,900 | 94.66% | 91.97% | +2.70 |
| Insufficient Funds | 57 | 109 | 2.92% | 5.28% | -2.35 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 21 | 27 | 1.08% | 1.31% | -0.23 |
| Other reasons | 26 | 29 | 1.33% | 1.40% | -0.07 |
| Unknown | 0 | 1 | 0.00% | 0.05% | -0.05 |

**Root Cause:** applepay + Braintree + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.09% | 90.41% | +0.75% | 414,676 | 427,697 |  |
| 2_PreDunningAR | 92.73% | 92.0% | +0.79% | 414,676 | 427,697 |  |
| 3_PostDunningAR | 94.16% | 93.64% | +0.55% | 414,676 | 427,697 |  |
| 6_PaymentApprovalRate | 94.79% | 94.15% | +0.68% | 414,676 | 427,697 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 392,524 | 375,016 | -4.5% | Stable |
| CF | High (>92%) | 53,720 | 52,629 | -2.0% | Stable |
| YE | Medium (>85%) | 44,452 | 44,478 | +0.1% | Stable |
| TT | High (>92%) | 4,762 | 4,567 | -4.1% | Stable |
| TO | Medium (>85%) | 3,206 | 2,871 | -10.4% | Stable |
| TZ | High (>92%) | 3,154 | 2,937 | -6.9% | Stable |
| TK | Medium (>85%) | 2,066 | 1,949 | -5.7% | Stable |
| TV | High (>92%) | 1,961 | 1,823 | -7.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↑ +2.93% | applepay +6.4% | Braintree +5.2% | Insufficient Funds -2.35pp | applepay + Braintree + Insufficient |

---

*Report: 2026-05-19*
