# AR Initial (LL0) Investigation: HF-INTL 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 92.14% → 90.15% (-2.16%)  
**Volume:** 23,042 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-INTL declined significantly from 92.14% to 90.15% (-2.16%) in 2026-W22, with volume also dropping from 28,979 to 23,042 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate dropped below 8-week baseline (91.28% avg) | -2.16% | ⚠️ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold (AT, DE, CH) | AT: -5.81%, DE: -4.39%, CH: -3.29% | ⚠️ |
| L1: Payment Method | Credit Card and Apple Pay showing significant declines | CC: -3.14%, Apple Pay: -3.05% | ⚠️ |
| L1: Payment Provider | ProcessOut and Braintree underperforming | ProcessOut: -3.32%, Braintree: -2.61% | ⚠️ |
| L2: Root Causes | Identified specific decline drivers per country | Insufficient Funds dominant | ⚠️ |
| L3: Related Metrics | All funnel metrics declined in sync | 1_FirstRunAR: -2.58% | ⚠️ |

**Key Findings:**
- **AT** experienced the largest AR decline (-5.81%), driven by credit_card via ProcessOut (-11.82%) with "Insufficient Funds" increasing by +4.63pp
- **DE** saw a -4.39% AR drop with ProcessOut credit_card transactions declining -16.06% and "Insufficient Funds" rising +2.19pp
- **ProcessOut** is the common underperforming provider across AT and DE, with both showing >11% declines in credit card acceptance
- **Volume contraction** observed in high-AR countries: FR (-34.7%), DE (-29.4%), AT (-25.8%), creating unfavorable mix shift
- **First Run AR** declined -2.58%, indicating the issue originates at initial charge attempt rather than retry logic

**Action:** **Escalate** — Coordinate with ProcessOut to investigate credit card processing issues in AT and DE, specifically around increased "Insufficient Funds" declines which may indicate fraud filter changes or BIN-level blocking.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 90.15% | 23,042 | -2.16% ← REPORTED CHANGE |
| 2026-W21 | 92.14% | 28,979 | -0.36% |
| 2026-W20 | 92.47% | 29,040 | -0.09% |
| 2026-W19 | 92.55% | 31,566 | +1.58% |
| 2026-W18 | 91.11% | 27,122 | -0.19% |
| 2026-W17 | 91.28% | 31,456 | +0.57% |
| 2026-W16 | 90.76% | 33,064 | -0.45% |
| 2026-W15 | 91.17% | 25,691 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AT | 88.00% | 93.43% | -5.81% | 350 | ⚠️ |
| DE | 90.57% | 94.73% | -4.39% | 4,114 | ⚠️ |
| CH | 83.33% | 86.17% | -3.29% | 108 | ⚠️ |
| AU | 83.06% | 84.54% | -1.75% | 2,598 |  |
| FR | 94.40% | 95.73% | -1.38% | 3,608 |  |
| GB | 90.14% | 91.09% | -1.05% | 5,688 |  |
| NZ | 76.98% | 75.10% | +2.49% | 721 |  |

**Countries exceeding ±2.5% threshold:** AT, DE, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 87.86% | 90.71% | -3.14% | 7,602 | ⚠️ |
| Apple Pay | 86.03% | 88.74% | -3.05% | 6,930 | ⚠️ |
| Paypal | 93.92% | 95.87% | -2.03% | 3,769 |  |
| Others | 96.84% | 96.61% | +0.24% | 4,741 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 86.54% | 89.51% | -3.32% | 8,515 | ⚠️ |
| Braintree | 90.11% | 92.53% | -2.61% | 9,468 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 43 |  |
| Adyen | 97.08% | 97.0% | +0.09% | 3,635 |  |
| Unknown | 94.06% | 93.32% | +0.79% | 1,381 |  |

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| credit_card | 80.74% | 91.02% | -11.29% | 135 | 167 | ⚠️ |
| applepay | 88.19% | 91.72% | -3.85% | 127 | 169 |  |
| paypal | 98.86% | 98.53% | +0.34% | 88 | 136 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| ProcessOut | 80.74% | 91.57% | -11.82% | 135 | 166 | ⚠️ |
| Braintree | 92.56% | 94.75% | -2.32% | 215 | 305 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 308 | 441 | 88.00% | 93.43% | -5.43 |
| Insufficient Funds | 34 | 24 | 9.71% | 5.08% | +4.63 |
| Other reasons | 6 | 5 | 1.71% | 1.06% | +0.65 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 2 | 0.57% | 0.42% | +0.15 |

