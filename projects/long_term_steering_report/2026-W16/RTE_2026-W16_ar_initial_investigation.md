# AR Initial (LL0) Investigation: RTE 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 91.73% → 92.56% (+0.90%)  
**Volume:** 32,099 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.73% to 92.56% (+0.90%) in W16, returning to W12 levels after a two-week dip, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.56% matches W12) | +0.90% | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold (YE, TV, TO) | +2.78% to +5.50% | ⚠️ |
| L1: Dimension Scan | Unknown PaymentProvider dropped -13.04% (low volume: 91) | -13.04% | ⚠️ |
| L2: Country Deep-Dives | All 3 flagged countries improved due to reduced Insufficient Funds declines | -2.13pp to -3.87pp | ✅ |
| L3: Related Metrics | All funnel metrics improved consistently (+0.90% to +1.04%) | Aligned | ✅ |
| Mix Shift | TO volume dropped -22.6% but minimal impact on overall rate | -22.6% vol | ⚠️ |

**Key Findings:**
- All three flagged countries (YE +2.78%, TV +5.21%, TO +5.50%) showed **improvement**, not degradation, driven by reduced "Insufficient Funds" declines (-2.13pp to -3.87pp)
- TV saw significant improvement in credit_card (+12.38%) and Braintree (+8.48%) acceptance rates
- TO experienced notable volume decline (-22.6%) but improved Adyen performance (+7.71%)
- The entire payment funnel moved in alignment: 1_FirstRunAR (+1.04%), 2_PreDunningAR (+0.90%), 3_PostDunningAR (+0.92%), 6_PaymentApprovalRate (+0.95%)
- Unknown PaymentProvider degradation (-13.04%) is contained to very low volume (91 orders)

**Action:** Monitor — The +0.90% improvement is positive but not statistically significant. Continue tracking to confirm the recovery trend from W13-W14 dip is sustained.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.56% | 32,099 | +0.90% ← REPORTED CHANGE |
| 2026-W15 | 91.73% | 30,171 | +0.99% |
| 2026-W14 | 90.83% | 31,907 | -0.66% |
| 2026-W13 | 91.43% | 36,491 | -1.22% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.23% |
| 2026-W10 | 92.72% | 48,166 | -0.93% |
| 2026-W09 | 93.59% | 46,087 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CF | 93.54% | 94.0% | -0.49% | 6,535 |  |
| FJ | 92.57% | 91.84% | +0.80% | 20,148 |  |
| TT | 97.79% | 95.6% | +2.28% | 587 |  |
| YE | 88.9% | 86.5% | +2.78% | 3,090 | ⚠️ |
| TV | 96.07% | 91.32% | +5.21% | 331 | ⚠️ |
| TO | 90.4% | 85.69% | +5.50% | 427 | ⚠️ |

