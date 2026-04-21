# Fraud Investigation: RTE 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.68% → 94.42% (-0.27%)  
**Volume:** 47,258 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 94.68% to 94.42% (-0.27pp) in 2026-W16, a change that is not statistically significant and remains within normal weekly variance observed over the 8-week trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | FAR within 8-week range (93.84%-94.95%) | -0.27pp | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold | TT +4.47pp, TO -3.54pp | ⚠️ |
| L1: Channel Scan | All categories within tolerance | Paid -0.17pp, Referral -0.57pp | ✅ |
| L2: TO Deep-Dive | Referral channel degradation | -9.79pp FAR, +72.88% Dup Rate | ⚠️ |
| L2: TT Deep-Dive | Improvement across both channels | +3.43pp Paid, +6.42pp Referral | ✅ |

**Key Findings:**
- TO Referral channel saw significant FAR decline (-9.79pp) driven by duplicate rate surge (+72.88%) and duplicate block increase (+59.58pp), though volume remains small (127 customers)
- TT showed unexpected improvement (+4.47pp FAR) with duplicate rate decreasing by 24.94%, suggesting improved traffic quality or fraud rule optimization
- Duplicate Rate increased globally from 14.62% to 15.72% (+7.53%), with FJ contributing the largest volume impact at +5.21% increase
- YE Referral channel showed notable degradation (-6.93pp FAR) with duplicate rate up 26.44%, following similar pattern to TO
- TZ Referral experienced the largest single-channel FAR drop (-13.25pp) with duplicate block rate increasing by 46.62%

**Action:** **Monitor** - The overall FAR change is not significant. Continue monitoring TO, TZ, and YE Referral channels for sustained duplicate rate increases. If Referral channel degradation persists for 2+ consecutive weeks, escalate for fraud rule review.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 94.42% | 15.72% | 4.58% | 0.33% | 47,258 | -0.27% ← REPORTED CHANGE |
| 2026-W15 | 94.68% | 14.62% | 4.13% | 0.31% | 45,746 | +0.04% |
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
| FJ | 2026-W15 | 95.17% | - | 15.43% | - | 31,326 |  |
| FJ | 2026-W16 | 94.81% | -0.37% | 16.24% | +5.21% | 32,338 |  |
| TT | 2026-W15 | 89.73% | - | 8.75% | - | 857 |  |
| TT | 2026-W16 | 93.74% | +4.47% | 6.57% | -24.94% | 1,294 | ⚠️ |
| YE | 2026-W15 | 94.72% | - | 16.84% | - | 3,860 |  |
| YE | 2026-W16 | 94.21% | -0.53% | 18.87% | +12.04% | 4,182 |  |
| TO | 2026-W15 | 93.68% | - | 6.32% | - | 427 |  |
| TO | 2026-W16 | 90.36% | -3.54% | 9.27% | +46.65% | 550 | ⚠️ |
| TV | 2026-W15 | 95.10% | - | 4.29% | - | 490 |  |
| TV | 2026-W16 | 92.92% | -2.29% | 7.52% | +75.52% | 452 |  |
| TK | 2026-W15 | 92.95% | - | 7.27% | - | 454 |  |
| TK | 2026-W16 | 91.15% | -1.94% | 11.80% | +62.29% | 373 |  |

**Countries exceeding ±2.5% threshold:** TT, TO

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 97.47% | - | 13.25% | - | 37,381 |  |
| Paid | 2026-W16 | 97.31% | -0.17% | 14.30% | +7.93% | 38,521 |  |
| Referral | 2026-W15 | 82.18% | - | 20.73% | - | 8,365 |  |
| Referral | 2026-W16 | 81.71% | -0.57% | 21.95% | +5.90% | 8,737 |  |

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 94.87% | - | 5.13% | - | 3.99% | - | 0.00% | - | 351 |  |
| Paid | 2026-W16 | 93.62% | -1.32% | 5.91% | +15.25% | 5.20% | +30.40% | 0.00% | - | 423 |  |
| Referral | 2026-W15 | 88.16% | - | 11.84% | - | 11.84% | - | 0.00% | - | 76 |  |
| Referral | 2026-W16 | 79.53% | -9.79% | 20.47% | +72.88% | 18.90% | +59.58% | 0.00% | - | 127 | ⚠️ |

**Analysis:** The -0.27pp FAR decline in 2026-W16 represents normal operational variance and does not require immediate intervention. The primary concern is isolated to the Referral channel across multiple smaller markets (TO, TZ, YE), where elevated duplicate rates are driving increased blocks—this pattern warrants monitoring but affects less than 3% of total volume. TT's improvement suggests potential positive signal that should be analyzed for replicable insights.

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 91.67% | - | 6.94% | - | 5.42% | - | 0.00% | - | 720 |  |
| Paid | 2026-W16 | 94.81% | +3.43% | 5.53% | -20.35% | 4.32% | -20.22% | 0.00% | - | 1,157 | ⚠️ |
| Referral | 2026-W15 | 79.56% | - | 18.25% | - | 18.25% | - | 0.00% | - | 137 |  |
| Referral | 2026-W16 | 84.67% | +6.42% | 15.33% | -16.00% | 15.33% | -16.00% | 0.00% | - | 137 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 92.96% | - | 7.65% | - | 5.63% | - | 0.00% | - | 497 |  |
| Paid | 2026-W16 | 96.08% | +3.36% | 6.47% | -15.37% | 3.53% | -37.35% | 0.00% | - | 510 | ⚠️ |
| Referral | 2026-W15 | 79.09% | - | 20.91% | - | 20.91% | - | 0.00% | - | 110 |  |
| Referral | 2026-W16 | 68.61% | -13.25% | 32.12% | +53.60% | 30.66% | +46.62% | 0.73% | - | 137 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 98.18% | - | 15.52% | - | 1.06% | - | 0.00% | - | 3,195 |  |
| Paid | 2026-W16 | 98.00% | -0.18% | 17.04% | +9.74% | 1.55% | +45.30% | 0.00% | - | 3,557 |  |
| Referral | 2026-W15 | 78.05% | - | 23.16% | - | 21.20% | - | 0.00% | - | 665 |  |
| Referral | 2026-W16 | 72.64% | -6.93% | 29.28% | +26.44% | 26.56% | +25.27% | 0.00% | - | 625 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TT | ↑ +4.47% | Paid ↑ +3.43%, Referral ↑ +6.42% | ↓ -24.94% | ↓ -26.53% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↓ -3.54% | Referral ↓ -9.79% | ↑ +46.65% | ↑ +55.27% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-21*
