# Fraud Investigation: RTE 2026-W23

**Metric:** Fraud Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 94.59% → 94.74% (+0.15%)  
**Volume:** 38,785 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 94.59% to 94.74% (+0.15 pp) in 2026-W23, a change that is not statistically significant, with 38,785 customers reaching the fraud service.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | 8-week stability | +0.15 pp | ✅ |
| L1: Country Scan | 3 countries exceeded ±2.5% threshold | TZ -5.17 pp, TT +3.18 pp, TO +3.56 pp | ⚠️ |
| L1: Channel Category | Paid/Referral breakdown | Paid +0.29 pp, Referral -0.64 pp | ✅ |
| L2: Duplicate Detection | New dup rate tracking in W23 | 16.01% overall dup rate | ⚠️ |

**Key Findings:**
- TZ experienced the largest FAR decline (-5.17 pp), driven by both Paid (-3.47 pp) and Referral (-14.03 pp) channels, with Referral showing a 28.77% duplicate rate and 23.29% duplicate block rate
- TT and TO showed FAR improvements (+3.18 pp and +3.56 pp respectively), primarily driven by Paid channel in TT (+4.09 pp) and Referral channel in TO (+12.84 pp)
- YE Referral channel declined -3.77 pp with the highest duplicate rate observed (31.64%) and duplicate block rate (29.02%)
- New duplicate detection metrics activated in W23 show significant duplicate rates in flagged countries (ranging from 9-32%), suggesting prior weeks had undetected duplicates
- Overall channel performance remains stable at the global level, with Paid channels (97.52% FAR) significantly outperforming Referral channels (81.62% FAR)

**Action:** Monitor — The overall FAR change is not significant and within normal operating range. Continue monitoring TZ performance, particularly the Referral channel which shows elevated duplicate rates and blocking. Validate that new duplicate detection is functioning as intended.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W23 | 94.74% | 16.01% | 4.14% | 0.35% | 38,785 | +0.15% ← REPORTED CHANGE |
| 2026-W22 | 94.59% | 0.00% | 0.00% | 0.34% | 37,867 | +0.29% |
| 2026-W21 | 94.32% | 0.00% | 0.00% | 0.30% | 37,903 | -0.33% |
| 2026-W20 | 94.64% | 0.00% | 0.00% | 0.27% | 41,540 | +0.41% |
| 2026-W19 | 94.25% | 0.00% | 0.00% | 0.24% | 40,830 | +0.46% |
| 2026-W18 | 93.82% | 0.00% | 0.00% | 0.24% | 42,201 | -0.13% |
| 2026-W17 | 93.94% | 0.00% | 0.00% | 0.35% | 44,526 | -0.40% |
| 2026-W16 | 94.32% | 0.00% | 0.00% | 0.31% | 45,898 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| YE | 2026-W22 | 92.32% | - | 0.00% | - | 3,517 |  |
| YE | 2026-W23 | 93.40% | +1.16% | 21.34% | - | 3,392 |  |
| TZ | 2026-W22 | 94.10% | - | 0.00% | - | 424 |  |
| TZ | 2026-W23 | 89.24% | -5.17% | 11.88% | - | 446 | ⚠️ |
| TT | 2026-W22 | 88.59% | - | 0.00% | - | 640 |  |
| TT | 2026-W23 | 91.41% | +3.18% | 10.22% | - | 675 | ⚠️ |
| TO | 2026-W22 | 88.09% | - | 0.00% | - | 403 |  |
| TO | 2026-W23 | 91.22% | +3.56% | 9.01% | - | 433 | ⚠️ |
| TK | 2026-W22 | 93.62% | - | 0.00% | - | 329 |  |
| TK | 2026-W23 | 92.10% | -1.62% | 9.28% | - | 291 |  |

**Countries exceeding ±2.5% threshold:** TZ, TT, TO

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 97.24% | - | 0.00% | - | 31,236 |  |
| Paid | 2026-W23 | 97.52% | +0.29% | 14.51% | - | 31,989 |  |
| Referral | 2026-W22 | 82.14% | - | 0.00% | - | 6,631 |  |
| Referral | 2026-W23 | 81.62% | -0.64% | 23.06% | - | 6,796 |  |

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 93.91% | - | 0.00% | - | 0.00% | - | 0.36% | - | 279 |  |
| Paid | 2026-W23 | 90.91% | -3.19% | 10.91% | - | 8.64% | - | 0.00% | -100.00% | 220 | ⚠️ |
| Referral | 2026-W22 | 92.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 50 |  |
| Referral | 2026-W23 | 95.77% | +4.10% | 4.23% | - | 4.23% | - | 0.00% | - | 71 | ⚠️ |

**Analysis:** The 2026-W23 Fraud Approval Rate shows a modest, non-significant improvement of +0.15 pp at the aggregate level, masking notable country-level variations. The introduction of duplicate detection in W23 reveals substantial duplicate traffic (16.01% overall), particularly impacting Referral channels in TZ and YE where duplicate block rates exceed 20%. No immediate action is required, but continued monitoring of TZ's declining performance and the effectiveness of the new duplicate blocking mechanism is recommended.

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 90.49% | - | 0.00% | - | 0.00% | - | 0.00% | - | 326 |  |
| Paid | 2026-W23 | 91.73% | +1.37% | 8.27% | - | 5.87% | - | 0.00% | - | 375 |  |
| Referral | 2026-W22 | 77.92% | - | 0.00% | - | 0.00% | - | 0.00% | - | 77 |  |
| Referral | 2026-W23 | 87.93% | +12.84% | 13.79% | - | 12.07% | - | 0.00% | - | 58 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 89.69% | - | 0.00% | - | 0.00% | - | 0.00% | - | 553 |  |
| Paid | 2026-W23 | 93.36% | +4.09% | 8.22% | - | 5.24% | - | 0.00% | - | 572 | ⚠️ |
| Referral | 2026-W22 | 81.61% | - | 0.00% | - | 0.00% | - | 0.00% | - | 87 |  |
| Referral | 2026-W23 | 80.58% | -1.26% | 21.36% | - | 19.42% | - | 0.00% | - | 103 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 94.99% | - | 0.00% | - | 0.00% | - | 0.00% | - | 359 |  |
| Paid | 2026-W23 | 91.69% | -3.47% | 8.58% | - | 6.70% | - | 0.00% | - | 373 | ⚠️ |
| Referral | 2026-W22 | 89.23% | - | 0.00% | - | 0.00% | - | 0.00% | - | 65 |  |
| Referral | 2026-W23 | 76.71% | -14.03% | 28.77% | - | 23.29% | - | 0.00% | - | 73 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 96.50% | - | 0.00% | - | 0.00% | - | 0.00% | - | 2,912 |  |
| Paid | 2026-W23 | 98.63% | +2.21% | 19.09% | - | 0.97% | - | 0.00% | - | 2,782 |  |
| Referral | 2026-W22 | 72.23% | - | 0.00% | - | 0.00% | - | 0.00% | - | 605 |  |
| Referral | 2026-W23 | 69.51% | -3.77% | 31.64% | - | 29.02% | - | 0.00% | - | 610 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TZ | ↓ -5.17% | Paid ↓ -3.47%, Referral ↓ -14.03% | → - | → - | → - | [AI_SUMMARY_PLACEHOLDER] |
| TT | ↑ +3.18% | Paid ↑ +4.09% | → - | → - | → - | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑ +3.56% | Referral ↑ +12.84% | → - | → - | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-06-09*
