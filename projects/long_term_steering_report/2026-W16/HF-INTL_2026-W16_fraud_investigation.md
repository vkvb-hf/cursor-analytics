# Fraud Investigation: HF-INTL 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 92.13% → 92.06% (-0.08%)  
**Volume:** 45,438 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined marginally from 92.13% to 92.06% (-0.08pp) in 2026-W16, a change deemed not statistically significant given the volume of 45,438 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | -0.08pp within normal range | -0.08pp | ✅ |
| L0: Dup Rate | Increased from 30.85% to 33.28% | +2.43pp | ⚠️ |
| L0: Dup Block | Increased from 6.69% to 6.87% | +0.18pp | ✅ |
| L1: Country Variance | 3 countries exceed ±2.5% threshold (NZ, AT, LU) | Mixed | ⚠️ |
| L1: Channel Category | Referral channel declined -3.10pp | -3.10pp | ⚠️ |
| L2: Referral Pattern | Consistent degradation across 10 countries | Systemic | ⚠️ |

**Key Findings:**
- **Referral channel systemic issue:** FAR declined in Referral across all 10 analyzed countries, with drops ranging from -2.74pp (SE) to -26.96pp (LU), while Paid channel remained stable or improved
- **Duplicate rate surge:** Overall Dup Rate increased +7.88% (30.85% → 33.28%), correlating with rising Dup Block rates in Referral channel across AT (+24.32%), BE (+54.29%), IE (+35.59%), and FR (+14.95%)
- **LU and AT show acute declines:** LU Referral FAR dropped from 83.33% to 60.87% (-26.96pp) and AT Referral from 79.38% to 70.07% (-11.72pp), both driven by elevated duplicate blocking
- **NZ counter-trend:** NZ improved +3.32pp overall, with Referral FAR rising +7.42pp due to reduced Dup Block (-12.04pp) despite higher duplicate rates
- **Low volume markets amplify variance:** LU (23 Referral customers) and CH (25 Referral customers) show high volatility due to small sample sizes

**Action:** **Monitor** - The overall FAR change is not significant, but the consistent Referral channel degradation across multiple markets warrants continued observation. If Referral FAR declines persist for 2+ consecutive weeks, escalate for investigation into duplicate detection rules affecting referred customers.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 92.06% | 33.28% | 6.87% | 0.28% | 45,438 | -0.08% ← REPORTED CHANGE |
| 2026-W15 | 92.13% | 30.85% | 6.69% | 0.24% | 42,758 | +0.50% |
| 2026-W14 | 91.68% | 29.94% | 6.97% | 0.22% | 37,163 | -0.10% |
| 2026-W13 | 91.77% | 30.39% | 6.49% | 0.27% | 46,641 | -0.20% |
| 2026-W12 | 91.95% | 30.51% | 6.77% | 0.19% | 44,677 | +0.24% |
| 2026-W11 | 91.73% | 29.85% | 7.04% | 0.15% | 49,900 | -0.69% |
| 2026-W10 | 92.37% | 29.79% | 6.39% | 0.22% | 52,825 | -0.01% |
| 2026-W09 | 92.38% | 29.13% | 6.24% | 0.37% | 54,944 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FR | 2026-W15 | 87.83% | - | 25.75% | - | 8,325 |  |
| FR | 2026-W16 | 85.67% | -2.46% | 28.27% | +9.79% | 7,636 |  |
| AU | 2026-W15 | 91.50% | - | 36.87% | - | 3,436 |  |
| AU | 2026-W16 | 92.92% | +1.55% | 37.49% | +1.68% | 3,670 |  |
| GB | 2026-W15 | 93.22% | - | 40.82% | - | 10,498 |  |
| GB | 2026-W16 | 93.51% | +0.32% | 41.40% | +1.44% | 12,885 |  |
| NZ | 2026-W15 | 86.82% | - | 34.83% | - | 933 |  |
| NZ | 2026-W16 | 89.70% | +3.32% | 36.18% | +3.86% | 1,078 | ⚠️ |
| AT | 2026-W15 | 94.09% | - | 17.99% | - | 728 |  |
| AT | 2026-W16 | 91.37% | -2.89% | 22.67% | +26.00% | 591 | ⚠️ |
| LU | 2026-W15 | 94.52% | - | 0.00% | - | 73 |  |
| LU | 2026-W16 | 88.89% | -5.96% | 13.89% | - | 108 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, AT, LU

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 97.70% | - | 31.33% | - | 31,540 |  |
| Paid | 2026-W16 | 97.97% | +0.28% | 33.64% | +7.39% | 34,176 |  |
| Referral | 2026-W15 | 76.48% | - | 29.52% | - | 11,218 |  |
| Referral | 2026-W16 | 74.12% | -3.10% | 32.16% | +8.97% | 11,262 | ⚠️ |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 98.24% | - | 17.08% | - | 0.53% | - | 0.35% | - | 568 |  |
| Paid | 2026-W16 | 97.80% | -0.45% | 21.59% | +26.40% | 0.44% | -16.59% | 0.00% | -100.00% | 454 |  |
| Referral | 2026-W15 | 79.38% | - | 21.25% | - | 19.38% | - | 0.00% | - | 160 |  |
| Referral | 2026-W16 | 70.07% | -11.72% | 26.28% | +23.66% | 24.09% | +24.32% | 0.00% | - | 137 | ⚠️ |

**Analysis:** The -0.08pp FAR decline in 2026-W16 falls within normal operational variance and does not require immediate intervention. However, the data reveals a systematic pattern of Referral channel underperformance across all analyzed markets, primarily driven by increased duplicate detection and blocking rates. This Referral-specific trend should be monitored closely, as sustained degradation could impact overall acquisition efficiency and partner relationships.

