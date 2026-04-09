# Fraud Investigation: WL 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.73% → 93.06% (+0.35%)  
**Volume:** 13,609 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 92.73% to 93.06% (+0.33pp), a change that is not statistically significant, with volume decreasing from 14,394 to 13,609 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | 92.73% → 93.06% | +0.33pp | ✅ |
| L0: Duplicate Rate | 15.53% → 15.81% | +0.28pp | ✅ |
| L0: Duplicate Block | 5.07% → 5.25% | +0.18pp | ✅ |
| L0: PF Block | 0.80% → 0.84% | +0.04pp | ✅ |
| L1: Country - KN | 92.92% → 90.22% | -2.70pp | ⚠️ |
| L1: Channel - Paid | 96.07% → 96.34% | +0.27pp | ✅ |
| L1: Channel - Referral | 76.10% → 75.04% | -1.06pp | ✅ |

**Key Findings:**
- KN is the only country exceeding the ±2.5% threshold, with FAR declining -2.90% (90.22%) and duplicate rate spiking +32.40% (from 6.90% to 9.13%)
- Overall volume continues a declining trend, dropping from 14,394 to 13,609 (-5.5% WoW), part of a sustained decrease from 19,099 in W07
- CK showed the strongest improvement at +2.49pp FAR (94.02%), accompanied by a -6.67% reduction in duplicate rate
- Referral channel maintains significantly lower FAR (75.04%) compared to Paid channel (96.34%), with increasing duplicate rates (+4.12%)
- PF Block rate remains stable at historically low levels (0.84%) after the anomaly in W07 (5.17%)

**Action:** Monitor – The overall change is not significant and metrics are within normal ranges. However, recommend focused monitoring of KN due to the notable FAR decline and duplicate rate increase.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 93.06% | 15.81% | 5.25% | 0.84% | 13,609 | +0.35% ← REPORTED CHANGE |
| 2026-W13 | 92.73% | 15.53% | 5.07% | 0.80% | 14,394 | -0.32% |
| 2026-W12 | 93.03% | 15.96% | 4.88% | 0.43% | 15,081 | -1.35% |
| 2026-W11 | 94.31% | 14.77% | 4.13% | 0.35% | 16,403 | +0.50% |
| 2026-W10 | 93.84% | 15.79% | 4.48% | 0.45% | 17,316 | +0.41% |
| 2026-W09 | 93.46% | 15.27% | 4.66% | 0.54% | 16,428 | +0.09% |
| 2026-W08 | 93.37% | 15.19% | 4.89% | 0.49% | 16,797 | +4.50% |
| 2026-W07 | 89.36% | 14.40% | 4.28% | 5.17% | 19,099 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| KN | 2026-W13 | 92.92% | - | 6.90% | - | 2,696 |  |
| KN | 2026-W14 | 90.22% | -2.90% | 9.13% | +32.40% | 2,310 | ⚠️ |
| CK | 2026-W13 | 91.74% | - | 26.62% | - | 2,190 |  |
| CK | 2026-W14 | 94.02% | +2.49% | 24.84% | -6.67% | 2,576 |  |
| CG | 2026-W13 | 92.62% | - | 12.90% | - | 2,194 |  |
| CG | 2026-W14 | 93.52% | +0.98% | 12.63% | -2.05% | 2,145 |  |
| AO | 2026-W13 | 86.17% | - | 26.34% | - | 1,063 |  |
| AO | 2026-W14 | 88.13% | +2.28% | 26.84% | +1.91% | 868 |  |

**Countries exceeding ±2.5% threshold:** KN

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W13 | 96.07% | - | 13.56% | - | 11,988 |  |
| Paid | 2026-W14 | 96.34% | +0.28% | 13.87% | +2.29% | 11,510 |  |
| Referral | 2026-W13 | 76.10% | - | 25.39% | - | 2,406 |  |
| Referral | 2026-W14 | 75.04% | -1.40% | 26.44% | +4.12% | 2,099 |  |

---

*Report: 2026-04-09*
