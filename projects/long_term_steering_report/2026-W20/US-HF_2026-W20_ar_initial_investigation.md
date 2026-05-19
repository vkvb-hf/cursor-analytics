# AR Initial (LL0) Investigation: US-HF 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 88.24% → 87.61% (-0.71%)  
**Volume:** 10,715 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF declined from 88.24% to 87.61% (-0.63pp) in W20, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Decline within normal variance | -0.71% | ✅ |
| L1: Country Breakdown | No countries exceed ±2.5% threshold | -0.72% | ✅ |
| L1: PaymentMethod | PayPal flagged with -4.47% decline | -4.47% | ⚠️ |
| L1: PaymentProvider | Adyen improved +4.05%, Braintree declined -1.42% | Mixed | ✅ |
| L3: Related Metrics | All metrics tracking consistently | -0.47% to -0.72% | ✅ |
| Mix Shift | US volume stable, no tier migration | +0.7% vol | ✅ |

**Key Findings:**
- PayPal payment method showed a significant decline of -4.47pp (84.37% vs 88.31%), though volume is relatively low at 870 orders (8.1% of total)
- The decline is consistent across the full funnel: FirstRunAR (-0.72%), PreDunningAR (-0.72%), and PostDunningAR (-0.47%) all moved in parallel
- Braintree provider (processing Apple Pay and PayPal) declined -1.42pp while ProcessOut remained stable at -0.26pp
- Adyen showed improvement of +4.05pp but on minimal volume (78 orders)
- Overall rate of 87.61% remains within the 8-week range (87.85% - 89.73%)

**Action:** Monitor - The decline is not statistically significant and falls within normal weekly variance. Continue to track PayPal performance over the next 1-2 weeks to determine if the -4.47pp drop represents a trend or an isolated fluctuation.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 87.61% | 10,715 | -0.71% ← REPORTED CHANGE |
| 2026-W19 | 88.24% | 10,636 | -0.01% |
| 2026-W18 | 88.25% | 10,892 | -0.79% |
| 2026-W17 | 88.95% | 12,909 | +0.04% |
| 2026-W16 | 88.91% | 12,321 | -0.91% |
| 2026-W15 | 89.73% | 10,849 | +0.87% |
| 2026-W14 | 88.96% | 11,536 | +1.26% |
| 2026-W13 | 87.85% | 10,877 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 87.61% | 88.24% | -0.72% | 10,715 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 84.37% | 88.31% | -4.47% | 870 | ⚠️ |
| Apple Pay | 84.48% | 85.05% | -0.67% | 3,666 |  |
| Credit Card | 89.88% | 90.18% | -0.34% | 5,917 |  |
| Others | 90.84% | 89.61% | +1.38% | 262 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 76.92% | 78.07% | -1.47% | 104 |  |
| Braintree | 84.39% | 85.61% | -1.42% | 4,683 |  |
| ProcessOut | 90.07% | 90.3% | -0.26% | 5,770 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 80 |  |
| Adyen | 100.0% | 96.1% | +4.05% | 78 | ⚠️ |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 86.68% | 87.31% | -0.72% | 10,715 | 10,636 |  |
| 2_PreDunningAR | 87.61% | 88.24% | -0.72% | 10,715 | 10,636 |  |
| 3_PostDunningAR | 87.96% | 88.38% | -0.47% | 10,715 | 10,636 |  |
| 6_PaymentApprovalRate | 88.59% | 88.57% | +0.02% | 10,715 | 10,636 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,636 | 10,715 | +0.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
