# Fraud Investigation: HF-NA 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 89.70% → 89.82% (+0.14%)  
**Volume:** 27,399 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-NA showed a minor improvement of +0.14% (from 89.70% to 89.82%) in 2026-W15, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within normal range | +0.14% | ✅ |
| L1: Country Scan | US exceeds ±2.5% threshold | -2.53% (US) | ⚠️ |
| L1: Channel Scan | Referral exceeds threshold | -6.74% | ⚠️ |
| L2: US Deep-Dive | Referral channel driving decline | -11.91% | ⚠️ |
| L2: CA Deep-Dive | Referral improving | +6.78% | ✅ |

**Key Findings:**
- US FAR declined -2.53% (91.59% → 89.28%), driven primarily by the Referral channel which dropped -11.91% (70.11% → 61.76%)
- US Referral PF Block % increased dramatically by +411.63% (2.48% → 12.70%), indicating heightened fraud prevention activity
- Regional Duplicate Rate increased to 28.10% (+1.62pp), with Dup Block % rising to 7.72% (+1.30pp)
- CA showed positive movement with FAR improving +1.53% and Referral channel up +6.78%
- Paid channels remain stable across both US (-1.03%) and CA (+0.07%)

**Action:** Investigate - The significant spike in US Referral PF Block % (+411.63%) requires immediate review to determine if this reflects a legitimate fraud attack or potential rule misconfiguration.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.82% | 28.10% | 7.72% | 1.60% | 27,399 | +0.14% |
| 2026-W15 | 89.70% | 26.48% | 6.42% | 2.73% | 27,685 | -1.40% ← REPORTED CHANGE |
| 2026-W14 | 90.97% | 25.99% | 6.42% | 1.36% | 23,597 | +2.09% |
| 2026-W13 | 89.11% | 25.96% | 6.23% | 3.32% | 24,577 | -1.35% |
| 2026-W12 | 90.33% | 25.53% | 6.01% | 2.49% | 24,830 | +0.07% |
| 2026-W11 | 90.26% | 24.95% | 5.88% | 2.65% | 26,801 | -1.38% |
| 2026-W10 | 91.52% | 25.46% | 5.83% | 1.39% | 27,713 | -0.06% |
| 2026-W09 | 91.58% | 24.86% | 5.80% | 1.26% | 30,553 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W14 | 91.59% | - | 25.42% | - | 16,719 |  |
| US | 2026-W15 | 89.28% | -2.53% | 25.91% | +1.93% | 20,224 | ⚠️ |
| CA | 2026-W14 | 89.47% | - | 27.38% | - | 6,878 |  |
| CA | 2026-W15 | 90.85% | +1.53% | 28.03% | +2.37% | 7,461 |  |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.20% | - | 24.25% | - | 19,232 |  |
| Paid | 2026-W15 | 95.50% | -0.73% | 25.45% | +4.95% | 22,689 |  |
| Referral | 2026-W14 | 67.95% | - | 33.65% | - | 4,365 |  |
| Referral | 2026-W15 | 63.37% | -6.74% | 31.14% | -7.46% | 4,996 | ⚠️ |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.07% | - | 24.63% | - | 0.53% | - | 2.02% | - | 5,494 |  |
| Paid | 2026-W15 | 96.13% | +0.07% | 25.97% | +5.47% | 0.61% | +15.31% | 1.89% | -6.37% | 6,079 |  |
| Referral | 2026-W14 | 63.29% | - | 38.29% | - | 29.84% | - | 4.84% | - | 1,384 |  |
| Referral | 2026-W15 | 67.58% | +6.78% | 37.05% | -3.26% | 27.42% | -8.10% | 2.97% | -38.72% | 1,382 | ⚠️ |

**Analysis:** While the overall HF-NA FAR shows marginal improvement (+0.14%), the US market experienced notable degradation driven by the Referral channel, where PF Block rates surged over 400%. This pattern suggests either an emerging fraud vector targeting US Referral traffic or an overly aggressive fraud prevention rule deployment. Recommend prioritizing investigation of US Referral PF blocking logic and validating whether blocked transactions represent true fraud or false positives.

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.25% | - | 24.10% | - | 2.18% | - | 0.50% | - | 13,738 |  |
| Paid | 2026-W15 | 95.26% | -1.03% | 25.26% | +4.82% | 2.90% | +33.05% | 0.85% | +70.21% | 16,610 |  |
| Referral | 2026-W14 | 70.11% | - | 31.50% | - | 25.93% | - | 2.48% | - | 2,981 |  |
| Referral | 2026-W15 | 61.76% | -11.91% | 28.89% | -8.29% | 24.35% | -6.10% | 12.70% | +411.63% | 3,614 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↓ -2.53% | Referral ↓ -11.91% | → +1.93% | ↑ +4.96% | ↑ +247.44% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-22*
