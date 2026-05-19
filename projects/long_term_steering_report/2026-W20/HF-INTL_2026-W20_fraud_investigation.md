# Fraud Investigation: HF-INTL 2026-W20

**Metric:** Fraud Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.16% → 91.39% (-0.83%)  
**Volume:** 39,005 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined by -0.83pp from 92.16% to 91.39% in 2026-W20, a change classified as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | 92.16% → 91.39% | -0.83pp | ✅ |
| L0: Duplicate Rate | 28.72% → 32.53% | +3.81pp | ⚠️ |
| L0: Duplicate Block Rate | 5.49% → 6.98% | +1.49pp | ⚠️ |
| L1: Country Variance | 4 countries exceed ±2.5% | NZ, AT, LU, CH | ⚠️ |
| L1: Channel Category | Referral ↓ -4.21pp | 77.43% → 74.17% | ⚠️ |
| L2: Referral Channel | Consistent declines across markets | -5% to -18% | ⚠️ |

**Key Findings:**
- **Referral channel is the primary driver:** FAR in the Referral category dropped -4.21pp (77.43% → 74.17%), while Paid improved +0.48pp. This pattern is consistent across all L2 country deep-dives.
- **Duplicate rates increased significantly:** Overall duplicate rate rose +3.81pp (28.72% → 32.53%), with Referral channel duplicate rates increasing +17.28% (26.90% → 31.55%).
- **NZ shows the largest decline:** NZ FAR dropped -3.35pp, driven almost entirely by Referral channel (-18.14pp), with duplicate block rate surging +39.48pp to 38.71%.
- **Small markets show high volatility:** LU (+12.86pp) and CH (+3.46pp) showed improvements, but with low volumes (98 and 151 customers respectively), making these statistically unreliable.
- **Duplicate block rates in Referral channel elevated across all markets:** GB (+25.04%), DE (+24.74%), FR (+20.07%), and NZ (+39.48%) all show substantial increases in duplicate blocking within Referral.

**Action:** **Monitor** — The overall change is not statistically significant and falls within normal weekly variance (8-week FAR range: 91.39%-92.16%). However, the consistent Referral channel deterioration and rising duplicate rates warrant continued observation. If Referral FAR declines persist for 2+ consecutive weeks, escalate for investigation into potential referral fraud patterns or duplicate detection policy changes.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W20 | 91.39% | 32.53% | 6.98% | 0.33% | 39,005 | -0.83% ← REPORTED CHANGE |
| 2026-W19 | 92.16% | 28.72% | 5.49% | 0.26% | 40,028 | +0.35% |
| 2026-W18 | 91.83% | 28.87% | 5.26% | 0.55% | 41,091 | -0.29% |
| 2026-W17 | 92.10% | 34.31% | 6.07% | 0.31% | 41,756 | +0.11% |
| 2026-W16 | 92.00% | 32.96% | 6.47% | 0.23% | 44,982 | -0.12% |
| 2026-W15 | 92.12% | 30.66% | 6.53% | 0.24% | 42,704 | +0.49% |
| 2026-W14 | 91.66% | 29.80% | 6.83% | 0.22% | 37,127 | -0.11% |
| 2026-W13 | 91.77% | 30.29% | 6.40% | 0.26% | 46,599 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| GB | 2026-W19 | 93.93% | - | 37.19% | - | 11,343 |  |
| GB | 2026-W20 | 92.53% | -1.49% | 43.39% | +16.66% | 10,262 |  |
| FR | 2026-W19 | 88.23% | - | 23.07% | - | 7,808 |  |
| FR | 2026-W20 | 87.01% | -1.38% | 25.24% | +9.43% | 7,662 |  |
| DE | 2026-W19 | 93.56% | - | 28.77% | - | 7,751 |  |
| DE | 2026-W20 | 92.72% | -0.90% | 31.38% | +9.08% | 7,488 |  |
| NZ | 2026-W19 | 88.57% | - | 30.99% | - | 910 |  |
| NZ | 2026-W20 | 85.60% | -3.35% | 36.70% | +18.43% | 1,000 | ⚠️ |
| AT | 2026-W19 | 93.58% | - | 18.29% | - | 514 |  |
| AT | 2026-W20 | 90.63% | -3.16% | 24.17% | +32.15% | 480 | ⚠️ |
| LU | 2026-W19 | 75.95% | - | 0.00% | - | 79 |  |
| LU | 2026-W20 | 85.71% | +12.86% | 10.20% | - | 98 | ⚠️ |
| CH | 2026-W19 | 85.14% | - | 11.49% | - | 148 |  |
| CH | 2026-W20 | 88.08% | +3.46% | 15.89% | +38.37% | 151 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, AT, LU, CH

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.09% | - | 29.33% | - | 29,983 |  |
| Paid | 2026-W20 | 97.56% | +0.48% | 32.88% | +12.09% | 28,722 |  |
| Referral | 2026-W19 | 77.43% | - | 26.90% | - | 10,045 |  |
| Referral | 2026-W20 | 74.17% | -4.21% | 31.55% | +17.28% | 10,283 | ⚠️ |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 98.20% | - | 19.02% | - | 0.26% | - | 0.26% | - | 389 |  |
| Paid | 2026-W20 | 96.69% | -1.54% | 23.48% | +23.43% | 1.10% | +329.83% | 0.00% | -100.00% | 362 |  |
| Referral | 2026-W19 | 79.20% | - | 16.00% | - | 13.60% | - | 0.00% | - | 125 |  |
| Referral | 2026-W20 | 72.03% | -9.05% | 26.27% | +64.19% | 20.34% | +49.55% | 0.00% | - | 118 | ⚠️ |

