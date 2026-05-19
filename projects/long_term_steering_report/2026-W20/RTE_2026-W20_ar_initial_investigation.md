# AR Initial (LL0) Investigation: RTE 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.31% → 93.63% (+1.43%)  
**Volume:** 30,254 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved significantly from 92.31% to 93.63% (+1.43%) in 2026-W20, with volume of 30,254 orders representing a healthy week-over-week increase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate at 8-week high (93.63%) | +1.43% | ✅ |
| L1: Country Breakdown | 2 countries flagged (TO, YE) | TO -3.84%, YE +2.59% | ⚠️ |
| L1: Payment Method | No segments exceeding threshold | Max +1.89% (Credit Card) | ✅ |
| L1: Payment Provider | No segments exceeding threshold | Max +2.16% (Unknown) | ✅ |
| L2: TO Deep-Dive | Apple Pay & Braintree degradation | applepay -9.03%, Braintree -5.80% | ⚠️ |
| L2: YE Deep-Dive | Improvement driven by lower Insufficient Funds | Insufficient Funds -1.71pp | ✅ |
| L3: Related Metrics | All funnel metrics improved consistently | +1.40% to +1.50% | ✅ |

**Key Findings:**
- TO experienced a -3.84% decline driven by Apple Pay (-9.03%) on Braintree (-5.80%), with Insufficient Funds increasing by +2.30pp
- YE improved by +2.59% due to reduced Insufficient Funds declines (-1.71pp), primarily on Adyen credit card transactions
- Credit Card payments showed the strongest improvement (+1.89%) at the global level, representing 63% of volume (19,187 orders)
- ProcessOut provider showed notable improvement (+2.05%) with the highest volume among providers (11,153 orders)
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) moved in lockstep, confirming genuine acceptance improvement

**Action:** Monitor - The overall metric improvement is positive and significant. Continue monitoring TO for Apple Pay/Braintree performance; if degradation persists beyond 2 weeks, escalate to payment operations team for Braintree investigation.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 93.63% | 30,254 | +1.43% ← REPORTED CHANGE |
| 2026-W19 | 92.31% | 29,699 | +0.02% |
| 2026-W18 | 92.29% | 32,312 | -0.80% |
| 2026-W17 | 93.03% | 30,454 | +0.71% |
| 2026-W16 | 92.37% | 31,013 | +0.88% |
| 2026-W15 | 91.56% | 29,016 | +0.78% |
| 2026-W14 | 90.85% | 31,964 | -0.57% |
| 2026-W13 | 91.37% | 36,469 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 90.03% | 93.62% | -3.84% | 361 | ⚠️ |
| CF | 94.87% | 94.22% | +0.69% | 6,164 |  |
| FJ | 93.86% | 92.43% | +1.55% | 18,885 |  |
| TZ | 94.31% | 92.39% | +2.07% | 439 |  |
| YE | 89.00% | 86.75% | +2.59% | 3,137 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TO, YE

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.63% | 96.18% | -0.57% | 3,595 |  |
| Others | 97.48% | 96.38% | +1.14% | 1,229 |  |
| Apple Pay | 92.44% | 91.22% | +1.34% | 6,243 |  |
| Credit Card | 93.39% | 91.66% | +1.89% | 19,187 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 47 |  |
| Braintree | 93.6% | 93.0% | +0.64% | 9,931 |  |
| Adyen | 92.95% | 91.54% | +1.54% | 9,039 |  |
| ProcessOut | 94.35% | 92.46% | +2.05% | 11,153 |  |
| Unknown | 70.24% | 68.75% | +2.16% | 84 |  |

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| applepay | 81.40% | 89.47% | -9.03% | 86 | 76 | ⚠️ |
| bancontact | 95.45% | 100.00% | -4.55% | 22 | 2 |  |
| credit_card | 91.21% | 93.14% | -2.07% | 182 | 204 |  |
| paypal | 98.46% | 100.00% | -1.54% | 65 | 62 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| Braintree | 88.74% | 94.20% | -5.80% | 151 | 138 | ⚠️ |
| Adyen | 91.67% | 93.20% | -1.65% | 204 | 206 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 325 | 323 | 90.03% | 93.62% | -3.60 |
| Insufficient Funds | 24 | 15 | 6.65% | 4.35% | +2.30 |
| Unknown | 2 | 0 | 0.55% | 0.00% | +0.55 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 5 | 3 | 1.39% | 0.87% | +0.52 |
| Other reasons | 5 | 4 | 1.39% | 1.16% | +0.23 |

**Root Cause:** applepay + Braintree + Insufficient

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 96.18% | 0.00% | +0.00% | 131 | 0 |  |
| None | 0.00% | 97.30% | -100.00% | 0 | 74 | ⚠️ |
| paypal | 95.10% | 94.14% | +1.02% | 714 | 768 |  |
| credit_card | 86.69% | 84.11% | +3.07% | 2,292 | 2,442 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 81.82% | 88.89% | -7.95% | 22 | 18 | ⚠️ |
| Braintree | 95.10% | 94.14% | +1.02% | 714 | 768 |  |
| Adyen | 87.26% | 84.47% | +3.30% | 2,401 | 2,498 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,792 | 2,849 | 89.00% | 86.75% | +2.25 |
| Insufficient Funds | 292 | 362 | 9.31% | 11.02% | -1.71 |
| Other reasons | 8 | 20 | 0.26% | 0.61% | -0.35 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 41 | 51 | 1.31% | 1.55% | -0.25 |
| Unknown | 4 | 2 | 0.13% | 0.06% | +0.07 |

**Root Cause:** None + Unknown + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.31% | 89.97% | +1.50% | 30,254 | 29,699 |  |
| 2_PreDunningAR | 93.63% | 92.31% | +1.43% | 30,254 | 29,699 |  |
| 3_PostDunningAR | 93.88% | 92.59% | +1.40% | 30,254 | 29,699 |  |
| 6_PaymentApprovalRate | 94.05% | 92.73% | +1.42% | 30,254 | 29,699 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 18,420 | 18,885 | +2.5% | Stable |
| CF | High (>92%) | 5,954 | 6,164 | +3.5% | Stable |
| YE | Medium (>85%) | 3,284 | 3,137 | -4.5% | Stable |
| TT | High (>92%) | 633 | 620 | -2.1% | Stable |
| TZ | High (>92%) | 460 | 439 | -4.6% | Stable |
| TO | High (>92%) | 345 | 361 | +4.6% | Stable |
| TV | High (>92%) | 323 | 319 | -1.2% | Stable |
| TK | High (>92%) | 280 | 329 | +17.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -3.84% | applepay -9.0% | Braintree -5.8% | Insufficient Funds +2.30pp | applepay + Braintree + Insufficient |
| YE | ↑ +2.59% | None -100.0% | Unknown -8.0% | Insufficient Funds -1.71pp | None + Unknown + Insufficient |

---

*Report: 2026-05-19*
