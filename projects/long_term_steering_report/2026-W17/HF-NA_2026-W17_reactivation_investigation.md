# Reactivation Investigation: HF-NA 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.41% → 90.35% (+1.05%)  
**Volume:** 20,799 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate improved from 89.41% to 90.35% (+1.05pp) in W17, returning to levels consistent with the 8-week historical range (88.23%-91.02%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Trend | Within historical range | +1.05pp | ✅ |
| L1: Country Breakdown | CA exceeded ±2.5% threshold | +5.79pp | ⚠️ |
| L1: Dimension Scan | Others payment method flagged (low volume) | -33.33% | ✅ |
| L2: CA Deep-Dive | Credit Card improvement identified | +7.29pp | ⚠️ |
| Mix Shift | US volume dropped 20.3%, CA volume grew 13.0% | - | ⚠️ |

**Key Findings:**
- CA drove the overall improvement with a +5.79pp increase (86.98% → 92.02%), while US slightly declined by -0.40pp
- Credit Card reactivations in CA improved significantly by +7.29pp (85.34% → 91.56%) on volume of 4,348 orders
- Decline reason "Others" increased to 93.92% of CA declines (+3.96pp), while fraud-related declines dropped from 1.69% to 0.31% (-1.38pp)
- US volume decreased by 20.3% (18,897 → 15,063) while CA volume increased by 13.0% (5,076 → 5,736)
- 3DS Authentication failures in CA dropped from 21 to 0 cases (-0.41pp)

**Action:** Monitor — The improvement is positive and driven by identifiable factors (Credit Card performance in CA). Continue monitoring US volume trends and CA performance stability in W18.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 90.35% | 20,799 | +1.05% ← REPORTED CHANGE |
| 2026-W16 | 89.41% | 23,973 | -0.92% |
| 2026-W15 | 90.24% | 26,178 | -0.78% |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.71% | 90.07% | -0.40% | 15,063 |  |
| CA | 92.02% | 86.98% | +5.79% | 5,736 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CA

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 33.33% | 50.0% | -33.33% | 3 | ⚠️ |
| Paypal | 92.31% | 92.99% | -0.73% | 3,342 |  |
| Apple Pay | 88.93% | 88.85% | +0.09% | 3,045 |  |
| Credit Card | 90.2% | 88.73% | +1.66% | 14,409 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CA Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| Apple Pay | 92.89% | 92.97% | -0.09% | 577 | 427 |  |
| Paypal | 94.07% | 92.50% | +1.69% | 809 | 707 |  |
| Credit Card | 91.56% | 85.34% | +7.29% | 4,348 | 3,942 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 5,387 | 4,566 | 93.92% | 89.95% | +3.96 |
| Fraud, Lost/Stolen Card, Security | 18 | 86 | 0.31% | 1.69% | -1.38 |
| Expired, Invalid, Closed Card, No Account | 218 | 249 | 3.80% | 4.91% | -1.10 |
| Blocked, Restricted, Not Permitted | 67 | 95 | 1.17% | 1.87% | -0.70 |
| 3DS Authentication Failed/Required | 0 | 21 | 0.00% | 0.41% | -0.41 |
| PayPal Declined, Revoked, Payer Issue | 40 | 47 | 0.70% | 0.93% | -0.23 |
| Call Issuer, Voice Auth Required | 0 | 5 | 0.00% | 0.10% | -0.10 |
| CVV/CVC Mismatch | 5 | 6 | 0.09% | 0.12% | -0.03 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 1 | 0.02% | 0.02% | +0.00 |

**Root Cause:** Credit + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 18,897 | 15,063 | -20.3% | ⚠️ Volume drop |
| CA | Medium (>85%) | 5,076 | 5,736 | +13.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CA | ↑ +5.79% | Credit Card +7.3% | → Stable | Others +3.96pp | Credit + Others |

---

*Report: 2026-04-27*
