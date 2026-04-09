# Fraud Investigation: WL 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.73% → 93.06% (+0.35%)  
**Volume:** 13,609 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 92.73% to 93.06% (+0.33pp), a non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | FAR within 8-week range (89.36%-94.31%) | +0.35pp | ✅ |
| L1: Country | KN exceeds ±2.5% threshold | -2.90pp | ⚠️ |
| L1: Channel | All channels within threshold | Paid +0.28pp, Referral -1.40pp | ✅ |
| Dup Rate | Elevated in KN | +32.40% relative increase | ⚠️ |
| PF Block | Slight increase | 0.80% → 0.84% | ✅ |

**Key Findings:**
- **KN country anomaly:** FAR dropped -2.90pp (92.92% → 90.22%) while duplicate rate spiked +32.40% (6.90% → 9.13%), suggesting potential fraud pattern or duplicate submission issue in KN
- **Volume decline:** Total fraud service volume decreased by 785 customers (14,394 → 13,609, -5.5% WoW), continuing a downward trend from W07 peak of 19,099
- **Dup Block Rate increasing:** Rose from 5.07% to 5.25% (+0.18pp), now at 8-week high, indicating more duplicate submissions being caught
- **Referral channel underperforms:** FAR at 75.04% vs Paid channel at 96.34%, with higher duplicate rates (26.44% vs 13.87%)

**Action:** **Monitor** – Overall FAR change is not significant, but recommend targeted monitoring of KN market due to FAR decline and duplicate rate spike. If KN trends persist for another week, escalate for deeper L2 investigation.

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
