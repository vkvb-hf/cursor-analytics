# Reactivation Investigation: RTE 2026-W20

**Metric:** Reactivation Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 89.01% → 89.27% (+0.29%)  
**Volume:** 18,697 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate improved slightly from 89.01% to 89.27% (+0.26 pp), a statistically non-significant change on 18,697 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (87.04%-90.41%) | +0.26 pp | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold | TO -10.71%, TV -7.69%, TT +2.78%, YE +4.91% | ⚠️ |
| L1: Dimension Scan | Apple Pay declined, Others improved | Apple Pay -3.34%, Others +10.30% | ⚠️ |
| L2: Volume Impact | TO and TT show major volume drops | TO -40.0%, TT -27.0% | ⚠️ |
| Mix Shift | Low-volume countries driving flags | Combined volume <60 orders | ✅ |

**Key Findings:**
- TO experienced a -10.71% rate decline driven by Apple Pay (0% from 100%) and Others payment methods, though total volume is only 18 orders
- TV declined -7.69% with Apple Pay failures and new 3DS authentication issues (+7.69 pp), on just 13 orders
- YE showed meaningful improvement (+4.91%) on substantial volume (2,352 orders), driven by Credit Card (+5.27%) and Others (+12.32%) payment methods
- Apple Pay is underperforming globally (-3.34%) with 1,706 orders, warranting monitoring
- Flagged declining countries (TO, TV) represent <0.2% of total volume, limiting overall impact

**Action:** Monitor - The overall rate change is not statistically significant, and the flagged declines occur in extremely low-volume countries (TO: 18, TV: 13 orders). Continue tracking Apple Pay performance globally and YE's positive trend.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 89.27% | 18,697 | +0.29% ← REPORTED CHANGE |
| 2026-W19 | 89.01% | 20,405 | +2.26% |
| 2026-W18 | 87.04% | 19,909 | -0.33% |
| 2026-W17 | 87.33% | 19,371 | -2.05% |
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 83.33% | 93.33% | -10.71% | 18 | ⚠️ |
| TV | 92.31% | 100.00% | -7.69% | 13 | ⚠️ |
| FJ | 89.03% | 89.76% | -0.81% | 14,144 |  |
| CF | 92.67% | 90.81% | +2.04% | 2,114 |  |
| TT | 100.00% | 97.30% | +2.78% | 27 | ⚠️ |
| YE | 87.37% | 83.29% | +4.91% | 2,352 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TO, TV, TT, YE

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 65.59% | 67.86% | -3.34% | 1,706 | ⚠️ |
| Paypal | 93.21% | 93.28% | -0.07% | 3,270 |  |
| Credit Card | 91.52% | 90.99% | +0.58% | 13,467 |  |
| Others | 77.95% | 70.67% | +10.30% | 254 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 0.00% | 100.00% | -100.00% | 1 | 2 | ⚠️ |
| Others | 0.00% | 71.43% | -100.00% | 1 | 7 | ⚠️ |
| Credit Card | 90.91% | 100.00% | -9.09% | 11 | 17 | ⚠️ |
| Paypal | 100.00% | 100.00% | +0.00% | 5 | 4 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 16 | 29 | 88.89% | 96.67% | -7.78 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 5.56% | 0.00% | +5.56 |
| Expired, Invalid, Closed Card, No Account | 1 | 1 | 5.56% | 3.33% | +2.22 |

**Root Cause:** Apple + Others

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 0.00% | 100.00% | -100.00% | 0 | 2 | ⚠️ |
| Paypal | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Credit Card | 88.89% | 100.00% | -11.11% | 9 | 2 | ⚠️ |
| Others | 100.00% | 100.00% | +0.00% | 4 | 6 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 3DS Authentication Failed/Required | 1 | 0 | 7.69% | 0.00% | +7.69 |
| Others | 12 | 11 | 92.31% | 100.00% | -7.69 |

**Root Cause:** Apple + 3DS

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 0.00% | 100.00% | -100.00% | 0 | 3 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| Credit Card | 100.00% | 100.00% | +0.00% | 6 | 7 |  |
| Others | 100.00% | 96.00% | +4.17% | 20 | 25 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 27 | 37 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Paypal

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 94.51% | 93.35% | +1.25% | 711 | 827 |  |
| Credit Card | 85.01% | 80.76% | +5.27% | 1,368 | 1,642 | ⚠️ |
| Others | 80.59% | 71.75% | +12.32% | 273 | 361 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 2,154 | 2,501 | 91.58% | 88.37% | +3.21 |
| Expired, Invalid, Closed Card, No Account | 103 | 178 | 4.38% | 6.29% | -1.91 |
| Blocked, Restricted, Not Permitted | 66 | 106 | 2.81% | 3.75% | -0.94 |
| PayPal Declined, Revoked, Payer Issue | 26 | 44 | 1.11% | 1.55% | -0.45 |
| 3DS Authentication Failed/Required | 1 | 0 | 0.04% | 0.00% | +0.04 |
| CVV/CVC Mismatch | 1 | 0 | 0.04% | 0.00% | +0.04 |
| Fraud, Lost/Stolen Card, Security | 1 | 1 | 0.04% | 0.04% | +0.01 |

**Root Cause:** Credit + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 15,339 | 14,144 | -7.8% | Stable |
| YE | Low (>85%) | 2,830 | 2,352 | -16.9% | Stable |
| CF | Medium (>85%) | 2,133 | 2,114 | -0.9% | Stable |
| TT | High (>92%) | 37 | 27 | -27.0% | ⚠️ Volume drop |
| TO | High (>92%) | 30 | 18 | -40.0% | ⚠️ Major mix shift |
| TZ | High (>92%) | 21 | 24 | +14.3% | Stable |
| TV | High (>92%) | 11 | 13 | +18.2% | Stable |
| TK | High (>92%) | 4 | 5 | +25.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -10.71% | Apple Pay -100.0% | → Stable | Others -7.78pp | Apple + Others |
| TV | ↓ -7.69% | Apple Pay -100.0% | → Stable | 3DS Authentication Failed/Required +7.69pp | Apple + 3DS |
| TT | ↑ +2.78% | Paypal -100.0% | → Stable | → Stable | Paypal |
| YE | ↑ +4.91% | Credit Card +5.3% | → Stable | Others +3.21pp | Credit + Others |

---

*Report: 2026-05-19*
