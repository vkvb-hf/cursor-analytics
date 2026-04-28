# PCAR Investigation: RTE 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.2% → 97.05% (-0.15%)  
**Volume:** 42,589 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 97.2% to 97.05% (-0.15pp) in W17, a change that is **not statistically significant** against a volume of 42,589 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (96.88%-97.22%) | -0.15pp | ✅ |
| L1: Country Scan | TT exceeds ±2.5% threshold | -5.00pp | ⚠️ |
| L1: Dimension Scan | Others PaymentMethod flagged | -5.03pp | ⚠️ |
| L2: TT Deep-Dive | IDeal + Adyen identified as root cause | -8.16pp / -5.93pp | ⚠️ |
| Mix Shift | TT volume dropped 39.1% | -478 orders | ⚠️ |

**Key Findings:**
- TT is the only country exceeding the ±2.5% threshold, declining from 80.54% to 76.51% (-5.00pp)
- Root cause identified as **IDeal + Adyen** combination in TT: IDeal declined -8.16pp (576 orders), Adyen declined -5.93pp (694 orders)
- TT volume dropped significantly by 39.1% (from 1,223 to 745 orders), reducing overall impact on global rate
- Decline reasons in TT show no meaningful shift—99.87% categorized as "Others" with no specific failure pattern
- Global impact is contained due to TT's small volume share (1.7% of total orders)

**Action:** **Monitor** — The overall change is not significant and TT's declining volume naturally limits impact. Continue monitoring IDeal/Adyen performance in TT for W18; escalate only if pattern persists or volume recovers while rate remains depressed.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 97.05% | 42,589 | -0.15% ← REPORTED CHANGE |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TT | 76.51% | 80.54% | -5.00% | 745 | ⚠️ |
| TZ | 96.17% | 98.12% | -1.99% | 496 |  |
| TK | 98.92% | 100.00% | -1.08% | 277 |  |
| CF | 98.03% | 98.61% | -0.59% | 5,929 |  |
| FJ | 97.45% | 97.69% | -0.25% | 30,705 |  |
| YE | 97.53% | 97.20% | +0.34% | 3,649 |  |

**Countries exceeding ±2.5% threshold:** TT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 73.89% | 77.8% | -5.03% | 877 | ⚠️ |
| Apple Pay | 96.81% | 97.42% | -0.62% | 10,314 |  |
| Paypal | 97.97% | 98.31% | -0.34% | 5,126 |  |
| Credit Card | 97.74% | 97.87% | -0.13% | 26,272 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| IDeal | 75.00% | 81.67% | -8.16% | 576 | 1,009 | ⚠️ |
| CreditCard | 95.00% | 100.00% | -5.00% | 40 | 41 |  |
| ApplePay | 100.00% | 98.28% | +1.75% | 36 | 58 |  |
| Paypal | 100.00% | 92.86% | +7.69% | 15 | 14 | ⚠️ |
| Klarna | 62.82% | 49.50% | +26.90% | 78 | 101 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 74.78% | 79.50% | -5.93% | 694 | 1,151 | ⚠️ |
| Braintree | 100.00% | 97.22% | +2.86% | 51 | 72 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.13% | 0.00% | +0.13 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.08% | -0.08 |
| Others | 744 | 1,222 | 99.87% | 99.92% | -0.05 |

**Root Cause:** IDeal + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 30,779 | 30,705 | -0.2% | Stable |
| CF | High (>92%) | 6,546 | 5,929 | -9.4% | Stable |
| YE | High (>92%) | 3,713 | 3,649 | -1.7% | Stable |
| TT | Low (>85%) | 1,223 | 745 | -39.1% | ⚠️ Volume drop |
| TZ | High (>92%) | 585 | 496 | -15.2% | Stable |
| TO | High (>92%) | 499 | 400 | -19.8% | Stable |
| TV | Medium (>85%) | 426 | 388 | -8.9% | Stable |
| TK | High (>92%) | 340 | 277 | -18.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TT | ↓ -5.00% | IDeal -8.2% | Adyen -5.9% | → Stable | IDeal + Adyen |

---

*Report: 2026-04-28*
