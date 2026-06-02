# PCAR Investigation: WL 2026-W22

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 96.86% → 97.14% (+0.29%)  
**Volume:** 9,304 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved by +0.29 percentage points (96.86% → 97.14%) on 9,304 orders in WL 2026-W22, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate at 97.14%, within normal range (95.28%-97.59%) | +0.29 pp | ✅ |
| L1: Country Scan | MR flagged with -2.70 pp decline | -2.70 pp | ⚠️ |
| L1: Dimension Scan | No payment methods or providers exceed threshold | <±2.5 pp | ✅ |
| L2: MR Deep-Dive | ApplePay (-7.69 pp) and Braintree (-6.25 pp) identified | -7.69 pp | ⚠️ |
| Mix Shift | CG volume dropped -20.4% but maintains high AR tier | Volume shift | ⚠️ |

**Key Findings:**
- MR is the only country exceeding the ±2.5% threshold with a -2.70 pp decline (100.00% → 97.30%), though volume is low at 111 orders
- Root cause in MR isolated to ApplePay via Braintree: ApplePay dropped -7.69 pp (100% → 92.31%) and Braintree dropped -6.25 pp (100% → 93.75%)
- Overall WL trend shows recovery from W20 trough (95.62%) back toward historical highs
- CG experienced significant volume decline (-20.4%) but rate actually improved +0.85 pp
- All decline reasons in MR categorized as "Others" with no specific error codes available

**Action:** Monitor – The overall metric change is not significant and the MR issue involves low volume (111 orders, 3 failures). Continue monitoring ApplePay + Braintree performance in MR for persistence before escalating.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 97.14% | 9,304 | +0.29% ← REPORTED CHANGE |
| 2026-W21 | 96.86% | 9,450 | +1.30% |
| 2026-W20 | 95.62% | 10,330 | +0.36% |
| 2026-W19 | 95.28% | 10,480 | -0.77% |
| 2026-W18 | 96.02% | 10,753 | -1.03% |
| 2026-W17 | 97.02% | 10,957 | -0.58% |
| 2026-W16 | 97.59% | 11,025 | +0.23% |
| 2026-W15 | 97.37% | 11,722 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 97.30% | 100.00% | -2.70% | 111 | ⚠️ |
| CK | 97.11% | 96.94% | +0.17% | 2,285 |  |
| GN | 97.39% | 96.67% | +0.74% | 918 |  |
| CG | 98.40% | 97.57% | +0.85% | 1,374 |  |
| AO | 97.29% | 96.46% | +0.86% | 738 |  |

**Countries exceeding ±2.5% threshold:** MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | nan% | nan% | +nan% | 0 |  |
| Paypal | 98.02% | 98.16% | -0.14% | 1,062 |  |
| Apple Pay | 96.73% | 96.46% | +0.28% | 2,936 |  |
| Credit Card | 97.19% | 96.79% | +0.42% | 5,306 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ApplePay | 92.31% | 100.00% | -7.69% | 39 | 33 | ⚠️ |
| CreditCard | 100.00% | 100.00% | +0.00% | 63 | 72 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 9 | 12 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 93.75% | 100.00% | -6.25% | 48 | 45 | ⚠️ |
| ProcessOut | 100.00% | 100.00% | +0.00% | 63 | 72 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 111 | 117 | 100.00% | 100.00% | +0.00 |

**Root Cause:** ApplePay + Braintree

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,220 | 2,379 | +7.2% | Stable |
| CK | High (>92%) | 1,995 | 2,285 | +14.5% | Stable |
| CG | High (>92%) | 1,727 | 1,374 | -20.4% | ⚠️ Volume drop |
| ER | High (>92%) | 1,610 | 1,499 | -6.9% | Stable |
| GN | High (>92%) | 961 | 918 | -4.5% | Stable |
| AO | High (>92%) | 820 | 738 | -10.0% | Stable |
| MR | High (>92%) | 117 | 111 | -5.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| MR | ↓ -2.70% | ApplePay -7.7% | Braintree -6.2% | → Stable | ApplePay + Braintree |

---

*Report: 2026-06-02*
