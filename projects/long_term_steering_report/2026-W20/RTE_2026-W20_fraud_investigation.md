# Fraud Investigation: RTE 2026-W20

**Metric:** Fraud Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 94.02% → 94.65% (+0.67%)  
**Volume:** 41,701 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) increased from 94.02% to 94.65% (+0.67pp) in 2026-W20, a statistically non-significant improvement across 41,701 customers reaching fraud service.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | FAR within normal 8-week range (93.82%-94.66%) | +0.67pp | ✅ |
| L1: Country Scan | 4 countries exceed ±2.5% threshold | TT +12.86pp, TV +23.09pp, TK +13.49pp, TO +9.74pp | ⚠️ |
| L1: Channel Category | Paid stable, Referral declining | Paid +0.91pp, Referral -2.44pp | ✅ |
| L2: Country Deep-Dive | Paid channel driving improvements; Dup Block decreases correlate with FAR gains | TV Dup Block -37.15%, TK -15.53% | ⚠️ |

**Key Findings:**
- TV experienced the largest FAR increase (+23.09pp), driven primarily by Paid channel (+26.27pp) with a significant decrease in Duplicate Block rate (-44.59pp in Paid)
- TT showed strong improvement (+12.86pp) with Referral channel gaining +17.43pp despite Paid Dup Block increasing +69.85%
- Referral channel globally continues to underperform with FAR declining -2.44pp and Dup Rate increasing +15.03%, indicating persistent duplicate/fraud issues in this acquisition path
- CF Referral channel shows deterioration (-3.40pp FAR) with Dup Block rate increasing +20.59pp, counter to the overall positive trend
- YE Referral shows significant FAR decline (-9.11pp) with Dup Rate increasing +25.29%, warranting monitoring

**Action:** Monitor — The overall FAR improvement is non-significant and within normal weekly variance. The country-level improvements (TT, TV, TK, TO) appear driven by reduced Duplicate Block rates in Paid channels, which may reflect legitimate traffic quality improvements or potential loosening of fraud controls. Continue monitoring Referral channel degradation across markets.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W20 | 94.65% | 15.40% | 4.37% | 0.29% | 41,701 | +0.67% ← REPORTED CHANGE |
| 2026-W19 | 94.02% | 14.15% | 4.07% | 0.25% | 40,965 | +0.21% |
| 2026-W18 | 93.82% | 14.51% | 3.85% | 0.24% | 42,230 | -0.14% |
| 2026-W17 | 93.95% | 16.40% | 4.56% | 0.35% | 44,542 | -0.39% |
| 2026-W16 | 94.31% | 15.41% | 4.23% | 0.31% | 45,913 | -0.37% |
| 2026-W15 | 94.66% | 14.50% | 4.02% | 0.30% | 45,710 | +0.04% |
| 2026-W14 | 94.62% | 13.99% | 4.06% | 0.18% | 41,360 | +0.52% |
| 2026-W13 | 94.13% | 14.35% | 3.91% | 0.26% | 43,915 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| TT | 2026-W19 | 82.99% | - | 6.44% | - | 823 |  |
| TT | 2026-W20 | 93.66% | +12.86% | 6.34% | -1.60% | 1,010 | ⚠️ |
| TV | 2026-W19 | 76.81% | - | 10.47% | - | 401 |  |
| TV | 2026-W20 | 94.54% | +23.09% | 7.18% | -31.41% | 348 | ⚠️ |
| CF | 2026-W19 | 93.11% | - | 14.12% | - | 6,835 |  |
| CF | 2026-W20 | 92.37% | -0.79% | 15.89% | +12.54% | 6,306 |  |
| TK | 2026-W19 | 81.52% | - | 10.33% | - | 368 |  |
| TK | 2026-W20 | 92.51% | +13.49% | 10.18% | -1.42% | 334 | ⚠️ |
| TO | 2026-W19 | 81.68% | - | 10.53% | - | 475 |  |
| TO | 2026-W20 | 89.64% | +9.74% | 10.81% | +2.70% | 444 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TT, TV, TK, TO

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 96.85% | - | 12.67% | - | 32,965 |  |
| Paid | 2026-W20 | 97.73% | +0.91% | 13.70% | +8.11% | 34,317 |  |
| Referral | 2026-W19 | 82.36% | - | 20.25% | - | 8,000 |  |
| Referral | 2026-W20 | 80.35% | -2.44% | 23.29% | +15.03% | 7,384 |  |

---

