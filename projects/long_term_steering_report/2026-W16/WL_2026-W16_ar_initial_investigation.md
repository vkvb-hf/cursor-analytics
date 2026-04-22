# AR Initial (LL0) Investigation: WL 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 91.05% → 91.28% (+0.25%)  
**Volume:** 13,021 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved slightly from 91.05% to 91.28% (+0.23pp) in W16, a change that is not statistically significant, with volume increasing 12.4% to 13,021 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.22%-91.98%) | +0.23pp | ✅ |
| L1: Country Variance | 3 countries exceed ±2.5% threshold | CK -4.01%, AO +2.64%, GN +4.04% | ⚠️ |
| L1: Dimension Scan | All payment methods/providers within tolerance | Max change -2.03% (Adyen) | ✅ |
| L2: Country Deep-Dive | CK decline driven by credit_card/Adyen | -5.45% on 1,662 orders | ⚠️ |
| L3: Related Metrics | All funnel metrics stable and improving | FirstRunAR +1.04%, PostDunningAR +0.24% | ✅ |

**Key Findings:**
- CK experienced a significant -4.01% decline driven by credit_card via Adyen (-5.45%), with "Other reasons" declines increasing by +3.84pp
- GN showed strong improvement (+4.04%) primarily from applepay via Braintree (+5.78%), with Insufficient Funds declining by -2.60pp
- AO improved +2.64% due to credit_card/Adyen recovery (+8.20%), offsetting a -4.78% drop in applepay/ProcessOut
- Volume growth was notable in MR (+26.1%), GN (+21.1%), and KN (+18.3%), all high/medium AR tier countries
- The entire payment funnel shows consistent improvement: FirstRunAR (+1.04pp), PreDunningAR (+0.26pp), PostDunningAR (+0.24pp)

**Action:** Monitor — The overall metric change is not significant and remains within historical norms. Continue monitoring CK's Adyen/credit_card performance for the "Other reasons" decline pattern; if the -4.01% trend persists for 2+ weeks, escalate for provider investigation.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.28% | 13,021 | +0.25% ← REPORTED CHANGE |
| 2026-W15 | 91.05% | 11,582 | +1.36% |
| 2026-W14 | 89.83% | 12,773 | +0.68% |
| 2026-W13 | 89.22% | 12,900 | -1.40% |
| 2026-W12 | 90.49% | 13,905 | -1.62% |
| 2026-W11 | 91.98% | 14,300 | +1.09% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 85.01% | 88.56% | -4.01% | 2,301 | ⚠️ |
| KN | 96.20% | 97.18% | -1.01% | 2,393 |  |
| MR | 94.95% | 93.06% | +2.03% | 2,437 |  |
| AO | 82.28% | 80.17% | +2.64% | 683 | ⚠️ |
| GN | 93.10% | 89.48% | +4.04% | 1,290 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CK, AO, GN

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.41% | 89.58% | -1.30% | 6,652 |  |
| Paypal | 94.16% | 95.37% | -1.26% | 1,371 |  |
| Apple Pay | 92.23% | 90.73% | +1.66% | 3,565 |  |
| Others | 99.51% | 97.68% | +1.88% | 1,433 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 84.53% | 86.28% | -2.03% | 2,450 |  |
| ProcessOut | 88.78% | 89.3% | -0.59% | 3,136 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 18 |  |
| Braintree | 93.4% | 93.08% | +0.34% | 6,048 |  |
| Unknown | 99.63% | 97.71% | +1.97% | 1,369 |  |

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 50.00% | 0.00% | +0.00% | 4 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 6 |  |
| cashcredit | 0.00% | 100.00% | -100.00% | 0 | 3 | ⚠️ |
| credit_card | 83.27% | 88.07% | -5.45% | 1,662 | 1,375 | ⚠️ |
| paypal | 86.42% | 88.43% | -2.27% | 243 | 216 |  |
| applepay | 91.84% | 91.90% | -0.07% | 392 | 358 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 50.00% | 0.00% | +0.00% | 4 | 6 |  |
| No Payment | 0.00% | 100.00% | -100.00% | 0 | 3 | ⚠️ |
| Adyen | 83.27% | 88.07% | -5.45% | 1,662 | 1,375 | ⚠️ |
| Braintree | 89.76% | 90.59% | -0.91% | 635 | 574 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Other reasons | 139 | 43 | 6.04% | 2.20% | +3.84 |
| 1. SUCCESSFULL | 1,956 | 1,734 | 85.01% | 88.56% | -3.55 |
| Unknown | 2 | 6 | 0.09% | 0.31% | -0.22 |
| Insufficient Funds | 150 | 130 | 6.52% | 6.64% | -0.12 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 54 | 45 | 2.35% | 2.30% | +0.05 |

