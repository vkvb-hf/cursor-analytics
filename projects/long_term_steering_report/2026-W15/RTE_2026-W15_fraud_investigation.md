# Fraud Investigation: RTE 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 94.68% → 94.42% (-0.27%)  
**Volume:** 47,258 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 94.68% to 94.42% (-0.27pp) in 2026-W15, a statistically non-significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | -0.27pp decline | Within ±1% threshold | ✅ |
| L1: Country Scan | TO flagged at +5.55pp | Exceeds ±2.5% threshold | ⚠️ |
| L1: Channel Scan | Paid +0.07pp, Referral +0.30pp | Within threshold | ✅ |
| L2: TO Deep-Dive | Paid +4.02pp, Referral +8.16pp | Low volume (427 total) | ⚠️ |
| L2: Referral Channel | Multiple countries flagged | Elevated dup rates | ⚠️ |

**Key Findings:**
- TO showed the largest FAR improvement (+5.55pp), driven by a significant drop in duplicate rate (-42.89%) and duplicate block rate (-46.32%) across both Paid and Referral channels
- Referral channel consistently underperforms Paid across all countries, with FAR ~15pp lower (82.18% vs 97.47%) and higher duplicate rates (20.73% vs 13.25%)
- TV Paid channel saw a +5.14pp FAR improvement with duplicate rate dropping -63.88%, while TV Referral declined -6.94pp with duplicate rate spiking +238.78%
- YE Referral showed notable improvement (+9.23pp FAR) with duplicate rate declining -23.89%
- TT Referral declined -5.28pp with duplicate block rate increasing +27.74%

**Action:** Monitor – The overall FAR change is not statistically significant and volume in flagged countries (TO: 427, TV: 490, TK: 454) is too low to materially impact the global metric. Continue standard monitoring with attention to Referral channel duplicate patterns.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 94.42% | 15.72% | 4.58% | 0.33% | 47,258 | -0.27% |
| 2026-W15 | 94.68% | 14.62% | 4.13% | 0.31% | 45,746 | +0.04% ← REPORTED CHANGE |
| 2026-W14 | 94.64% | 14.07% | 4.14% | 0.18% | 41,388 | +0.54% |
| 2026-W13 | 94.13% | 14.42% | 3.98% | 0.25% | 43,934 | +0.31% |
| 2026-W12 | 93.84% | 14.46% | 4.21% | 0.21% | 45,556 | -0.60% |
| 2026-W11 | 94.41% | 14.51% | 3.88% | 0.21% | 48,701 | -0.57% |
| 2026-W10 | 94.95% | 13.96% | 3.73% | 0.16% | 50,488 | +0.53% |
| 2026-W09 | 94.45% | 14.25% | 4.06% | 0.21% | 51,695 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W14 | 95.47% | - | 14.30% | - | 28,854 |  |
| FJ | 2026-W15 | 95.17% | -0.32% | 15.43% | +7.94% | 31,326 |  |
| YE | 2026-W14 | 93.06% | - | 18.40% | - | 3,256 |  |
| YE | 2026-W15 | 94.72% | +1.78% | 16.84% | -8.47% | 3,860 |  |
| TO | 2026-W14 | 88.75% | - | 11.07% | - | 578 |  |
| TO | 2026-W15 | 93.68% | +5.55% | 6.32% | -42.89% | 427 | ⚠️ |
| TV | 2026-W14 | 92.78% | - | 7.73% | - | 388 |  |
| TV | 2026-W15 | 95.10% | +2.50% | 4.29% | -44.57% | 490 |  |
| TT | 2026-W14 | 88.88% | - | 9.97% | - | 863 |  |
| TT | 2026-W15 | 89.73% | +0.96% | 8.75% | -12.18% | 857 |  |

**Countries exceeding ±2.5% threshold:** TO

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.41% | - | 12.45% | - | 33,974 |  |
| Paid | 2026-W15 | 97.47% | +0.07% | 13.25% | +6.40% | 37,381 |  |
| Referral | 2026-W14 | 81.93% | - | 21.49% | - | 7,414 |  |
| Referral | 2026-W15 | 82.18% | +0.30% | 20.73% | -3.52% | 8,365 |  |

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 93.48% | - | 6.16% | - | 4.71% | - | 0.00% | - | 276 |  |
| Paid | 2026-W15 | 93.96% | +0.52% | 5.77% | -6.25% | 4.99% | +5.88% | 0.26% | - | 381 |  |
| Referral | 2026-W14 | 91.53% | - | 6.78% | - | 6.78% | - | 0.00% | - | 59 |  |
| Referral | 2026-W15 | 87.67% | -4.21% | 15.07% | +122.26% | 12.33% | +81.85% | 0.00% | - | 73 | ⚠️ |

**Analysis:** The -0.27pp decline in Fraud Approval Rate for 2026-W15 represents normal operational variance and does not indicate a systemic issue requiring immediate intervention. The flagged movements in TO, TV, and TT are primarily driven by low-volume Referral channel fluctuations in duplicate detection patterns, which naturally exhibit higher volatility. No escalation is required at this time; standard weekly monitoring should continue with particular attention to whether Referral channel duplicate rate trends persist across multiple weeks.

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 91.20% | - | 8.56% | - | 7.18% | - | 0.00% | - | 432 |  |
| Paid | 2026-W15 | 94.87% | +4.02% | 5.13% | -40.12% | 3.99% | -44.42% | 0.00% | - | 351 | ⚠️ |
| Referral | 2026-W14 | 81.51% | - | 18.49% | - | 18.49% | - | 0.00% | - | 146 |  |
| Referral | 2026-W15 | 88.16% | +8.16% | 11.84% | -35.96% | 11.84% | -35.96% | 0.00% | - | 76 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 90.12% | - | 8.58% | - | 6.54% | - | 0.00% | - | 688 |  |
| Paid | 2026-W15 | 91.67% | +1.72% | 6.94% | -19.02% | 5.42% | -17.19% | 0.00% | - | 720 |  |
| Referral | 2026-W14 | 84.00% | - | 15.43% | - | 14.29% | - | 0.00% | - | 175 |  |
| Referral | 2026-W15 | 79.56% | -5.28% | 18.25% | +18.28% | 18.25% | +27.74% | 0.00% | - | 137 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TV Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 91.48% | - | 9.18% | - | 6.56% | - | 0.00% | - | 305 |  |
| Paid | 2026-W15 | 96.17% | +5.14% | 3.32% | -63.88% | 1.79% | -72.77% | 0.00% | - | 392 | ⚠️ |
| Referral | 2026-W14 | 97.59% | - | 2.41% | - | 2.41% | - | 0.00% | - | 83 |  |
| Referral | 2026-W15 | 90.82% | -6.94% | 8.16% | +238.78% | 8.16% | +238.78% | 0.00% | - | 98 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.79% | - | 15.76% | - | 1.39% | - | 0.00% | - | 2,671 |  |
| Paid | 2026-W15 | 98.18% | +0.40% | 15.52% | -1.51% | 1.06% | -23.18% | 0.00% | - | 3,195 |  |
| Referral | 2026-W14 | 71.45% | - | 30.43% | - | 27.35% | - | 0.00% | - | 585 |  |
| Referral | 2026-W15 | 78.05% | +9.23% | 23.16% | -23.89% | 21.20% | -22.48% | 0.00% | - | 665 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TO | ↑ +5.55% | Paid ↑ +4.02%, Referral ↑ +8.16% | ↓ -42.89% | ↓ -46.32% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-22*
