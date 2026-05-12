# Fraud Investigation: HF-INTL 2026-W19

**Metric:** Fraud Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.87% → 91.78% (-0.10%)  
**Volume:** 40,723 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined marginally from 91.87% to 91.78% (-0.10pp) in 2026-W19, a change deemed not statistically significant with stable volume of 40,723 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | -0.10pp within normal range | -0.10pp | ✅ |
| L0: 8-Week Trend | FAR stable between 91.66%-92.12% | Normal variance | ✅ |
| L1: Country Scan | AU +2.96pp, LU -14.00pp exceed ±2.5% threshold | 2 countries flagged | ⚠️ |
| L1: Channel Scan | Referral -3.00pp exceeds threshold | 1 channel flagged | ⚠️ |
| L2: Referral Channel | Declines across DE (-6.32pp), DK (-9.45pp), NO (-7.70pp), NL (-5.01pp), NZ (-6.64pp) | Consistent pattern | ⚠️ |
| L2: Dup Rate Impact | Dup Rate increased +13.77% overall (28.96% → 32.95%) | Elevated duplicates | ⚠️ |

**Key Findings:**
- **Referral channel degradation:** Referral FAR dropped -3.00pp (77.19% → 74.88%) with significant declines across multiple countries—DK (-9.45pp), NO (-7.70pp), NZ (-6.64pp), DE (-6.32pp), and NL (-5.01pp)
- **Duplicate rate surge:** Overall Dup Rate increased +13.77% (28.96% → 32.95%), with corresponding Dup Block increases in Referral channels driving FAR declines (e.g., DK Referral Dup Block +101.99%, NO Referral +104.86%)
- **LU small volume anomaly:** LU Referral FAR collapsed -37.82pp (57.89% → 36.00%), but volume is minimal (25 customers) limiting business impact
- **AU positive offset:** AU FAR improved +2.96pp driven by Paid channel (+4.38pp) due to PF Block reduction (-84.25%), partially offsetting global Referral declines
- **Paid channel stable:** Paid channel FAR improved +1.27pp (96.45% → 97.67%) across most markets, containing overall metric impact

**Action:** **Monitor** - The overall FAR change is not significant and within normal variance. However, the consistent Referral channel degradation driven by elevated duplicate rates warrants close monitoring in 2026-W20. If Referral FAR continues declining or Dup Block rates remain elevated, escalate for duplicate detection rule review.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W19 | 91.78% | 32.95% | 6.64% | 0.31% | 40,723 | -0.10% ← REPORTED CHANGE |
| 2026-W18 | 91.87% | 28.96% | 5.33% | 0.55% | 41,111 | -0.26% |
| 2026-W17 | 92.11% | 34.36% | 6.13% | 0.32% | 41,764 | +0.12% |
| 2026-W16 | 92.00% | 33.00% | 6.51% | 0.24% | 44,993 | -0.14% |
| 2026-W15 | 92.12% | 30.68% | 6.54% | 0.24% | 42,712 | +0.51% |
| 2026-W14 | 91.66% | 29.83% | 6.86% | 0.22% | 37,134 | -0.12% |
| 2026-W13 | 91.77% | 30.31% | 6.41% | 0.26% | 46,608 | -0.19% |
| 2026-W12 | 91.95% | 30.46% | 6.72% | 0.19% | 44,662 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| AU | 2026-W18 | 89.55% | - | 32.88% | - | 3,683 |  |
| AU | 2026-W19 | 92.20% | +2.96% | 38.05% | +15.72% | 3,293 | ⚠️ |
| GB | 2026-W18 | 93.31% | - | 38.43% | - | 11,443 |  |
| GB | 2026-W19 | 93.02% | -0.31% | 42.65% | +10.96% | 11,511 |  |
| DE | 2026-W18 | 93.74% | - | 27.72% | - | 8,356 |  |
| DE | 2026-W19 | 93.40% | -0.37% | 32.34% | +16.67% | 7,830 |  |
| DK | 2026-W18 | 95.11% | - | 24.31% | - | 1,226 |  |
| DK | 2026-W19 | 93.20% | -2.01% | 27.12% | +11.58% | 1,014 |  |
| NO | 2026-W18 | 96.68% | - | 19.80% | - | 783 |  |
| NO | 2026-W19 | 94.65% | -2.10% | 22.32% | +12.77% | 654 |  |
| LU | 2026-W18 | 89.00% | - | 0.00% | - | 100 |  |
| LU | 2026-W19 | 76.54% | -14.00% | 7.41% | - | 81 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AU, LU

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 96.45% | - | 29.75% | - | 31,348 |  |
| Paid | 2026-W19 | 97.67% | +1.27% | 33.50% | +12.60% | 30,199 |  |
| Referral | 2026-W18 | 77.19% | - | 26.43% | - | 9,763 |  |
| Referral | 2026-W19 | 74.88% | -3.00% | 31.39% | +18.77% | 10,524 | ⚠️ |

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 93.74% | - | 32.60% | - | 0.74% | - | 3.90% | - | 2,972 |  |
| Paid | 2026-W19 | 97.85% | +4.38% | 37.86% | +16.11% | 1.11% | +50.56% | 0.61% | -84.25% | 2,602 | ⚠️ |
| Referral | 2026-W18 | 72.01% | - | 34.04% | - | 23.91% | - | 0.28% | - | 711 |  |
| Referral | 2026-W19 | 70.91% | -1.53% | 38.78% | +13.95% | 25.62% | +7.13% | 0.29% | +2.89% | 691 |  |

