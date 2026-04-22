# Reactivation Investigation: RTE 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 90.41% → 89.16% (-1.38%)  
**Volume:** 18,508 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate declined from 90.41% to 89.16% (-1.38%) in W16, representing a reversal of the prior week's gains but remaining within the upward trend observed since W09 (84.48%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate dropped after 6 weeks of improvement | -1.25pp | ⚠️ |
| L1: Country Breakdown | 5 countries exceed ±2.5% threshold (TO, TT, YE, TZ, TV) | Mixed | ⚠️ |
| L1: Dimension Scan | PaymentMethod "Others" flagged at +2.78% | +2.78% | ⚠️ |
| L2: TO Deep-Dive | "Others" payment method dropped -33.33%, Expired card issues +11.11pp | -11.11% | ⚠️ |
| L2: TT Deep-Dive | Credit Card dropped -25.00%, Expired card issues +3.03pp | -6.70% | ⚠️ |
| L2: YE Deep-Dive | Credit Card improved +5.52%, positive contributor | +3.60% | ✅ |
| L2: TZ Deep-Dive | Apple Pay improved +33.33%, small volume (19 orders) | +6.67% | ✅ |
| Mix Shift | YE volume dropped -38.0%, TV dropped -33.3% | Volume shift | ⚠️ |

**Key Findings:**
- TO experienced the largest rate decline (-11.11%), driven by "Others" payment method failure (-33.33%) and a new emergence of "Expired, Invalid, Closed Card" decline reasons (+11.11pp), though volume remains very low (18 orders)
- TT declined -6.70% due to Credit Card performance dropping from 100% to 75%, with new Expired Card issues appearing (+3.03pp)
- YE showed positive improvement (+3.60%) driven by Credit Card gains (+5.52%), partially offsetting declines elsewhere, despite a -38.0% volume drop
- The overall decline is concentrated in low-volume markets (TO: 18 orders, TT: 33 orders), while the largest market FJ (16,241 orders, 87.7% of volume) remained relatively stable (+1.30%)
- Expired/Invalid Card issues emerged as a new decline reason in both TO and TT, suggesting potential card lifecycle issues in these markets

**Action:** Monitor - The decline is driven primarily by low-volume markets (TO, TT combined = 51 orders, 0.3% of total volume). The dominant market FJ shows stable performance. Continue monitoring for 1-2 weeks to determine if Expired Card issues spread to higher-volume markets.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | +1.36% ← REPORTED CHANGE |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | +0.75% |
| 2026-W09 | 84.48% | 24,364 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 88.89% | 100.00% | -11.11% | 18 | ⚠️ |
| TT | 90.91% | 97.44% | -6.70% | 33 | ⚠️ |
| CF | 91.42% | 92.52% | -1.19% | 2,029 |  |
| FJ | 90.36% | 89.20% | +1.30% | 16,241 |  |
| YE | 89.45% | 86.35% | +3.60% | 1,403 | ⚠️ |
| TZ | 100.00% | 93.75% | +6.67% | 19 | ⚠️ |
| TV | 91.67% | 83.33% | +10.00% | 12 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TO, TT, YE, TZ, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 68.62% | 69.66% | -1.50% | 1,893 |  |
| Paypal | 93.4% | 92.54% | +0.92% | 3,241 |  |
| Credit Card | 92.71% | 91.26% | +1.59% | 14,461 |  |
| Others | 80.25% | 78.08% | +2.78% | 162 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 66.67% | 0.00% | +0.00% | 3 | 0 |  |
| Others | 66.67% | 100.00% | -33.33% | 3 | 1 | ⚠️ |
| Credit Card | 100.00% | 100.00% | +0.00% | 8 | 2 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 4 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 2 | 0 | 11.11% | 0.00% | +11.11 |
| Others | 16 | 6 | 88.89% | 100.00% | -11.11 |

**Root Cause:** Others + Expired,

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 75.00% | 100.00% | -25.00% | 8 | 8 | ⚠️ |
| Others | 95.24% | 96.15% | -0.95% | 21 | 26 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 4 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 3.03% | 0.00% | +3.03 |
| Others | 32 | 39 | 96.97% | 100.00% | -3.03 |

**Root Cause:** Credit + Expired,

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 94.03% | 93.79% | +0.26% | 402 | 676 |  |
| Others | 82.69% | 79.62% | +3.86% | 156 | 265 |  |
| Credit Card | 88.52% | 83.89% | +5.52% | 845 | 1,322 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,293 | 2,046 | 92.16% | 90.41% | +1.75 |
| Expired, Invalid, Closed Card, No Account | 54 | 110 | 3.85% | 4.86% | -1.01 |
| PayPal Declined, Revoked, Payer Issue | 16 | 36 | 1.14% | 1.59% | -0.45 |
| Blocked, Restricted, Not Permitted | 37 | 68 | 2.64% | 3.00% | -0.37 |
| CVV/CVC Mismatch | 3 | 1 | 0.21% | 0.04% | +0.17 |
| Fraud, Lost/Stolen Card, Security | 0 | 2 | 0.00% | 0.09% | -0.09 |

**Root Cause:** Credit + Others

---

## L2: TZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 100.00% | 100.00% | +0.00% | 7 | 3 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 8 | 9 |  |
| Apple Pay | 100.00% | 75.00% | +33.33% | 4 | 4 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 19 | 16 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Apple

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 13,089 | 16,241 | +24.1% | Stable |
| YE | Medium (>85%) | 2,263 | 1,403 | -38.0% | ⚠️ Volume drop |
| CF | High (>92%) | 1,832 | 2,029 | +10.8% | Stable |
| TT | High (>92%) | 39 | 33 | -15.4% | Stable |
| TV | Low (>85%) | 18 | 12 | -33.3% | ⚠️ Volume drop |
| TZ | High (>92%) | 16 | 19 | +18.8% | Stable |
| TO | High (>92%) | 6 | 18 | +200.0% | Stable |
| TK | High (>92%) | 1 | 2 | +100.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -11.11% | Others -33.3% | → Stable | Expired, Invalid, Closed Card, No Account +11.11pp | Others + Expired, |
| TT | ↓ -6.70% | Credit Card -25.0% | → Stable | Expired, Invalid, Closed Card, No Account +3.03pp | Credit + Expired, |
| YE | ↑ +3.60% | Credit Card +5.5% | → Stable | Others +1.75pp | Credit + Others |
| TZ | ↑ +6.67% | Apple Pay +33.3% | → Stable | → Stable | Apple |

---

*Report: 2026-04-22*
