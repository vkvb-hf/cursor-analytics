# PAR Investigation: US-HF 2026-W22

**Metric:** Payment Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 93.23% → 92.92% (-0.33%)  
**Volume:** 368,679 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined by -0.33pp (93.23% → 92.92%) on 368,679 orders in US-HF for 2026-W22, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Base conversion | -0.30pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | -0.33pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.53pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.33pp | ✅ |

**Key Findings:**
- The -0.33pp PAR decline continues a 7-week downward trend from 93.75% (W15) to 92.92% (W22), representing a cumulative -0.83pp erosion
- Post-Dunning AR shows the largest funnel step decline at -0.53pp, suggesting reduced recovery effectiveness in later retry stages
- PaymentProvider "Unknown" flagged with -14.58% change (51.95% → 44.38%), though volume is minimal (329 orders, <0.1% of total)
- No payment methods or countries exceeded the ±2.5% investigation threshold
- Order volume declined -4.7% WoW (386,911 → 368,679), consistent with the overall 8-week volume decline pattern

**Action:** Monitor — The decline is not statistically significant and no dimensions breach investigation thresholds. However, track the cumulative downward trend and Post-Dunning AR performance over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 92.92% | 368,679 | -0.33% ← REPORTED CHANGE |
| 2026-W21 | 93.23% | 386,911 | -0.29% |
| 2026-W20 | 93.5% | 401,763 | +0.18% |
| 2026-W19 | 93.33% | 416,724 | -0.30% |
| 2026-W18 | 93.61% | 414,920 | -0.19% |
| 2026-W17 | 93.79% | 419,106 | -0.03% |
| 2026-W16 | 93.82% | 421,948 | +0.07% |
| 2026-W15 | 93.75% | 408,631 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.95% | 94.24% | -0.31% | 455,505 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 91.3% | 92.51% | -1.31% | 2,149 |  |
| Apple Pay | 86.67% | 87.13% | -0.52% | 50,040 |  |
| Credit Card | 93.55% | 93.84% | -0.31% | 271,909 |  |
| Paypal | 96.16% | 96.35% | -0.20% | 44,581 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 44.38% | 51.95% | -14.58% | 329 | ⚠️ |
| ProcessOut | 88.4% | 89.26% | -0.97% | 56,627 |  |
| Braintree | 93.75% | 93.94% | -0.20% | 309,575 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,720 |  |
| Adyen | 95.33% | 94.98% | +0.37% | 428 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.1% | 90.37% | -0.30% | 368,679 | 386,911 |  |
| 2_PreDunningAR | 91.27% | 91.58% | -0.33% | 368,679 | 386,911 |  |
| 3_PostDunningAR | 92.01% | 92.5% | -0.53% | 368,679 | 386,911 |  |
| 6_PaymentApprovalRate | 92.92% | 93.23% | -0.33% | 368,679 | 386,911 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 478,645 | 455,505 | -4.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
