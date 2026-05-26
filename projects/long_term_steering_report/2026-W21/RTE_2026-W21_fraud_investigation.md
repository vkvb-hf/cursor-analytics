# Fraud Investigation: RTE 2026-W21

**Metric:** Fraud Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 94.65% → 94.30% (-0.37%)  
**Volume:** 38,080 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by -0.37pp from 94.65% to 94.30% in 2026-W21, which is **not statistically significant** and remains within the normal 8-week fluctuation range (93.82% - 94.66%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | FAR within 8-week range | -0.37pp | ✅ |
| L1: Country Scan | TT, TK exceed ±2.5% threshold | TT -5.19pp, TK -3.22pp | ⚠️ |
| L1: Channel Category | Referral underperforms Paid | Referral -2.13pp vs Paid -0.11pp | ⚠️ |
| L2: TT Deep-Dive | Both channels declining, Dup Rate surge | Dup Rate +107.54% | ⚠️ |
| L2: TK Deep-Dive | Paid channel driving decline | Paid FAR -3.59pp, Dup Rate +25.22% | ⚠️ |

**Key Findings:**
- TT experienced the largest FAR decline (-5.19pp) driven by a **+107.54% surge in Duplicate Rate** and **+112.83% increase in Duplicate Blocks**, affecting both Paid (-4.19pp) and Referral (-9.33pp) channels
- TK Paid channel declined -3.59pp with Duplicate Rate increasing +25.22% and Duplicate Block Rate rising +26.60%, indicating potential duplicate fraud attempts
- Referral channel consistently underperforms across multiple countries (FJ -3.11pp, TO -5.86pp, TT -9.33pp) with elevated Duplicate Rates and Duplicate Blocks
- Overall volume decreased by 8.4% (41,569 → 38,080), which may amplify percentage fluctuations in smaller markets
- PF Block rates remain stable and low (0.27% → 0.32%), indicating no systemic policy filter issues

**Action:** **Monitor** - The overall RTE change is not significant. However, recommend focused monitoring of TT and TK duplicate detection patterns over the next 1-2 weeks to determine if the elevated Duplicate Rates represent a new fraud vector or transient behavior.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W21 | 94.30% | 15.88% | 4.61% | 0.32% | 38,080 | -0.37% ← REPORTED CHANGE |
| 2026-W20 | 94.65% | 15.15% | 4.13% | 0.27% | 41,569 | +0.66% |
| 2026-W19 | 94.03% | 14.07% | 4.00% | 0.25% | 40,948 | +0.23% |
| 2026-W18 | 93.82% | 14.47% | 3.81% | 0.24% | 42,219 | -0.15% |
| 2026-W17 | 93.96% | 16.37% | 4.54% | 0.35% | 44,533 | -0.38% |
| 2026-W16 | 94.31% | 15.40% | 4.21% | 0.31% | 45,908 | -0.37% |
| 2026-W15 | 94.66% | 14.48% | 4.01% | 0.30% | 45,705 | +0.02% |
| 2026-W14 | 94.64% | 13.97% | 4.04% | 0.18% | 41,350 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W20 | 95.59% | - | 15.20% | - | 28,844 |  |
| FJ | 2026-W21 | 95.17% | -0.44% | 15.38% | +1.18% | 26,694 |  |
| TT | 2026-W20 | 93.33% | - | 6.07% | - | 1,005 |  |
| TT | 2026-W21 | 88.49% | -5.19% | 12.60% | +107.54% | 643 | ⚠️ |
| CF | 2026-W20 | 92.44% | - | 15.48% | - | 6,325 |  |
| CF | 2026-W21 | 92.94% | +0.54% | 16.37% | +5.79% | 5,808 |  |
| TZ | 2026-W20 | 90.33% | - | 10.95% | - | 548 |  |
| TZ | 2026-W21 | 88.10% | -2.47% | 14.52% | +32.65% | 420 |  |
| TK | 2026-W20 | 92.47% | - | 9.34% | - | 332 |  |
| TK | 2026-W21 | 89.49% | -3.22% | 10.85% | +16.17% | 295 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TT, TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 97.61% | - | 13.60% | - | 34,250 |  |
| Paid | 2026-W21 | 97.50% | -0.11% | 14.06% | +3.37% | 31,476 |  |
| Referral | 2026-W20 | 80.78% | - | 22.41% | - | 7,319 |  |
| Referral | 2026-W21 | 79.06% | -2.13% | 24.55% | +9.54% | 6,604 |  |

---

## L2: FJ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 97.80% | - | 14.04% | - | 1.23% | - | 0.37% | - | 24,493 |  |
| Paid | 2026-W21 | 97.63% | -0.18% | 13.86% | -1.32% | 1.27% | +2.93% | 0.47% | +26.03% | 22,851 |  |
| Referral | 2026-W20 | 83.18% | - | 21.72% | - | 15.24% | - | 0.46% | - | 4,351 |  |
| Referral | 2026-W21 | 80.59% | -3.11% | 24.43% | +12.50% | 18.19% | +19.37% | 0.34% | -26.41% | 3,843 | ⚠️ |

**Analysis:** The -0.37pp decline in Fraud Approval Rate for 2026-W21 falls within normal operational variance and does not require immediate escalation. The primary drivers are localized duplicate fraud surges in TT (+107.54% Dup Rate) and TK (+25.22% Dup Rate), where increased Duplicate Blocks are correctly preventing approvals. If TT and TK Duplicate Rates remain elevated beyond 2026-W22, a deeper investigation into the source of duplicate applications in these markets should be initiated.

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 93.00% | - | 8.95% | - | 5.45% | - | 0.39% | - | 257 |  |
| Paid | 2026-W21 | 89.66% | -3.59% | 11.21% | +25.22% | 6.90% | +26.60% | 0.43% | +10.78% | 232 | ⚠️ |
| Referral | 2026-W20 | 90.67% | - | 10.67% | - | 8.00% | - | 1.33% | - | 75 |  |
| Referral | 2026-W21 | 88.89% | -1.96% | 9.52% | -10.71% | 9.52% | +19.05% | 0.00% | -100.00% | 63 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 92.35% | - | 6.47% | - | 3.82% | - | 0.00% | - | 340 |  |
| Paid | 2026-W21 | 92.54% | +0.20% | 8.66% | +33.79% | 3.88% | +1.49% | 0.00% | - | 335 |  |
| Referral | 2026-W20 | 81.00% | - | 21.00% | - | 19.00% | - | 0.00% | - | 100 |  |
| Referral | 2026-W21 | 76.25% | -5.86% | 23.75% | +13.10% | 23.75% | +25.00% | 0.00% | - | 80 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 94.17% | - | 4.78% | - | 3.61% | - | 0.00% | - | 858 |  |
| Paid | 2026-W21 | 90.23% | -4.19% | 10.90% | +128.15% | 7.89% | +118.51% | 0.00% | - | 532 | ⚠️ |
| Referral | 2026-W20 | 88.44% | - | 13.61% | - | 10.88% | - | 0.00% | - | 147 |  |
| Referral | 2026-W21 | 80.18% | -9.33% | 20.72% | +52.30% | 19.82% | +82.09% | 0.00% | - | 111 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TV Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 92.93% | - | 7.42% | - | 4.95% | - | 0.00% | - | 283 |  |
| Paid | 2026-W21 | 93.73% | +0.85% | 9.23% | +24.32% | 5.90% | +19.35% | 0.00% | - | 271 |  |
| Referral | 2026-W20 | 93.85% | - | 6.15% | - | 6.15% | - | 0.00% | - | 65 |  |
| Referral | 2026-W21 | 91.18% | -2.84% | 10.29% | +67.28% | 8.82% | +43.38% | 0.00% | - | 68 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 94.81% | - | 5.87% | - | 3.61% | - | 0.23% | - | 443 |  |
| Paid | 2026-W21 | 91.88% | -3.09% | 10.63% | +81.03% | 7.50% | +107.66% | 0.31% | +38.44% | 320 | ⚠️ |
| Referral | 2026-W20 | 71.43% | - | 32.38% | - | 28.57% | - | 0.00% | - | 105 |  |
| Referral | 2026-W21 | 76.00% | +6.40% | 27.00% | -16.62% | 24.00% | -16.00% | 0.00% | - | 100 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 98.34% | - | 16.00% | - | 0.94% | - | 0.00% | - | 3,081 |  |
| Paid | 2026-W21 | 98.32% | -0.02% | 18.39% | +14.91% | 1.32% | +40.34% | 0.00% | - | 2,801 |  |
| Referral | 2026-W20 | 67.34% | - | 34.21% | - | 30.65% | - | 0.00% | - | 646 |  |
| Referral | 2026-W21 | 69.47% | +3.17% | 33.08% | -3.30% | 29.47% | -3.84% | 0.00% | - | 665 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TT | ↓ -5.19% | Paid ↓ -4.19%, Referral ↓ -9.33% | ↑ +107.54% | ↑ +112.83% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↓ -3.22% | Paid ↓ -3.59% | ↑ +16.17% | ↑ +23.80% | ↓ -43.73% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-26*