**Countries exceeding ±2.5% threshold:** YE, TV, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.37% | 96.38% | -0.01% | 1,047 |  |
| Credit Card | 91.79% | 91.14% | +0.71% | 20,066 |  |
| Paypal | 96.61% | 95.67% | +0.98% | 3,834 |  |
| Apple Pay | 91.99% | 90.6% | +1.53% | 7,152 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 69.23% | 79.61% | -13.04% | 91 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 30 |  |
| ProcessOut | 92.18% | 91.67% | +0.55% | 11,581 |  |
| Adyen | 92.03% | 91.16% | +0.95% | 9,308 |  |
| Braintree | 93.57% | 92.37% | +1.30% | 11,089 |  |

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 89.89% | 0.0% | +0.00% | 89 | 0 |  |
| None | 0.0% | 96.88% | -100.00% | 0 | 64 | ⚠️ |
| paypal | 95.78% | 93.27% | +2.70% | 759 | 728 |  |
| credit_card | 86.53% | 83.97% | +3.04% | 2,242 | 2,215 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 65.22% | 77.78% | -16.15% | 23 | 9 | ⚠️ |
| Braintree | 95.78% | 93.27% | +2.70% | 759 | 728 |  |
| Adyen | 86.87% | 84.36% | +2.98% | 2,308 | 2,270 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,747 | 2,601 | 88.90% | 86.50% | +2.40 |
| Insufficient Funds | 260 | 317 | 8.41% | 10.54% | -2.13 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 55 | 77 | 1.78% | 2.56% | -0.78 |
| Other reasons | 20 | 10 | 0.65% | 0.33% | +0.31 |
| Unknown | 8 | 2 | 0.26% | 0.07% | +0.19 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 2 | 5 |  |
| klarna | 98.73% | 97.5% | +1.26% | 157 | 160 |  |
| applepay | 93.33% | 87.67% | +6.46% | 75 | 73 | ⚠️ |
| credit_card | 94.51% | 84.09% | +12.38% | 91 | 88 | ⚠️ |
| paypal | 100.0% | 75.0% | +33.33% | 5 | 8 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2 | 5 |  |
| Adyen | 97.18% | 92.74% | +4.78% | 248 | 248 |  |
| Braintree | 93.75% | 86.42% | +8.48% | 80 | 81 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 318 | 305 | 96.07% | 91.32% | +4.76 |
| Insufficient Funds | 8 | 21 | 2.42% | 6.29% | -3.87 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1 | 3 | 0.30% | 0.90% | -0.60 |
| Other reasons | 3 | 5 | 0.91% | 1.50% | -0.59 |
| Unknown | 1 | 0 | 0.30% | 0.00% | +0.30 |

**Root Cause:** applepay + Braintree + Insufficient

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 3 | 0 |  |
| None | 0.0% | 0.0% | +0.00% | 0 | 4 |  |
| sepadirectdebit | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| paypal | 98.59% | 98.85% | -0.26% | 71 | 87 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 1 | 2 |  |
| applepay | 85.44% | 82.35% | +3.74% | 103 | 153 |  |
| credit_card | 91.16% | 84.59% | +7.77% | 249 | 305 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 3 | 4 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1 | 2 |  |
| Braintree | 90.8% | 88.33% | +2.80% | 174 | 240 |  |
| Adyen | 91.16% | 84.64% | +7.71% | 249 | 306 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 386 | 473 | 90.40% | 85.69% | +4.71 |
| Insufficient Funds | 19 | 38 | 4.45% | 6.88% | -2.43 |
| Other reasons | 6 | 20 | 1.41% | 3.62% | -2.22 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 13 | 17 | 3.04% | 3.08% | -0.04 |
| Unknown | 3 | 4 | 0.70% | 0.72% | -0.02 |

**Root Cause:** sepadirectdebit + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.11% | 89.19% | +1.04% | 32,099 | 30,171 |  |
| 2_PreDunningAR | 92.56% | 91.73% | +0.90% | 32,099 | 30,171 |  |
| 3_PostDunningAR | 92.81% | 91.96% | +0.92% | 32,099 | 30,171 |  |
| 6_PaymentApprovalRate | 92.97% | 92.1% | +0.95% | 32,099 | 30,171 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 18,773 | 20,148 | +7.3% | Stable |
| CF | High (>92%) | 6,117 | 6,535 | +6.8% | Stable |
| YE | Medium (>85%) | 3,007 | 3,090 | +2.8% | Stable |
| TT | High (>92%) | 614 | 587 | -4.4% | Stable |
| TO | Medium (>85%) | 552 | 427 | -22.6% | ⚠️ Volume drop |
| TZ | Medium (>85%) | 477 | 582 | +22.0% | Stable |
| TV | Medium (>85%) | 334 | 331 | -0.9% | Stable |
| TK | High (>92%) | 297 | 399 | +34.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| YE | ↑ +2.78% | None -100.0% | Unknown -16.1% | Insufficient Funds -2.13pp | None + Unknown + Insufficient |
| TV | ↑ +5.21% | applepay +6.5% | Braintree +8.5% | Insufficient Funds -3.87pp | applepay + Braintree + Insufficient |
| TO | ↑ +5.50% | sepadirectdebit -100.0% | Adyen +7.7% | Insufficient Funds -2.43pp | sepadirectdebit + Adyen + Insufficient |

---

*Report: 2026-04-21*
