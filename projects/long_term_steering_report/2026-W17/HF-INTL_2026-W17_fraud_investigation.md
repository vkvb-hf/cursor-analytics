# Fraud Investigation: HF-INTL 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.77% → 92.23% (+0.50%)  
**Volume:** 42,244 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL improved slightly from 91.77% to 92.23% (+0.46pp) in 2026-W17, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | 91.77% → 92.23% | +0.46pp | ✅ |
| L0: Duplicate Rate | 33.87% → 34.60% | +0.73pp | ✅ |
| L0: Duplicate Block | 6.79% → 6.47% | -0.32pp | ✅ |
| L0: PF Block | 0.26% → 0.35% | +0.09pp | ✅ |
| L1: Country Outliers | 4 countries exceed ±2.5% | BE, IE, DK, NZ | ⚠️ |
| L1: Channel Category | Paid stable, Referral -1.43% | Minor shift | ✅ |
| L2: Referral Channel | Multiple countries flagged | Elevated blocks | ⚠️ |

**Key Findings:**
- BE showed the largest positive FAR movement (+5.10pp), driven by a sharp decrease in duplicate rate (-47.83%) and duplicate block rate (-58.99%)
- NZ experienced the largest FAR decline (-4.52pp), with the Referral channel showing increased duplicate block rates (+46.23%) and elevated PF block (+85.90%)
- Referral channel consistently underperforms Paid channel across all markets, with FAR gap of ~24pp (73.50% vs 97.85% overall)
- LU Referral channel shows extreme volatility with FAR dropping -36.11pp (60.87% → 38.89%), though on very low volume (18 customers)
- DK and IE improvements appear driven by reduced duplicate and PF blocking activity

**Action:** Monitor — The overall change is not statistically significant and falls within the 8-week variance range (91.67%-92.38%). Continue tracking NZ Referral channel for potential escalation if blocking rates persist.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 92.23% | 34.60% | 6.47% | 0.35% | 42,244 | +0.50% ← REPORTED CHANGE |
| 2026-W16 | 91.77% | 33.87% | 6.79% | 0.26% | 44,014 | -0.39% |
| 2026-W15 | 92.13% | 30.78% | 6.64% | 0.24% | 42,742 | +0.50% |
| 2026-W14 | 91.67% | 29.90% | 6.93% | 0.22% | 37,155 | -0.11% |
| 2026-W13 | 91.77% | 30.36% | 6.46% | 0.26% | 46,628 | -0.19% |
| 2026-W12 | 91.94% | 30.50% | 6.76% | 0.19% | 44,675 | +0.24% |
| 2026-W11 | 91.72% | 29.84% | 7.03% | 0.15% | 49,898 | -0.71% |
| 2026-W10 | 92.38% | 29.79% | 6.38% | 0.22% | 52,823 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| BE | 2026-W16 | 91.54% | - | 31.47% | - | 1,147 |  |
| BE | 2026-W17 | 96.21% | +5.10% | 16.42% | -47.83% | 2,351 | ⚠️ |
| FR | 2026-W16 | 85.58% | - | 27.90% | - | 7,537 |  |
| FR | 2026-W17 | 86.60% | +1.19% | 28.21% | +1.10% | 6,806 |  |
| AU | 2026-W16 | 92.68% | - | 37.19% | - | 3,635 |  |
| AU | 2026-W17 | 91.06% | -1.75% | 38.71% | +4.08% | 3,725 |  |
| DE | 2026-W16 | 94.33% | - | 33.32% | - | 9,586 |  |
| DE | 2026-W17 | 94.77% | +0.47% | 35.37% | +6.15% | 9,520 |  |
| IE | 2026-W16 | 89.98% | - | 25.02% | - | 1,647 |  |
| IE | 2026-W17 | 92.34% | +2.62% | 24.26% | -3.02% | 1,789 | ⚠️ |
| DK | 2026-W16 | 89.09% | - | 32.07% | - | 1,347 |  |
| DK | 2026-W17 | 92.50% | +3.83% | 32.72% | +2.01% | 1,186 | ⚠️ |
| NZ | 2026-W16 | 89.42% | - | 35.86% | - | 1,068 |  |
| NZ | 2026-W17 | 85.38% | -4.52% | 38.51% | +7.39% | 766 | ⚠️ |

**Countries exceeding ±2.5% threshold:** BE, IE, DK, NZ

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.60% | - | 34.73% | - | 32,875 |  |
| Paid | 2026-W17 | 97.85% | +0.25% | 35.26% | +1.53% | 32,500 |  |
| Referral | 2026-W16 | 74.57% | - | 31.35% | - | 11,139 |  |
| Referral | 2026-W17 | 73.50% | -1.43% | 32.42% | +3.42% | 9,744 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.53% | - | 21.97% | - | 0.45% | - | 0.00% | - | 446 |  |
| Paid | 2026-W17 | 97.84% | +0.31% | 28.13% | +28.00% | 0.72% | +60.82% | 0.00% | - | 416 |  |
| Referral | 2026-W16 | 70.07% | - | 26.28% | - | 24.09% | - | 0.00% | - | 137 |  |
| Referral | 2026-W17 | 75.40% | +7.60% | 24.60% | -6.37% | 22.22% | -7.74% | 0.00% | - | 126 | ⚠️ |

