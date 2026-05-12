# Fraud Investigation: WL 2026-W19

**Metric:** Fraud Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 92.96% → 92.79% (-0.18%)  
**Volume:** 14,500 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined marginally from 92.96% to 92.79% (-0.18pp) in 2026-W19, a change deemed not statistically significant with volume at 14,500 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability check | -0.18pp (within normal range 91.72%-93.27%) | ✅ |
| L1: Country Scan | ±2.5% threshold | CG -3.40pp exceeds threshold | ⚠️ |
| L1: Channel Scan | ±2.5% threshold | Referral -3.22pp exceeds threshold | ⚠️ |
| L2: CG Deep-Dive | Channel breakdown | Referral FAR -10.94pp, Dup Block +144.77% | ⚠️ |
| L2: Cross-Country Referral | Pattern detection | CG, ER, GN, KN all show Referral declines | ⚠️ |

**Key Findings:**
- **Referral channel degradation across multiple countries:** CG Referral FAR dropped -10.94pp, KN Referral -12.33pp, ER Referral -7.07pp, and GN Referral -3.54pp, indicating a systemic issue rather than country-specific problem
- **Duplicate rates surging in Referral:** CG Referral duplicate rate increased +56.37% (16.36% → 25.59%), KN Referral +55.78% (17.27% → 26.90%), directly driving higher duplicate blocks
- **Duplicate Block rates spiking:** CG Referral Dup Block increased +74.71% (13.64% → 23.82%), CG Paid Dup Block +144.77% (1.18% → 2.88%), suggesting potential referral fraud ring activity or policy change impact
- **Paid channel remains stable:** Across all countries, Paid channel FAR changes are minimal (CG -1.79pp, ER -1.14pp), confirming the issue is isolated to Referral
- **CK shows positive counter-trend:** CK Referral FAR improved +5.26pp with Dup Block declining -10.97%, warranting investigation of differing market conditions

**Action:** **Investigate** – The consistent Referral channel degradation across CG, ER, GN, and KN driven by elevated duplicate rates and blocks suggests either (1) a coordinated referral abuse pattern or (2) a recent fraud policy tightening affecting referral traffic disproportionately. Recommend immediate review of referral duplicate detection rules and recent policy changes.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W19 | 92.79% | 15.96% | 5.35% | 1.13% | 14,500 | -0.18% ← REPORTED CHANGE |
| 2026-W18 | 92.96% | 14.81% | 4.55% | 1.07% | 13,785 | +1.36% |
| 2026-W17 | 91.72% | 17.67% | 5.63% | 1.10% | 13,950 | -1.20% |
| 2026-W16 | 92.84% | 16.69% | 4.80% | 0.93% | 13,989 | -0.47% |
| 2026-W15 | 93.27% | 15.55% | 4.80% | 0.67% | 15,129 | +0.45% |
| 2026-W14 | 92.85% | 15.16% | 4.76% | 0.81% | 13,275 | +0.24% |
| 2026-W13 | 92.63% | 15.40% | 4.96% | 0.79% | 14,386 | -0.42% |
| 2026-W12 | 93.02% | 15.85% | 4.77% | 0.42% | 15,068 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| CG | 2026-W18 | 93.29% | - | 13.13% | - | 2,117 |  |
| CG | 2026-W19 | 90.12% | -3.40% | 16.26% | +23.83% | 1,974 | ⚠️ |
| CK | 2026-W18 | 92.18% | - | 27.77% | - | 2,276 |  |
| CK | 2026-W19 | 94.30% | +2.30% | 27.82% | +0.19% | 2,437 |  |
| ER | 2026-W18 | 91.99% | - | 19.34% | - | 2,259 |  |
| ER | 2026-W19 | 89.86% | -2.32% | 23.66% | +22.29% | 2,139 |  |
| MR | 2026-W18 | 95.67% | - | 4.11% | - | 2,333 |  |
| MR | 2026-W19 | 97.00% | +1.39% | 4.14% | +0.53% | 3,070 |  |

