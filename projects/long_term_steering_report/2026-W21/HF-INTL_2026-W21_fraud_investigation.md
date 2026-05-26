# Fraud Investigation: HF-INTL 2026-W21

**Metric:** Fraud Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 91.21% → 92.22% (+1.10%)  
**Volume:** 34,892 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL improved by +1.10pp week-over-week (91.21% → 92.22%) on a volume of 34,892 customers, representing a statistically significant positive change that returns the metric to its typical range observed over the past 8 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR Trend | Within normal 8-week range (91.67%-92.22%) | +1.10pp | ✅ |
| L1: Country Breakdown | CH exceeds ±2.5% threshold (-7.22%) | Mixed | ⚠️ |
| L1: Channel Category | Paid +0.46pp, Referral -0.46pp | Stable | ✅ |
| L2: Referral Channel | Multiple countries flagged with FAR declines | Declining | ⚠️ |

**Key Findings:**
- **CH anomaly:** CH experienced the largest FAR decline (-7.22pp) driven by Paid channel dropping -3.84pp, coupled with a dramatic -60.37% decrease in Duplicate Rate (15.89% → 6.30%) on low volume (127 customers)
- **Referral channel weakness:** Referral FAR declined across multiple countries including IE (-7.50pp), BE (-6.30%), AU (-5.59pp), and LU (-11.11pp), consistently showing elevated Duplicate Block rates
- **GB and DE drove overall improvement:** GB (+1.24pp) and DE (+1.49pp) contributed most to the aggregate FAR increase, with GB showing improved Duplicate Rate (-3.94%)
- **Volume decline:** Overall volume decreased by 10.1% (38,823 → 34,892), consistent across most countries
- **NL positive reversal:** NL showed strong FAR improvement (+2.35pp) with Duplicate Rate declining -6.89%

**Action:** **Monitor** – The overall FAR improvement is positive and within historical norms. However, **Investigate** the CH market specifically given the unusual combination of FAR decline with dramatically reduced Duplicate Rate, which may indicate a data quality issue or operational change. Also monitor Referral channel performance across IE, BE, and AU where Duplicate Block rates are elevated.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W21 | 92.22% | 31.42% | 6.06% | 0.31% | 34,892 | +1.10% ← REPORTED CHANGE |
| 2026-W20 | 91.21% | 32.35% | 6.78% | 0.31% | 38,823 | -1.01% |
| 2026-W19 | 92.14% | 28.66% | 5.44% | 0.26% | 40,009 | +0.35% |
| 2026-W18 | 91.82% | 28.84% | 5.22% | 0.54% | 41,078 | -0.31% |
| 2026-W17 | 92.11% | 34.28% | 6.05% | 0.31% | 41,748 | +0.12% |
| 2026-W16 | 92.00% | 32.94% | 6.44% | 0.23% | 44,975 | -0.12% |
| 2026-W15 | 92.11% | 30.64% | 6.50% | 0.24% | 42,699 | +0.49% |
| 2026-W14 | 91.67% | 29.77% | 6.80% | 0.22% | 37,120 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FR | 2026-W20 | 86.81% | - | 24.85% | - | 7,641 |  |
| FR | 2026-W21 | 88.45% | +1.89% | 25.51% | +2.64% | 6,492 |  |
| GB | 2026-W20 | 92.51% | - | 43.18% | - | 10,248 |  |
| GB | 2026-W21 | 93.65% | +1.24% | 41.48% | -3.94% | 8,573 |  |
| DE | 2026-W20 | 92.49% | - | 31.18% | - | 7,473 |  |
| DE | 2026-W21 | 93.87% | +1.49% | 31.61% | +1.39% | 6,871 |  |
| AU | 2026-W20 | 91.90% | - | 37.71% | - | 3,739 |  |
| AU | 2026-W21 | 90.93% | -1.05% | 37.86% | +0.39% | 3,550 |  |
| NL | 2026-W20 | 90.20% | - | 29.89% | - | 1,673 |  |
| NL | 2026-W21 | 92.32% | +2.35% | 27.83% | -6.89% | 1,380 |  |
| NZ | 2026-W20 | 85.10% | - | 36.40% | - | 1,000 |  |
| NZ | 2026-W21 | 86.86% | +2.06% | 37.75% | +3.71% | 951 |  |
| CH | 2026-W20 | 87.42% | - | 15.89% | - | 151 |  |
| CH | 2026-W21 | 81.10% | -7.22% | 6.30% | -60.37% | 127 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CH

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 97.25% | - | 32.85% | - | 28,609 |  |
| Paid | 2026-W21 | 97.69% | +0.46% | 31.61% | -3.79% | 26,843 |  |
| Referral | 2026-W20 | 74.29% | - | 30.93% | - | 10,214 |  |
| Referral | 2026-W21 | 73.95% | -0.46% | 30.79% | -0.46% | 8,049 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 96.41% | - | 23.48% | - | 1.10% | - | 0.00% | - | 362 |  |
| Paid | 2026-W21 | 97.96% | +1.61% | 22.79% | -2.95% | 0.00% | -100.00% | 0.00% | - | 294 |  |
| Referral | 2026-W20 | 73.28% | - | 25.00% | - | 18.97% | - | 0.00% | - | 116 |  |
| Referral | 2026-W21 | 71.43% | -2.52% | 21.05% | -15.79% | 16.54% | -12.78% | 0.00% | - | 133 | ⚠️ |

