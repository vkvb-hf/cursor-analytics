# Fraud Investigation: RTE 2026-W18

**Metric:** Fraud Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 93.94% → 94.29% (+0.37%)  
**Volume:** 43,137 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) improved slightly from 93.94% to 94.29% (+0.35pp) in W18, a non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within ±1% band | +0.37% | ✅ |
| L1: Country Scan | 1 country exceeds ±2.5% | TK +8.34% | ⚠️ |
| L1: Channel Scan | All channels within threshold | Paid +0.65%, Referral -0.55% | ✅ |
| L2: TK Deep-Dive | Paid channel driving change | Paid +10.27%, Dup Block -54.89% | ⚠️ |
| L2: Referral Health | Multiple countries show stress | TZ -16.24%, YE -7.24%, TO -5.69% | ⚠️ |

**Key Findings:**
- TK showed an anomalous +8.34pp FAR increase driven entirely by Paid channel (+10.27pp), with duplicate rate dropping -36.51% and duplicate block rate falling -54.89%, suggesting reduced fraud detection activity
- Referral channel shows consistent degradation across multiple countries: TZ (-16.24pp FAR with +48.72% dup rate increase), YE (-7.24pp FAR with +22.81% dup block increase), and TO (-5.69pp FAR with +31.32% dup rate increase)
- Global duplicate rate increased to 16.91% (+2.3% WoW), the highest level in the 8-week window, indicating elevated duplicate submission attempts
- Overall volume decreased by 3.2% (44,582 → 43,137), with the decline concentrated in the largest market FJ (-5.0%)
- PF Block rate decreased from 0.36% to 0.29% (-19.4%), contributing marginally to the FAR improvement

**Action:** Monitor - The overall change is not significant, but recommend focused monitoring on TK Paid channel for sustained pattern changes and investigate root cause of declining Referral performance across TZ, YE, and TO markets.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W18 | 94.29% | 16.91% | 4.73% | 0.29% | 43,137 | +0.37% ← REPORTED CHANGE |
| 2026-W17 | 93.94% | 16.53% | 4.69% | 0.36% | 44,582 | -0.39% |
| 2026-W16 | 94.31% | 15.46% | 4.28% | 0.31% | 45,937 | -0.39% |
| 2026-W15 | 94.68% | 14.53% | 4.05% | 0.30% | 45,718 | +0.05% |
| 2026-W14 | 94.63% | 14.03% | 4.10% | 0.18% | 41,366 | +0.53% |
| 2026-W13 | 94.13% | 14.38% | 3.94% | 0.26% | 43,921 | +0.32% |
| 2026-W12 | 93.82% | 14.44% | 4.18% | 0.21% | 45,547 | -0.60% |
| 2026-W11 | 94.39% | 14.50% | 3.87% | 0.21% | 48,688 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W17 | 94.56% | - | 16.70% | - | 31,496 |  |
| FJ | 2026-W18 | 95.04% | +0.51% | 17.13% | +2.58% | 29,933 |  |
| YE | 2026-W17 | 94.33% | - | 20.14% | - | 3,882 |  |
| YE | 2026-W18 | 93.28% | -1.12% | 20.08% | -0.32% | 3,735 |  |
| CF | 2026-W17 | 92.15% | - | 16.03% | - | 6,676 |  |
| CF | 2026-W18 | 92.62% | +0.50% | 16.93% | +5.63% | 6,852 |  |
| TK | 2026-W17 | 85.94% | - | 12.19% | - | 320 |  |
| TK | 2026-W18 | 93.10% | +8.34% | 8.91% | -26.91% | 348 | ⚠️ |
| TT | 2026-W17 | 90.82% | - | 9.93% | - | 806 |  |
| TT | 2026-W18 | 91.85% | +1.14% | 9.03% | -9.01% | 908 |  |
| TZ | 2026-W17 | 91.16% | - | 9.76% | - | 543 |  |
| TZ | 2026-W18 | 89.43% | -1.90% | 12.33% | +26.31% | 511 |  |
| TO | 2026-W17 | 88.64% | - | 11.80% | - | 449 |  |
| TO | 2026-W18 | 90.09% | +1.63% | 10.57% | -10.43% | 454 |  |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 96.79% | - | 15.29% | - | 35,898 |  |
| Paid | 2026-W18 | 97.42% | +0.65% | 15.34% | +0.32% | 34,524 |  |
| Referral | 2026-W17 | 82.16% | - | 21.63% | - | 8,684 |  |
| Referral | 2026-W18 | 81.71% | -0.55% | 23.21% | +7.32% | 8,613 |  |

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 86.75% | - | 10.84% | - | 9.64% | - | 0.40% | - | 249 |  |
| Paid | 2026-W18 | 95.65% | +10.27% | 6.88% | -36.51% | 4.35% | -54.89% | 0.00% | -100.00% | 276 | ⚠️ |
| Referral | 2026-W17 | 83.10% | - | 16.90% | - | 16.90% | - | 0.00% | - | 71 |  |
| Referral | 2026-W18 | 83.33% | +0.28% | 16.67% | -1.39% | 16.67% | -1.39% | 0.00% | - | 72 |  |

**Analysis:** The W18 FAR increase of +0.35pp represents normal week-over-week fluctuation and does not indicate a systemic change in fraud approval patterns. However, the TK market warrants attention due to a sharp reduction in duplicate blocking activity within the Paid channel, and the Referral channel shows emerging stress signals across multiple smaller markets (TZ, YE, TO) with rising duplicate rates and declining approval rates. Continued monitoring through W19 is recommended to determine if these localized patterns stabilize or require intervention.

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 90.70% | - | 10.14% | - | 7.61% | - | 0.00% | - | 355 |  |
| Paid | 2026-W18 | 93.05% | +2.58% | 7.75% | -23.54% | 5.61% | -26.17% | 0.00% | - | 374 | ⚠️ |
| Referral | 2026-W17 | 80.85% | - | 18.09% | - | 18.09% | - | 0.00% | - | 94 |  |
| Referral | 2026-W18 | 76.25% | -5.69% | 23.75% | +31.32% | 23.75% | +31.32% | 0.00% | - | 80 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 94.81% | - | 6.32% | - | 4.06% | - | 0.00% | - | 443 |  |
| Paid | 2026-W18 | 94.23% | -0.61% | 7.85% | +24.23% | 5.31% | +30.73% | 0.00% | - | 433 |  |
| Referral | 2026-W17 | 75.00% | - | 25.00% | - | 25.00% | - | 0.00% | - | 100 |  |
| Referral | 2026-W18 | 62.82% | -16.24% | 37.18% | +48.72% | 37.18% | +48.72% | 0.00% | - | 78 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 97.74% | - | 18.60% | - | 1.52% | - | 0.00% | - | 3,280 |  |
| Paid | 2026-W18 | 98.12% | +0.39% | 17.63% | -5.21% | 1.39% | -8.59% | 0.00% | - | 3,086 |  |
| Referral | 2026-W17 | 75.75% | - | 28.57% | - | 23.59% | - | 0.00% | - | 602 |  |
| Referral | 2026-W18 | 70.26% | -7.24% | 31.74% | +11.09% | 28.97% | +22.81% | 0.00% | - | 649 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TK | ↑ +8.34% | Paid ↑ +10.27% | ↓ -26.91% | ↓ -38.70% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-05*