**Countries exceeding ±2.5% threshold:** CG

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 95.51% | - | 13.51% | - | 11,680 |  |
| Paid | 2026-W19 | 95.55% | +0.05% | 14.41% | +6.69% | 12,418 |  |
| Referral | 2026-W18 | 78.86% | - | 22.00% | - | 2,105 |  |
| Referral | 2026-W19 | 76.32% | -3.22% | 25.17% | +14.43% | 2,082 | ⚠️ |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 94.91% | - | 12.53% | - | 1.18% | - | 3.02% | - | 1,787 |  |
| Paid | 2026-W19 | 93.21% | -1.79% | 14.32% | +14.25% | 2.88% | +144.77% | 3.18% | +5.31% | 1,634 |  |
| Referral | 2026-W18 | 84.55% | - | 16.36% | - | 13.64% | - | 0.30% | - | 330 |  |
| Referral | 2026-W19 | 75.29% | -10.94% | 25.59% | +56.37% | 23.82% | +74.71% | 0.59% | +94.12% | 340 | ⚠️ |

**Analysis:** While the overall WL FAR decline of -0.18pp is not statistically significant, the underlying data reveals a concerning systemic pattern: Referral channel performance is deteriorating across multiple countries (CG, ER, GN, KN) with duplicate rates and duplicate blocks sharply increasing. This pattern strongly suggests either emerging referral fraud abuse or unintended consequences from recent duplicate detection policy changes. The Paid channel remains healthy across all markets, confirming this is a Referral-specific issue requiring targeted investigation before it materially impacts overall approval rates.

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 98.09% | - | 27.31% | - | 0.45% | - | 0.00% | - | 1,776 |  |
| Paid | 2026-W19 | 99.03% | +0.96% | 27.73% | +1.55% | 0.36% | -20.63% | 0.00% | - | 1,958 |  |
| Referral | 2026-W18 | 71.20% | - | 29.40% | - | 27.20% | - | 0.00% | - | 500 |  |
| Referral | 2026-W19 | 74.95% | +5.26% | 28.18% | -4.14% | 24.22% | -10.97% | 0.00% | - | 479 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 94.75% | - | 18.75% | - | 1.45% | - | 1.71% | - | 1,867 |  |
| Paid | 2026-W19 | 93.67% | -1.14% | 22.77% | +21.47% | 2.70% | +86.89% | 2.47% | +44.27% | 1,739 |  |
| Referral | 2026-W18 | 78.83% | - | 22.19% | - | 19.64% | - | 0.77% | - | 392 |  |
| Referral | 2026-W19 | 73.25% | -7.07% | 27.50% | +23.91% | 25.50% | +29.82% | 0.25% | -67.33% | 400 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 99.30% | - | 15.01% | - | 0.40% | - | 0.00% | - | 1,006 |  |
| Paid | 2026-W19 | 98.89% | -0.42% | 15.17% | +1.10% | 0.34% | -14.24% | 0.00% | - | 1,173 |  |
| Referral | 2026-W18 | 82.32% | - | 20.26% | - | 17.68% | - | 0.00% | - | 311 |  |
| Referral | 2026-W19 | 79.40% | -3.54% | 22.59% | +11.52% | 20.27% | +14.59% | 0.00% | - | 301 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 91.93% | - | 6.52% | - | 5.84% | - | 0.24% | - | 2,516 |  |
| Paid | 2026-W19 | 91.23% | -0.77% | 8.38% | +28.60% | 7.68% | +31.40% | 0.20% | -17.87% | 2,553 |  |
| Referral | 2026-W18 | 84.17% | - | 17.27% | - | 14.39% | - | 0.00% | - | 139 |  |
| Referral | 2026-W19 | 73.79% | -12.33% | 26.90% | +55.78% | 23.45% | +62.97% | 0.69% | - | 145 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| CG | ↓ -3.40% | Referral ↓ -10.94% | ↑ +23.83% | ↑ +107.99% | ↑ +5.29% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-12*