**Analysis:** The W21 FAR improvement of +1.10pp represents a recovery from W20's -1.01pp decline, returning HF-INTL to its baseline performance range. While the aggregate trend is healthy, the CH market warrants attention due to its -7.22pp FAR decline paired with anomalous Duplicate Rate behavior on low volume. The consistent underperformance of the Referral channel across multiple countries (IE, BE, AU, LU) suggests a systematic pattern that may benefit from deeper investigation if it persists in W22.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 97.04% | - | 37.50% | - | 0.69% | - | 0.99% | - | 3,043 |  |
| Paid | 2026-W21 | 96.81% | -0.24% | 36.49% | -2.68% | 1.14% | +65.86% | 1.46% | +47.77% | 2,883 |  |
| Referral | 2026-W20 | 69.40% | - | 38.65% | - | 26.58% | - | 0.86% | - | 696 |  |
| Referral | 2026-W21 | 65.52% | -5.59% | 43.78% | +13.27% | 31.63% | +19.01% | 0.00% | -100.00% | 667 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: BE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 98.73% | - | 17.53% | - | 0.30% | - | 0.12% | - | 1,654 |  |
| Paid | 2026-W21 | 98.74% | +0.01% | 13.20% | -24.69% | 0.05% | -85.09% | 0.32% | +160.88% | 2,219 |  |
| Referral | 2026-W20 | 79.26% | - | 25.85% | - | 14.49% | - | 0.00% | - | 352 |  |
| Referral | 2026-W21 | 74.26% | -6.30% | 33.46% | +29.41% | 18.75% | +29.41% | 0.00% | - | 272 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 97.41% | - | 18.10% | - | 0.00% | - | 0.00% | - | 116 |  |
| Paid | 2026-W21 | 93.67% | -3.84% | 5.06% | -72.03% | 0.00% | - | 2.53% | - | 79 | ⚠️ |
| Referral | 2026-W20 | 54.29% | - | 8.57% | - | 2.86% | - | 0.00% | - | 35 |  |
| Referral | 2026-W21 | 60.42% | +11.29% | 8.33% | -2.78% | 2.08% | -27.08% | 0.00% | - | 48 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GB Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 98.34% | - | 44.60% | - | 0.62% | - | 0.30% | - | 8,125 |  |
| Paid | 2026-W21 | 98.77% | +0.44% | 42.70% | -4.27% | 0.52% | -15.35% | 0.27% | -6.93% | 6,911 |  |
| Referral | 2026-W20 | 70.18% | - | 37.73% | - | 27.08% | - | 0.14% | - | 2,123 |  |
| Referral | 2026-W21 | 72.38% | +3.13% | 36.40% | -3.52% | 25.63% | -5.36% | 0.06% | -57.42% | 1,662 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: IE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 98.86% | - | 20.53% | - | 0.53% | - | 0.00% | - | 1,140 |  |
| Paid | 2026-W21 | 98.85% | -0.01% | 22.43% | +9.25% | 0.19% | -63.43% | 0.10% | - | 1,039 |  |
| Referral | 2026-W20 | 80.09% | - | 24.07% | - | 17.28% | - | 0.15% | - | 648 |  |
| Referral | 2026-W21 | 74.08% | -7.50% | 24.54% | +1.94% | 22.02% | +27.39% | 0.00% | -100.00% | 436 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 100.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 76 |  |
| Paid | 2026-W21 | 100.00% | +0.00% | 7.55% | - | 0.00% | - | 0.00% | - | 106 |  |
| Referral | 2026-W20 | 33.33% | - | 0.00% | - | 0.00% | - | 0.00% | - | 21 |  |
| Referral | 2026-W21 | 29.63% | -11.11% | 3.70% | - | 3.70% | - | 0.00% | - | 27 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NL Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 91.79% | - | 31.79% | - | 6.64% | - | 0.00% | - | 1,145 |  |
| Paid | 2026-W21 | 93.39% | +1.74% | 30.34% | -4.58% | 5.74% | -13.49% | 0.00% | - | 923 |  |
| Referral | 2026-W20 | 86.74% | - | 25.76% | - | 10.23% | - | 0.00% | - | 528 |  |
| Referral | 2026-W21 | 90.15% | +3.93% | 22.76% | -11.65% | 7.66% | -25.12% | 0.00% | - | 457 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 99.42% | - | 27.03% | - | 0.29% | - | 0.00% | - | 344 |  |
| Paid | 2026-W21 | 99.02% | -0.40% | 19.32% | -28.55% | 0.00% | -100.00% | 0.00% | - | 409 |  |
| Referral | 2026-W20 | 81.02% | - | 20.44% | - | 6.57% | - | 0.00% | - | 137 |  |
| Referral | 2026-W21 | 83.33% | +2.85% | 16.67% | -18.45% | 5.75% | -12.52% | 0.00% | - | 174 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 96.41% | - | 33.24% | - | 0.66% | - | 1.20% | - | 752 |  |
| Paid | 2026-W21 | 97.75% | +1.39% | 36.06% | +8.46% | 0.56% | -15.27% | 0.56% | -52.93% | 710 |  |
| Referral | 2026-W20 | 50.81% | - | 45.97% | - | 38.31% | - | 2.02% | - | 248 |  |
| Referral | 2026-W21 | 54.77% | +7.80% | 42.74% | -7.02% | 37.76% | -1.43% | 0.00% | -100.00% | 241 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| CH | ↓ -7.22% | Paid ↓ -3.84%, Referral ↑ +11.29% | ↓ -60.37% | ↑ +18.90% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-26*
