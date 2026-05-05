# PCAR Investigation: RTE 2026-W18

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 97.05% → 96.52% (-0.55%)  
**Volume:** 40,202 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 97.05% to 96.52% (-0.53pp) in W18, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (96.52% vs 96.88-97.22% baseline) | -0.55% | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (TO, TV) | TO -5.64%, TV -4.00% | ⚠️ |
| L1: Dimension Scan | No payment methods exceed threshold | Max: Others -1.01% | ✅ |
| L2: TO Deep-Dive | CreditCard + Adyen identified as root cause | -9.07% | ⚠️ |
| L2: TV Deep-Dive | Klarna + Adyen identified as root cause | Klarna -8.34%, Adyen -5.66% | ⚠️ |
| Mix Shift | All countries stable, no significant volume shifts | - | ✅ |

**Key Findings:**
- TO experienced a significant approval rate drop of -5.64pp (97.75% → 92.23%), driven by CreditCard transactions via Adyen declining -9.07pp (97.52% → 88.67%) on 256 orders
- TV declined -4.00pp (84.79% → 81.40%), with Klarna payments dropping -8.34pp (74.31% → 68.12%) on 207 orders, also linked to Adyen provider issues
- Both affected countries have low volume (TO: 412 orders, TV: 371 orders), representing only 1.9% of total weekly volume (40,202 orders)
- Decline reasons in TO show a slight increase in "3DS Authentication Failed/Required" (+0.96pp) and "Fraud, Lost/Stolen Card, Security" (+0.48pp)
- Overall metric change is not statistically significant, and the 8-week trend shows the rate remains within historical range (96.88%-97.22%)

**Action:** Monitor - The overall decline is not statistically significant and is isolated to two low-volume markets (TO, TV) representing <2% of orders. Continue monitoring Adyen performance in these regions for W19. If the pattern persists or spreads to higher-volume markets (FJ, CF), escalate to payments team for Adyen investigation.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 96.52% | 40,202 | -0.55% ← REPORTED CHANGE |
| 2026-W17 | 97.05% | 42,589 | -0.15% |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 92.23% | 97.75% | -5.64% | 412 | ⚠️ |
| TV | 81.40% | 84.79% | -4.00% | 371 | ⚠️ |
| YE | 96.23% | 97.53% | -1.33% | 3,291 |  |
| CF | 97.31% | 98.03% | -0.73% | 5,977 |  |
| FJ | 97.19% | 97.45% | -0.27% | 28,528 |  |
| TT | 77.34% | 76.51% | +1.09% | 843 |  |

**Countries exceeding ±2.5% threshold:** TO, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 73.15% | 73.89% | -1.01% | 957 |  |
| Credit Card | 96.9% | 97.74% | -0.86% | 25,373 |  |
| Paypal | 98.14% | 97.97% | +0.17% | 4,569 |  |
| Apple Pay | 97.07% | 96.81% | +0.26% | 9,303 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 88.67% | 97.52% | -9.07% | 256 | 242 | ⚠️ |
| ApplePay | 96.55% | 98.85% | -2.33% | 87 | 87 |  |
| Paypal | 100.00% | 97.18% | +2.90% | 69 | 71 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 88.67% | 97.52% | -9.07% | 256 | 242 | ⚠️ |
| Braintree | 98.08% | 98.10% | -0.02% | 156 | 158 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 3DS Authentication Failed/Required | 6 | 2 | 1.46% | 0.50% | +0.96 |
| Others | 403 | 395 | 97.82% | 98.75% | -0.93 |
| PayPal Declined, Revoked, Payer Issue | 0 | 2 | 0.00% | 0.50% | -0.50 |
| Fraud, Lost/Stolen Card, Security | 3 | 1 | 0.73% | 0.25% | +0.48 |

**Root Cause:** CreditCard + Adyen

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 68.12% | 74.31% | -8.34% | 207 | 218 | ⚠️ |
| CreditCard | 97.65% | 98.85% | -1.22% | 85 | 87 |  |
| ApplePay | 98.59% | 98.70% | -0.11% | 71 | 77 |  |
| Paypal | 100.00% | 83.33% | +20.00% | 8 | 6 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 76.71% | 81.31% | -5.66% | 292 | 305 | ⚠️ |
| Braintree | 98.73% | 97.59% | +1.17% | 79 | 83 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 371 | 386 | 100.00% | 99.48% | +0.52 |
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 0.26% | -0.26 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.26% | -0.26 |

**Root Cause:** Klarna + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 30,705 | 28,528 | -7.1% | Stable |
| CF | High (>92%) | 5,929 | 5,977 | +0.8% | Stable |
| YE | High (>92%) | 3,649 | 3,291 | -9.8% | Stable |
| TT | Low (>85%) | 745 | 843 | +13.2% | Stable |
| TZ | High (>92%) | 496 | 456 | -8.1% | Stable |
| TO | High (>92%) | 400 | 412 | +3.0% | Stable |
| TV | Low (>85%) | 388 | 371 | -4.4% | Stable |
| TK | High (>92%) | 277 | 324 | +17.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -5.64% | CreditCard -9.1% | Adyen -9.1% | → Stable | CreditCard + Adyen |
| TV | ↓ -4.00% | Klarna -8.3% | Adyen -5.7% | → Stable | Klarna + Adyen |

---

*Report: 2026-05-05*
