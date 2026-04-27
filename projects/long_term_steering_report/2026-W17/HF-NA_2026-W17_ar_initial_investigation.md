# AR Initial (LL0) Investigation: HF-NA 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.38% → 89.87% (+0.55%)  
**Volume:** 18,383 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-NA improved from 89.38% to 89.87% (+0.49pp) in W17, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.45pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.49pp | ✅ |
| 3_PostDunningAR | Post-Dunning | +0.48pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.54pp | ✅ |

**Key Findings:**
- All funnel stages showed consistent modest improvement (+0.45pp to +0.54pp), indicating no isolated bottleneck
- Adyen payment provider showed a significant spike of +9.47pp (87.84% → 96.15%) but with low volume (468 orders) — flagged ⚠️
- CA outperformed US with +1.59pp improvement (90.63% → 92.08%) vs US at +0.24pp (88.80% → 89.01%)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation
- Volume decreased in CA (-9.2%) while US volume increased (+7.3%), with minimal impact on overall rate due to stable AR tiers

**Action:** Monitor — The improvement is not statistically significant and falls within normal weekly fluctuation (8-week range: 89.33% - 90.82%). Continue tracking Adyen performance given the flagged improvement.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 89.87% | 18,383 | +0.55% ← REPORTED CHANGE |
| 2026-W16 | 89.38% | 18,010 | -0.70% |
| 2026-W15 | 90.01% | 16,108 | +0.38% |
| 2026-W14 | 89.67% | 17,159 | +0.38% |
| 2026-W13 | 89.33% | 16,127 | -0.35% |
| 2026-W12 | 89.64% | 21,112 | -1.30% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.01% | 88.80% | +0.24% | 13,208 |  |
| CA | 92.08% | 90.63% | +1.59% | 5,175 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 87.54% | 88.44% | -1.03% | 353 |  |
| Others | 90.48% | 90.45% | +0.03% | 10,681 |  |
| Paypal | 90.05% | 89.6% | +0.49% | 1,487 |  |
| Apple Pay | 88.86% | 87.64% | +1.40% | 5,862 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 89.98% | +nan% | 0 |  |
| Unknown | 90.14% | 90.3% | -0.18% | 10,304 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 108 |  |
| Braintree | 88.96% | 87.84% | +1.28% | 7,503 |  |
| Adyen | 96.15% | 87.84% | +9.47% | 468 | ⚠️ |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.74% | 88.35% | +0.45% | 18,383 | 18,010 |  |
| 2_PreDunningAR | 89.87% | 89.38% | +0.55% | 18,383 | 18,010 |  |
| 3_PostDunningAR | 89.96% | 89.53% | +0.48% | 18,383 | 18,010 |  |
| 6_PaymentApprovalRate | 90.25% | 89.77% | +0.54% | 18,383 | 18,010 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 12,308 | 13,208 | +7.3% | Stable |
| CA | Medium (>85%) | 5,702 | 5,175 | -9.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
