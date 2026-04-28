# Fraud Investigation: HF-INTL 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.99% → 92.23% (+0.26%)  
**Volume:** 42,244 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL increased slightly from 91.99% to 92.23% (+0.24pp) in 2026-W17, a change deemed not statistically significant with volume of 42,244 customers reaching fraud service.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-INTL Trend | 8-week stability | +0.26% WoW | ✅ |
| L1: Country Scan | ±2.5% threshold | IE +2.62%, DK +3.47%, NZ -4.62% | ⚠️ |
| L1: Channel Category | ±2.5% threshold | Paid +0.16%, Referral -1.55% | ✅ |
| L2: Country Deep-Dives | Referral channel pattern | Multiple countries show Referral declines | ⚠️ |

**Key Findings:**
- **NZ experienced the largest FAR decline (-4.62pp)**, driven by Referral channel (-5.39pp) with increased Dup Block rates (+6.92pp) and elevated Dup Rate (+7.11%)
- **DK and IE showed significant FAR improvements** (+3.47pp and +2.62pp respectively), correlating with decreased Dup Block rates (-29.42% and -22.49%)
- **Referral channel underperforms across all countries**, with FAR ranging from 38.89% (LU) to 78.24% (NO), consistently 20-50pp below Paid channel performance
- **LU shows extreme volatility** with Paid channel at 100% FAR (+5.06pp) but Referral collapsing to 38.89% (-36.11pp) on very low volumes (18-64 customers)
- **Dup Rate increased globally** (+1.48pp to 34.60%), with AU (+3.95%), DE (+6.22%), and NZ (+7.11%) showing the largest increases

**Action:** **Monitor** – The overall FAR change is not significant and within normal variance. Continue monitoring NZ Referral channel for sustained decline patterns and LU for volume stabilization before drawing conclusions from extreme percentage swings.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 92.23% | 34.60% | 6.47% | 0.35% | 42,244 | +0.26% ← REPORTED CHANGE |
| 2026-W16 | 91.99% | 33.12% | 6.63% | 0.25% | 45,020 | -0.15% |
| 2026-W15 | 92.13% | 30.78% | 6.63% | 0.24% | 42,738 | +0.51% |
| 2026-W14 | 91.66% | 29.90% | 6.93% | 0.22% | 37,155 | -0.12% |
| 2026-W13 | 91.77% | 30.36% | 6.46% | 0.26% | 46,625 | -0.18% |
| 2026-W12 | 91.94% | 30.50% | 6.76% | 0.19% | 44,675 | +0.24% |
| 2026-W11 | 91.72% | 29.84% | 7.03% | 0.15% | 49,897 | -0.71% |
| 2026-W10 | 92.38% | 29.78% | 6.37% | 0.22% | 52,821 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| AU | 2026-W16 | 92.82% | - | 37.24% | - | 3,636 |  |
| AU | 2026-W17 | 91.06% | -1.90% | 38.71% | +3.95% | 3,725 |  |
| FR | 2026-W16 | 85.67% | - | 27.87% | - | 7,538 |  |
| FR | 2026-W17 | 86.60% | +1.08% | 28.21% | +1.21% | 6,806 |  |
| IE | 2026-W16 | 89.99% | - | 25.00% | - | 1,648 |  |
| IE | 2026-W17 | 92.34% | +2.62% | 24.26% | -2.96% | 1,789 | ⚠️ |
| DE | 2026-W16 | 94.34% | - | 33.30% | - | 9,584 |  |
| DE | 2026-W17 | 94.77% | +0.45% | 35.37% | +6.22% | 9,520 |  |
| DK | 2026-W16 | 89.39% | - | 32.12% | - | 1,348 |  |
| DK | 2026-W17 | 92.50% | +3.47% | 32.72% | +1.85% | 1,186 | ⚠️ |
| NZ | 2026-W16 | 89.51% | - | 35.96% | - | 1,068 |  |
| NZ | 2026-W17 | 85.38% | -4.62% | 38.51% | +7.11% | 766 | ⚠️ |
| CH | 2026-W16 | 90.30% | - | 13.33% | - | 165 |  |
| CH | 2026-W17 | 88.10% | -2.44% | 11.90% | -10.71% | 168 |  |

