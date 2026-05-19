# Reactivation Investigation: WL 2026-W20

**Metric:** Reactivation Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 88.73% → 89.41% (+0.77%)  
**Volume:** 7,570 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate improved from 88.73% to 89.41% (+0.77pp) in 2026-W20, a non-significant increase on volume of 7,570 orders, continuing a positive trend from the previous week.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (85.35%-89.41%) | +0.77pp | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (AO, CK) | AO +3.00pp, CK +7.54pp | ⚠️ |
| L1: PaymentMethod | 1 method flagged (Others) but minimal volume (3 orders) | Others -16.67pp | ✅ |
| L2: AO Deep-Dive | Improvement driven by PayPal (+4.96pp) and Credit Card (+2.20pp) | +3.00pp overall | ✅ |
| L2: CK Deep-Dive | Broad improvement across all payment methods | PayPal +6.62pp, Credit Card +7.69pp, Apple Pay +8.26pp | ✅ |
| Mix Shift | MR shows significant volume drop (-45.1%) | 1,613 → 885 orders | ⚠️ |

**Key Findings:**
- CK showed the largest improvement (+7.54pp) with gains across all payment methods, particularly Apple Pay (+8.26pp) and Credit Card (+7.69pp), driven by reduced "Expired, Invalid, Closed Card" declines (-2.54pp)
- AO improved +3.00pp with volume increasing significantly (+69.6%, from 161 to 273 orders), primarily from PayPal performance improvement (+4.96pp)
- MR experienced a substantial volume drop of -45.1% (1,613 → 885 orders), which may warrant monitoring despite rate stability
- The "Others" PaymentMethod decline (-16.67pp) is not actionable due to minimal volume (only 3 orders)
- Overall trend shows recovery toward the 8-week high of 89.41%, matching 2026-W15 levels (89.29%)

**Action:** Monitor - The improvement is positive but not statistically significant. Continue tracking CK and AO performance to confirm sustained improvement, and investigate the MR volume decline to ensure it's not indicative of a broader issue.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 89.41% | 7,570 | +0.77% ← REPORTED CHANGE |
| 2026-W19 | 88.73% | 9,047 | +2.57% |
| 2026-W18 | 86.51% | 7,436 | +1.36% |
| 2026-W17 | 85.35% | 7,827 | -1.68% |
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 89.28% | 90.85% | -1.73% | 429 |  |
| ER | 88.95% | 90.40% | -1.60% | 2,543 |  |
| CG | 90.25% | 91.16% | -1.00% | 1,149 |  |
| GN | 91.10% | 89.33% | +1.97% | 730 |  |
| AO | 90.84% | 88.20% | +3.00% | 273 | ⚠️ |
| CK | 89.43% | 83.16% | +7.54% | 1,561 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AO, CK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 66.67% | 80.0% | -16.67% | 3 | ⚠️ |
| Apple Pay | 73.52% | 74.11% | -0.80% | 676 |  |
| Credit Card | 90.35% | 89.6% | +0.84% | 5,474 |  |
| Paypal | 93.37% | 92.34% | +1.11% | 1,417 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 69.23% | 0.00% | +0.00% | 13 | 3 |  |
| Credit Card | 90.34% | 88.39% | +2.20% | 207 | 112 |  |
| Paypal | 98.11% | 93.48% | +4.96% | 53 | 46 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 13 | 5 | 4.76% | 3.11% | +1.66 |
| PayPal Declined, Revoked, Payer Issue | 1 | 3 | 0.37% | 1.86% | -1.50 |
| CVV/CVC Mismatch | 0 | 2 | 0.00% | 1.24% | -1.24 |
| Others | 256 | 150 | 93.77% | 93.17% | +0.61 |
| Blocked, Restricted, Not Permitted | 3 | 1 | 1.10% | 0.62% | +0.48 |

**Root Cause:** Expired,

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| Paypal | 94.91% | 89.02% | +6.62% | 216 | 264 | ⚠️ |
| Credit Card | 88.79% | 82.45% | +7.69% | 1,258 | 1,339 | ⚠️ |
| Apple Pay | 85.06% | 78.57% | +8.26% | 87 | 112 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,452 | 1,502 | 93.02% | 87.53% | +5.49 |
| Expired, Invalid, Closed Card, No Account | 75 | 126 | 4.80% | 7.34% | -2.54 |
| Blocked, Restricted, Not Permitted | 17 | 57 | 1.09% | 3.32% | -2.23 |
| PayPal Declined, Revoked, Payer Issue | 10 | 21 | 0.64% | 1.22% | -0.58 |
| Fraud, Lost/Stolen Card, Security | 6 | 9 | 0.38% | 0.52% | -0.14 |
| Call Issuer, Voice Auth Required | 1 | 1 | 0.06% | 0.06% | +0.01 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,937 | 2,543 | -13.4% | Stable |
| CK | Low (>85%) | 1,716 | 1,561 | -9.0% | Stable |
| MR | Medium (>85%) | 1,613 | 885 | -45.1% | ⚠️ Volume drop |
| CG | Medium (>85%) | 1,358 | 1,149 | -15.4% | Stable |
| GN | Medium (>85%) | 825 | 730 | -11.5% | Stable |
| KN | Medium (>85%) | 437 | 429 | -1.8% | Stable |
| AO | Medium (>85%) | 161 | 273 | +69.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↑ +3.00% | → Stable | → Stable | Expired, Invalid, Closed Card, No Account +1.66pp | Expired, |
| CK | ↑ +7.54% | Paypal +6.6% | → Stable | Others +5.49pp | Paypal + Others |

---

*Report: 2026-05-19*