**Analysis:** The -0.10pp FAR decline in 2026-W19 is not statistically significant and reflects normal weekly variance within the 8-week trend (91.66%-92.12%). The primary driver is systematic Referral channel deterioration across multiple markets (DE, DK, NO, NL, NZ), linked to increased duplicate detection rates and corresponding blocks. No immediate action is required, but the Referral channel pattern should be monitored next week to determine if duplicate detection thresholds require recalibration.

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 94.96% | - | 10.08% | - | 0.00% | - | 0.00% | - | 119 |  |
| Paid | 2026-W19 | 97.39% | +2.56% | 11.30% | +12.10% | 0.00% | - | 0.87% | - | 115 | ⚠️ |
| Referral | 2026-W18 | 46.43% | - | 17.86% | - | 17.86% | - | 3.57% | - | 28 |  |
| Referral | 2026-W19 | 44.12% | -4.98% | 14.71% | -17.65% | 14.71% | -17.65% | 0.00% | -100.00% | 34 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 96.89% | - | 27.74% | - | 0.44% | - | 0.07% | - | 7,034 |  |
| Paid | 2026-W19 | 98.13% | +1.28% | 31.98% | +15.28% | 0.59% | +34.62% | 0.09% | +31.78% | 6,405 |  |
| Referral | 2026-W18 | 77.00% | - | 27.61% | - | 21.03% | - | 0.08% | - | 1,322 |  |
| Referral | 2026-W19 | 72.14% | -6.32% | 33.96% | +23.02% | 26.04% | +23.81% | 0.14% | +85.54% | 1,425 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 97.60% | - | 28.49% | - | 0.24% | - | 0.24% | - | 832 |  |
| Paid | 2026-W19 | 99.55% | +2.00% | 26.97% | -5.32% | 0.30% | +26.06% | 0.00% | -100.00% | 660 |  |
| Referral | 2026-W18 | 89.85% | - | 15.48% | - | 6.85% | - | 0.00% | - | 394 |  |
| Referral | 2026-W19 | 81.36% | -9.45% | 27.40% | +76.98% | 13.84% | +101.99% | 0.00% | - | 354 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 96.30% | - | 0.00% | - | 0.00% | - | 1.23% | - | 81 |  |
| Paid | 2026-W19 | 94.64% | -1.72% | 10.71% | - | 0.00% | - | 5.36% | +333.93% | 56 |  |
| Referral | 2026-W18 | 57.89% | - | 0.00% | - | 0.00% | - | 0.00% | - | 19 |  |
| Referral | 2026-W19 | 36.00% | -37.82% | 0.00% | - | 0.00% | - | 0.00% | - | 25 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NL Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 91.51% | - | 24.13% | - | 4.21% | - | 0.56% | - | 1,260 |  |
| Paid | 2026-W19 | 92.11% | +0.66% | 33.49% | +38.79% | 6.59% | +56.67% | 0.38% | -31.03% | 1,305 |  |
| Referral | 2026-W18 | 90.14% | - | 18.51% | - | 6.40% | - | 0.00% | - | 578 |  |
| Referral | 2026-W19 | 85.62% | -5.01% | 29.26% | +58.08% | 10.54% | +64.58% | 0.00% | - | 598 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 98.59% | - | 22.85% | - | 0.70% | - | 0.00% | - | 569 |  |
| Paid | 2026-W19 | 98.91% | +0.32% | 26.09% | +14.18% | 0.22% | -69.08% | 0.00% | - | 460 |  |
| Referral | 2026-W18 | 91.59% | - | 11.68% | - | 3.27% | - | 0.00% | - | 214 |  |
| Referral | 2026-W19 | 84.54% | -7.70% | 13.40% | +14.72% | 6.70% | +104.86% | 0.00% | - | 194 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 96.56% | - | 29.75% | - | 0.90% | - | 1.05% | - | 669 |  |
| Paid | 2026-W19 | 98.38% | +1.89% | 36.18% | +21.62% | 0.15% | -83.60% | 0.74% | -29.73% | 680 |  |
| Referral | 2026-W18 | 64.89% | - | 33.78% | - | 27.11% | - | 0.00% | - | 225 |  |
| Referral | 2026-W19 | 60.58% | -6.64% | 41.49% | +22.84% | 32.37% | +19.38% | 0.00% | - | 241 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| AU | ↑ +2.96% | Paid ↑ +4.38% | ↑ +15.72% | ↑ +20.00% | ↓ -82.94% | [AI_SUMMARY_PLACEHOLDER] |
| LU | ↓ -14.00% | Referral ↓ -37.82% | → - | → - | ↑ +270.37% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-12*
