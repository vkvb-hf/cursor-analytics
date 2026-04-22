# Fraud Investigation: WL 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 93.28% → 92.95% (-0.35%)  
**Volume:** 14,308 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 93.28% to 92.95% (-0.33pp) in 2026-W16, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | FAR within 8-week range (92.70%-94.33%) | -0.33pp | ✅ |
| L1: Country Scan | No country exceeds ±2.5% threshold | Max: ER +1.37% | ✅ |
| L1: Channel Category | Referral underperforms Paid | -1.82pp vs -0.18pp | ✅ |
| L2: CG Referral | Elevated Dup Rate & Dup Block | +26.37%, +45.95% | ⚠️ |
| L2: KN Referral | Severe FAR decline, Dup Rate spike | -16.91pp, +91.81% | ⚠️ |

**Key Findings:**
- KN Referral channel experienced a sharp FAR decline of -16.91pp (84.54% → 70.25%) driven by Duplicate Rate nearly doubling (+91.81%) and Duplicate Block Rate surging +76.42%
- CG Referral channel showed elevated Duplicate activity with Dup Rate +26.37% and Dup Block +45.95%, resulting in FAR decline of -4.60pp
- Overall Referral channel across WL shows consistent underperformance vs Paid (75.50% vs 96.15% FAR) with higher duplicate rates (26.62% vs 15.40%)
- ER showed positive movement with FAR improving +1.37pp, partially offsetting declines in other countries
- Total volume decreased by 5.5% (15,142 → 14,308), with KN showing the largest proportional drop (-14.2%)

**Action:** Monitor – The aggregate WL change is non-significant; however, closely monitor KN Referral channel for continued duplicate activity spikes. If KN Referral Dup Rate remains elevated (>25%) for 2+ consecutive weeks, escalate for fraud pattern review.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 92.95% | 17.14% | 5.26% | 0.96% | 14,308 | -0.35% ← REPORTED CHANGE |
| 2026-W15 | 93.28% | 15.71% | 4.96% | 0.69% | 15,142 | +0.43% |
| 2026-W14 | 92.88% | 15.25% | 4.84% | 0.82% | 13,279 | +0.19% |
| 2026-W13 | 92.70% | 15.44% | 4.98% | 0.79% | 14,388 | -0.36% |
| 2026-W12 | 93.03% | 15.90% | 4.82% | 0.42% | 15,071 | -1.39% |
| 2026-W11 | 94.33% | 14.70% | 4.06% | 0.35% | 16,393 | +0.53% |
| 2026-W10 | 93.83% | 15.76% | 4.45% | 0.44% | 17,314 | +0.39% |
| 2026-W09 | 93.47% | 15.23% | 4.62% | 0.54% | 16,425 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| ER | 2026-W15 | 92.75% | - | 22.13% | - | 2,539 |  |
| ER | 2026-W16 | 94.02% | +1.37% | 22.92% | +3.56% | 2,408 |  |
| KN | 2026-W15 | 91.46% | - | 7.28% | - | 2,706 |  |
| KN | 2026-W16 | 90.66% | -0.88% | 9.08% | +24.77% | 2,323 |  |
| MR | 2026-W15 | 96.87% | - | 4.59% | - | 2,748 |  |
| MR | 2026-W16 | 96.19% | -0.70% | 5.52% | +20.29% | 2,230 |  |
| CK | 2026-W15 | 92.98% | - | 27.56% | - | 2,591 |  |
| CK | 2026-W16 | 92.37% | -0.65% | 28.31% | +2.71% | 2,413 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.33% | - | 14.09% | - | 12,766 |  |
| Paid | 2026-W16 | 96.15% | -0.18% | 15.40% | +9.27% | 12,092 |  |
| Referral | 2026-W15 | 76.89% | - | 24.41% | - | 2,376 |  |
| Referral | 2026-W16 | 75.50% | -1.82% | 26.62% | +9.07% | 2,216 |  |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 94.63% | - | 12.40% | - | 2.40% | - | 1.94% | - | 1,750 |  |
| Paid | 2026-W16 | 94.39% | -0.25% | 11.06% | -10.81% | 1.56% | -35.10% | 3.12% | +60.34% | 1,926 |  |
| Referral | 2026-W15 | 83.92% | - | 15.53% | - | 12.81% | - | 0.27% | - | 367 |  |
| Referral | 2026-W16 | 80.06% | -4.60% | 19.63% | +26.37% | 18.69% | +45.95% | 0.00% | -100.00% | 321 | ⚠️ |

**Analysis:** The 2026-W16 FAR decline of -0.33pp is not statistically significant and falls within normal operating range. The primary area of concern is the KN Referral channel, which exhibited anomalous duplicate behavior resulting in a 16.91pp FAR drop on low volume (121 customers). No immediate action is required at the aggregate level, but targeted monitoring of Referral channel duplicate patterns in KN and CG is recommended for the coming weeks.

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.57% | - | 21.23% | - | 2.27% | - | 0.48% | - | 2,068 |  |
| Paid | 2026-W16 | 97.16% | +0.61% | 22.52% | +6.09% | 1.69% | -25.46% | 0.70% | +44.26% | 2,007 |  |
| Referral | 2026-W15 | 76.01% | - | 26.11% | - | 22.93% | - | 0.42% | - | 471 |  |
| Referral | 2026-W16 | 78.30% | +3.02% | 24.94% | -4.51% | 21.45% | -6.47% | 0.00% | -100.00% | 401 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 92.04% | - | 6.56% | - | 5.64% | - | 0.60% | - | 2,499 |  |
| Paid | 2026-W16 | 91.78% | -0.28% | 7.90% | +20.41% | 6.86% | +21.54% | 0.36% | -39.47% | 2,202 |  |
| Referral | 2026-W15 | 84.54% | - | 15.94% | - | 15.46% | - | 0.00% | - | 207 |  |
| Referral | 2026-W16 | 70.25% | -16.91% | 30.58% | +91.81% | 27.27% | +76.42% | 1.65% | - | 121 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-22*
