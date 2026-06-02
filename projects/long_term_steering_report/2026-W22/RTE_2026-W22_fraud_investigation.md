# Fraud Investigation: RTE 2026-W22

**Metric:** Fraud Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 94.31% → 94.52% (+0.22%)  
**Volume:** 38,012 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 94.31% to 94.52% (+0.21 pp) in W22, representing a statistically non-significant change across 38,012 customers reaching fraud service.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE 8-Week Trend | FAR within normal range (93.83%-94.67%) | +0.22% | ✅ |
| L1: Country Scan | TZ +6.82%, TK +4.26% exceed ±2.5% threshold | 2 flags | ⚠️ |
| L1: Channel Category | Referral +2.52% exceeds threshold | 1 flag | ⚠️ |
| L2: TZ Deep-Dive | Referral FAR +17.41%, Dup Rate -53.77% | Major shift | ⚠️ |
| L2: TK Deep-Dive | Paid FAR +4.29%, Dup Rate -30.45% | Improved | ⚠️ |

**Key Findings:**
- TZ showed the largest FAR improvement (+6.82 pp), driven primarily by Referral channel (+17.41 pp) with a dramatic decrease in duplicate rate (-53.77%) and duplicate blocks (-51.53%)
- TK FAR improved +4.26 pp, with Paid channel duplicate rate dropping -30.45% and duplicate blocks decreasing -11.68%
- Referral channel globally improved +2.01 pp (79.58% → 81.59%) while maintaining stable duplicate rates (-0.43%)
- FJ (largest market at 26,432 volume) remained stable with Paid FAR flat at 97.56%, though Referral improved +3.53 pp with reduced duplicate blocks (-12.14%)
- Overall duplicate rate increased slightly (+0.50 pp to 16.12%) but duplicate block rate remained stable at 4.41%

**Action:** Monitor — The overall change is not statistically significant. The improvements in TZ and TK appear driven by reduced duplicate detection/blocking, which warrants monitoring to ensure this reflects genuine improvement in traffic quality rather than detection gaps.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W22 | 94.52% | 16.12% | 4.41% | 0.35% | 38,012 | +0.22% ← REPORTED CHANGE |
| 2026-W21 | 94.31% | 15.62% | 4.35% | 0.30% | 37,888 | -0.36% |
| 2026-W20 | 94.65% | 15.07% | 4.05% | 0.27% | 41,550 | +0.68% |
| 2026-W19 | 94.02% | 14.04% | 3.97% | 0.24% | 40,939 | +0.20% |
| 2026-W18 | 93.83% | 14.45% | 3.78% | 0.24% | 42,207 | -0.13% |
| 2026-W17 | 93.94% | 16.35% | 4.52% | 0.35% | 44,531 | -0.40% |
| 2026-W16 | 94.32% | 15.38% | 4.20% | 0.31% | 45,904 | -0.37% |
| 2026-W15 | 94.67% | 14.47% | 3.99% | 0.30% | 45,700 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W21 | 95.20% | - | 15.17% | - | 26,569 |  |
| FJ | 2026-W22 | 95.51% | +0.33% | 15.90% | +4.78% | 26,432 |  |
| TZ | 2026-W21 | 88.10% | - | 14.29% | - | 420 |  |
| TZ | 2026-W22 | 94.10% | +6.82% | 6.60% | -53.77% | 424 | ⚠️ |
| YE | 2026-W21 | 92.87% | - | 20.84% | - | 3,436 |  |
| YE | 2026-W22 | 92.18% | -0.75% | 22.15% | +6.28% | 3,540 |  |
| CF | 2026-W21 | 92.89% | - | 15.97% | - | 5,780 |  |
| CF | 2026-W22 | 92.59% | -0.33% | 16.08% | +0.69% | 5,759 |  |
| TK | 2026-W21 | 89.80% | - | 10.54% | - | 294 |  |
| TK | 2026-W22 | 93.62% | +4.26% | 8.21% | -22.17% | 329 | ⚠️ |
| TV | 2026-W21 | 93.22% | - | 9.44% | - | 339 |  |
| TV | 2026-W22 | 94.80% | +1.70% | 5.82% | -38.33% | 481 |  |
| TO | 2026-W21 | 89.10% | - | 11.38% | - | 413 |  |
| TO | 2026-W22 | 88.40% | -0.80% | 12.35% | +8.48% | 405 |  |

