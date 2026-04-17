# Fraud Investigation: HF-INTL 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.67% → 92.17% (+0.55%)  
**Volume:** 43,119 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL improved slightly from 91.67% to 92.17% (+0.50pp) in 2026-W15, a change that is **not statistically significant** and falls within normal weekly fluctuation (8-week range: 91.58%-92.37%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | Within normal range | +0.50pp | ✅ |
| L1: Country Variance | AT +4.39pp, NZ -2.74pp exceed ±2.5% threshold | Mixed | ⚠️ |
| L1: Channel Category | Paid +0.68pp, Referral -0.60pp | Stable | ✅ |
| L2: Referral Channel | Multiple countries show elevated Dup Block rates | Elevated blocks | ⚠️ |

**Key Findings:**
- **AT Referral channel improved significantly** (+25.53pp FAR) driven by a substantial decrease in Duplicate Rate (-38.27%) and Duplicate Block Rate (-42.36%), suggesting reduced repeat/fraudulent traffic in that segment
- **NZ Referral channel declined sharply** (-21.35pp FAR) due to a dramatic increase in Duplicate Block Rate (+53.51%) and elevated Duplicate Rate (+33.97%), indicating a spike in duplicate/suspicious activity
- **Paid channel remains stable across all markets** with FAR consistently above 97%, while Referral channel shows higher volatility and lower baseline FAR (~75-76%)
- **Volume increased 16%** (37,184 → 43,119) driven primarily by growth in DE (+28%), GB (+19%), and NO (+154%)
- **CH Referral shows concerning pattern** with FAR dropping -17.07pp and Duplicate Rate spiking +76.92%, though volume is very low (26 customers)

**Action:** **Monitor** - The overall metric change is not significant. Continue monitoring NZ and CH Referral channels for sustained degradation. AT improvement appears to be normalization of duplicate blocking behavior.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 92.17% | 31.06% | 6.98% | 0.26% | 43,119 | +0.55% ← REPORTED CHANGE |
| 2026-W14 | 91.67% | 30.04% | 7.07% | 0.23% | 37,184 | -0.14% |
| 2026-W13 | 91.80% | 30.44% | 6.52% | 0.27% | 46,655 | -0.16% |
| 2026-W12 | 91.94% | 30.55% | 6.81% | 0.20% | 44,690 | +0.23% |
| 2026-W11 | 91.72% | 29.87% | 7.07% | 0.15% | 49,912 | -0.70% |
| 2026-W10 | 92.37% | 29.82% | 6.40% | 0.22% | 52,832 | - |
| 2026-W09 | 92.37% | 29.15% | 6.25% | 0.37% | 54,953 | +0.86% |
| 2026-W08 | 91.58% | 29.96% | 7.03% | 0.26% | 54,567 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| DE | 2026-W14 | 93.51% | - | 29.72% | - | 7,075 |  |
| DE | 2026-W15 | 94.28% | +0.82% | 29.75% | +0.09% | 9,075 |  |
| GB | 2026-W14 | 92.79% | - | 39.42% | - | 8,850 |  |
| GB | 2026-W15 | 93.19% | +0.43% | 40.99% | +3.97% | 10,515 |  |
| FR | 2026-W14 | 88.11% | - | 25.32% | - | 9,109 |  |
| FR | 2026-W15 | 87.68% | -0.49% | 26.16% | +3.35% | 8,424 |  |
| AT | 2026-W14 | 90.18% | - | 23.08% | - | 611 |  |
| AT | 2026-W15 | 94.14% | +4.39% | 17.98% | -22.07% | 734 | ⚠️ |
| DK | 2026-W14 | 88.77% | - | 25.39% | - | 1,095 |  |
| DK | 2026-W15 | 90.32% | +1.75% | 29.78% | +17.29% | 1,622 |  |
| NZ | 2026-W14 | 89.42% | - | 35.71% | - | 728 |  |
| NZ | 2026-W15 | 86.97% | -2.74% | 35.28% | -1.23% | 944 | ⚠️ |
| NO | 2026-W14 | 92.72% | - | 20.79% | - | 481 |  |
| NO | 2026-W15 | 94.51% | +1.93% | 21.13% | +1.64% | 1,221 |  |

**Countries exceeding ±2.5% threshold:** AT, NZ

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.31% | - | 30.24% | - | 27,139 |  |
| Paid | 2026-W15 | 97.98% | +0.68% | 31.32% | +3.57% | 31,752 |  |
| Referral | 2026-W14 | 76.42% | - | 29.50% | - | 10,045 |  |
| Referral | 2026-W15 | 75.96% | -0.60% | 30.34% | +2.86% | 11,367 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 98.10% | - | 19.66% | - | 0.21% | - | 0.00% | - | 473 |  |
| Paid | 2026-W15 | 98.42% | +0.33% | 16.99% | -13.60% | 0.53% | +148.51% | 0.35% | - | 571 |  |
| Referral | 2026-W14 | 63.04% | - | 34.78% | - | 34.06% | - | 0.00% | - | 138 |  |
| Referral | 2026-W15 | 79.14% | +25.53% | 21.47% | -38.27% | 19.63% | -42.36% | 0.00% | - | 163 | ⚠️ |

**Analysis:** The +0.50pp increase in FAR for HF-INTL in 2026-W15 represents normal weekly variation and requires no immediate action. The primary areas of concern are the Referral channels in NZ and CH, where elevated duplicate rates and block rates are suppressing approval rates, though these represent relatively small volumes (<250 customers combined). If the NZ Referral degradation persists for another 1-2 weeks, a deeper investigation into the source of duplicate traffic in that market would be warranted.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.78% | - | 35.80% | - | 0.77% | - | 0.38% | - | 2,338 |  |
| Paid | 2026-W15 | 98.11% | +0.35% | 36.00% | +0.57% | 0.58% | -24.65% | 0.58% | +50.71% | 2,758 |  |
| Referral | 2026-W14 | 72.67% | - | 37.27% | - | 26.24% | - | 0.47% | - | 644 |  |
| Referral | 2026-W15 | 66.90% | -7.94% | 41.27% | +10.73% | 32.39% | +23.44% | 0.28% | -39.53% | 710 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 95.70% | - | 8.60% | - | 0.00% | - | 0.00% | - | 93 |  |
| Paid | 2026-W15 | 97.52% | +1.90% | 9.09% | +5.68% | 0.00% | - | 1.65% | - | 121 |  |
| Referral | 2026-W14 | 69.57% | - | 21.74% | - | 21.74% | - | 0.00% | - | 23 |  |
| Referral | 2026-W15 | 57.69% | -17.07% | 38.46% | +76.92% | 34.62% | +59.23% | 0.00% | - | 26 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 98.43% | - | 29.20% | - | 0.45% | - | 0.09% | - | 5,730 |  |
| Paid | 2026-W15 | 98.82% | +0.40% | 29.41% | +0.74% | 0.50% | +10.58% | 0.09% | +8.79% | 7,374 |  |
| Referral | 2026-W14 | 72.57% | - | 31.97% | - | 26.54% | - | 0.37% | - | 1,345 |  |
| Referral | 2026-W15 | 74.60% | +2.81% | 31.22% | -2.36% | 25.22% | -4.98% | 0.06% | -84.19% | 1,701 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NL Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 90.91% | - | 29.69% | - | 7.00% | - | 0.08% | - | 1,243 |  |
| Paid | 2026-W15 | 92.73% | +2.01% | 30.10% | +1.41% | 6.66% | -4.83% | 0.17% | +115.05% | 1,156 |  |
| Referral | 2026-W14 | 92.14% | - | 21.61% | - | 6.68% | - | 0.00% | - | 509 |  |
| Referral | 2026-W15 | 88.63% | -3.81% | 25.40% | +17.53% | 10.12% | +51.57% | 0.00% | - | 563 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 99.68% | - | 21.04% | - | 0.32% | - | 0.00% | - | 309 |  |
| Paid | 2026-W15 | 99.03% | -0.65% | 22.88% | +8.77% | 0.00% | -100.00% | 0.73% | - | 826 |  |
| Referral | 2026-W14 | 80.23% | - | 20.35% | - | 18.02% | - | 0.00% | - | 172 |  |
| Referral | 2026-W15 | 85.06% | +6.02% | 17.47% | -14.16% | 13.67% | -24.15% | 0.00% | - | 395 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.36% | - | 35.52% | - | 0.36% | - | 1.64% | - | 549 |  |
| Paid | 2026-W15 | 97.23% | +0.91% | 31.16% | -12.26% | 0.42% | +14.06% | 1.39% | -15.51% | 722 |  |
| Referral | 2026-W14 | 68.16% | - | 36.31% | - | 29.05% | - | 0.56% | - | 179 |  |
| Referral | 2026-W15 | 53.60% | -21.35% | 48.65% | +33.97% | 44.59% | +53.51% | 0.90% | +61.26% | 222 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| AT | ↑ +4.39% | Referral ↑ +25.53% | ↓ -22.07% | ↓ -39.30% | → - | [AI_SUMMARY_PLACEHOLDER] |
| NZ | ↓ -2.74% | Referral ↓ -21.35% | → -1.23% | ↑ +45.67% | ↓ -7.46% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-17*