**Analysis:** The HF-INTL Fraud Approval Rate increase of +0.46pp in 2026-W17 represents normal week-over-week fluctuation, with the metric remaining within its established 8-week operating band. Country-level variance is notable in BE (positive) and NZ (negative), both driven primarily by changes in duplicate detection and blocking behavior within the Referral channel. No immediate action is required, but the NZ Referral segment warrants continued monitoring given the sustained elevation in blocking metrics.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.88% | - | 36.08% | - | 0.74% | - | 0.50% | - | 2,977 |  |
| Paid | 2026-W17 | 97.20% | -0.70% | 38.40% | +6.43% | 0.80% | +8.44% | 1.27% | +151.81% | 2,995 |  |
| Referral | 2026-W16 | 69.15% | - | 42.25% | - | 29.33% | - | 0.00% | - | 658 |  |
| Referral | 2026-W17 | 65.89% | -4.71% | 40.00% | -5.32% | 31.78% | +8.35% | 0.27% | - | 730 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 96.45% | - | 12.77% | - | 0.00% | - | 0.00% | - | 141 |  |
| Paid | 2026-W17 | 96.40% | -0.05% | 9.35% | -26.74% | 0.00% | - | 0.72% | - | 139 |  |
| Referral | 2026-W16 | 54.17% | - | 16.67% | - | 12.50% | - | 0.00% | - | 24 |  |
| Referral | 2026-W17 | 48.28% | -10.88% | 24.14% | +44.83% | 20.69% | +65.52% | 0.00% | - | 29 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 98.26% | - | 33.68% | - | 0.70% | - | 0.23% | - | 861 |  |
| Paid | 2026-W17 | 99.41% | +1.17% | 32.82% | -2.55% | 0.24% | -66.24% | 0.12% | -49.35% | 850 |  |
| Referral | 2026-W16 | 72.84% | - | 29.22% | - | 24.28% | - | 0.00% | - | 486 |  |
| Referral | 2026-W17 | 75.00% | +2.97% | 32.44% | +11.03% | 22.32% | -8.07% | 0.00% | - | 336 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GB Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 98.60% | - | 42.60% | - | 0.67% | - | 0.26% | - | 10,195 |  |
| Paid | 2026-W17 | 98.55% | -0.05% | 44.49% | +4.43% | 0.60% | -9.52% | 0.44% | +73.26% | 9,279 |  |
| Referral | 2026-W16 | 74.26% | - | 35.99% | - | 24.32% | - | 0.04% | - | 2,673 |  |
| Referral | 2026-W17 | 71.99% | -3.05% | 38.66% | +7.42% | 26.68% | +9.70% | 0.04% | +14.82% | 2,328 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 95.83% | - | 0.00% | - | 2.78% | - | 1.39% | - | 72 |  |
| Paid | 2026-W17 | 100.00% | +4.35% | 17.19% | - | 0.00% | -100.00% | 0.00% | -100.00% | 64 | ⚠️ |
| Referral | 2026-W16 | 60.87% | - | 0.00% | - | 13.04% | - | 0.00% | - | 23 |  |
| Referral | 2026-W17 | 38.89% | -36.11% | 5.56% | - | 5.56% | -57.41% | 0.00% | - | 18 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NL Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 89.32% | - | 32.64% | - | 6.98% | - | 0.17% | - | 1,161 |  |
| Paid | 2026-W17 | 91.61% | +2.56% | 32.01% | -1.95% | 7.09% | +1.67% | 0.17% | +0.43% | 1,156 | ⚠️ |
| Referral | 2026-W16 | 90.63% | - | 24.13% | - | 7.47% | - | 0.00% | - | 576 |  |
| Referral | 2026-W17 | 90.17% | -0.50% | 23.72% | -1.72% | 8.12% | +8.77% | 0.00% | - | 468 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 98.93% | - | 23.17% | - | 0.27% | - | 0.53% | - | 751 |  |
| Paid | 2026-W17 | 99.66% | +0.74% | 30.98% | +33.70% | 0.17% | -36.78% | 0.00% | -100.00% | 594 |  |
| Referral | 2026-W16 | 86.11% | - | 18.06% | - | 10.42% | - | 0.00% | - | 288 |  |
| Referral | 2026-W17 | 78.24% | -9.14% | 24.54% | +35.90% | 16.67% | +60.00% | 0.00% | - | 216 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.30% | - | 33.29% | - | 0.12% | - | 1.06% | - | 853 |  |
| Paid | 2026-W17 | 96.93% | -0.38% | 36.46% | +9.51% | 0.18% | +53.97% | 2.17% | +105.29% | 554 |  |
| Referral | 2026-W16 | 58.14% | - | 46.05% | - | 37.67% | - | 0.00% | - | 215 |  |
| Referral | 2026-W17 | 55.19% | -5.08% | 43.87% | -4.73% | 40.09% | +6.42% | 0.00% | - | 212 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| BE | ↑ +5.10% | - | ↓ -47.83% | ↓ -58.99% | ↓ -60.97% | [AI_SUMMARY_PLACEHOLDER] |
| IE | ↑ +2.62% | - | ↓ -3.02% | ↓ -22.54% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |
| DK | ↑ +3.83% | Referral ↑ +2.97% | → +2.01% | ↓ -29.47% | ↓ -43.21% | [AI_SUMMARY_PLACEHOLDER] |
| NZ | ↓ -4.52% | Referral ↓ -5.08% | ↑ +7.39% | ↑ +46.23% | ↑ +85.90% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-27*
