# Fraud Investigation: WL 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 92.89% → 93.41% (+0.57%)  
**Volume:** 15,464 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) improved slightly from 92.89% to 93.41% (+0.52pp) week-over-week, though this change is not statistically significant and remains within normal 8-week operating range (93.37%-94.33%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL 8-Week Trend | FAR within normal range | +0.52pp | ✅ |
| L1: Country Scan | No country exceeds ±2.5% threshold | Max: MR +2.25% | ✅ |
| L1: Channel Category | Paid & Referral stable | +0.60%, +0.65% | ✅ |
| L2: AO Referral | FAR increased significantly | +8.44% | ⚠️ |
| L2: CK Referral | FAR declined | -2.96% | ⚠️ |
| L2: MR Paid | FAR increased above threshold | +2.53% | ⚠️ |
| L2: MR Referral | FAR declined significantly | -4.16% | ⚠️ |

**Key Findings:**
- MR shows divergent channel behavior: Paid FAR improved +2.53% (to 97.96%) while Referral FAR declined -4.16% (to 83.77%), with Referral duplicate rates spiking +35.83%
- Referral channel shows elevated duplicate blocking across multiple countries: CK (30.13%), AO (28.66%), KN (19.43%), indicating potential abuse patterns
- CK Referral FAR declined -2.96% with duplicate rate increasing +10.63% and duplicate blocks rising +16.04%
- Overall volume increased +16.4% (13,283 → 15,464), primarily driven by MR (+36.8%) and KN (+23.6%)
- KN Paid channel shows +1136% increase in PF Block rate (0.05% → 0.59%), though absolute impact remains small

**Action:** Monitor — No immediate escalation required. Changes are not statistically significant at the aggregate level. Continue monitoring MR Referral channel for sustained duplicate rate elevation and CK Referral for potential further FAR degradation.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 93.41% | 16.06% | 5.23% | 0.70% | 15,464 | +0.57% ← REPORTED CHANGE |
| 2026-W14 | 92.89% | 15.35% | 4.94% | 0.84% | 13,283 | +0.20% |
| 2026-W13 | 92.70% | 15.48% | 5.02% | 0.79% | 14,390 | -0.33% |
| 2026-W12 | 93.01% | 15.91% | 4.83% | 0.42% | 15,076 | -1.40% |
| 2026-W11 | 94.33% | 14.73% | 4.09% | 0.35% | 16,397 | +0.54% |
| 2026-W10 | 93.83% | 15.77% | 4.46% | 0.45% | 17,315 | +0.38% |
| 2026-W09 | 93.47% | 15.24% | 4.63% | 0.54% | 16,426 | +0.11% |
| 2026-W08 | 93.37% | 15.18% | 4.88% | 0.49% | 16,796 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| MR | 2026-W14 | 95.02% | - | 5.87% | - | 2,010 |  |
| MR | 2026-W15 | 97.16% | +2.25% | 4.73% | -19.45% | 2,749 |  |
| KN | 2026-W14 | 90.20% | - | 8.20% | - | 2,244 |  |
| KN | 2026-W15 | 91.46% | +1.40% | 7.97% | -2.84% | 2,774 |  |
| ER | 2026-W14 | 93.72% | - | 20.00% | - | 2,390 |  |
| ER | 2026-W15 | 92.98% | -0.79% | 22.44% | +12.20% | 2,607 |  |
| CK | 2026-W14 | 93.71% | - | 24.50% | - | 2,498 |  |
| CK | 2026-W15 | 93.00% | -0.76% | 28.02% | +14.37% | 2,673 |  |
| AO | 2026-W14 | 87.68% | - | 26.44% | - | 836 |  |
| AO | 2026-W15 | 89.14% | +1.66% | 26.50% | +0.23% | 902 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.06% | - | 13.54% | - | 11,220 |  |
| Paid | 2026-W15 | 96.63% | +0.60% | 14.27% | +5.39% | 13,036 |  |
| Referral | 2026-W14 | 75.62% | - | 25.21% | - | 2,063 |  |
| Referral | 2026-W15 | 76.11% | +0.65% | 25.70% | +1.96% | 2,428 |  |

---

## L2: AO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.89% | - | 21.75% | - | 0.18% | - | 0.00% | - | 570 |  |
| Paid | 2026-W15 | 98.97% | +1.10% | 23.41% | +7.60% | 0.00% | -100.00% | 0.00% | - | 581 |  |
| Referral | 2026-W14 | 65.79% | - | 36.47% | - | 33.83% | - | 0.00% | - | 266 |  |
| Referral | 2026-W15 | 71.34% | +8.44% | 32.09% | -12.01% | 28.66% | -15.29% | 0.00% | - | 321 | ⚠️ |

**Analysis:** The +0.52pp FAR improvement in WL for 2026-W15 reflects normal week-over-week variation within established operating parameters. While L2 analysis reveals some channel-specific volatility—particularly in MR and CK Referral segments—these movements do not materially impact the aggregate metric and no countries breached the ±2.5% significance threshold. Continued monitoring of Referral channel duplicate patterns across markets is recommended, with no immediate action required.

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 95.86% | - | 11.01% | - | 1.57% | - | 1.75% | - | 1,716 |  |
| Paid | 2026-W15 | 95.03% | -0.87% | 12.27% | +11.36% | 2.32% | +47.48% | 1.99% | +13.77% | 1,810 |  |
| Referral | 2026-W14 | 81.65% | - | 17.82% | - | 15.69% | - | 0.53% | - | 376 |  |
| Referral | 2026-W15 | 84.22% | +3.15% | 16.04% | -9.97% | 13.37% | -14.80% | 0.80% | +50.80% | 374 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 98.64% | - | 23.36% | - | 0.15% | - | 0.10% | - | 2,059 |  |
| Paid | 2026-W15 | 98.93% | +0.30% | 26.81% | +14.77% | 0.28% | +91.36% | 0.05% | -52.16% | 2,152 |  |
| Referral | 2026-W14 | 70.62% | - | 29.84% | - | 25.97% | - | 0.00% | - | 439 |  |
| Referral | 2026-W15 | 68.52% | -2.96% | 33.01% | +10.63% | 30.13% | +16.04% | 0.00% | - | 521 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 91.05% | - | 7.20% | - | 6.39% | - | 0.05% | - | 2,112 |  |
| Paid | 2026-W15 | 92.35% | +1.43% | 6.98% | -2.96% | 6.09% | -4.78% | 0.59% | +1136.05% | 2,563 |  |
| Referral | 2026-W14 | 76.52% | - | 24.24% | - | 22.73% | - | 0.00% | - | 132 |  |
| Referral | 2026-W15 | 80.57% | +5.30% | 19.91% | -17.89% | 19.43% | -14.50% | 0.00% | - | 211 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: MR Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 95.54% | - | 5.36% | - | 0.05% | - | 3.19% | - | 1,883 |  |
| Paid | 2026-W15 | 97.96% | +2.53% | 3.93% | -26.72% | 0.00% | -100.00% | 1.50% | -52.83% | 2,595 | ⚠️ |
| Referral | 2026-W14 | 87.40% | - | 13.39% | - | 10.24% | - | 2.36% | - | 127 |  |
| Referral | 2026-W15 | 83.77% | -4.16% | 18.18% | +35.83% | 14.29% | +39.56% | 1.30% | -45.02% | 154 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-17*
