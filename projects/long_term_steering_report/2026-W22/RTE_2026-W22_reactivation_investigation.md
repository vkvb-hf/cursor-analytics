# Reactivation Investigation: RTE 2026-W22

**Metric:** Reactivation Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 89.38% → 89.71% (+0.37%)  
**Volume:** 19,183 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate improved marginally from 89.38% to 89.71% (+0.37pp) in W22 with 19,183 orders, though the change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend since W18 | +0.37pp | ✅ |
| L1: Country Breakdown | 4 countries flagged (TZ, TT, TO, TV) | Mixed | ⚠️ |
| L1: Dimension Scan | "Others" PaymentMethod declined | -5.92pp | ⚠️ |
| L2: Deep-Dives | Low-volume fluctuations identified | Variable | ✅ |
| Mix Shift Analysis | All countries stable impact | No concern | ✅ |

**Key Findings:**
- TZ experienced a -3.70pp decline (96.30% → 100.00% prior) driven by Credit Card failures (-14.29pp) with CVV/CVC Mismatch appearing as a new decline reason (+3.70pp share)
- TO showed strong improvement (+15.79pp) with 100% reactivation rate this week, though Apple Pay volume dropped to 0 orders from 2 prior
- TT improved +3.94pp despite PayPal declining -33.33pp (66.67% vs 100.00%), offset by Credit Card surge (+85.71pp)
- TV improved +40.00pp but with extremely low volume (15 orders), making the change statistically unreliable
- All flagged countries have very low volumes (15-62 orders), limiting the business impact of observed fluctuations

**Action:** Monitor - The overall metric shows continued stability within normal operating range. Low-volume country fluctuations are expected and do not warrant escalation.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 89.71% | 19,183 | +0.37% ← REPORTED CHANGE |
| 2026-W21 | 89.38% | 17,485 | +0.12% |
| 2026-W20 | 89.27% | 18,697 | +0.29% |
| 2026-W19 | 89.01% | 20,405 | +2.26% |
| 2026-W18 | 87.04% | 19,909 | -0.33% |
| 2026-W17 | 87.33% | 19,371 | -2.05% |
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TZ | 96.30% | 100.00% | -3.70% | 27 | ⚠️ |
| YE | 87.50% | 88.50% | -1.13% | 2,792 |  |
| CF | 91.83% | 92.42% | -0.64% | 2,570 |  |
| FJ | 89.71% | 89.09% | +0.70% | 13,682 |  |
| TT | 93.55% | 90.00% | +3.94% | 62 | ⚠️ |
| TO | 100.00% | 86.36% | +15.79% | 25 | ⚠️ |
| TV | 93.33% | 66.67% | +40.00% | 15 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TZ, TT, TO, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 72.55% | 77.11% | -5.92% | 306 | ⚠️ |
| Paypal | 93.01% | 93.45% | -0.47% | 3,361 |  |
| Credit Card | 91.88% | 91.38% | +0.54% | 13,850 |  |
| Apple Pay | 68.25% | 67.62% | +0.93% | 1,666 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 85.71% | 100.00% | -14.29% | 7 | 6 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 5 | 4 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 15 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| CVV/CVC Mismatch | 1 | 0 | 3.70% | 0.00% | +3.70 |
| Others | 26 | 15 | 96.30% | 100.00% | -3.70 |

**Root Cause:** Credit + CVV/CVC

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 66.67% | 100.00% | -33.33% | 3 | 3 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 4 | 2 |  |
| Others | 95.12% | 92.31% | +3.05% | 41 | 13 |  |
| Credit Card | 92.86% | 50.00% | +85.71% | 14 | 2 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 61 | 20 | 98.39% | 100.00% | -1.61 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 1.61% | 0.00% | +1.61 |

**Root Cause:** Paypal + Others

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 0.00% | 100.00% | -100.00% | 0 | 2 | ⚠️ |
| Credit Card | 100.00% | 88.89% | +12.50% | 12 | 9 | ⚠️ |
| Paypal | 100.00% | 87.50% | +14.29% | 5 | 8 | ⚠️ |
| Others | 100.00% | 66.67% | +50.00% | 8 | 3 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 25 | 21 | 100.00% | 95.45% | +4.55 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 4.55% | -4.55 |

**Root Cause:** Apple + Others

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Apple Pay | 80.00% | 100.00% | -20.00% | 5 | 1 | ⚠️ |
| Credit Card | 100.00% | 100.00% | +0.00% | 4 | 2 |  |
| Others | 100.00% | 33.33% | +200.00% | 5 | 3 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 15 | 6 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Apple

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 12,709 | 13,682 | +7.7% | Stable |
| YE | Medium (>85%) | 2,705 | 2,792 | +3.2% | Stable |
| CF | High (>92%) | 2,006 | 2,570 | +28.1% | Stable |
| TO | Medium (>85%) | 22 | 25 | +13.6% | Stable |
| TT | Medium (>85%) | 20 | 62 | +210.0% | Stable |
| TZ | High (>92%) | 15 | 27 | +80.0% | Stable |
| TV | Low (>85%) | 6 | 15 | +150.0% | Stable |
| TK | High (>92%) | 2 | 10 | +400.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TZ | ↓ -3.70% | Credit Card -14.3% | → Stable | CVV/CVC Mismatch +3.70pp | Credit + CVV/CVC |
| TT | ↑ +3.94% | Paypal -33.3% | → Stable | Others -1.61pp | Paypal + Others |
| TO | ↑ +15.79% | Apple Pay -100.0% | → Stable | Others +4.55pp | Apple + Others |
| TV | ↑ +40.00% | Apple Pay -20.0% | → Stable | → Stable | Apple |

---

*Report: 2026-06-02*
