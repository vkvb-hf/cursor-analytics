# AR Initial (LL0) Investigation: RTE 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.85% → 91.78% (+1.02%)  
**Volume:** 31,091 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 90.85% to 91.78% (+1.02%) in W15, representing a significant positive change against a backdrop of declining volume (31,091 orders, down from 31,951).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate recovering after 3-week decline | +1.02% | ⚠️ |
| Country Variance | 4 countries exceed ±2.5% threshold | TV -5.75%, TT -3.25%, TZ +3.23%, TO +10.03% | ⚠️ |
| Payment Method | Credit Card improved +1.37%, Others declined -2.21% | Mixed | ✅ |
| Payment Provider | Adyen improved +2.15%, all providers stable or positive | Positive | ✅ |
| Related Metrics | All funnel metrics improved in parallel | +0.85% to +1.02% | ✅ |
| Mix Shift | No significant volume shifts impacting rate | Stable | ✅ |

**Key Findings:**
- **TO drove significant improvement:** +10.03% AR increase driven by credit_card (+11.4%) and Braintree (+9.7%) performance, with Insufficient Funds declines dropping by 6.10pp
- **TV experienced sharp decline:** -5.75% AR drop due to PayPal collapse (-32.5%) and Adyen issues (-6.2%), with Insufficient Funds increasing +3.03pp (volume: 375 orders)
- **TT declined via Braintree:** -3.25% AR drop linked to Braintree performance (-12.8%) and spike in "Other reasons" declines (+1.91pp)
- **TZ improved through Adyen:** +3.23% AR increase driven by credit_card and Adyen both improving +18.1%
- **Overall volume continues downward trend:** 8-week volume declined from 46,567 (W08) to 31,091 (W15), a 33% reduction

**Action:** **Monitor** - The overall metric improved significantly and all related funnel metrics moved in parallel. However, investigate TV's PayPal/Adyen performance and TT's Braintree issues as isolated concerns that could impact future weeks if not addressed.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.78% | 31,091 | +1.02% ← REPORTED CHANGE |
| 2026-W14 | 90.85% | 31,951 | -0.57% |
| 2026-W13 | 91.37% | 36,416 | -1.29% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.24% |
| 2026-W10 | 92.73% | 48,166 | -0.92% |
| 2026-W09 | 93.59% | 46,087 | +0.47% |
| 2026-W08 | 93.15% | 46,567 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 86.4% | 91.67% | -5.75% | 375 | ⚠️ |
| TT | 91.39% | 94.46% | -3.25% | 685 | ⚠️ |
| YE | 74.09% | 75.73% | -2.17% | 5,723 |  |
| FJ | 82.38% | 82.6% | -0.26% | 35,734 |  |
| CF | 85.96% | 84.89% | +1.26% | 7,864 |  |
| TZ | 86.09% | 83.4% | +3.23% | 539 | ⚠️ |
| TO | 75.22% | 68.36% | +10.03% | 686 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV, TT, TZ, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 95.89% | 98.06% | -2.21% | 1,023 |  |
| Paypal | 95.74% | 95.66% | +0.08% | 3,682 |  |
| Apple Pay | 90.8% | 90.02% | +0.87% | 6,957 |  |
| Credit Card | 91.16% | 89.93% | +1.37% | 19,429 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 78.64% | 79.17% | -0.66% | 103 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 40 |  |
| ProcessOut | 91.72% | 91.41% | +0.34% | 11,281 |  |
| Braintree | 92.48% | 91.68% | +0.88% | 10,759 |  |
| Adyen | 91.12% | 89.2% | +2.15% | 8,908 |  |

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 60.0% | 88.89% | -32.50% | 10 | 9 | ⚠️ |
| credit_card | 76.64% | 85.71% | -10.59% | 107 | 98 | ⚠️ |
| klarna | 96.47% | 99.01% | -2.56% | 170 | 202 |  |
| applepay | 80.72% | 82.47% | -2.12% | 83 | 97 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 5 | 2 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 88.81% | 94.67% | -6.19% | 277 | 300 | ⚠️ |
| Braintree | 78.49% | 83.02% | -5.45% | 93 | 106 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 5 | 2 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 324 | 374 | 86.40% | 91.67% | -5.27 |
| Insufficient Funds | 38 | 29 | 10.13% | 7.11% | +3.03 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 7 | 2 | 1.87% | 0.49% | +1.38 |
| Other reasons | 6 | 3 | 1.60% | 0.74% | +0.86 |