## L2: CF Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 98.10% | - | 12.07% | - | 0.29% | - | 0.00% | - | 4,832 |  |
| Paid | 2026-W20 | 98.18% | +0.09% | 13.29% | +10.17% | 0.27% | -7.16% | 0.00% | - | 4,461 |  |
| Referral | 2026-W19 | 81.08% | - | 19.07% | - | 16.67% | - | 0.00% | - | 2,003 |  |
| Referral | 2026-W20 | 78.32% | -3.40% | 22.17% | +16.24% | 20.11% | +20.59% | 0.00% | - | 1,845 | ⚠️ |

**Analysis:** The +0.67pp increase in Fraud Approval Rate for 2026-W20 represents normal weekly fluctuation within the established 8-week range and is not statistically significant. While several smaller markets (TV, TT, TK, TO) showed substantial FAR improvements primarily through reduced Duplicate Block rates in Paid channels, the Referral channel continues to exhibit elevated duplicate activity and declining approval rates across multiple countries. No immediate action is required, but ongoing monitoring of Referral channel quality and the sustainability of Duplicate Block rate reductions is recommended.

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 80.84% | - | 9.76% | - | 8.01% | - | 0.00% | - | 287 |  |
| Paid | 2026-W20 | 93.41% | +15.56% | 9.69% | -0.68% | 6.20% | -22.62% | 0.39% | - | 258 | ⚠️ |
| Referral | 2026-W19 | 83.95% | - | 12.35% | - | 8.64% | - | 0.00% | - | 81 |  |
| Referral | 2026-W20 | 89.47% | +6.58% | 11.84% | -4.08% | 9.21% | +6.58% | 1.32% | - | 76 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 82.95% | - | 8.53% | - | 6.20% | - | 0.00% | - | 387 |  |
| Paid | 2026-W20 | 92.67% | +11.72% | 7.33% | -14.02% | 4.69% | -24.34% | 0.00% | - | 341 | ⚠️ |
| Referral | 2026-W19 | 76.14% | - | 19.32% | - | 19.32% | - | 0.00% | - | 88 |  |
| Referral | 2026-W20 | 79.61% | +4.56% | 22.33% | +15.59% | 20.39% | +5.54% | 0.00% | - | 103 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 84.47% | - | 4.06% | - | 2.32% | - | 0.00% | - | 689 |  |
| Paid | 2026-W20 | 94.55% | +11.93% | 5.10% | +25.60% | 3.94% | +69.85% | 0.00% | - | 862 | ⚠️ |
| Referral | 2026-W19 | 75.37% | - | 18.66% | - | 18.66% | - | 0.00% | - | 134 |  |
| Referral | 2026-W20 | 88.51% | +17.43% | 13.51% | -27.57% | 10.81% | -42.05% | 0.00% | - | 148 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TV Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 75.00% | - | 11.31% | - | 8.93% | - | 0.00% | - | 336 |  |
| Paid | 2026-W20 | 94.70% | +26.27% | 7.42% | -34.39% | 4.95% | -44.59% | 0.00% | - | 283 | ⚠️ |
| Referral | 2026-W19 | 86.15% | - | 6.15% | - | 4.62% | - | 0.00% | - | 65 |  |
| Referral | 2026-W20 | 93.85% | +8.93% | 6.15% | +0.00% | 6.15% | +33.33% | 0.00% | - | 65 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 86.31% | - | 5.57% | - | 4.18% | - | 0.00% | - | 431 |  |
| Paid | 2026-W20 | 94.82% | +9.86% | 6.08% | +9.21% | 3.83% | -8.32% | 0.23% | - | 444 | ⚠️ |
| Referral | 2026-W19 | 70.89% | - | 27.85% | - | 25.32% | - | 0.00% | - | 79 |  |
| Referral | 2026-W20 | 71.70% | +1.15% | 32.08% | +15.18% | 28.30% | +11.79% | 0.00% | - | 106 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 98.33% | - | 17.12% | - | 0.58% | - | 0.00% | - | 2,751 |  |
| Paid | 2026-W20 | 98.52% | +0.19% | 16.15% | -5.70% | 1.06% | +82.85% | 0.00% | - | 3,103 |  |
| Referral | 2026-W19 | 73.68% | - | 28.32% | - | 25.56% | - | 0.00% | - | 798 |  |
| Referral | 2026-W20 | 66.97% | -9.11% | 35.48% | +25.29% | 31.95% | +24.98% | 0.00% | - | 651 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TT | ↑ +12.86% | Paid ↑ +11.93%, Referral ↑ +17.43% | → -1.60% | → -0.63% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TV | ↑ +23.09% | Paid ↑ +26.27%, Referral ↑ +8.93% | ↓ -31.41% | ↓ -37.15% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↑ +13.49% | Paid ↑ +15.56%, Referral ↑ +6.58% | → -1.42% | ↓ -15.53% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑ +9.74% | Paid ↑ +11.72%, Referral ↑ +4.56% | ↑ +2.70% | ↓ -3.46% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-19*
