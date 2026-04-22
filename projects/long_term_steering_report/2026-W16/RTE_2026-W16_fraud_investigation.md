# Fraud Investigation: RTE 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.67% → 94.42% (-0.26%)  
**Volume:** 47,258 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined marginally from 94.67% to 94.42% (-0.26pp) in W16, a statistically non-significant change within normal weekly fluctuation range observed over the 8-week trend (93.84% - 94.95%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | FAR within 8-week range | -0.26pp | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold | TT +4.60pp, TO -3.54pp | ⚠️ |
| L1: Channel Scan | No channels exceed threshold | Paid -0.16pp, Referral -0.58pp | ✅ |
| L2: TO Deep-Dive | Referral channel driver | FAR -9.79pp, Dup Rate +72.88% | ⚠️ |
| L2: TT Deep-Dive | Both channels improved | Paid +3.59pp, Referral +6.42pp | ✅ |

**Key Findings:**
- TO experienced a -3.54pp FAR decline driven primarily by Referral channel (-9.79pp), with duplicate rate surging +72.88% and duplicate blocks up +59.58%
- TT showed unexpected improvement (+4.60pp FAR) across both Paid (+3.59pp) and Referral (+6.42pp) channels, coinciding with a -23.93% decrease in duplicate rate
- YE Referral channel declined -7.07pp with duplicate rate increasing +27.07%, though overall YE FAR change remains within threshold (-0.56pp)
- TZ Referral channel showed significant deterioration (-13.25pp FAR) with duplicate rate up +53.60%, despite low volume (137 customers)
- Global duplicate rate increased from 14.61% to 15.72% (+7.60%), with duplicate blocks rising from 4.13% to 4.58%

**Action:** Monitor - The overall FAR change is not statistically significant. Continue monitoring TO and TZ Referral channels for sustained duplicate rate increases. No immediate escalation required.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 94.42% | 15.72% | 4.58% | 0.33% | 47,258 | -0.26% ← REPORTED CHANGE |
| 2026-W15 | 94.67% | 14.61% | 4.13% | 0.31% | 45,743 | +0.04% |
| 2026-W14 | 94.64% | 14.07% | 4.14% | 0.18% | 41,385 | +0.54% |
| 2026-W13 | 94.13% | 14.42% | 3.98% | 0.25% | 43,934 | +0.31% |
| 2026-W12 | 93.84% | 14.46% | 4.20% | 0.21% | 45,555 | -0.60% |
| 2026-W11 | 94.40% | 14.50% | 3.88% | 0.21% | 48,700 | -0.58% |
| 2026-W10 | 94.95% | 13.95% | 3.72% | 0.16% | 50,487 | +0.53% |
| 2026-W09 | 94.45% | 14.25% | 4.06% | 0.21% | 51,694 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W15 | 95.16% | - | 15.44% | - | 31,324 |  |
| FJ | 2026-W16 | 94.81% | -0.37% | 16.24% | +5.20% | 32,338 |  |
| TT | 2026-W15 | 89.61% | - | 8.63% | - | 857 |  |
| TT | 2026-W16 | 93.74% | +4.60% | 6.57% | -23.93% | 1,294 | ⚠️ |
| YE | 2026-W15 | 94.74% | - | 16.82% | - | 3,859 |  |
| YE | 2026-W16 | 94.21% | -0.56% | 18.87% | +12.18% | 4,182 |  |
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
| Paid | 2026-W15 | 97.47% | - | 13.25% | - | 37,380 |  |
| Paid | 2026-W16 | 97.31% | -0.16% | 14.30% | +7.95% | 38,521 |  |
| Referral | 2026-W15 | 82.18% | - | 20.71% | - | 8,363 |  |
| Referral | 2026-W16 | 81.71% | -0.58% | 21.95% | +6.00% | 8,737 |  |

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 94.87% | - | 5.13% | - | 3.99% | - | 0.00% | - | 351 |  |
| Paid | 2026-W16 | 93.62% | -1.32% | 5.91% | +15.25% | 5.20% | +30.40% | 0.00% | - | 423 |  |
| Referral | 2026-W15 | 88.16% | - | 11.84% | - | 11.84% | - | 0.00% | - | 76 |  |
| Referral | 2026-W16 | 79.53% | -9.79% | 20.47% | +72.88% | 18.90% | +59.58% | 0.00% | - | 127 | ⚠️ |

**Analysis:** The W16 FAR decline of -0.26pp is within normal operating variance and does not indicate systemic issues. The offsetting movements in TT (improvement) and TO (decline) are localized to low-volume markets with Referral channel duplicate detection being the primary driver of country-level fluctuations. Recommend continued monitoring of duplicate rate trends in TO, TZ, and YE Referral channels, with escalation only if patterns persist beyond W17.

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 91.53% | - | 6.81% | - | 5.28% | - | 0.00% | - | 720 |  |
| Paid | 2026-W16 | 94.81% | +3.59% | 5.53% | -18.72% | 4.32% | -18.12% | 0.00% | - | 1,157 | ⚠️ |
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
| Referral | 2026-W15 | 78.16% | - | 23.04% | - | 21.08% | - | 0.00% | - | 664 |  |
| Referral | 2026-W16 | 72.64% | -7.07% | 29.28% | +27.07% | 26.56% | +25.97% | 0.00% | - | 625 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TT | ↑ +4.60% | Paid ↑ +3.59%, Referral ↑ +6.42% | ↓ -23.93% | ↓ -25.36% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↓ -3.54% | Referral ↓ -9.79% | ↑ +46.65% | ↑ +55.27% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-22*
