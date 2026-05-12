# PAR Investigation: RTE 2026-W19

**Metric:** Payment Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 94.65% → 94.15% (-0.53%)  
**Volume:** 427,697 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate declined modestly from 94.65% to 94.15% (-0.50pp) in W19, representing a statistically non-significant change across 427,697 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Gradual decline from 95.18% (W12) to 94.15% (W19) | -1.03pp over 8 weeks | ⚠️ |
| L1: Country Scan | TV flagged at +2.87% (positive); no major negative outliers | Within threshold | ✅ |
| L1: Dimension Scan | Unknown PaymentProvider +31.43% but negligible volume (119) | Low impact | ✅ |
| L2: TV Deep-Dive | credit_card +5.09%, applepay +5.43% (improvements) | Positive movement | ✅ |
| L3: Related Metrics | All funnel stages declined ~0.6pp consistently | Aligned decline | ⚠️ |

**Key Findings:**
- The -0.53% WoW decline continues a gradual 8-week downward trend from 95.18% (W12) to 94.15% (W19), representing cumulative erosion of -1.03pp
- TV showed the only flagged country movement at +2.87%, driven by improved credit_card (+5.09pp) and applepay (+5.43pp) approval rates, with "Insufficient Funds" declines dropping by -2.74pp
- All funnel metrics (FirstRunAR through PaymentApprovalRate) declined consistently by ~0.59-0.67pp, indicating a systemic upstream issue rather than isolated failure point
- YE showed the largest negative country movement at -0.92pp but remained below the ±2.5% flag threshold
- Mix shift analysis shows stable volume distribution across all countries with no significant tier migrations

**Action:** Monitor - The decline is not statistically significant, the flagged country (TV) shows improvement rather than degradation, and no single root cause requires immediate intervention. Continue tracking the gradual 8-week trend for potential pattern development.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 94.15% | 427,697 | -0.53% ← REPORTED CHANGE |
| 2026-W18 | 94.65% | 430,745 | -0.19% |
| 2026-W17 | 94.83% | 430,820 | +0.02% |
| 2026-W16 | 94.81% | 429,384 | -0.06% |
| 2026-W15 | 94.87% | 421,405 | +0.13% |
| 2026-W14 | 94.75% | 431,855 | -0.20% |
| 2026-W13 | 94.94% | 442,529 | -0.25% |
| 2026-W12 | 95.18% | 443,993 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| YE | 92.73% | 93.60% | -0.92% | 44,452 |  |
| FJ | 94.93% | 95.40% | -0.49% | 392,524 |  |
| CF | 94.94% | 95.11% | -0.17% | 53,720 |  |
| TK | 93.03% | 91.97% | +1.15% | 2,066 |  |
| TO | 91.20% | 89.95% | +1.39% | 3,206 |  |
| TV | 94.75% | 92.11% | +2.87% | 1,961 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 91.74% | 92.54% | -0.87% | 54,675 |  |
| Credit Card | 93.93% | 94.44% | -0.53% | 312,610 |  |
| Paypal | 97.42% | 97.69% | -0.28% | 54,684 |  |
| Others | 98.08% | 97.16% | +0.95% | 5,728 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 92.41% | 92.93% | -0.57% | 84,879 |  |
| Braintree | 95.09% | 95.6% | -0.54% | 264,430 |  |
| Adyen | 92.88% | 93.23% | -0.37% | 77,693 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 576 |  |
| Unknown | 57.98% | 44.12% | +31.43% | 119 | ⚠️ |

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| paypal | 91.23% | 91.67% | -0.48% | 57 | 60 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 29 | 21 |  |
| klarna | 98.47% | 97.97% | +0.52% | 786 | 787 |  |
| credit_card | 94.04% | 89.48% | +5.09% | 738 | 770 | ⚠️ |
| applepay | 88.29% | 83.74% | +5.43% | 350 | 326 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 29 | 21 |  |
| Adyen | 96.33% | 93.77% | +2.73% | 1,524 | 1,557 |  |
| Braintree | 88.70% | 84.97% | +4.38% | 407 | 386 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 64 | 118 | 3.26% | 6.01% | -2.74 |
| 1. SUCCESSFULL | 1,858 | 1,809 | 94.75% | 92.11% | +2.64 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 29 | 26 | 1.48% | 1.32% | +0.16 |
| Other reasons | 9 | 11 | 0.46% | 0.56% | -0.10 |
| Unknown | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** credit_card + Insufficient

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
| YE | High (>92%) | 45,256 | 44,452 | -1.8% | Stable |
| TT | High (>92%) | 4,511 | 4,762 | +5.6% | Stable |
| TO | Medium (>85%) | 3,214 | 3,206 | -0.2% | Stable |
| TZ | High (>92%) | 3,134 | 3,154 | +0.6% | Stable |
| TK | Medium (>85%) | 2,017 | 2,066 | +2.4% | Stable |
| TV | High (>92%) | 1,964 | 1,961 | -0.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↑ +2.87% | credit_card +5.1% | → Stable | Insufficient Funds -2.74pp | credit_card + Insufficient |

---

*Report: 2026-05-12*
