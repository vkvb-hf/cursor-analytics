# AR Initial (LL0) Investigation: HF-NA 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.33% → 90.32% (+1.11%)  
**Volume:** 18,241 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-NA improved from 89.33% to 90.32% (+1.11%) in W17, representing a significant positive change across 18,241 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | Rate at 90.32%, highest in 8 weeks | +1.11% | ✅ |
| L1: Country Split | CA +2.73% exceeds ±2.5% threshold | US +0.57%, CA +2.73% | ⚠️ |
| L1: PaymentProvider | Adyen +10.43% flagged | Apple Pay +1.97% | ⚠️ |
| L2: CA Deep-Dive | ProcessOut volume dropped to 0 | -100% volume | ⚠️ |
| L2: CA Decline Reasons | Insufficient Funds decreased | -2.15pp | ✅ |
| L3: Related Metrics | All funnel metrics improved | +1.01% to +1.13% | ✅ |

**Key Findings:**
- CA drove the regional improvement with +2.73% AR increase, while US contributed a modest +0.57% gain
- ProcessOut volume in CA dropped from 247 to 0 orders (-100%), coinciding with Adyen volume surge from 65 to 427 orders (+12.27pp AR improvement)
- Insufficient Funds declines in CA decreased significantly from 6.26% to 4.11% (-2.15pp), directly contributing to higher acceptance rates
- Credit card acceptance in CA improved substantially from 86.04% to 92.75% (+7.80%), though volume decreased from 308 to 193 orders
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) showed parallel improvements of +1.01% to +1.13%

**Action:** Monitor - The improvement appears driven by a payment provider shift from ProcessOut to Adyen in CA, combined with reduced Insufficient Funds declines. Continue monitoring to confirm sustainability of gains and verify ProcessOut migration was intentional.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 90.32% | 18,241 | +1.11% ← REPORTED CHANGE |
| 2026-W16 | 89.33% | 18,067 | -0.61% |
| 2026-W15 | 89.88% | 16,127 | +0.31% |
| 2026-W14 | 89.6% | 17,074 | +0.36% |
| 2026-W13 | 89.28% | 16,133 | -0.40% |
| 2026-W12 | 89.64% | 21,113 | -1.30% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.24% | 88.73% | +0.57% | 13,134 |  |
| CA | 93.09% | 90.62% | +2.73% | 5,107 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CA

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.39% | 88.79% | -0.46% | 353 |  |
| Others | 90.83% | 90.33% | +0.55% | 10,599 |  |
| Paypal | 90.88% | 89.53% | +1.51% | 1,480 |  |
| Apple Pay | 89.36% | 87.63% | +1.97% | 5,809 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 90.13% | +nan% | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 111 |  |
| Unknown | 90.49% | 90.18% | +0.34% | 10,217 |  |
| Braintree | 89.52% | 87.86% | +1.90% | 7,446 |  |
| Adyen | 97.0% | 87.84% | +10.43% | 467 | ⚠️ |

---

## L2: CA Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 92.57% | 0.00% | +0.00% | 3,228 | 0 |  |
| None | 0.00% | 90.81% | -100.00% | 0 | 3,503 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 45 | 51 |  |
| paypal | 91.47% | 89.88% | +1.76% | 457 | 504 |  |
| applepay | 94.93% | 91.09% | +4.22% | 1,184 | 1,336 |  |
| credit_card | 92.75% | 86.04% | +7.80% | 193 | 308 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 85.83% | -100.00% | 0 | 247 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 45 | 51 |  |
| Unknown | 91.98% | 90.82% | +1.28% | 2,994 | 3,498 |  |
| Braintree | 93.97% | 90.77% | +3.53% | 1,641 | 1,841 |  |
| Adyen | 96.72% | 86.15% | +12.27% | 427 | 65 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 4,754 | 5,167 | 93.09% | 90.62% | +2.47 |
| Insufficient Funds | 210 | 357 | 4.11% | 6.26% | -2.15 |
| Other reasons | 78 | 104 | 1.53% | 1.82% | -0.30 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 48 | 63 | 0.94% | 1.10% | -0.16 |
| Unknown | 17 | 11 | 0.33% | 0.19% | +0.14 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.24% | 88.24% | +1.13% | 18,241 | 18,067 |  |
| 2_PreDunningAR | 90.32% | 89.33% | +1.11% | 18,241 | 18,067 |  |
| 3_PostDunningAR | 90.41% | 89.49% | +1.02% | 18,241 | 18,067 |  |
| 6_PaymentApprovalRate | 90.62% | 89.72% | +1.01% | 18,241 | 18,067 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 12,365 | 13,134 | +6.2% | Stable |
| CA | Medium (>85%) | 5,702 | 5,107 | -10.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CA | ↑ +2.73% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -2.15pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-28*
