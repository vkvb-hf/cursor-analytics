# PAR Investigation: RTE 2026-W20

**Metric:** Payment Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 94.15% → 94.79% (+0.68%)  
**Volume:** 414,676 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate improved from 94.15% to 94.79% (+0.68%) in W20, a statistically non-significant increase within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.75% | ✅ |
| 2_PreDunningAR | Within normal range | +0.79% | ✅ |
| 3_PostDunningAR | Within normal range | +0.55% | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.68% | ✅ |

**Key Findings:**
- TK flagged with +2.69% improvement, driven by Apple Pay (+6.12%) and Braintree (+5.04%) performance gains
- Insufficient Funds declines in TK dropped significantly (-2.14pp), contributing to the country's rate improvement
- Unknown PaymentProvider shows +25.26% change but represents minimal volume (113 orders), not operationally significant
- All major countries (FJ, CF, YE) showed modest improvements between +0.22% and +1.35%
- Volume decreased 3.0% week-over-week (427,697 → 414,676) with no material mix shift impact

**Action:** Monitor – No action required. The improvement is positive but not statistically significant, and all funnel steps are performing within expected ranges.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 94.79% | 414,676 | +0.68% ← REPORTED CHANGE |
| 2026-W19 | 94.15% | 427,697 | -0.52% |
| 2026-W18 | 94.64% | 430,745 | -0.20% |
| 2026-W17 | 94.83% | 430,820 | +0.02% |
| 2026-W16 | 94.81% | 429,384 | -0.06% |
| 2026-W15 | 94.87% | 421,405 | +0.13% |
| 2026-W14 | 94.75% | 431,855 | -0.20% |
| 2026-W13 | 94.94% | 442,529 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CF | 95.15% | 94.94% | +0.22% | 52,629 |  |
| FJ | 95.42% | 94.93% | +0.51% | 375,016 |  |
| TT | 98.23% | 97.25% | +1.01% | 4,567 |  |
| YE | 93.97% | 92.72% | +1.35% | 44,478 |  |
| TO | 92.93% | 91.20% | +1.89% | 2,871 |  |
| TK | 95.54% | 93.03% | +2.69% | 1,949 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 97.59% | 97.41% | +0.18% | 53,613 |  |
| Others | 98.79% | 98.08% | +0.73% | 5,555 |  |
| Credit Card | 94.63% | 93.93% | +0.74% | 303,503 |  |
| Apple Pay | 92.46% | 91.74% | +0.78% | 52,005 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 597 |  |
| Braintree | 95.59% | 95.09% | +0.53% | 255,001 |  |
| Adyen | 93.69% | 92.88% | +0.87% | 75,585 |  |
| ProcessOut | 93.35% | 92.4% | +1.03% | 83,380 |  |
| Unknown | 70.8% | 56.52% | +25.26% | 113 | ⚠️ |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 8 | 15 |  |
| paypal | 95.76% | 94.49% | +1.35% | 118 | 127 |  |
| credit_card | 95.72% | 94.05% | +1.77% | 1,377 | 1,462 |  |
| applepay | 94.84% | 89.37% | +6.12% | 446 | 461 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 8 | 15 |  |
| Adyen | 95.72% | 94.05% | +1.77% | 1,377 | 1,462 |  |
| Braintree | 95.04% | 90.48% | +5.04% | 564 | 588 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,862 | 1,922 | 95.54% | 93.03% | +2.51 |
| Insufficient Funds | 47 | 94 | 2.41% | 4.55% | -2.14 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 18 | 26 | 0.92% | 1.26% | -0.33 |
| Unknown | 0 | 1 | 0.00% | 0.05% | -0.05 |
| Other reasons | 22 | 23 | 1.13% | 1.11% | +0.02 |

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
| YE | High (>92%) | 44,452 | 44,478 | +0.1% | Stable |
| TT | High (>92%) | 4,762 | 4,567 | -4.1% | Stable |
| TO | Medium (>85%) | 3,206 | 2,871 | -10.4% | Stable |
| TZ | High (>92%) | 3,154 | 2,937 | -6.9% | Stable |
| TK | High (>92%) | 2,066 | 1,949 | -5.7% | Stable |
| TV | High (>92%) | 1,961 | 1,823 | -7.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↑ +2.69% | applepay +6.1% | Braintree +5.0% | Insufficient Funds -2.14pp | applepay + Braintree + Insufficient |

---

*Report: 2026-05-19*