**Countries exceeding ±2.5% threshold:** TZ, TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 97.38% | - | 13.98% | - | 31,349 |  |
| Paid | 2026-W22 | 97.28% | -0.10% | 14.58% | +4.28% | 31,325 |  |
| Referral | 2026-W21 | 79.58% | - | 23.47% | - | 6,539 |  |
| Referral | 2026-W22 | 81.59% | +2.52% | 23.37% | -0.43% | 6,687 | ⚠️ |

---

## L2: FJ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 97.56% | - | 13.79% | - | 1.22% | - | 0.44% | - | 22,756 |  |
| Paid | 2026-W22 | 97.56% | +0.00% | 14.55% | +5.56% | 1.33% | +9.08% | 0.52% | +18.63% | 22,444 |  |
| Referral | 2026-W21 | 81.12% | - | 23.45% | - | 17.15% | - | 0.31% | - | 3,813 |  |
| Referral | 2026-W22 | 83.98% | +3.53% | 23.47% | +0.10% | 15.07% | -12.14% | 0.35% | +11.55% | 3,988 | ⚠️ |

**Analysis:** The W22 FAR increase of +0.21 pp is within normal weekly fluctuation and not statistically significant. The notable improvements in TZ (+6.82 pp) and TK (+4.26 pp) correlate strongly with decreased duplicate rates and duplicate blocking, suggesting either improved traffic quality or potential changes in duplicate detection sensitivity that should be monitored. No immediate escalation is required, but continued observation of duplicate metrics in these smaller markets is recommended to confirm the positive trend is sustainable.

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 90.04% | - | 10.82% | - | 6.49% | - | 0.43% | - | 231 |  |
| Paid | 2026-W22 | 93.91% | +4.29% | 7.53% | -30.45% | 5.73% | -11.68% | 0.36% | -17.20% | 279 | ⚠️ |
| Referral | 2026-W21 | 88.89% | - | 9.52% | - | 9.52% | - | 0.00% | - | 63 |  |
| Referral | 2026-W22 | 92.00% | +3.50% | 12.00% | +26.00% | 8.00% | -16.00% | 0.00% | - | 50 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 92.22% | - | 8.68% | - | 3.89% | - | 0.00% | - | 334 |  |
| Paid | 2026-W22 | 90.85% | -1.48% | 9.45% | +8.85% | 6.10% | +56.66% | 0.00% | - | 328 |  |
| Referral | 2026-W21 | 75.95% | - | 22.78% | - | 22.78% | - | 0.00% | - | 79 |  |
| Referral | 2026-W22 | 77.92% | +2.60% | 24.68% | +8.30% | 22.08% | -3.10% | 0.00% | - | 77 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TV Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 93.73% | - | 9.23% | - | 5.90% | - | 0.00% | - | 271 |  |
| Paid | 2026-W22 | 94.65% | +0.98% | 6.08% | -34.06% | 3.65% | -38.18% | 0.00% | - | 411 |  |
| Referral | 2026-W21 | 91.18% | - | 10.29% | - | 8.82% | - | 0.00% | - | 68 |  |
| Referral | 2026-W22 | 95.71% | +4.98% | 4.29% | -58.37% | 4.29% | -51.43% | 0.00% | - | 70 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 91.88% | - | 10.31% | - | 7.19% | - | 0.31% | - | 320 |  |
| Paid | 2026-W22 | 94.99% | +3.39% | 5.57% | -45.98% | 4.46% | -37.99% | 0.00% | -100.00% | 359 | ⚠️ |
| Referral | 2026-W21 | 76.00% | - | 27.00% | - | 24.00% | - | 0.00% | - | 100 |  |
| Referral | 2026-W22 | 89.23% | +17.41% | 12.31% | -54.42% | 10.77% | -55.13% | 0.00% | - | 65 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TZ | ↑ +6.82% | Paid ↑ +3.39%, Referral ↑ +17.41% | ↓ -53.77% | ↓ -51.53% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↑ +4.26% | Paid ↑ +4.29%, Referral ↑ +3.50% | ↓ -22.17% | ↓ -14.89% | ↓ -10.64% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-06-02*
