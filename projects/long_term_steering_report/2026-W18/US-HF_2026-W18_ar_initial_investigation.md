# AR Initial (LL0) Investigation: US-HF 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 88.95% → 88.24% (-0.80%)  
**Volume:** 11,092 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF declined from 88.95% to 88.24% (-0.71 pp) in W18, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (87.62%-90.11%) | -0.71 pp | ✅ |
| L1: Country Breakdown | US only, no country >±2.5% threshold | -0.71 pp | ✅ |
| L1: Payment Method | PayPal largest decline (-1.42 pp) | Mixed | ✅ |
| L1: Payment Provider | No significant provider issues | Stable | ✅ |
| L3: Related Metrics | All funnel metrics declined similarly | -0.76 to -0.84 pp | ⚠️ |
| Mix Shift | Volume down 14.7%, AR tier stable | N/A | ✅ |

**Key Findings:**
- The -0.71 pp decline is within normal weekly fluctuation observed over the 8-week period (range: 87.62% to 90.11%)
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show parallel declines of -0.76 pp to -0.84 pp, indicating a systemic rather than stage-specific issue
- PayPal showed the largest payment method decline (-1.42 pp), though volume is relatively low (850 orders)
- Order volume decreased 14.7% (13,007 → 11,092) but the mix remained in the Medium AR tier (>85%)
- No payment providers flagged for concern; ProcessOut and Adyen show no current volume

**Action:** Monitor — The decline is not statistically significant and falls within normal weekly variance. Continue standard monitoring in W19.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 88.24% | 11,092 | -0.80% ← REPORTED CHANGE |
| 2026-W17 | 88.95% | 13,007 | +0.02% |
| 2026-W16 | 88.93% | 12,343 | -0.65% |
| 2026-W15 | 89.51% | 10,921 | +0.67% |
| 2026-W14 | 88.91% | 11,594 | +1.47% |
| 2026-W13 | 87.62% | 10,917 | -1.27% |
| 2026-W12 | 88.75% | 14,779 | -1.51% |
| 2026-W11 | 90.11% | 15,868 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 88.24% | 88.95% | -0.80% | 11,092 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 89.06% | 90.34% | -1.42% | 850 |  |
| Others | 88.78% | 89.79% | -1.13% | 6,353 |  |
| Apple Pay | 87.34% | 87.51% | -0.20% | 3,744 |  |
| Credit Card | 83.45% | 82.69% | +0.91% | 145 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Adyen | nan% | 100.0% | +nan% | 0 |  |
| Unknown | 88.66% | 89.65% | -1.10% | 6,290 |  |
| Braintree | 87.53% | 87.88% | -0.39% | 4,741 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 61 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.41% | 88.15% | -0.84% | 11,092 | 13,007 |  |
| 2_PreDunningAR | 88.24% | 88.95% | -0.80% | 11,092 | 13,007 |  |
| 3_PostDunningAR | 88.4% | 89.08% | -0.76% | 11,092 | 13,007 |  |
| 6_PaymentApprovalRate | 88.52% | 89.22% | -0.78% | 11,092 | 13,007 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 13,007 | 11,092 | -14.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