**Root Cause:** cashcredit + No + Other

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 3 |  |
| applepay | 77.12% | 80.99% | -4.78% | 236 | 263 |  |
| paypal | 93.33% | 93.46% | -0.13% | 105 | 107 |  |
| credit_card | 82.46% | 76.20% | +8.20% | 342 | 353 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 3 |  |
| ProcessOut | 77.12% | 80.99% | -4.78% | 236 | 263 |  |
| Braintree | 93.33% | 93.46% | -0.13% | 105 | 107 |  |
| Adyen | 82.46% | 76.20% | +8.20% | 342 | 353 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 562 | 582 | 82.28% | 80.17% | +2.12 |
| Insufficient Funds | 108 | 125 | 15.81% | 17.22% | -1.41 |
| Unknown | 0 | 2 | 0.00% | 0.28% | -0.28 |
| Other reasons | 4 | 6 | 0.59% | 0.83% | -0.24 |
| PROVIDER_ERROR: failure executing charge with provider | 0 | 1 | 0.00% | 0.14% | -0.14 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 9 | 10 | 1.32% | 1.38% | -0.06 |

**Root Cause:** credit_card + Adyen + Insufficient

---

## L2: GN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 98.31% | 0.00% | +0.00% | 118 | 0 |  |
| None | 0.00% | 98.68% | -100.00% | 0 | 76 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 5 | 3 |  |
| paypal | 95.72% | 94.59% | +1.19% | 187 | 148 |  |
| credit_card | 89.80% | 88.55% | +1.42% | 402 | 358 |  |
| applepay | 93.43% | 87.08% | +7.28% | 578 | 480 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 97.30% | 98.15% | -0.87% | 74 | 54 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 5 | 4 |  |
| Adyen | 90.81% | 89.18% | +1.82% | 446 | 379 |  |
| Braintree | 93.99% | 88.85% | +5.78% | 765 | 628 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,201 | 953 | 93.10% | 89.48% | +3.62 |
| Insufficient Funds | 73 | 88 | 5.66% | 8.26% | -2.60 |
| Other reasons | 2 | 10 | 0.16% | 0.94% | -0.78 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 12 | 13 | 0.93% | 1.22% | -0.29 |
| Unknown | 2 | 1 | 0.16% | 0.09% | +0.06 |

**Root Cause:** None + Braintree + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.26% | 88.34% | +1.04% | 13,021 | 11,582 |  |
| 2_PreDunningAR | 91.28% | 91.05% | +0.26% | 13,021 | 11,582 |  |
| 3_PostDunningAR | 91.52% | 91.31% | +0.24% | 13,021 | 11,582 |  |
| 6_PaymentApprovalRate | 91.7% | 91.46% | +0.26% | 13,021 | 11,582 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,048 | 2,079 | +1.5% | Stable |
| KN | High (>92%) | 2,023 | 2,393 | +18.3% | Stable |
| CK | Medium (>85%) | 1,958 | 2,301 | +17.5% | Stable |
| MR | High (>92%) | 1,932 | 2,437 | +26.1% | Stable |
| CG | High (>92%) | 1,830 | 1,838 | +0.4% | Stable |
| GN | Medium (>85%) | 1,065 | 1,290 | +21.1% | Stable |
| AO | Low (>85%) | 726 | 683 | -5.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CK | ↓ -4.01% | cashcredit -100.0% | No Payment -100.0% | Other reasons +3.84pp | cashcredit + No + Other |
| AO | ↑ +2.64% | credit_card +8.2% | Adyen +8.2% | Insufficient Funds -1.41pp | credit_card + Adyen + Insufficient |
| GN | ↑ +4.04% | None -100.0% | Braintree +5.8% | Insufficient Funds -2.60pp | None + Braintree + Insufficient |

---

*Report: 2026-04-22*
