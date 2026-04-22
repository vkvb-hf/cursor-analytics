# AR Initial (LL0) Investigation: HF-NA 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.8% → 89.31% (-0.55%)  
**Volume:** 18,136 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.55pp (89.8% → 89.31%) on 18,136 orders in W16, a change that is not statistically significant and falls within normal weekly fluctuation patterns.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (89.18%-90.82%) | -0.55pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | US: -0.75pp, CA: -0.08pp | ✅ |
| L1: Payment Method | All methods within tolerance | -0.67pp to +0.23pp | ✅ |
| L1: Payment Provider | Adyen flagged (-3.96pp) | Low volume (63 orders) | ⚠️ |
| L3: Related Metrics | All funnel steps declined similarly | -0.55pp to -0.66pp | ✅ |
| Mix Shift | Volume increased, distribution stable | US +13.5%, CA +10.6% | ✅ |

**Key Findings:**
- The -0.55pp decline is consistent across the entire payment funnel (FirstRunAR: -0.66pp, PostDunningAR: -0.61pp, PaymentApprovalRate: -0.57pp), indicating a systemic rather than localized issue
- Adyen shows a -3.96pp decline but only processed 63 orders, making this statistically unreliable and not material to overall performance
- US drove the majority of the decline (-0.75pp on 12,430 orders) while CA remained nearly flat (-0.08pp)
- Volume increased 12.6% WoW (16,108 → 18,136), with no adverse mix shift effects detected
- Current rate of 89.31% remains within the 8-week range of 89.18%-90.82%

**Action:** Monitor — No investigation required. The decline is not significant, falls within historical variance, and no dimensional breakdowns exceed actionable thresholds. Continue standard monitoring in W17.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.31% | 18,136 | -0.55% ← REPORTED CHANGE |
| 2026-W15 | 89.8% | 16,108 | +0.09% |
| 2026-W14 | 89.72% | 17,175 | +0.61% |
| 2026-W13 | 89.18% | 16,198 | -0.58% |
| 2026-W12 | 89.7% | 21,078 | -1.23% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 88.70% | 89.37% | -0.75% | 12,430 |  |
| CA | 90.64% | 90.71% | -0.08% | 5,706 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 87.69% | 88.28% | -0.67% | 5,653 |  |
| Credit Card | 89.68% | 90.1% | -0.47% | 10,300 |  |
| Others | 96.94% | 96.88% | +0.06% | 687 |  |
| Paypal | 89.37% | 89.17% | +0.23% | 1,496 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 88.89% | 92.55% | -3.96% | 63 | ⚠️ |
| Braintree | 87.85% | 88.27% | -0.47% | 7,226 |  |
| ProcessOut | 89.84% | 90.26% | -0.47% | 10,164 |  |
| Unknown | 95.95% | 96.34% | -0.40% | 519 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 164 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.18% | 88.77% | -0.66% | 18,136 | 16,108 |  |
| 2_PreDunningAR | 89.31% | 89.8% | -0.55% | 18,136 | 16,108 |  |
| 3_PostDunningAR | 89.49% | 90.04% | -0.61% | 18,136 | 16,108 |  |
| 6_PaymentApprovalRate | 89.73% | 90.25% | -0.57% | 18,136 | 16,108 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,950 | 12,430 | +13.5% | Stable |
| CA | Medium (>85%) | 5,158 | 5,706 | +10.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