---

## L2: BE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 98.74% | - | 15.09% | - | 0.40% | - | 0.20% | - | 1,511 |  |
| Paid | 2026-W16 | 99.16% | +0.43% | 13.75% | -8.89% | 0.21% | -47.34% | 0.26% | +31.64% | 1,913 |  |
| Referral | 2026-W15 | 85.37% | - | 26.27% | - | 12.24% | - | 0.00% | - | 335 |  |
| Referral | 2026-W16 | 78.72% | -7.79% | 28.72% | +9.34% | 18.88% | +54.29% | 0.27% | - | 376 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 97.52% | - | 9.09% | - | 0.00% | - | 1.65% | - | 121 |  |
| Paid | 2026-W16 | 97.16% | -0.37% | 12.77% | +40.43% | 0.00% | - | 0.00% | -100.00% | 141 |  |
| Referral | 2026-W15 | 60.00% | - | 36.00% | - | 32.00% | - | 0.00% | - | 25 |  |
| Referral | 2026-W16 | 52.00% | -13.33% | 20.00% | -44.44% | 16.00% | -50.00% | 0.00% | - | 25 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 98.44% | - | 29.28% | - | 0.50% | - | 0.09% | - | 7,374 |  |
| Paid | 2026-W16 | 98.96% | +0.52% | 33.72% | +15.15% | 0.45% | -9.67% | 0.05% | -46.95% | 7,943 |  |
| Referral | 2026-W15 | 75.25% | - | 30.46% | - | 24.39% | - | 0.06% | - | 1,681 |  |
| Referral | 2026-W16 | 72.01% | -4.31% | 32.95% | +8.20% | 27.33% | +12.06% | 0.12% | +101.08% | 1,672 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 98.70% | - | 30.73% | - | 0.33% | - | 0.33% | - | 921 |  |
| Paid | 2026-W16 | 98.75% | +0.06% | 33.83% | +10.08% | 0.68% | +109.08% | 0.23% | -30.31% | 881 |  |
| Referral | 2026-W15 | 78.88% | - | 28.36% | - | 19.79% | - | 0.00% | - | 677 |  |
| Referral | 2026-W16 | 73.42% | -6.93% | 29.65% | +4.56% | 24.54% | +23.98% | 0.00% | - | 489 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: FR Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.41% | - | 26.26% | - | 3.10% | - | 0.32% | - | 4,969 |  |
| Paid | 2026-W16 | 95.23% | -0.19% | 27.38% | +4.24% | 3.41% | +10.14% | 0.23% | -28.85% | 4,365 |  |
| Referral | 2026-W15 | 76.61% | - | 25.00% | - | 22.02% | - | 0.45% | - | 3,356 |  |
| Referral | 2026-W16 | 72.91% | -4.82% | 29.47% | +17.88% | 25.31% | +14.95% | 1.01% | +125.72% | 3,271 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: IE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 97.69% | - | 23.43% | - | 0.74% | - | 0.28% | - | 1,084 |  |
| Paid | 2026-W16 | 98.37% | +0.69% | 23.39% | -0.16% | 0.77% | +4.50% | 0.17% | -38.07% | 1,167 |  |
| Referral | 2026-W15 | 78.02% | - | 25.20% | - | 20.97% | - | 0.00% | - | 496 |  |
| Referral | 2026-W16 | 70.97% | -9.04% | 29.42% | +16.75% | 28.43% | +35.59% | 0.00% | - | 503 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.72% | - | 0.00% | - | 0.00% | - | 1.64% | - | 61 |  |
| Paid | 2026-W16 | 96.47% | -0.26% | 12.94% | - | 2.35% | - | 1.18% | -28.24% | 85 |  |
| Referral | 2026-W15 | 83.33% | - | 0.00% | - | 0.00% | - | 0.00% | - | 12 |  |
| Referral | 2026-W16 | 60.87% | -26.96% | 17.39% | - | 13.04% | - | 0.00% | - | 23 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.66% | - | 30.88% | - | 0.56% | - | 0.97% | - | 719 |  |
| Paid | 2026-W16 | 97.90% | +1.28% | 33.45% | +8.34% | 0.12% | -79.05% | 1.17% | +19.71% | 858 |  |
| Referral | 2026-W15 | 53.74% | - | 48.13% | - | 43.93% | - | 0.93% | - | 214 |  |
| Referral | 2026-W16 | 57.73% | +7.42% | 46.82% | -2.73% | 38.64% | -12.04% | 0.00% | -100.00% | 220 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: SE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 98.76% | - | 27.82% | - | 0.46% | - | 0.00% | - | 1,294 |  |
| Paid | 2026-W16 | 99.03% | +0.27% | 29.99% | +7.80% | 0.32% | -30.26% | 0.08% | - | 1,237 |  |
| Referral | 2026-W15 | 86.73% | - | 26.54% | - | 11.42% | - | 0.00% | - | 324 |  |
| Referral | 2026-W16 | 84.36% | -2.74% | 29.14% | +9.79% | 11.35% | -0.61% | 0.00% | - | 326 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| NZ | ↑ +3.32% | Referral ↑ +7.42% | ↑ +3.86% | ↓ -24.05% | ↓ -3.83% | [AI_SUMMARY_PLACEHOLDER] |
| AT | ↓ -2.89% | Referral ↓ -11.72% | ↑ +26.00% | ↑ +26.80% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |
| LU | ↓ -5.96% | Referral ↓ -26.96% | → - | → - | ↓ -32.41% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-22*