**Analysis:** The -0.83pp FAR decline in 2026-W20 is not statistically significant and represents normal operational variance within the 8-week trend. The primary driver is deteriorating performance in the Referral channel across all major markets, correlated with increased duplicate rates and duplicate block rates—suggesting either a shift in Referral traffic quality or tightened fraud controls disproportionately affecting this segment. No immediate action is required, but the Referral channel should be monitored closely over the next 2-3 weeks to determine if this represents a sustained trend requiring intervention.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.15% | - | 32.83% | - | 1.08% | - | 0.58% | - | 2,601 |  |
| Paid | 2026-W20 | 97.40% | +0.25% | 37.64% | +14.65% | 0.72% | -32.75% | 1.05% | +82.59% | 3,039 |  |
| Referral | 2026-W19 | 72.96% | - | 33.69% | - | 22.21% | - | 0.30% | - | 662 |  |
| Referral | 2026-W20 | 68.85% | -5.64% | 39.12% | +16.13% | 27.17% | +22.35% | 0.85% | +182.50% | 703 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: BE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.33% | - | 13.94% | - | 0.24% | - | 0.18% | - | 1,650 |  |
| Paid | 2026-W20 | 99.20% | +1.92% | 16.52% | +18.55% | 0.23% | -6.30% | 0.17% | -6.30% | 1,761 |  |
| Referral | 2026-W19 | 84.18% | - | 20.91% | - | 9.92% | - | 0.00% | - | 373 |  |
| Referral | 2026-W20 | 79.66% | -5.37% | 27.12% | +29.68% | 15.25% | +53.78% | 0.00% | - | 354 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.37% | - | 10.53% | - | 0.00% | - | 0.00% | - | 114 |  |
| Paid | 2026-W20 | 97.41% | +0.05% | 18.10% | +71.98% | 0.00% | - | 0.00% | - | 116 |  |
| Referral | 2026-W19 | 44.12% | - | 14.71% | - | 14.71% | - | 0.00% | - | 34 |  |
| Referral | 2026-W20 | 57.14% | +29.52% | 8.57% | -41.71% | 2.86% | -80.57% | 0.00% | - | 35 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.57% | - | 28.51% | - | 0.53% | - | 0.08% | - | 6,388 |  |
| Paid | 2026-W20 | 98.68% | +1.14% | 30.64% | +7.48% | 0.42% | -20.58% | 0.02% | -78.40% | 5,914 |  |
| Referral | 2026-W19 | 74.76% | - | 30.01% | - | 22.82% | - | 0.15% | - | 1,363 |  |
| Referral | 2026-W20 | 70.33% | -5.93% | 34.18% | +13.91% | 28.46% | +24.74% | 0.13% | -13.41% | 1,574 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: FR Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 94.74% | - | 22.67% | - | 2.60% | - | 0.41% | - | 4,579 |  |
| Paid | 2026-W20 | 94.72% | -0.02% | 23.88% | +5.35% | 3.56% | +37.15% | 0.51% | +23.48% | 4,489 |  |
| Referral | 2026-W19 | 79.00% | - | 23.63% | - | 18.43% | - | 0.31% | - | 3,229 |  |
| Referral | 2026-W20 | 76.11% | -3.66% | 27.17% | +14.97% | 22.12% | +20.07% | 0.47% | +52.65% | 3,173 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GB Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 98.34% | - | 38.26% | - | 0.52% | - | 0.36% | - | 9,170 |  |
| Paid | 2026-W20 | 98.43% | +0.08% | 44.64% | +16.68% | 0.64% | +22.22% | 0.30% | -17.95% | 8,128 |  |
| Referral | 2026-W19 | 75.29% | - | 32.72% | - | 22.41% | - | 0.05% | - | 2,173 |  |
| Referral | 2026-W20 | 70.06% | -6.95% | 38.66% | +18.15% | 28.02% | +25.04% | 0.19% | +307.31% | 2,134 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: IE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 98.14% | - | 17.09% | - | 0.78% | - | 0.00% | - | 1,024 |  |
| Paid | 2026-W20 | 98.95% | +0.82% | 20.53% | +20.11% | 0.53% | -32.63% | 0.09% | - | 1,140 |  |
| Referral | 2026-W19 | 77.05% | - | 19.44% | - | 17.80% | - | 0.70% | - | 427 |  |
| Referral | 2026-W20 | 80.12% | +3.99% | 24.35% | +25.25% | 17.57% | -1.31% | 0.15% | -78.07% | 649 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 94.44% | - | 0.00% | - | 0.00% | - | 5.56% | - | 54 |  |
| Paid | 2026-W20 | 100.00% | +5.88% | 11.69% | - | 0.00% | - | 0.00% | -100.00% | 77 | ⚠️ |
| Referral | 2026-W19 | 36.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 25 |  |
| Referral | 2026-W20 | 33.33% | -7.41% | 4.76% | - | 0.00% | - | 0.00% | - | 21 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.22% | - | 29.43% | - | 0.29% | - | 0.44% | - | 683 |  |
| Paid | 2026-W20 | 96.94% | -0.28% | 33.38% | +13.42% | 0.66% | +127.06% | 1.33% | +202.75% | 752 |  |
| Referral | 2026-W19 | 62.56% | - | 35.68% | - | 27.75% | - | 0.00% | - | 227 |  |
| Referral | 2026-W20 | 51.21% | -18.14% | 46.77% | +31.08% | 38.71% | +39.48% | 2.02% | - | 248 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: SE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.72% | - | 27.63% | - | 0.76% | - | 0.11% | - | 923 |  |
| Paid | 2026-W20 | 98.27% | +0.56% | 31.56% | +14.23% | 0.62% | -18.41% | 0.12% | +14.23% | 808 |  |
| Referral | 2026-W19 | 83.70% | - | 25.00% | - | 7.61% | - | 0.00% | - | 276 |  |
| Referral | 2026-W20 | 86.47% | +3.31% | 27.44% | +9.77% | 6.02% | -20.95% | 0.00% | - | 266 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| NZ | ↓ -3.35% | Referral ↓ -18.14% | ↑ +18.43% | ↑ +41.40% | ↑ +355.00% | [AI_SUMMARY_PLACEHOLDER] |
| AT | ↓ -3.16% | Referral ↓ -9.05% | ↑ +32.15% | ↑ +66.57% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |
| LU | ↑ +12.86% | Paid ↑ +5.88%, Referral ↓ -7.41% | → - | → - | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |
| CH | ↑ +3.46% | Referral ↑ +29.52% | ↑ +38.37% | ↓ -80.40% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-19*