**Root Cause:** credit_card + ProcessOut + Insufficient

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 26.92% | 0.00% | +0.00% | 52 | 0 |  |
| None | 0.00% | 65.44% | -100.00% | 0 | 136 | ⚠️ |
| credit_card | 74.20% | 88.35% | -16.01% | 469 | 635 | ⚠️ |
| applepay | 89.06% | 93.42% | -4.67% | 795 | 1,064 |  |
| paypal | 93.97% | 96.78% | -2.90% | 2,273 | 3,385 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 14 | 32 |  |
| klarna | 99.02% | 98.78% | +0.25% | 511 | 572 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 22.45% | 63.85% | -64.84% | 49 | 130 | ⚠️ |
| ProcessOut | 74.14% | 88.32% | -16.06% | 464 | 625 | ⚠️ |
| Braintree | 92.70% | 95.98% | -3.42% | 3,068 | 4,449 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 14 | 32 |  |
| Adyen | 98.84% | 98.64% | +0.21% | 519 | 588 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 3,726 | 5,517 | 90.57% | 94.73% | -4.16 |
| Insufficient Funds | 172 | 116 | 4.18% | 1.99% | +2.19 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 154 | 118 | 3.74% | 2.03% | +1.72 |
| Other reasons | 27 | 28 | 0.66% | 0.48% | +0.18 |
| Unknown | 35 | 45 | 0.85% | 0.77% | +0.08 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| twint | 94.12% | 0.00% | +0.00% | 17 | 0 |  |
| applepay | 78.38% | 96.88% | -19.09% | 37 | 32 | ⚠️ |
| paypal | 90.91% | 94.74% | -4.04% | 11 | 19 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| credit_card | 80.95% | 73.17% | +10.63% | 42 | 41 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 94.12% | 0.00% | +0.00% | 17 | 0 |  |
| Braintree | 81.25% | 96.08% | -15.43% | 48 | 51 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| ProcessOut | 80.95% | 73.17% | +10.63% | 42 | 41 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 90 | 81 | 83.33% | 86.17% | -2.84 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 3 | 1 | 2.78% | 1.06% | +1.71 |
| Insufficient Funds | 13 | 10 | 12.04% | 10.64% | +1.40 |
| Other reasons | 2 | 2 | 1.85% | 2.13% | -0.28 |

**Root Cause:** applepay + Braintree + Refused

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.97% | 90.3% | -2.58% | 23,042 | 28,979 | ⚠️ |
| 2_PreDunningAR | 90.15% | 92.14% | -2.16% | 23,042 | 28,979 |  |
| 3_PostDunningAR | 90.59% | 92.69% | -2.27% | 23,042 | 28,979 |  |
| 6_PaymentApprovalRate | 90.88% | 92.94% | -2.22% | 23,042 | 28,979 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 7,410 | 5,688 | -23.2% | ⚠️ Volume drop |
| DE | High (>92%) | 5,824 | 4,114 | -29.4% | ⚠️ Volume drop |
| FR | High (>92%) | 5,522 | 3,608 | -34.7% | ⚠️ Major mix shift |
| AU | Low (>85%) | 2,458 | 2,598 | +5.7% | Stable |
| BE | High (>92%) | 1,679 | 1,579 | -6.0% | Stable |
| IE | Medium (>85%) | 1,429 | 1,348 | -5.7% | Stable |
| NL | High (>92%) | 1,100 | 820 | -25.5% | ⚠️ Volume drop |
| SE | Medium (>85%) | 889 | 847 | -4.7% | Stable |
| DK | High (>92%) | 813 | 750 | -7.7% | Stable |
| NZ | Low (>85%) | 727 | 721 | -0.8% | Stable |
| NO | High (>92%) | 510 | 455 | -10.8% | Stable |
| AT | High (>92%) | 472 | 350 | -25.8% | ⚠️ Volume drop |
| CH | Medium (>85%) | 94 | 108 | +14.9% | Stable |
| LU | Low (>85%) | 52 | 56 | +7.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AT | ↓ -5.81% | credit_card -11.3% | ProcessOut -11.8% | Insufficient Funds +4.63pp | credit_card + ProcessOut + Insufficient |
| DE | ↓ -4.39% | None -100.0% | Unknown -64.8% | Insufficient Funds +2.19pp | None + Unknown + Insufficient |
| CH | ↓ -3.29% | applepay -19.1% | Braintree -15.4% | Refused - eg: Declined, Closed Card, Do Not Honor, etc. +1.71pp | applepay + Braintree + Refused |

---

*Report: 2026-06-02*
