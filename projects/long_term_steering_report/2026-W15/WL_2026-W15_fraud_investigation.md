# Fraud Investigation: WL 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 93.28% → 92.95% (-0.35%)  
**Volume:** 14,308 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 93.28% to 92.95% (-0.33 pp) in 2026-W15, a change that is not statistically significant and falls within normal weekly fluctuation range (8-week range: 92.70%-94.34%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Global FAR | -0.35% WoW | -0.33 pp | ✅ |
| L1: Country Threshold (±2.5%) | No countries exceeded | - | ✅ |
| L1: Channel Category | Paid +0.34%, Referral +1.44% | Both improved | ✅ |
| L2: Referral Channel (AO, CG, KN, MR) | Mixed signals flagged | ⚠️ 4 flags | ⚠️ |

**Key Findings:**
- Global FAR decline of 0.33 pp is within normal variance; 8-week trend shows FAR oscillating between 92.70% and 94.34%
- Duplicate Rate increased from 15.74% to 17.14% (+1.40 pp), with corresponding Duplicate Block Rate rising from 4.98% to 5.26%
- ER and CK showed elevated Duplicate Rates (22.17% and 27.56% respectively), contributing to slightly lower FAR in those markets
- Referral channel across multiple countries (AO, CG, KN, MR) shows FAR improvements ranging from +2.51% to +10.49%, with KN Referral improving +10.49 pp driven by a 32.12% reduction in Duplicate Rate
- MR Paid channel showed strong FAR improvement (+2.19 pp) with Duplicate Rate declining 26.78% and PF Block Rate dropping 52.07%

**Action:** Monitor - No escalation required. The FAR decline is not significant and within normal operating range. Continue standard monitoring with attention to Duplicate Rate trends in ER and CK.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 92.95% | 17.14% | 5.26% | 0.96% | 14,308 | -0.35% |
| 2026-W15 | 93.28% | 15.74% | 4.98% | 0.69% | 15,143 | +0.44% ← REPORTED CHANGE |
| 2026-W14 | 92.88% | 15.25% | 4.84% | 0.82% | 13,279 | +0.19% |
| 2026-W13 | 92.70% | 15.44% | 4.99% | 0.79% | 14,388 | -0.35% |
| 2026-W12 | 93.02% | 15.90% | 4.82% | 0.42% | 15,072 | -1.40% |
| 2026-W11 | 94.34% | 14.70% | 4.06% | 0.35% | 16,393 | +0.54% |
| 2026-W10 | 93.83% | 15.76% | 4.45% | 0.44% | 17,314 | +0.39% |
| 2026-W09 | 93.47% | 15.24% | 4.63% | 0.54% | 16,425 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| MR | 2026-W14 | 94.98% | - | 5.82% | - | 2,010 |  |
| MR | 2026-W15 | 96.87% | +2.00% | 4.59% | -21.23% | 2,748 |  |
| KN | 2026-W14 | 90.28% | - | 7.98% | - | 2,242 |  |
| KN | 2026-W15 | 91.43% | +1.28% | 7.35% | -7.92% | 2,707 |  |
| ER | 2026-W14 | 93.72% | - | 19.89% | - | 2,388 |  |
| ER | 2026-W15 | 92.83% | -0.95% | 22.17% | +11.48% | 2,539 |  |
| CK | 2026-W14 | 93.71% | - | 24.46% | - | 2,498 |  |
| CK | 2026-W15 | 92.98% | -0.79% | 27.56% | +12.66% | 2,591 |  |
| AO | 2026-W14 | 87.56% | - | 26.20% | - | 836 |  |
| AO | 2026-W15 | 88.91% | +1.55% | 26.56% | +1.38% | 866 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.01% | - | 13.48% | - | 11,221 |  |
| Paid | 2026-W15 | 96.33% | +0.34% | 14.11% | +4.68% | 12,767 |  |
| Referral | 2026-W14 | 75.80% | - | 24.88% | - | 2,058 |  |
| Referral | 2026-W15 | 76.89% | +1.44% | 24.45% | -1.71% | 2,376 |  |

---

## L2: AO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.55% | - | 21.54% | - | 0.18% | - | 0.00% | - | 571 |  |
| Paid | 2026-W15 | 98.56% | +1.04% | 23.70% | +10.01% | 0.00% | -100.00% | 0.00% | - | 557 |  |
| Referral | 2026-W14 | 66.04% | - | 36.23% | - | 33.58% | - | 0.00% | - | 265 |  |
| Referral | 2026-W15 | 71.52% | +8.30% | 31.72% | -12.45% | 28.16% | -16.17% | 0.00% | - | 309 | ⚠️ |

**Analysis:** The 0.33 pp decline in Fraud Approval Rate during 2026-W15 represents normal weekly fluctuation rather than a systemic issue, as evidenced by the non-significant classification and the metric remaining within the established 8-week variance band. The Referral channel showed positive momentum across multiple countries with notable FAR improvements, while the slight uptick in global Duplicate Rate warrants continued observation but does not require immediate intervention. Standard monitoring protocols should continue with no escalation needed at this time.

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 95.75% | - | 11.01% | - | 1.57% | - | 1.75% | - | 1,717 |  |
| Paid | 2026-W15 | 94.63% | -1.17% | 12.40% | +12.65% | 2.40% | +52.62% | 1.94% | +11.20% | 1,750 |  |
| Referral | 2026-W14 | 81.87% | - | 17.60% | - | 15.47% | - | 0.53% | - | 375 |  |
| Referral | 2026-W15 | 83.92% | +2.51% | 15.80% | -10.21% | 13.08% | -15.44% | 0.27% | -48.91% | 367 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 91.14% | - | 7.01% | - | 6.21% | - | 0.05% | - | 2,110 |  |
| Paid | 2026-W15 | 92.00% | +0.95% | 6.64% | -5.34% | 5.72% | -7.87% | 0.60% | +1166.00% | 2,500 |  |
| Referral | 2026-W14 | 76.52% | - | 23.48% | - | 21.97% | - | 0.00% | - | 132 |  |
| Referral | 2026-W15 | 84.54% | +10.49% | 15.94% | -32.12% | 15.46% | -29.64% | 0.00% | - | 207 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: MR Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 95.49% | - | 5.36% | - | 0.05% | - | 3.13% | - | 1,883 |  |
| Paid | 2026-W15 | 97.57% | +2.19% | 3.93% | -26.78% | 0.00% | -100.00% | 1.50% | -52.07% | 2,597 |  |
| Referral | 2026-W14 | 87.40% | - | 12.60% | - | 9.45% | - | 2.36% | - | 127 |  |
| Referral | 2026-W15 | 84.77% | -3.01% | 15.89% | +26.16% | 11.92% | +26.16% | 1.32% | -43.93% | 151 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-22*
