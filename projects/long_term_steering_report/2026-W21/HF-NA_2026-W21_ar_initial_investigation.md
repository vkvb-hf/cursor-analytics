# AR Initial (LL0) Investigation: HF-NA 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 89.34% → 88.39% (-1.06%)  
**Volume:** 13,666 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 89.34% to 88.39% (-0.95 pp) in W21, representing a significant week-over-week decrease across 13,666 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -1.07 pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | -1.06 pp | ⚠️ |
| 3_PostDunningAR | Dunning Recovery | -0.91 pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.80 pp | ⚠️ |

**Key Findings:**
- Decline is broad-based across the entire payment funnel, with FirstRunAR showing the largest drop (-1.07 pp), indicating the issue originates at initial charge attempt rather than recovery stages
- PayPal shows the steepest decline at -2.98 pp (84.09% vs 86.68%), flagged as the only payment method exceeding threshold
- Unknown PaymentProvider declined -2.79 pp (81.36% vs 83.70%), though volume is limited (279 orders)
- Both countries declined proportionally: US -1.10 pp (86.81%) and CA -1.19 pp (92.17%), neither exceeding the ±2.5% threshold
- Order volume decreased 8.5% week-over-week (14,940 → 13,666), with mix shift analysis showing stable tier distribution

**Action:** **Investigate** – The PayPal payment method decline (-2.98 pp) warrants immediate investigation into potential processor issues or PayPal-specific authorization problems. Coordinate with payment operations to review PayPal transaction logs for W21.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 88.39% | 13,666 | -1.06% ← REPORTED CHANGE |
| 2026-W20 | 89.34% | 14,940 | -0.40% |
| 2026-W19 | 89.7% | 15,383 | +0.25% |
| 2026-W18 | 89.48% | 15,679 | -0.73% |
| 2026-W17 | 90.14% | 18,108 | +0.91% |
| 2026-W16 | 89.33% | 17,987 | -0.63% |
| 2026-W15 | 89.9% | 16,008 | +0.19% |
| 2026-W14 | 89.73% | 17,062 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 92.17% | 93.28% | -1.19% | 4,023 |  |
| US | 86.81% | 87.77% | -1.10% | 9,643 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 84.09% | 86.68% | -2.98% | 1,144 | ⚠️ |
| Credit Card | 90.21% | 91.35% | -1.25% | 7,477 |  |
| Others | 93.09% | 93.99% | -0.96% | 810 |  |
| Apple Pay | 85.43% | 85.68% | -0.29% | 4,235 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 81.36% | 83.7% | -2.79% | 279 | ⚠️ |
| ProcessOut | 90.1% | 91.47% | -1.50% | 7,090 |  |
| Braintree | 85.24% | 85.83% | -0.69% | 5,507 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 134 |  |
| Adyen | 96.95% | 96.54% | +0.43% | 656 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.31% | 88.25% | -1.07% | 13,666 | 14,940 |  |
| 2_PreDunningAR | 88.39% | 89.34% | -1.06% | 13,666 | 14,940 |  |
| 3_PostDunningAR | 88.84% | 89.66% | -0.91% | 13,666 | 14,940 |  |
| 6_PaymentApprovalRate | 89.15% | 89.87% | -0.80% | 13,666 | 14,940 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,697 | 9,643 | -9.9% | Stable |
| CA | High (>92%) | 4,243 | 4,023 | -5.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
