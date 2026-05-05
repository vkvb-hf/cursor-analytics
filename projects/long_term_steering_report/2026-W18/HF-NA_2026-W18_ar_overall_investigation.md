# AR Overall Investigation: HF-NA 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 92.19% → 92.11% (-0.09%)  
**Volume:** 506,463 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined marginally from 92.19% to 92.11% (-0.08 pp) on volume of 506,463 orders, a statistically insignificant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.09 pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.08 pp | ✅ |
| 3_PostDunningAR | Post-Recovery | -0.15 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.10 pp | ✅ |

**Key Findings:**
- All funnel stages show minor declines (-0.08 pp to -0.15 pp), indicating no isolated breakdown point—the small dip is distributed across the entire payment flow
- No country exceeded the ±2.5% threshold; US declined only -0.01 pp while CA improved +0.38 pp
- 8-week trend shows gradual decline from 92.27% (W11) to 92.11% (W18), representing a cumulative -0.16 pp drift over the period
- Payment methods and providers show no significant anomalies; "Unknown" provider and "Others" payment method declined -0.40 pp and -0.38 pp respectively, but remain within tolerance
- Mix shift analysis confirms stable volume distribution across AR tiers with no structural changes

**Action:** Monitor — Continue standard weekly observation. The change is not statistically significant and no dimensional anomalies were detected. Escalate only if the gradual downward trend continues beyond W20 or cumulative decline exceeds 0.5 pp from W11 baseline.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 92.11% | 506,463 | -0.09% ← REPORTED CHANGE |
| 2026-W17 | 92.19% | 510,064 | -0.12% |
| 2026-W16 | 92.3% | 513,372 | -0.12% |
| 2026-W15 | 92.41% | 497,776 | +0.27% |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | -0.15% |
| 2026-W11 | 92.27% | 539,763 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.98% | 92.99% | -0.01% | 516,129 |  |
| CA | 93.48% | 93.13% | +0.38% | 104,972 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.2% | 90.55% | -0.38% | 105,439 |  |
| Apple Pay | 86.41% | 86.55% | -0.16% | 67,968 |  |
| Credit Card | 93.43% | 93.43% | +0.00% | 271,280 |  |
| Paypal | 95.87% | 95.77% | +0.10% | 61,776 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 100.0% | nan% | +nan% | 1 |  |
| Unknown | 89.85% | 90.2% | -0.40% | 101,635 |  |
| Braintree | 92.62% | 92.67% | -0.05% | 375,399 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,459 |  |
| Adyen | 92.68% | 91.87% | +0.88% | 25,969 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.88% | 90.96% | -0.09% | 506,463 | 510,064 |  |
| 2_PreDunningAR | 92.11% | 92.19% | -0.08% | 506,463 | 510,064 |  |
| 3_PostDunningAR | 93.24% | 93.38% | -0.15% | 506,463 | 510,064 |  |
| 6_PaymentApprovalRate | 93.93% | 94.02% | -0.10% | 506,463 | 510,064 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 508,019 | 516,129 | +1.6% | Stable |
| CA | High (>92%) | 104,317 | 104,972 | +0.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
