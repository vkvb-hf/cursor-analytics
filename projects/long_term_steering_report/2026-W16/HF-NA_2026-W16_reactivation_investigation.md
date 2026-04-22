# Reactivation Investigation: HF-NA 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.24% → 89.41% (-0.92%)  
**Volume:** 23,973 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined from 90.24% to 89.41% (-0.92%) in W16, a statistically non-significant change within normal weekly fluctuation, primarily driven by CA's -2.57% decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (86.89%-91.02%) | -0.92% | ✅ |
| L1: Country Breakdown | CA exceeds ±2.5% threshold | CA: -2.57% | ⚠️ |
| L1: Dimension Scan | PaymentMethod stable (Others flagged but n=2) | Credit Card: -1.60% | ✅ |
| L2: CA Deep-Dive | Credit Card underperforming | -3.05% | ⚠️ |
| L2: Decline Reasons | "Others" dominant but declining; Fraud/Security rising | Others: -1.57pp | ⚠️ |
| Mix Shift | Volume distribution stable | US: -10.7%, CA: +1.1% | ✅ |

**Key Findings:**
- CA drove the overall decline with a -2.57% drop in reactivation rate (86.98% vs 89.27%), exceeding the ±2.5% threshold
- Within CA, Credit Card payments declined -3.05% (85.34% vs 88.02%) on volume of 3,942 orders
- Fraud, Lost/Stolen Card, Security decline reasons increased +0.88pp in CA (from 0.82% to 1.69%), representing a 110% increase in count (41 → 86)
- 3DS Authentication Failed/Required increased +0.33pp in CA (4 → 21 occurrences), a 5x increase
- US remained relatively stable at -0.44% with the majority of volume (18,897 orders)

**Action:** Monitor - The decline is not statistically significant and the 8-week trend shows W16 rate (89.41%) remains above W09-W11 levels. However, continue monitoring CA's Fraud/Security and 3DS authentication trends for potential emerging issues.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.41% | 23,973 | -0.92% ← REPORTED CHANGE |
| 2026-W15 | 90.24% | 26,178 | -0.78% |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | +1.54% |
| 2026-W09 | 86.89% | 23,884 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 86.98% | 89.27% | -2.57% | 5,076 | ⚠️ |
| US | 90.07% | 90.47% | -0.44% | 18,897 |  |

**Countries exceeding ±2.5% threshold:** CA

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.73% | 90.17% | -1.60% | 16,661 |  |
| Paypal | 92.99% | 92.78% | +0.23% | 3,767 |  |
| Apple Pay | 88.85% | 87.98% | +0.99% | 3,543 |  |
| Others | 50.0% | 28.57% | +75.00% | 2 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CA Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 0 | 3 |  |
| Credit Card | 85.34% | 88.02% | -3.05% | 3,942 | 3,857 |  |
| Paypal | 92.50% | 94.11% | -1.71% | 707 | 713 |  |
| Apple Pay | 92.97% | 92.89% | +0.09% | 427 | 450 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 4,566 | 4,597 | 89.95% | 91.52% | -1.57 |
| Fraud, Lost/Stolen Card, Security | 86 | 41 | 1.69% | 0.82% | +0.88 |
| Blocked, Restricted, Not Permitted | 95 | 73 | 1.87% | 1.45% | +0.42 |
| Expired, Invalid, Closed Card, No Account | 249 | 266 | 4.91% | 5.30% | -0.39 |
| 3DS Authentication Failed/Required | 21 | 4 | 0.41% | 0.08% | +0.33 |
| PayPal Declined, Revoked, Payer Issue | 47 | 30 | 0.93% | 0.60% | +0.33 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 5 | 0.02% | 0.10% | -0.08 |
| Call Issuer, Voice Auth Required | 5 | 3 | 0.10% | 0.06% | +0.04 |
| CVV/CVC Mismatch | 6 | 4 | 0.12% | 0.08% | +0.04 |

**Root Cause:** Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 21,155 | 18,897 | -10.7% | Stable |
| CA | Medium (>85%) | 5,023 | 5,076 | +1.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CA | ↓ -2.57% | → Stable | → Stable | Others -1.57pp | Others |

---

*Report: 2026-04-22*
