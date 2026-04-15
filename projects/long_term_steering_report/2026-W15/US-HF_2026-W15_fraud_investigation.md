# Fraud Investigation: US-HF 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.59% → 89.20% (-2.61%)  
**Volume:** 20,057 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate declined from 91.59% to 89.20% (-2.39pp) in 2026-W15, representing a significant decrease alongside a 19.9% increase in volume (16,726 → 20,057 customers).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR Trend | FAR dropped below 8-week baseline (~91%) | -2.39pp | ⚠️ |
| L0: Duplicate Rate | Increased from 25.49% to 26.41% | +0.92pp | ⚠️ |
| L0: Duplicate Block Rate | Increased from 6.49% to 7.03% | +0.54pp | ⚠️ |
| L0: PF Block Rate | Increased from 0.85% to 3.03% | +2.18pp | ⚠️ |
| L1: Country (US) | Only country, exceeds ±2.5% threshold | -2.61% | ⚠️ |
| L1: Channel (Paid) | Minor decline, stable performance | -0.98% | ✅ |
| L1: Channel (Referral) | Significant FAR decline | -12.15% | ⚠️ |

**Key Findings:**
- PF Block Rate spiked significantly from 0.85% to 3.03% (+2.18pp), the highest level in the 8-week trend and a primary driver of FAR decline
- Referral channel experienced severe FAR degradation of -12.15% (70.00% → 61.50%), far exceeding the overall decline
- Volume increased by 19.9% week-over-week while FAR decreased, suggesting potential quality issues with new traffic
- Duplicate Rate reached its highest point in 8 weeks at 26.41%, contributing to increased blocking
- Paid channel remains relatively stable at 95.34% FAR despite the overall decline, indicating issues are concentrated in Referral

**Action:** Investigate — Focus immediate analysis on the Referral channel's 12.15% FAR drop and the 2.18pp spike in PF Block Rate to identify root cause of increased rejections.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.20% | 26.41% | 7.03% | 3.03% | 20,057 | -2.61% ← REPORTED CHANGE |
| 2026-W14 | 91.59% | 25.49% | 6.49% | 0.85% | 16,726 | +3.41% |
| 2026-W13 | 88.57% | 25.07% | 6.68% | 3.59% | 17,570 | -1.45% |
| 2026-W12 | 89.87% | 24.65% | 6.31% | 2.72% | 17,514 | +0.13% |
| 2026-W11 | 89.75% | 23.87% | 6.18% | 2.92% | 19,067 | -2.02% |
| 2026-W10 | 91.60% | 24.70% | 5.94% | 1.22% | 20,601 | -0.08% |
| 2026-W09 | 91.68% | 24.02% | 5.90% | 1.16% | 23,224 | +0.30% |
| 2026-W08 | 91.41% | 23.86% | 6.49% | 0.90% | 21,168 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W14 | 91.59% | - | 25.49% | - | 16,726 |  |
| US | 2026-W15 | 89.20% | -2.61% | 26.41% | +3.60% | 20,057 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.28% | - | 24.13% | - | 13,739 |  |
| Paid | 2026-W15 | 95.34% | -0.98% | 25.68% | +6.43% | 16,421 |  |
| Referral | 2026-W14 | 70.00% | - | 31.77% | - | 2,987 |  |
| Referral | 2026-W15 | 61.50% | -12.15% | 29.70% | -6.51% | 3,636 | ⚠️ |

---

*Report: 2026-04-15*