**Countries exceeding ±2.5% threshold:** IE, DK, NZ

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.69% | - | 33.71% | - | 33,892 |  |
| Paid | 2026-W17 | 97.85% | +0.16% | 35.25% | +4.57% | 32,499 |  |
| Referral | 2026-W16 | 74.66% | - | 31.31% | - | 11,128 |  |
| Referral | 2026-W17 | 73.50% | -1.55% | 32.43% | +3.57% | 9,745 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.76% | - | 21.97% | - | 0.45% | - | 0.00% | - | 446 |  |
| Paid | 2026-W17 | 97.84% | +0.08% | 28.13% | +28.00% | 0.72% | +60.82% | 0.00% | - | 416 |  |
| Referral | 2026-W16 | 70.07% | - | 26.28% | - | 24.09% | - | 0.00% | - | 137 |  |
| Referral | 2026-W17 | 75.40% | +7.60% | 24.60% | -6.37% | 22.22% | -7.74% | 0.00% | - | 126 | ⚠️ |

**Analysis:** The +0.24pp increase in HF-INTL Fraud Approval Rate represents normal week-over-week fluctuation within the established 91.66%-92.38% range observed over the past 8 weeks. While three countries (IE, DK, NZ) exceeded the ±2.5% threshold, the opposing directions largely offset at the aggregate level, and the Referral channel's structural underperformance remains a known pattern rather than a new development. No immediate escalation is required, but the NZ market warrants continued observation given its combination of declining FAR and increasing duplicate-related blocks.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.99% | - | 36.13% | - | 0.81% | - | 0.50% | - | 2,981 |  |
| Paid | 2026-W17 | 97.20% | -0.81% | 38.40% | +6.28% | 0.80% | -0.47% | 1.27% | +152.15% | 2,995 |  |
| Referral | 2026-W16 | 69.31% | - | 42.29% | - | 29.31% | - | 0.00% | - | 655 |  |
| Referral | 2026-W17 | 65.89% | -4.94% | 40.00% | -5.42% | 31.78% | +8.42% | 0.27% | - | 730 | ⚠️ |

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

## L2: GB Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 98.57% | - | 42.59% | - | 0.67% | - | 0.25% | - | 10,195 |  |
| Paid | 2026-W17 | 98.54% | -0.02% | 44.48% | +4.44% | 0.60% | -9.51% | 0.44% | +80.21% | 9,278 |  |
| Referral | 2026-W16 | 74.29% | - | 35.93% | - | 24.25% | - | 0.04% | - | 2,672 |  |
| Referral | 2026-W17 | 72.01% | -3.07% | 38.69% | +7.68% | 26.66% | +9.95% | 0.04% | +14.73% | 2,329 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 95.18% | - | 1.20% | - | 3.61% | - | 1.20% | - | 83 |  |
| Paid | 2026-W17 | 100.00% | +5.06% | 17.19% | +1326.56% | 0.00% | -100.00% | 0.00% | -100.00% | 64 | ⚠️ |
| Referral | 2026-W16 | 60.87% | - | 0.00% | - | 13.04% | - | 0.00% | - | 23 |  |
| Referral | 2026-W17 | 38.89% | -36.11% | 5.56% | - | 5.56% | -57.41% | 0.00% | - | 18 | ⚠️ |

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
| Paid | 2026-W16 | 97.42% | - | 33.45% | - | 0.12% | - | 1.06% | - | 852 |  |
| Paid | 2026-W17 | 96.93% | -0.50% | 36.46% | +9.00% | 0.18% | +53.79% | 2.17% | +105.05% | 554 |  |
| Referral | 2026-W16 | 58.33% | - | 45.83% | - | 37.50% | - | 0.00% | - | 216 |  |
| Referral | 2026-W17 | 55.19% | -5.39% | 43.87% | -4.29% | 40.09% | +6.92% | 0.00% | - | 212 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| IE | ↑ +2.62% | - | ↓ -2.96% | ↓ -22.49% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |
| DK | ↑ +3.47% | - | → +1.85% | ↓ -29.42% | ↓ -43.17% | [AI_SUMMARY_PLACEHOLDER] |
| NZ | ↓ -4.62% | Referral ↓ -5.39% | ↑ +7.11% | ↑ +46.23% | ↑ +85.90% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-28*
