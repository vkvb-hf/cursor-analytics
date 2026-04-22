# AR Initial (LL0) Investigation: US-HF 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.37% → 88.7% (-0.75%)  
**Volume:** 12,430 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 89.37% to 88.7% (-0.67pp) week-over-week, a statistically non-significant change within normal operational variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (87.66%-90.11%) | -0.67pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | -0.75% | ✅ |
| L1: PaymentMethod | All methods declined uniformly | -0.43% to -1.13% | ✅ |
| L1: PaymentProvider | Unknown provider flagged (-3.19%) | -3.19% | ⚠️ |
| L3: Related Metrics | All funnel metrics declined proportionally | -0.66% to -0.87% | ✅ |
| Mix Shift | Volume increased +13.5%, AR tier stable | N/A | ✅ |

**Key Findings:**
- The -0.67pp decline is within the 8-week historical range (87.66%-90.11%) and marked as not statistically significant
- Unknown PaymentProvider showed the largest decline (-3.19%) but represents minimal volume (168 orders, 1.4% of total)
- All payment methods declined uniformly (Apple Pay -0.70%, Credit Card -0.60%, PayPal -0.43%), suggesting no isolated payment channel issues
- Volume increased significantly (+13.5%, from 10,950 to 12,430 orders) while maintaining Medium AR tier stability
- Related metrics (1_FirstRunAR, 3_PostDunningAR, 6_PaymentApprovalRate) all declined proportionally, indicating a systemic rather than stage-specific pattern

**Action:** Monitor — No escalation required. The decline is non-significant, within historical variance, and shows uniform distribution across dimensions with no actionable anomalies outside the low-volume Unknown provider segment.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 88.7% | 12,430 | -0.75% ← REPORTED CHANGE |
| 2026-W15 | 89.37% | 10,950 | +0.48% |
| 2026-W14 | 88.94% | 11,659 | +1.46% |
| 2026-W13 | 87.66% | 10,943 | -1.25% |
| 2026-W12 | 88.77% | 14,784 | -1.49% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 88.70% | 89.37% | -0.75% | 12,430 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.44% | 97.54% | -1.13% | 281 |  |
| Apple Pay | 86.63% | 87.24% | -0.70% | 4,316 |  |
| Credit Card | 89.62% | 90.16% | -0.60% | 6,840 |  |
| Paypal | 89.12% | 89.5% | -0.43% | 993 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 94.05% | 97.14% | -3.19% | 168 | ⚠️ |
| Braintree | 86.85% | 87.41% | -0.64% | 5,385 |  |
| ProcessOut | 89.83% | 90.4% | -0.63% | 6,755 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 113 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 9 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.82% | 88.59% | -0.87% | 12,430 | 10,950 |  |
| 2_PreDunningAR | 88.7% | 89.37% | -0.75% | 12,430 | 10,950 |  |
| 3_PostDunningAR | 88.92% | 89.6% | -0.75% | 12,430 | 10,950 |  |
| 6_PaymentApprovalRate | 89.23% | 89.82% | -0.66% | 12,430 | 10,950 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,950 | 12,430 | +13.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
