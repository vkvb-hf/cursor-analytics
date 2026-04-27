# AR Initial (LL0) Investigation: US-HF 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 88.8% → 89.01% (+0.24%)  
**Volume:** 13,208 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved marginally from 88.8% to 89.01% (+0.21 pp) in W17, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (87.87%-90.11%) | +0.21 pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +0.24% | ✅ |
| L1: PaymentMethod | Credit Card showed significant decline | -7.30% | ⚠️ |
| L1: PaymentProvider | No significant changes in major providers | - | ✅ |
| L3: Related Metrics | All funnel metrics stable | +0.01 to +0.24% | ✅ |

**Key Findings:**
- Credit Card payment method showed a notable decline of -7.30% (from 89.32% to 82.8%), though volume is low at 157 orders (1.2% of total)
- Volume increased by 7.3% WoW (12,308 → 13,208 orders), indicating healthy order growth
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) remained stable with minimal movement (+0.01 to +0.24%)
- Apple Pay showed improvement (+1.18 pp) with significant volume (4,661 orders, 35% of total)
- Braintree provider improved by +1.14% (86.83% → 87.82%) handling 44% of volume

**Action:** Monitor — The Credit Card payment method decline warrants observation in W18 to determine if it's an anomaly or emerging trend, but low volume makes it non-critical.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 89.01% | 13,208 | +0.24% ← REPORTED CHANGE |
| 2026-W16 | 88.8% | 12,308 | -0.98% |
| 2026-W15 | 89.68% | 10,952 | +0.91% |
| 2026-W14 | 88.87% | 11,645 | +1.14% |
| 2026-W13 | 87.87% | 10,874 | -0.92% |
| 2026-W12 | 88.69% | 14,817 | -1.58% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.01% | 88.80% | +0.24% | 13,208 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 82.8% | 89.32% | -7.30% | 157 | ⚠️ |
| Others | 89.94% | 90.16% | -0.24% | 7,367 |  |
| Paypal | 89.74% | 89.46% | +0.31% | 1,023 |  |
| Apple Pay | 87.58% | 86.55% | +1.18% | 4,661 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 91.34% | +nan% | 0 |  |
| Unknown | 89.8% | 89.99% | -0.20% | 7,268 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 40 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 62 |  |
| Braintree | 87.82% | 86.83% | +1.14% | 5,838 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.12% | 88.05% | +0.08% | 13,208 | 12,308 |  |
| 2_PreDunningAR | 89.01% | 88.8% | +0.24% | 13,208 | 12,308 |  |
| 3_PostDunningAR | 89.12% | 88.99% | +0.15% | 13,208 | 12,308 |  |
| 6_PaymentApprovalRate | 89.29% | 89.28% | +0.01% | 13,208 | 12,308 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 12,308 | 13,208 | +7.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
