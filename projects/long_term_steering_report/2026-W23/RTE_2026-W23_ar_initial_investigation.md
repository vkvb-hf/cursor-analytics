# AR Initial (LL0) Investigation: RTE 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 92.76% → 91.91% (-0.92%)  
**Volume:** 27,494 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 92.76% to 91.91% (-0.92%) in 2026-W23, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (91.91%-93.06%) | -0.85pp | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold | TK -5.51%, TO +4.24% | ⚠️ |
| L1: Dimension Scan | PaymentProvider "Unknown" flagged | -4.55% | ⚠️ |
| L2: TK Deep-Dive | Apple Pay + Braintree degradation | -9.41%, -8.40% | ⚠️ |
| L2: TO Deep-Dive | Credit Card + Adyen improvement | +7.21%, +5.30% | ✅ |
| L3: Related Metrics | All loyalty metrics declined similarly | -0.91% to -1.28% | ⚠️ |
| Mix Shift | No significant volume shifts | All stable | ✅ |

**Key Findings:**
- TK experienced a significant decline (-5.51%) driven by Apple Pay via Braintree, with "Insufficient Funds" declines increasing by +4.49pp (from 5.99% to 10.47%)
- TO showed strong improvement (+4.24%) due to credit card performance via Adyen, with "Insufficient Funds" declines decreasing by -3.13pp
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) declined in parallel, suggesting a systemic rather than isolated issue
- The TK decline is concentrated in low volume (296 orders) but the root cause (Braintree + Apple Pay + Insufficient Funds) is clearly identifiable
- "Unknown" PaymentProvider showed a -4.55% decline but with minimal volume impact (66 orders)

**Action:** Monitor — The overall change is not statistically significant and within normal 8-week variance. Continue monitoring TK's Braintree/Apple Pay performance for persistence in W24. No escalation required unless TK decline persists for 2+ consecutive weeks.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 91.91% | 27,494 | -0.92% ← REPORTED CHANGE |
| 2026-W22 | 92.76% | 27,332 | -0.19% |
| 2026-W21 | 92.94% | 26,965 | +0.01% |
| 2026-W20 | 92.93% | 29,030 | +0.93% |
| 2026-W19 | 92.07% | 29,461 | -0.27% |
| 2026-W18 | 92.32% | 32,344 | -0.80% |
| 2026-W17 | 93.06% | 30,373 | +0.64% |
| 2026-W16 | 92.47% | 31,083 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 87.84% | 92.96% | -5.51% | 296 | ⚠️ |
| CF | 91.84% | 93.78% | -2.07% | 5,344 |  |
| FJ | 92.12% | 92.98% | -0.92% | 17,481 |  |
| TV | 95.15% | 93.70% | +1.55% | 330 |  |
| TO | 90.85% | 87.16% | +4.24% | 317 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.06% | 96.66% | -1.66% | 3,298 |  |
| Credit Card | 91.37% | 92.39% | -1.10% | 17,075 |  |
| Others | 95.26% | 96.08% | -0.86% | 1,139 |  |
| Apple Pay | 91.07% | 91.15% | -0.08% | 5,982 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 54.55% | 57.14% | -4.55% | 66 | ⚠️ |
| ProcessOut | 92.26% | 93.36% | -1.18% | 10,100 |  |
| Adyen | 91.01% | 91.87% | -0.93% | 7,911 |  |
| Braintree | 92.52% | 93.03% | -0.55% | 9,370 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 47 |  |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| applepay | 82.35% | 90.91% | -9.41% | 119 | 110 | ⚠️ |
| credit_card | 90.32% | 93.71% | -3.62% | 155 | 159 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 8 | 1 |  |
| paypal | 100.00% | 100.00% | +0.00% | 14 | 14 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 84.21% | 91.94% | -8.40% | 133 | 124 | ⚠️ |
| Adyen | 90.32% | 93.71% | -3.62% | 155 | 159 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 8 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 260 | 264 | 87.84% | 92.96% | -5.12 |
| Insufficient Funds | 31 | 17 | 10.47% | 5.99% | +4.49 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 1 | 0.68% | 0.35% | +0.32 |
| Other reasons | 3 | 2 | 1.01% | 0.70% | +0.31 |

**Root Cause:** applepay + Braintree + Insufficient

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 7 | 2 |  |
| paypal | 97.62% | 96.36% | +1.30% | 42 | 55 |  |
| bancontact | 90.28% | 87.76% | +2.87% | 144 | 49 |  |
| applepay | 85.42% | 82.19% | +3.92% | 48 | 73 |  |
| credit_card | 92.00% | 85.81% | +7.21% | 75 | 148 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 7 | 2 |  |
| Braintree | 91.11% | 88.28% | +3.21% | 90 | 128 |  |
| Adyen | 90.87% | 86.29% | +5.30% | 219 | 197 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 288 | 285 | 90.85% | 87.16% | +3.70 |
| Insufficient Funds | 24 | 35 | 7.57% | 10.70% | -3.13 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1 | 6 | 0.32% | 1.83% | -1.52 |
| Other reasons | 3 | 1 | 0.95% | 0.31% | +0.64 |
| Unknown | 1 | 0 | 0.32% | 0.00% | +0.32 |

**Root Cause:** credit_card + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.14% | 90.3% | -1.28% | 27,494 | 27,332 |  |
| 2_PreDunningAR | 91.91% | 92.76% | -0.91% | 27,494 | 27,332 |  |
| 3_PostDunningAR | 92.19% | 93.08% | -0.96% | 27,494 | 27,332 |  |
| 6_PaymentApprovalRate | 92.35% | 93.22% | -0.93% | 27,494 | 27,332 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 17,482 | 17,481 | +0.0% | Stable |
| CF | High (>92%) | 5,195 | 5,344 | +2.9% | Stable |
| YE | Medium (>85%) | 2,823 | 2,703 | -4.3% | Stable |
| TT | High (>92%) | 585 | 581 | -0.7% | Stable |
| TZ | Medium (>85%) | 382 | 442 | +15.7% | Stable |
| TO | Medium (>85%) | 327 | 317 | -3.1% | Stable |
| TK | High (>92%) | 284 | 296 | +4.2% | Stable |
| TV | High (>92%) | 254 | 330 | +29.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↓ -5.51% | applepay -9.4% | Braintree -8.4% | Insufficient Funds +4.49pp | applepay + Braintree + Insufficient |
| TO | ↑ +4.24% | credit_card +7.2% | Adyen +5.3% | Insufficient Funds -3.13pp | credit_card + Adyen + Insufficient |

---

*Report: 2026-06-09*
