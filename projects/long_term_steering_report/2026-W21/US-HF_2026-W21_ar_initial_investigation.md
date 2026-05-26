# AR Initial (LL0) Investigation: US-HF 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 87.77% → 86.81% (-1.09%)  
**Volume:** 9,643 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF Initial Charges declined from 87.77% to 86.81% (-0.96pp) in W21, representing the fifth consecutive week of decline and reaching the lowest point in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | -1.07pp | ⚠️ |
| 2_PreDunningAR | Before retry logic | -0.96pp | ⚠️ |
| 3_PostDunningAR | After retry logic | -0.81pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.84pp | ⚠️ |

**Key Findings:**
- **Sustained downward trend:** Rate has declined for 5 consecutive weeks, dropping 2.22pp from W14 (88.95%) to W21 (86.81%)
- **Volume contraction:** Order volume decreased 9.9% WoW (10,697 → 9,643), coinciding with rate decline
- **ProcessOut underperformance:** ProcessOut showed the largest provider decline at -1.58pp (90.50% → 88.92%), handling 53% of volume
- **Credit Card method most impacted:** Credit Card declined -1.38pp (90.32% → 88.94%), representing the largest payment method drop with 54% of transactions
- **Funnel-wide degradation:** All funnel stages declined proportionally, indicating the issue originates at FirstRunAR (-1.07pp) rather than in retry/dunning logic

**Action:** **Investigate** — The persistent 5-week decline pattern and ProcessOut-specific degradation warrant immediate investigation into processor-level issues, particularly for Credit Card transactions routed through ProcessOut.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 86.81% | 9,643 | -1.09% ← REPORTED CHANGE |
| 2026-W20 | 87.77% | 10,697 | -0.51% |
| 2026-W19 | 88.22% | 10,687 | -0.23% |
| 2026-W18 | 88.42% | 10,792 | -0.69% |
| 2026-W17 | 89.03% | 13,012 | +0.34% |
| 2026-W16 | 88.73% | 12,303 | -0.90% |
| 2026-W15 | 89.54% | 10,871 | +0.66% |
| 2026-W14 | 88.95% | 11,559 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 86.81% | 87.77% | -1.10% | 9,643 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.94% | 90.32% | -1.53% | 5,255 |  |
| Paypal | 83.66% | 84.69% | -1.21% | 771 |  |
| Others | 89.54% | 90.19% | -0.72% | 306 |  |
| Apple Pay | 83.9% | 84.24% | -0.40% | 3,311 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 88.92% | 90.5% | -1.74% | 5,128 |  |
| Braintree | 84.01% | 84.29% | -0.33% | 4,210 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 93 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 84 |  |
| Unknown | 75.78% | 74.76% | +1.37% | 128 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 85.71% | 86.78% | -1.23% | 9,643 | 10,697 |  |
| 2_PreDunningAR | 86.81% | 87.77% | -1.10% | 9,643 | 10,697 |  |
| 3_PostDunningAR | 87.35% | 88.16% | -0.93% | 9,643 | 10,697 |  |
| 6_PaymentApprovalRate | 87.59% | 88.43% | -0.95% | 9,643 | 10,697 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,697 | 9,643 | -9.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
