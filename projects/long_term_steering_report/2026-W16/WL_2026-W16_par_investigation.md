# PAR Investigation: WL 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 91.65% → 91.69% (+0.04%)  
**Volume:** 164,785 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate showed a minimal increase from 91.65% to 91.69% (+0.04pp), a statistically non-significant change within normal operational variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within tolerance | -0.11pp | ✅ |
| 2_PreDunningAR | Within tolerance | -0.08pp | ✅ |
| 3_PostDunningAR | Within tolerance | -0.13pp | ✅ |
| 6_PaymentApprovalRate | Within tolerance | +0.04pp | ✅ |

**Key Findings:**
- The +0.04pp increase in Payment Approval Rate is not statistically significant; the metric remains stable at 91.69% on 164,785 orders
- No countries exceeded the ±2.5% threshold; KN showed the largest decline (-1.02pp to 88.90%) while GN showed the largest improvement (+1.08pp to 95.58%)
- PaymentProvider "Unknown" flagged with +2.58pp change, but represents minimal volume (1,378 orders, <1% of total)
- Upstream funnel metrics (FirstRunAR, PreDunningAR, PostDunningAR) all showed slight declines (-0.08pp to -0.13pp), offset by recovery mechanisms
- 8-week trend shows steady improvement from 89.92% (W09) to 91.69% (W16), indicating healthy long-term trajectory

**Action:** Monitor — No investigation required. The change is within normal variance, no dimensional breakdowns exceeded thresholds, and the 8-week trend remains positive.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.69% | 164,785 | +0.04% ← REPORTED CHANGE |
| 2026-W15 | 91.65% | 160,979 | +0.66% |
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,965 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 88.90% | 89.82% | -1.02% | 11,057 |  |
| CK | 95.41% | 95.88% | -0.48% | 43,017 |  |
| AO | 94.03% | 93.21% | +0.87% | 14,640 |  |
| GN | 95.58% | 94.56% | +1.08% | 15,445 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.91% | 96.03% | -0.13% | 24,589 |  |
| Credit Card | 91.35% | 91.41% | -0.06% | 116,930 |  |
| Apple Pay | 87.88% | 87.44% | +0.51% | 21,131 |  |
| Others | 99.58% | 98.35% | +1.25% | 2,135 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 82.29% | 82.67% | -0.46% | 17,167 |  |
| Adyen | 94.08% | 94.13% | -0.05% | 38,434 |  |
| Braintree | 92.18% | 92.22% | -0.03% | 107,117 |  |
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
| AO | High (>92%) | 13,883 | 14,640 | +5.5% | Stable |
| GN | High (>92%) | 13,110 | 15,445 | +17.8% | Stable |
| KN | Medium (>85%) | 10,259 | 11,057 | +7.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
