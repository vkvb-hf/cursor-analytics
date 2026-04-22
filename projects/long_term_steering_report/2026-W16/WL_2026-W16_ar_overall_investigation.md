# AR Overall Investigation: WL 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.1% → 90.03% (-0.08%)  
**Volume:** 164,785 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined marginally from 90.1% to 90.03% (-0.07 pp) in W16, a change that is not statistically significant given the volume of 164,785 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.11 pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.08 pp | ✅ |
| 3_PostDunningAR | Recovery | -0.13 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.04 pp | ✅ |

**Key Findings:**
- **8-week trend is positive:** Rate improved from 88.19% (W09) to 90.03% (W16), representing a +1.84 pp gain over the period despite the minor W16 dip
- **No country breached threshold:** All countries remained within ±2.5% tolerance; KN showed the largest decline at -1.06 pp (87.81%) but did not trigger escalation
- **Payment Provider anomaly flagged:** "Unknown" provider showed +2.58 pp change (96.99% → 99.49%) but represents minimal volume (1,378 orders)
- **Mix shift neutral:** GN volume increased +17.8% week-over-week, but as a High AR tier country (94.19%), this positively supports overall rates
- **All funnel steps moving in parallel:** Slight declines across FirstRunAR, PreDunningAR, and PostDunningAR suggest no isolated bottleneck

**Action:** **Monitor** — Continue standard weekly tracking. No investigation or escalation required as the change is not significant and the 8-week trend remains healthy.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 90.03% | 164,785 | -0.08% ← REPORTED CHANGE |
| 2026-W15 | 90.1% | 160,979 | +0.87% |
| 2026-W14 | 89.32% | 165,018 | -0.45% |
| 2026-W13 | 89.72% | 169,667 | +0.08% |
| 2026-W12 | 89.65% | 169,891 | -0.14% |
| 2026-W11 | 89.78% | 174,933 | +0.79% |
| 2026-W10 | 89.08% | 179,965 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.81% | 88.75% | -1.06% | 11,057 |  |
| MR | 80.82% | 81.37% | -0.68% | 18,584 |  |
| CK | 93.32% | 93.91% | -0.63% | 43,017 |  |
| AO | 87.79% | 87.06% | +0.83% | 14,640 |  |
| GN | 94.19% | 93.32% | +0.94% | 15,445 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.03% | 95.25% | -0.23% | 24,589 |  |
| Credit Card | 89.45% | 89.65% | -0.22% | 116,930 |  |
| Apple Pay | 86.42% | 86.04% | +0.45% | 21,131 |  |
| Others | 99.44% | 98.21% | +1.26% | 2,135 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 81.23% | 81.62% | -0.48% | 17,167 |  |
| Adyen | 90.35% | 90.56% | -0.23% | 38,434 |  |
| Braintree | 91.13% | 91.25% | -0.13% | 107,117 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 689 |  |
| Unknown | 99.49% | 96.99% | +2.58% | 1,378 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.07% | 88.17% | -0.11% | 164,785 | 160,979 |  |
| 2_PreDunningAR | 90.03% | 90.1% | -0.08% | 164,785 | 160,979 |  |
| 3_PostDunningAR | 91.1% | 91.21% | -0.13% | 164,785 | 160,979 |  |
| 6_PaymentApprovalRate | 91.69% | 91.65% | +0.04% | 164,785 | 160,979 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 68,811 | 69,808 | +1.4% | Stable |
| CG | High (>92%) | 43,937 | 42,996 | -2.1% | Stable |
| CK | High (>92%) | 42,398 | 43,017 | +1.5% | Stable |
| MR | Low (>85%) | 19,468 | 18,584 | -4.5% | Stable |
| AO | Medium (>85%) | 13,883 | 14,640 | +5.5% | Stable |
| GN | High (>92%) | 13,110 | 15,445 | +17.8% | Stable |
| KN | Medium (>85%) | 10,259 | 11,057 | +7.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