**Root Cause:** paypal + Adyen + Insufficient

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 9 | 0 |  |
| cashcredit | 100.0% | 0.0% | +0.00% | 1 | 0 |  |
| None | 0.0% | 14.29% | -100.00% | 0 | 7 | ⚠️ |
| sepadirectdebit | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| applepay | 76.79% | 89.83% | -14.52% | 56 | 59 | ⚠️ |
| paypal | 60.0% | 68.18% | -12.00% | 15 | 22 | ⚠️ |
| ideal | 97.6% | 100.0% | -2.40% | 500 | 533 |  |
| klarna | 85.25% | 87.27% | -2.32% | 61 | 55 |  |
| credit_card | 76.74% | 68.89% | +11.40% | 43 | 45 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 9 | 6 |  |
| Braintree | 73.24% | 83.95% | -12.76% | 71 | 81 | ⚠️ |
| Adyen | 94.87% | 96.69% | -1.88% | 604 | 634 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 626 | 682 | 91.39% | 94.46% | -3.07 |
| Other reasons | 15 | 2 | 2.19% | 0.28% | +1.91 |
| Unknown | 9 | 6 | 1.31% | 0.83% | +0.48 |
| Insufficient Funds | 16 | 14 | 2.34% | 1.94% | +0.40 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 19 | 18 | 2.77% | 2.49% | +0.28 |

**Root Cause:** None + Braintree + Other

---

## L2: TZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| applepay | 83.08% | 84.85% | -2.09% | 130 | 132 |  |
| paypal | 93.63% | 92.91% | +0.78% | 267 | 268 |  |
| credit_card | 74.65% | 63.24% | +18.05% | 142 | 136 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 90.18% | 90.25% | -0.08% | 397 | 400 |  |
| Adyen | 74.65% | 63.24% | +18.05% | 142 | 136 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 464 | 447 | 86.09% | 83.40% | +2.69 |
| Other reasons | 6 | 12 | 1.11% | 2.24% | -1.13 |
| Insufficient Funds | 41 | 46 | 7.61% | 8.58% | -0.98 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 28 | 31 | 5.19% | 5.78% | -0.59 |

**Root Cause:** credit_card + Adyen + Other

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 4 | 0 |  |
| sepadirectdebit | 100.0% | 0.0% | +0.00% | 2 | 0 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 3 | 6 |  |
| paypal | 93.62% | 90.32% | +3.65% | 94 | 93 |  |
| credit_card | 72.41% | 64.99% | +11.42% | 395 | 377 | ⚠️ |
| applepay | 72.87% | 62.09% | +17.36% | 188 | 153 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 4 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3 | 6 |  |
| Braintree | 79.79% | 72.76% | +9.65% | 282 | 246 | ⚠️ |
| Adyen | 72.54% | 64.99% | +11.63% | 397 | 377 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 516 | 430 | 75.22% | 68.36% | +6.86 |
| Insufficient Funds | 77 | 109 | 11.22% | 17.33% | -6.10 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 42 | 45 | 6.12% | 7.15% | -1.03 |
| Unknown | 4 | 0 | 0.58% | 0.00% | +0.58 |
| Other reasons | 47 | 45 | 6.85% | 7.15% | -0.30 |

**Root Cause:** credit_card + Braintree + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.3% | 88.45% | +0.96% | 31,091 | 31,951 |  |
| 2_PreDunningAR | 91.78% | 90.85% | +1.02% | 31,091 | 31,951 |  |
| 3_PostDunningAR | 91.99% | 91.21% | +0.86% | 31,091 | 31,951 |  |
| 6_PaymentApprovalRate | 92.15% | 91.37% | +0.85% | 31,091 | 31,951 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Low (>85%) | 38,808 | 35,734 | -7.9% | Stable |
| CF | Low (>85%) | 7,763 | 7,864 | +1.3% | Stable |
| YE | Low (>85%) | 6,365 | 5,723 | -10.1% | Stable |
| TT | High (>92%) | 722 | 685 | -5.1% | Stable |
| TO | Low (>85%) | 629 | 686 | +9.1% | Stable |
| TZ | Low (>85%) | 536 | 539 | +0.6% | Stable |
| TV | Medium (>85%) | 408 | 375 | -8.1% | Stable |
| TK | Medium (>85%) | 232 | 347 | +49.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↓ -5.75% | paypal -32.5% | Adyen -6.2% | Insufficient Funds +3.03pp | paypal + Adyen + Insufficient |
| TT | ↓ -3.25% | None -100.0% | Braintree -12.8% | Other reasons +1.91pp | None + Braintree + Other |
| TZ | ↑ +3.23% | credit_card +18.1% | Adyen +18.1% | Other reasons -1.13pp | credit_card + Adyen + Other |
| TO | ↑ +10.03% | credit_card +11.4% | Braintree +9.7% | Insufficient Funds -6.10pp | credit_card + Braintree + Insufficient |

---

*Report: 2026-04-15*
