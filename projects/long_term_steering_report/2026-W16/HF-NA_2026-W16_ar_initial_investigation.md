# AR Initial (LL0) Investigation: HF-NA 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.82% → 89.44% (-0.42%)  
**Volume:** 18,103 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.42pp (89.82% → 89.44%) on 18,103 orders in W16, a change that is not statistically significant and falls within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (89.15%-90.82%) | -0.42pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US: -0.55pp, CA: -0.10pp | ✅ |
| L1: PaymentMethod | All methods within tolerance | -0.47pp to +0.18pp | ✅ |
| L1: PaymentProvider | Adyen flagged (-3.96pp) | Low volume (63 orders) | ⚠️ |
| L3: Related Metrics | All funnel metrics declined similarly | -0.41pp to -0.48pp | ✅ |
| Mix Shift | Volume growth stable across tiers | US +13.5%, CA +10.6% | ✅ |

**Key Findings:**
- The -0.42pp decline is within the 8-week variance band (89.15%-90.82%) and is not statistically significant
- Adyen shows a -3.96pp decline but represents only 63 orders (0.35% of volume), limiting material impact
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show parallel declines of -0.41pp to -0.48pp, indicating a systemic rather than stage-specific issue
- Both US (-0.55pp) and CA (-0.10pp) declined modestly, with neither exceeding investigation thresholds
- Volume increased +12.5% WoW (16,084 → 18,103), with no adverse mix shift impact detected

**Action:** Monitor — Continue standard tracking. No escalation required as the decline is not significant and no dimension exceeded threshold limits. Flag Adyen for observation if low-volume volatility persists in subsequent weeks.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.44% | 18,103 | -0.42% ← REPORTED CHANGE |
| 2026-W15 | 89.82% | 16,084 | +0.20% |
| 2026-W14 | 89.64% | 17,161 | +0.55% |
| 2026-W13 | 89.15% | 16,163 | -0.57% |
| 2026-W12 | 89.66% | 21,062 | -1.28% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 88.9% | 89.39% | -0.55% | 12,393 |  |
| CA | 90.63% | 90.72% | -0.10% | 5,710 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 87.95% | 88.37% | -0.47% | 5,645 |  |
| Credit Card | 89.79% | 90.07% | -0.32% | 10,263 |  |
| Others | 96.81% | 97.01% | -0.21% | 689 |  |
| Paypal | 89.31% | 89.15% | +0.18% | 1,506 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 88.89% | 92.55% | -3.96% | 63 | ⚠️ |
| Unknown | 95.79% | 96.47% | -0.71% | 522 |  |
| ProcessOut | 89.94% | 90.24% | -0.33% | 10,131 |  |
| Braintree | 88.05% | 88.33% | -0.32% | 7,224 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 163 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.35% | 88.78% | -0.48% | 18,103 | 16,084 |  |
| 2_PreDunningAR | 89.44% | 89.82% | -0.41% | 18,103 | 16,084 |  |
| 3_PostDunningAR | 89.6% | 90.03% | -0.47% | 18,103 | 16,084 |  |
| 6_PaymentApprovalRate | 89.85% | 90.25% | -0.45% | 18,103 | 16,084 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,922 | 12,393 | +13.5% | Stable |
| CA | Medium (>85%) | 5,162 | 5,710 | +10.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
