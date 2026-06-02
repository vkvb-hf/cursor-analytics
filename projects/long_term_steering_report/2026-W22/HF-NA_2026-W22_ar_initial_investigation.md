# AR Initial (LL0) Investigation: HF-NA 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 88.2% → 87.09% (-1.26%)  
**Volume:** 14,606 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined from 88.2% to 87.09% (-1.26pp) in W22, continuing a downward trend observed over the past 4 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -1.68pp | ⚠️ |
| 2_PreDunningAR | Pre-Dunning Recovery | -1.26pp | ⚠️ |
| 3_PostDunningAR | Post-Dunning Recovery | -1.68pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -1.94pp | ⚠️ |

**Key Findings:**
- **PayPal underperformance:** PayPal payment method declined -4.50pp (84.4% → 80.6%) with 1,294 orders, significantly exceeding the threshold
- **Unknown provider deterioration:** Unknown payment provider dropped -6.38pp (81.78% → 76.56%), though volume is limited (256 orders)
- **Sustained decline pattern:** The metric has declined for 4 consecutive weeks, dropping from 90.16% (W17) to 87.09% (W22), a cumulative -3.07pp erosion
- **Both countries declining:** US fell -1.31pp (86.57% → 85.43%) and CA fell -1.59pp (92.14% → 90.67%), with neither exceeding the ±2.5% threshold individually
- **Full funnel impact:** All related metrics show parallel declines (-1.26pp to -1.94pp), indicating the issue originates at first charge attempt

**Action:** **Investigate** – The PayPal payment method decline (-4.50pp) warrants immediate investigation into potential processor issues, while the 4-week sustained downward trend requires monitoring for systemic causes.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 87.09% | 14,606 | -1.26% ← REPORTED CHANGE |
| 2026-W21 | 88.2% | 13,732 | -1.23% |
| 2026-W20 | 89.3% | 14,958 | -0.36% |
| 2026-W19 | 89.62% | 15,299 | +0.19% |
| 2026-W18 | 89.45% | 15,696 | -0.79% |
| 2026-W17 | 90.16% | 18,029 | +0.95% |
| 2026-W16 | 89.31% | 18,018 | -0.72% |
| 2026-W15 | 89.96% | 16,147 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 90.67% | 92.14% | -1.59% | 4,611 |  |
| US | 85.43% | 86.57% | -1.31% | 9,995 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 80.6% | 84.4% | -4.50% | 1,294 | ⚠️ |
| Credit Card | 88.23% | 89.94% | -1.90% | 8,113 |  |
| Others | 91.87% | 93.52% | -1.76% | 763 |  |
| Apple Pay | 86.07% | 85.1% | +1.14% | 4,436 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 76.56% | 81.78% | -6.38% | 256 | ⚠️ |
| ProcessOut | 88.16% | 89.81% | -1.83% | 7,679 |  |
| Braintree | 84.67% | 85.05% | -0.45% | 5,878 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 118 |  |
| Adyen | 97.63% | 97.13% | +0.51% | 675 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 85.66% | 87.12% | -1.68% | 14,606 | 13,732 |  |
| 2_PreDunningAR | 87.09% | 88.2% | -1.26% | 14,606 | 13,732 |  |
| 3_PostDunningAR | 87.21% | 88.71% | -1.68% | 14,606 | 13,732 |  |
| 6_PaymentApprovalRate | 87.26% | 88.99% | -1.94% | 14,606 | 13,732 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 9,714 | 9,995 | +2.9% | Stable |
| CA | High (>92%) | 4,018 | 4,611 | +14.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
