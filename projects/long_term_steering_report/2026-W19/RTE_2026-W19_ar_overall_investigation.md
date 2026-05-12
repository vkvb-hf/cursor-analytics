# AR Overall Investigation: RTE 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 92.55% → 92.0% (-0.59%)  
**Volume:** 427,697 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.55 pp (92.55% → 92.0%) on 427,697 orders in 2026-W19, a statistically not significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (92.0%-93.09%) | -0.55 pp | ✅ |
| L1: Country Scan | 1 country (TV) exceeds ±2.5% threshold | TV +4.61% | ⚠️ |
| L1: Dimension Scan | Unknown PaymentProvider flagged (+33.20%) | Low volume (119) | ✅ |
| L2: TV Deep-Dive | applepay +7.79%, credit_card +8.75%, Braintree +6.36% | Positive improvements | ✅ |
| L3: Related Metrics | All funnel metrics declined similarly (-0.52% to -0.67%) | Correlated movement | ✅ |
| Mix Shift | All countries stable, no significant volume shifts | No impact | ✅ |

**Key Findings:**
- TV showed a significant positive improvement (+4.61 pp), driven by reduced "Insufficient Funds" declines (-4.37 pp) and improved performance on applepay (+7.79%) and credit_card (+8.75%) via Braintree
- YE experienced the largest decline among major markets (-1.80 pp), moving from 88.42% to 86.82% on 44,452 orders
- All payment methods declined slightly (Apple Pay -0.84 pp, Credit Card -0.63 pp, PayPal -0.31 pp), indicating a broad-based rather than isolated issue
- The decline aligns with correlated drops across the full funnel: FirstRunAR (-0.59%), PostDunningAR (-0.67%), and PaymentApprovalRate (-0.52%)
- Volume remains stable week-over-week (427,697 vs 430,745), with no significant mix shift impact

**Action:** Monitor — The decline is not statistically significant and falls within the 8-week historical range. Continue monitoring YE performance and track if the positive TV trend sustains.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 92.0% | 427,697 | -0.59% ← REPORTED CHANGE |
| 2026-W18 | 92.55% | 430,745 | -0.22% |
| 2026-W17 | 92.75% | 430,820 | +0.12% |
| 2026-W16 | 92.64% | 429,384 | -0.20% |
| 2026-W15 | 92.83% | 421,405 | +0.41% |
| 2026-W14 | 92.45% | 431,855 | -0.36% |
| 2026-W13 | 92.78% | 442,529 | -0.33% |
| 2026-W12 | 93.09% | 443,993 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| YE | 86.82% | 88.42% | -1.80% | 44,452 |  |
| FJ | 93.22% | 93.69% | -0.50% | 392,524 |  |
| CF | 93.65% | 93.81% | -0.17% | 53,720 |  |
| TO | 88.40% | 86.81% | +1.83% | 3,206 |  |
| TK | 91.97% | 90.23% | +1.92% | 2,066 |  |
| TV | 94.49% | 90.33% | +4.61% | 1,961 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 89.6% | 90.35% | -0.84% | 54,675 |  |
| Credit Card | 91.58% | 92.16% | -0.63% | 312,610 |  |
| Paypal | 96.27% | 96.56% | -0.31% | 54,684 |  |
| Others | 97.56% | 96.62% | +0.97% | 5,728 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 90.57% | 91.16% | -0.65% | 84,879 |  |
| Adyen | 89.24% | 89.81% | -0.63% | 77,693 |  |
| Braintree | 93.28% | 93.79% | -0.55% | 264,430 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 576 |  |
| Unknown | 57.98% | 43.53% | +33.20% | 119 | ⚠️ |

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| paypal | 89.47% | 90.00% | -0.58% | 57 | 60 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 29 | 21 |  |
| klarna | 98.47% | 97.84% | +0.65% | 786 | 787 |  |
| applepay | 88.29% | 81.90% | +7.79% | 350 | 326 | ⚠️ |
| credit_card | 93.50% | 85.97% | +8.75% | 738 | 770 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 29 | 21 |  |
| Adyen | 96.06% | 91.97% | +4.45% | 1,524 | 1,557 |  |
| Braintree | 88.45% | 83.16% | +6.36% | 407 | 386 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 65 | 151 | 3.31% | 7.69% | -4.37 |
| 1. SUCCESSFULL | 1,853 | 1,774 | 94.49% | 90.33% | +4.17 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 33 | 28 | 1.68% | 1.43% | +0.26 |
| Other reasons | 9 | 11 | 0.46% | 0.56% | -0.10 |
| Unknown | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** applepay + Braintree + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.41% | 90.94% | -0.59% | 427,697 | 430,745 |  |
| 2_PreDunningAR | 92.0% | 92.55% | -0.59% | 427,697 | 430,745 |  |
| 3_PostDunningAR | 93.51% | 94.14% | -0.67% | 427,697 | 430,745 |  |
| 6_PaymentApprovalRate | 94.15% | 94.65% | -0.52% | 427,697 | 430,745 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 396,038 | 392,524 | -0.9% | Stable |
| CF | High (>92%) | 53,548 | 53,720 | +0.3% | Stable |
| YE | Medium (>85%) | 45,256 | 44,452 | -1.8% | Stable |
| TT | High (>92%) | 4,511 | 4,762 | +5.6% | Stable |
| TO | Medium (>85%) | 3,214 | 3,206 | -0.2% | Stable |
| TZ | Medium (>85%) | 3,134 | 3,154 | +0.6% | Stable |
| TK | Medium (>85%) | 2,017 | 2,066 | +2.4% | Stable |
| TV | Medium (>85%) | 1,964 | 1,961 | -0.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↑ +4.61% | applepay +7.8% | Braintree +6.4% | Insufficient Funds -4.37pp | applepay + Braintree + Insufficient |

---

*Report: 2026-05-12*
