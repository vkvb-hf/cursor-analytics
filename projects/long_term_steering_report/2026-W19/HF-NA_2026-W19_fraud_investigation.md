# Fraud Investigation: HF-NA 2026-W19

**Metric:** Fraud Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.81% → 91.22% (-0.64%)  
**Volume:** 24,576 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by -0.64% (from 91.81% to 91.22%) in 2026-W19, a change that is not statistically significant and remains within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Overall | FAR 91.81% → 91.22% | -0.59pp | ✅ |
| L1: Country - US | FAR 92.19% → 91.34% | -0.85pp | ✅ |
| L1: Country - CA | FAR 90.69% → 90.85% | +0.16pp | ✅ |
| L1: Channel - Paid | FAR 95.96% → 96.66% | +0.70pp | ✅ |
| L1: Channel - Referral | FAR 70.39% → 65.18% | -5.21pp | ⚠️ |
| L2: US Paid | FAR 95.66% → 96.39% | +0.73pp | ✅ |
| L2: US Referral | FAR 72.90% → 65.68% | -7.22pp | ⚠️ |

**Key Findings:**
- US Referral channel experienced a significant FAR decline of -9.90% (72.90% → 65.68%) with PF Block % increasing by +835.02% (1.12% → 10.45%), indicating a major shift in fraud prevention blocking
- Duplicate Rate increased across HF-NA overall (+2.12pp) and notably in US Paid channel (+15.37%), though this did not negatively impact Paid channel FAR
- Referral channel overall dropped -7.40% in FAR (70.39% → 65.18%) while volume increased by 7.1% (3,962 → 4,242 customers)
- Paid channel performance improved slightly (+0.73%) and continues to drive strong approval rates at 96.66%
- The overall FAR decline is primarily attributable to the Referral channel deterioration, not systemic issues

**Action:** Investigate – The sharp increase in PF Block % (+835.02%) within US Referral channel requires immediate review of fraud prevention rule changes or model updates deployed between W18 and W19.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W19 | 91.22% | 25.28% | 5.70% | 2.24% | 24,576 | -0.64% ← REPORTED CHANGE |
| 2026-W18 | 91.81% | 23.16% | 5.23% | 0.95% | 24,408 | +1.24% |
| 2026-W17 | 90.69% | 27.65% | 6.81% | 1.19% | 23,805 | +1.05% |
| 2026-W16 | 89.75% | 27.68% | 7.35% | 1.54% | 27,334 | +0.09% |
| 2026-W15 | 89.66% | 26.36% | 6.31% | 2.73% | 27,669 | -1.46% |
| 2026-W14 | 90.99% | 25.88% | 6.30% | 1.34% | 23,581 | +2.12% |
| 2026-W13 | 89.10% | 25.90% | 6.17% | 3.30% | 24,569 | -1.37% |
| 2026-W12 | 90.33% | 25.50% | 5.98% | 2.49% | 24,820 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W18 | 92.19% | - | 21.41% | - | 18,198 |  |
| US | 2026-W19 | 91.34% | -0.92% | 24.02% | +12.19% | 18,589 |  |
| CA | 2026-W18 | 90.69% | - | 28.26% | - | 6,210 |  |
| CA | 2026-W19 | 90.85% | +0.17% | 29.16% | +3.19% | 5,987 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 95.96% | - | 21.57% | - | 20,446 |  |
| Paid | 2026-W19 | 96.66% | +0.73% | 24.04% | +11.47% | 20,334 |  |
| Referral | 2026-W18 | 70.39% | - | 31.35% | - | 3,962 |  |
| Referral | 2026-W19 | 65.18% | -7.40% | 31.19% | -0.51% | 4,242 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 95.66% | - | 20.05% | - | 1.55% | - | 0.60% | - | 15,423 |  |
| Paid | 2026-W19 | 96.39% | +0.76% | 23.13% | +15.37% | 2.10% | +35.42% | 0.81% | +34.51% | 15,535 |  |
| Referral | 2026-W18 | 72.90% | - | 29.01% | - | 24.07% | - | 1.12% | - | 2,775 |  |
| Referral | 2026-W19 | 65.68% | -9.90% | 28.59% | -1.46% | 22.92% | -4.78% | 10.45% | +835.02% | 3,054 | ⚠️ |

**Analysis:** The W19 FAR decline of -0.64% is not statistically significant at the aggregate level; however, the Referral channel—particularly US Referral—shows a material deterioration driven by a dramatic spike in PF Block rate (1.12% → 10.45%). This isolated pattern suggests a recent fraud prevention policy or model change disproportionately impacting Referral traffic. Recommend reviewing any rule deployments affecting Referral customers and assessing whether the increased blocking is intentional risk mitigation or an unintended consequence requiring calibration.

---



*Report: 2026-05-12*
