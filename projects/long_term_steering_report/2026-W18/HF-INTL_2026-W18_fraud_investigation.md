# Fraud Investigation: HF-INTL 2026-W18

**Metric:** Fraud Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 92.13% → 91.87% (-0.28%)  
**Volume:** 42,018 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined marginally from 92.13% to 91.87% (-0.26pp) in 2026-W18, a change that is **not statistically significant** and remains within the normal 8-week fluctuation range (91.66% - 92.13%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | -0.28% WoW | -0.26pp | ✅ |
| L1: Country Variance | 4 countries exceed ±2.5% threshold | IE, DK, NZ, LU flagged | ⚠️ |
| L1: Channel Category | Paid -0.11%, Referral +0.46% | Minimal movement | ✅ |
| L2: Referral Channel | Multiple countries show large swings | Low volume, high volatility | ⚠️ |

**Key Findings:**
- **IE Referral decline:** FAR dropped -4.30% driven by Dup Rate increase (+22.22%) and Dup Block increase (+20.86%), indicating elevated duplicate submission activity in the referral channel
- **DK, NO, NZ, LU Referral improvements:** All showed FAR gains of +13.73%, +13.20%, +14.68%, and +48.87% respectively, primarily driven by reduced Dup Block rates—suggesting fewer duplicate submissions or policy changes
- **AU Paid channel concern:** PF Block spiked +228.89% (from 1.21% to 3.99%), causing FAR to drop -2.41% despite stable Dup metrics
- **GB Referral deterioration:** FAR fell -5.99% with Dup Block increasing +19.42%, representing the largest absolute volume impact among flagged segments (2,284 customers)
- **Referral channel volatility:** All flagged movements are isolated to the Referral channel, which has inherently lower volumes and higher week-over-week variance

**Action:** **Monitor** — The overall FAR change is not significant. Country-level movements are concentrated in the low-volume Referral channel where small absolute changes create large percentage swings. Continue standard monitoring; no escalation required unless AU PF Block elevation persists into W19.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W18 | 91.87% | 34.17% | 6.55% | 0.59% | 42,018 | -0.28% ← REPORTED CHANGE |
| 2026-W17 | 92.13% | 34.47% | 6.23% | 0.32% | 41,790 | +0.13% |
| 2026-W16 | 92.01% | 33.04% | 6.55% | 0.24% | 45,000 | -0.12% |
| 2026-W15 | 92.12% | 30.73% | 6.58% | 0.24% | 42,725 | +0.50% |
| 2026-W14 | 91.66% | 29.86% | 6.89% | 0.22% | 37,142 | -0.12% |
| 2026-W13 | 91.76% | 30.33% | 6.43% | 0.26% | 46,616 | -0.20% |
| 2026-W12 | 91.95% | 30.48% | 6.73% | 0.19% | 44,668 | +0.24% |
| 2026-W11 | 91.73% | 29.82% | 7.02% | 0.15% | 49,889 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| GB | 2026-W17 | 93.20% | - | 43.15% | - | 11,596 |  |
| GB | 2026-W18 | 92.55% | -0.70% | 44.20% | +2.44% | 11,628 |  |
| AU | 2026-W17 | 91.15% | - | 38.46% | - | 3,684 |  |
| AU | 2026-W18 | 89.53% | -1.78% | 38.78% | +0.82% | 3,734 |  |
| BE | 2026-W17 | 95.42% | - | 17.31% | - | 2,184 |  |
| BE | 2026-W18 | 97.36% | +2.03% | 16.13% | -6.82% | 2,195 |  |
| IE | 2026-W17 | 92.28% | - | 23.49% | - | 1,775 |  |
| IE | 2026-W18 | 89.48% | -3.03% | 26.06% | +10.92% | 1,512 | ⚠️ |
| DK | 2026-W17 | 92.28% | - | 33.04% | - | 1,153 |  |
| DK | 2026-W18 | 95.21% | +3.17% | 31.15% | -5.73% | 1,252 | ⚠️ |
| NZ | 2026-W17 | 85.87% | - | 38.04% | - | 757 |  |
| NZ | 2026-W18 | 88.77% | +3.38% | 37.40% | -1.68% | 917 | ⚠️ |
| LU | 2026-W17 | 86.25% | - | 0.00% | - | 80 |  |
| LU | 2026-W18 | 91.09% | +5.61% | 10.89% | - | 101 | ⚠️ |

**Countries exceeding ±2.5% threshold:** IE, DK, NZ, LU

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 97.54% | - | 35.38% | - | 32,019 |  |
| Paid | 2026-W18 | 97.43% | -0.11% | 34.98% | -1.13% | 31,723 |  |
| Referral | 2026-W17 | 74.41% | - | 31.51% | - | 9,771 |  |
| Referral | 2026-W18 | 74.75% | +0.46% | 31.69% | +0.58% | 10,295 |  |

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 96.97% | - | 38.44% | - | 0.88% | - | 1.21% | - | 2,966 |  |
| Paid | 2026-W18 | 94.63% | -2.41% | 38.64% | +0.54% | 0.70% | -19.64% | 3.99% | +228.89% | 2,981 |  |
| Referral | 2026-W17 | 67.13% | - | 38.58% | - | 29.94% | - | 0.28% | - | 718 |  |
| Referral | 2026-W18 | 69.32% | +3.26% | 39.31% | +1.89% | 28.02% | -6.42% | 0.27% | -4.65% | 753 | ⚠️ |

**Analysis:** The -0.28% decline in HF-INTL Fraud Approval Rate represents normal operational variance within historical bounds. The flagged country movements (IE, DK, NZ, LU) are entirely attributable to the Referral channel, which represents only ~25% of total volume and exhibits expected volatility at smaller sample sizes. The only metric warranting continued observation is AU's PF Block rate spike in the Paid channel (+228.89%), which should be monitored for persistence in the coming week.

---

## L2: BE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 98.36% | - | 14.54% | - | 0.11% | - | 0.16% | - | 1,829 |  |
| Paid | 2026-W18 | 99.26% | +0.91% | 14.47% | -0.52% | 0.11% | -2.71% | 0.16% | -2.71% | 1,880 |  |
| Referral | 2026-W17 | 80.28% | - | 31.55% | - | 16.06% | - | 0.28% | - | 355 |  |
| Referral | 2026-W18 | 86.03% | +7.16% | 26.03% | -17.49% | 10.79% | -32.78% | 0.00% | -100.00% | 315 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 96.38% | - | 9.42% | - | 0.00% | - | 0.72% | - | 138 |  |
| Paid | 2026-W18 | 95.80% | -0.60% | 11.76% | +24.89% | 0.00% | - | 0.00% | -100.00% | 119 |  |
| Referral | 2026-W17 | 48.28% | - | 24.14% | - | 20.69% | - | 0.00% | - | 29 |  |
| Referral | 2026-W18 | 50.00% | +3.57% | 17.86% | -26.02% | 17.86% | -13.69% | 3.57% | - | 28 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 99.12% | - | 33.25% | - | 0.38% | - | 0.13% | - | 797 |  |
| Paid | 2026-W18 | 98.93% | -0.19% | 34.88% | +4.89% | 0.36% | -5.46% | 0.24% | +89.09% | 843 |  |
| Referral | 2026-W17 | 76.97% | - | 32.58% | - | 20.51% | - | 0.00% | - | 356 |  |
| Referral | 2026-W18 | 87.53% | +13.73% | 23.47% | -27.97% | 10.76% | -47.54% | 0.00% | - | 409 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GB Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 98.41% | - | 44.41% | - | 0.58% | - | 0.43% | - | 9,268 |  |
| Paid | 2026-W18 | 98.52% | +0.11% | 44.88% | +1.07% | 0.66% | +13.88% | 0.30% | -30.57% | 9,344 |  |
| Referral | 2026-W17 | 72.47% | - | 38.14% | - | 25.77% | - | 0.04% | - | 2,328 |  |
| Referral | 2026-W18 | 68.13% | -5.99% | 41.42% | +8.58% | 30.78% | +19.42% | 0.13% | +205.78% | 2,284 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: IE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 98.71% | - | 23.06% | - | 0.30% | - | 0.00% | - | 1,314 |  |
| Paid | 2026-W18 | 98.53% | -0.18% | 24.04% | +4.27% | 0.79% | +157.90% | 0.20% | - | 1,019 |  |
| Referral | 2026-W17 | 73.97% | - | 24.73% | - | 22.99% | - | 0.00% | - | 461 |  |
| Referral | 2026-W18 | 70.79% | -4.30% | 30.22% | +22.22% | 27.79% | +20.86% | 0.00% | - | 493 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 100.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 62 |  |
| Paid | 2026-W18 | 98.78% | -1.22% | 13.41% | - | 0.00% | - | 1.22% | - | 82 |  |
| Referral | 2026-W17 | 38.89% | - | 0.00% | - | 5.56% | - | 0.00% | - | 18 |  |
| Referral | 2026-W18 | 57.89% | +48.87% | 0.00% | - | 0.00% | -100.00% | 0.00% | - | 19 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 99.65% | - | 31.25% | - | 0.17% | - | 0.00% | - | 576 |  |
| Paid | 2026-W18 | 99.12% | -0.53% | 25.96% | -16.91% | 0.53% | +203.16% | 0.00% | - | 570 |  |
| Referral | 2026-W17 | 79.83% | - | 24.03% | - | 15.45% | - | 0.00% | - | 233 |  |
| Referral | 2026-W18 | 90.37% | +13.20% | 15.14% | -37.02% | 5.05% | -67.34% | 0.00% | - | 218 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 97.44% | - | 36.45% | - | 0.18% | - | 1.47% | - | 546 |  |
| Paid | 2026-W18 | 97.35% | -0.09% | 36.76% | +0.87% | 0.59% | +221.18% | 1.47% | +0.37% | 680 |  |
| Referral | 2026-W17 | 55.92% | - | 42.18% | - | 38.39% | - | 0.47% | - | 211 |  |
| Referral | 2026-W18 | 64.14% | +14.68% | 39.24% | -6.97% | 31.22% | -18.66% | 0.42% | -10.97% | 237 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| IE | ↓ -3.03% | Referral ↓ -4.30% | ↑ +10.92% | ↑ +54.75% | → - | [AI_SUMMARY_PLACEHOLDER] |
| DK | ↑ +3.17% | Referral ↑ +13.73% | ↓ -5.73% | ↓ -43.05% | ↑ +84.19% | [AI_SUMMARY_PLACEHOLDER] |
| NZ | ↑ +3.38% | Referral ↑ +14.68% | → -1.68% | ↓ -21.48% | → +0.90% | [AI_SUMMARY_PLACEHOLDER] |
| LU | ↑ +5.61% | Referral ↑ +48.87% | → - | ↓ -100.00% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-05*
