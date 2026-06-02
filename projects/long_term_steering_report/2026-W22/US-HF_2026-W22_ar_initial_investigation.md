# AR Initial (LL0) Investigation: US-HF 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 86.57% → 85.43% (-1.32%)  
**Volume:** 9,995 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF Initial Charges declined from 86.57% to 85.43% (-1.14 pp) in 2026-W22, continuing a 7-week downward trend from 89.64% in W15.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | -1.10% | ⚠️ |
| 2_PreDunningAR | Before retry logic | -1.31% | ⚠️ |
| 3_PostDunningAR | After retry logic | -1.93% | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -2.18% | ⚠️ |

**Key Findings:**
- **Sustained decline:** The Pre-Dunning AR has dropped 4.21 pp over 7 weeks (89.64% → 85.43%), indicating a systemic issue rather than a one-week anomaly
- **Payment method degradation:** "Others" payment method declined -4.54% (267 vol) and Credit Card declined -2.51% (5,535 vol), while PayPal improved +3.85%
- **Unknown provider issue:** The "Unknown" payment provider shows a significant -14.00% decline, though volume is low (110 orders)
- **Funnel-wide impact:** All related metrics are declining, with PaymentApprovalRate showing the largest drop (-2.18%), suggesting issues are compounding through the funnel
- **No country threshold breach:** US is the only market and did not exceed the ±2.5% threshold for individual week-over-week change

**Action:** **Investigate** – The persistent 7-week declining trend combined with Credit Card and Unknown provider degradation warrants deeper investigation into payment processing issues, particularly with ProcessOut (-2.22%) and the Unknown provider segment.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 85.43% | 9,995 | -1.32% ← REPORTED CHANGE |
| 2026-W21 | 86.57% | 9,714 | -1.30% |
| 2026-W20 | 87.71% | 10,719 | -0.44% |
| 2026-W19 | 88.1% | 10,605 | -0.32% |
| 2026-W18 | 88.38% | 10,808 | -0.74% |
| 2026-W17 | 89.04% | 12,934 | +0.36% |
| 2026-W16 | 88.72% | 12,335 | -1.03% |
| 2026-W15 | 89.64% | 11,009 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 85.43% | 86.57% | -1.31% | 9,995 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 86.52% | 90.64% | -4.54% | 267 | ⚠️ |
| Credit Card | 86.38% | 88.6% | -2.51% | 5,535 | ⚠️ |
| Apple Pay | 83.36% | 83.5% | -0.17% | 3,395 |  |
| Paypal | 87.34% | 84.11% | +3.85% | 798 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 67.27% | 78.23% | -14.00% | 110 | ⚠️ |
| ProcessOut | 86.6% | 88.56% | -2.22% | 5,388 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 79 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 77 |  |
| Braintree | 83.92% | 83.78% | +0.17% | 4,341 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 84.52% | 85.46% | -1.10% | 9,995 | 9,714 |  |
| 2_PreDunningAR | 85.43% | 86.57% | -1.31% | 9,995 | 9,714 |  |
| 3_PostDunningAR | 85.48% | 87.16% | -1.93% | 9,995 | 9,714 |  |
| 6_PaymentApprovalRate | 85.49% | 87.4% | -2.18% | 9,995 | 9,714 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 9,714 | 9,995 | +2.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
