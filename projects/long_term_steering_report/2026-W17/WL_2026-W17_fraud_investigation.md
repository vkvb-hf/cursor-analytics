# Fraud Investigation: WL 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.89% → 91.88% (-1.08%)  
**Volume:** 14,244 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined from 92.89% to 91.88% (-1.01 pp) in 2026-W17, representing a statistically significant decrease affecting 14,244 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | FAR declining for 2 consecutive weeks | -1.08% | ⚠️ |
| L1: Country | No country exceeds ±2.5% threshold | ER -2.28%, CK -1.87% | ✅ |
| L1: Channel Category | Referral channel significant drop | -4.59% | ⚠️ |
| L2: CK Referral | Severe FAR decline + Dup Rate spike | FAR -11.79%, Dup +31.25% | ⚠️ |
| L2: ER Referral | Moderate FAR decline | FAR -2.80% | ⚠️ |
| L2: CG Referral | FAR decline with Dup Block increase | FAR -5.51%, Dup Block +11.51% | ⚠️ |

**Key Findings:**
- **Referral channel is the primary driver:** Referral FAR dropped from 76.11% to 72.61% (-4.59%), while Paid channel remained stable at 95.54% (-0.44%)
- **CK Referral shows critical deterioration:** FAR plummeted 11.79 pp (71.25% → 62.85%) with duplicate rate surging 31.25% (30.87% → 40.51%) and duplicate block rate increasing 34.28%
- **Duplicate rates rising across all flagged segments:** WL-level duplicate rate increased from 16.80% to 18.16% (+8.10%), with CK showing the most severe increase
- **PF Block rate showing unusual spikes:** ER Paid PF Block increased 254.25% (0.72% → 2.56%), suggesting potential new fraud pattern detection
- **Volume remained stable:** Total volume increased slightly from 13,995 to 14,244 (+1.78%), ruling out volume-driven anomalies

**Action:** **Investigate** — The concentrated impact on Referral channels across multiple countries (CK, ER, CG), combined with sharply rising duplicate rates and block rates, suggests potential coordinated abuse of the referral program requiring immediate review of referral fraud controls and duplicate detection thresholds.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 91.88% | 18.16% | 6.11% | 1.14% | 14,244 | -1.08% ← REPORTED CHANGE |
| 2026-W16 | 92.89% | 16.80% | 4.91% | 0.94% | 13,995 | -0.40% |
| 2026-W15 | 93.26% | 15.64% | 4.89% | 0.68% | 15,139 | +0.44% |
| 2026-W14 | 92.85% | 15.23% | 4.83% | 0.81% | 13,277 | +0.19% |
| 2026-W13 | 92.67% | 15.41% | 4.96% | 0.79% | 14,387 | -0.37% |
| 2026-W12 | 93.02% | 15.88% | 4.80% | 0.42% | 15,070 | -1.39% |
| 2026-W11 | 94.33% | 14.67% | 4.03% | 0.35% | 16,393 | +0.53% |
| 2026-W10 | 93.83% | 15.75% | 4.44% | 0.44% | 17,314 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| ER | 2026-W16 | 93.91% | - | 22.78% | - | 2,331 |  |
| ER | 2026-W17 | 91.77% | -2.28% | 23.12% | +1.49% | 2,418 |  |
| CK | 2026-W16 | 92.40% | - | 28.05% | - | 2,342 |  |
| CK | 2026-W17 | 90.67% | -1.87% | 32.49% | +15.80% | 2,241 |  |
| KN | 2026-W16 | 91.08% | - | 7.90% | - | 2,253 |  |
| KN | 2026-W17 | 90.18% | -0.99% | 9.35% | +18.33% | 2,749 |  |
| GN | 2026-W16 | 94.61% | - | 19.83% | - | 1,669 |  |
| GN | 2026-W17 | 94.13% | -0.51% | 19.48% | -1.76% | 1,550 |  |
| AO | 2026-W16 | 87.92% | - | 27.23% | - | 977 |  |
| AO | 2026-W17 | 87.45% | -0.53% | 30.15% | +10.74% | 1,068 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 95.97% | - | 15.16% | - | 11,827 |  |
| Paid | 2026-W17 | 95.54% | -0.44% | 16.23% | +7.04% | 11,973 |  |
| Referral | 2026-W16 | 76.11% | - | 25.74% | - | 2,168 |  |
| Referral | 2026-W17 | 72.61% | -4.59% | 28.36% | +10.18% | 2,271 | ⚠️ |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 93.78% | - | 11.06% | - | 1.49% | - | 3.03% | - | 1,880 |  |
| Paid | 2026-W17 | 94.90% | +1.20% | 12.72% | +15.01% | 1.63% | +9.14% | 2.69% | -11.26% | 1,784 |  |
| Referral | 2026-W16 | 80.57% | - | 18.79% | - | 17.83% | - | 0.00% | - | 314 |  |
| Referral | 2026-W17 | 76.14% | -5.51% | 20.45% | +8.86% | 19.89% | +11.51% | 1.70% | - | 352 | ⚠️ |

**Analysis:** The 1.01 pp decline in Fraud Approval Rate is primarily driven by deteriorating performance in the Referral channel, with CK Referral experiencing the most severe impact (FAR down 11.79 pp, duplicate rate up 31.25%). The correlation between rising duplicate rates and increasing duplicate block rates across CK, ER, and CG suggests the fraud systems are correctly identifying suspicious patterns, but the underlying referral abuse activity warrants investigation into the source of these duplicate applications and potential tightening of referral program controls.

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.75% | - | 27.34% | - | 0.43% | - | 0.05% | - | 1,869 |  |
| Paid | 2026-W17 | 98.79% | +1.06% | 30.14% | +10.25% | 0.40% | -5.74% | 0.00% | -100.00% | 1,735 |  |
| Referral | 2026-W16 | 71.25% | - | 30.87% | - | 26.64% | - | 0.00% | - | 473 |  |
| Referral | 2026-W17 | 62.85% | -11.79% | 40.51% | +31.25% | 35.77% | +34.28% | 0.20% | - | 506 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 96.86% | - | 22.51% | - | 1.65% | - | 0.72% | - | 1,941 |  |
| Paid | 2026-W17 | 94.89% | -2.03% | 22.95% | +1.92% | 1.85% | +12.44% | 2.56% | +254.25% | 1,996 |  |
| Referral | 2026-W16 | 79.23% | - | 24.10% | - | 20.51% | - | 0.00% | - | 390 |  |
| Referral | 2026-W17 | 77.01% | -2.80% | 23.93% | -0.70% | 21.33% | +3.97% | 1.42% | - | 422 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-28*
