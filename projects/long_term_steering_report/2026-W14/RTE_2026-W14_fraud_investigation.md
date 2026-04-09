# Fraud Investigation: RTE 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.14% → 94.72% (+0.61%)  
**Volume:** 42,650 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The Fraud Approval Rate improved from 94.14% to 94.72% (+0.58 pp), remaining within normal 8-week fluctuation range and flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within historical range (93.82%-94.95%) | +0.61% | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (TO, TK) | TO: -4.22%, TK: +5.01% | ⚠️ |
| L1: Channel Category | Both channels within threshold | Paid: +1.00%, Referral: -1.15% | ✅ |
| Duplicate Rate | Overall slight decrease | -0.19 pp (14.50%→14.31%) | ✅ |
| Duplicate Block Rate | Slight increase | +0.40 pp (4.06%→4.46%) | ✅ |

**Key Findings:**
- FJ (largest market, 70% of volume) drove the overall FAR improvement with +1.11 pp increase (94.47%→95.51%) while duplicate rate decreased by 2.85%
- TO showed significant decline in FAR (-4.22 pp to 88.60%) coupled with a 70.52% spike in duplicate rate (6.99%→11.92%), though volume is low (579 customers)
- TK showed strong FAR improvement (+5.01 pp to 92.86%) with duplicate rate dropping 37.46%, but volume is minimal (336 customers)
- Overall volume declined 3% week-over-week (43,962→42,650 customers)
- Paid channel outperforms Referral significantly (97.60% vs 81.40% FAR) with Referral showing elevated duplicate rates (+8.01% increase to 22.61%)

**Action:** Monitor — The overall change is not significant and driven by positive movement in the largest market (FJ). Continue monitoring TO for potential duplicate rate issues, but low volume does not warrant immediate escalation.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 94.72% | 14.31% | 4.46% | 0.20% | 42,650 | +0.61% ← REPORTED CHANGE |
| 2026-W13 | 94.14% | 14.50% | 4.06% | 0.26% | 43,962 | +0.34% |
| 2026-W12 | 93.82% | 14.53% | 4.28% | 0.22% | 45,581 | -0.63% |
| 2026-W11 | 94.41% | 14.54% | 3.91% | 0.21% | 48,713 | -0.57% |
| 2026-W10 | 94.95% | 13.98% | 3.74% | 0.16% | 50,499 | +0.53% |
| 2026-W09 | 94.45% | 14.28% | 4.09% | 0.22% | 51,707 | +0.43% |
| 2026-W08 | 94.05% | 14.98% | 4.35% | 0.12% | 48,963 | -0.20% |
| 2026-W07 | 94.25% | 14.89% | 4.17% | 0.12% | 50,465 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W13 | 94.47% | - | 14.88% | - | 30,231 |  |
| FJ | 2026-W14 | 95.51% | +1.11% | 14.45% | -2.85% | 29,804 |  |
| CF | 2026-W13 | 94.14% | - | 13.47% | - | 6,672 |  |
| CF | 2026-W14 | 93.52% | -0.66% | 13.48% | +0.04% | 6,632 |  |
| TO | 2026-W13 | 92.50% | - | 6.99% | - | 787 |  |
| TO | 2026-W14 | 88.60% | -4.22% | 11.92% | +70.52% | 579 | ⚠️ |
| YE | 2026-W13 | 94.01% | - | 18.55% | - | 3,839 |  |
| YE | 2026-W14 | 93.50% | -0.54% | 18.29% | -1.41% | 3,418 |  |
| TT | 2026-W13 | 91.28% | - | 8.53% | - | 1,055 |  |
| TT | 2026-W14 | 89.32% | -2.14% | 10.56% | +23.82% | 871 |  |
| TK | 2026-W13 | 88.42% | - | 11.90% | - | 311 |  |
| TK | 2026-W14 | 92.86% | +5.01% | 7.44% | -37.46% | 336 | ⚠️ |
| TV | 2026-W13 | 90.91% | - | 7.79% | - | 462 |  |
| TV | 2026-W14 | 93.08% | +2.38% | 8.21% | +5.30% | 390 |  |

**Countries exceeding ±2.5% threshold:** TO, TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W13 | 96.63% | - | 13.14% | - | 36,315 |  |
| Paid | 2026-W14 | 97.60% | +1.00% | 12.52% | -4.75% | 35,066 |  |
| Referral | 2026-W13 | 82.35% | - | 20.94% | - | 7,647 |  |
| Referral | 2026-W14 | 81.40% | -1.15% | 22.61% | +8.01% | 7,584 |  |

---

*Report: 2026-04-09*
