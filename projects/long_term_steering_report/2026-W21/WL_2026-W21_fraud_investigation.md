# Fraud Investigation: WL 2026-W21

**Metric:** Fraud Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.83% → 93.13% (+0.33%)  
**Volume:** 13,327 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate increased slightly from 92.83% to 93.13% (+0.30 pp) in 2026-W21, a non-significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | FAR within 8-week range (91.71%-93.26%) | +0.30 pp | ✅ |
| L1: Country Scan | No country exceeds ±2.5% threshold | Max: GN +0.97 pp | ✅ |
| L1: Channel Scan | Paid/Referral stable | Paid +0.09 pp, Referral +0.62 pp | ✅ |
| L2: CG Deep-Dive | Referral FAR +6.06 pp (low volume: 340) | Flagged ⚠️ | ⚠️ |
| L2: KN Deep-Dive | Referral FAR -20.32 pp (low volume: 111) | Flagged ⚠️ | ⚠️ |
| L2: MR Deep-Dive | Referral FAR +10.58 pp (low volume: 188) | Flagged ⚠️ | ⚠️ |

**Key Findings:**
- KN Referral channel shows significant FAR decline of -20.32 pp (81.41% → 64.86%) with duplicate rate surging +70.74% and duplicate block rate doubling (+100.37%), though volume is small (111 customers)
- MR Referral channel improved substantially with FAR +10.58 pp (83.22% → 92.02%) driven by duplicate rate dropping -39.78% and duplicate block rate falling -58.16%
- CG Referral shows moderate improvement (+6.06 pp FAR) with reduced duplicate activity (-12.24% dup rate, -11.86% dup block rate)
- Overall Paid channel remains stable at ~96% FAR across all markets, representing 86% of total volume
- Total volume decreased slightly by 2.8% (13,706 → 13,327 customers)

**Action:** Monitor — The +0.30 pp change is not statistically significant. KN Referral degradation warrants watching due to the sharp duplicate increase, but low volume (111 customers, <1% of total) limits overall impact. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W21 | 93.13% | 16.86% | 5.17% | 1.00% | 13,327 | +0.33% ← REPORTED CHANGE |
| 2026-W20 | 92.83% | 17.40% | 5.11% | 0.83% | 13,706 | -0.25% |
| 2026-W19 | 93.06% | 13.91% | 4.48% | 1.01% | 14,279 | +0.13% |
| 2026-W18 | 92.94% | 14.66% | 4.41% | 1.05% | 13,777 | +1.34% |
| 2026-W17 | 91.71% | 17.56% | 5.53% | 1.10% | 13,944 | -1.20% |
| 2026-W16 | 92.82% | 16.62% | 4.73% | 0.92% | 13,988 | -0.47% |
| 2026-W15 | 93.26% | 15.51% | 4.75% | 0.66% | 15,128 | +0.44% |
| 2026-W14 | 92.85% | 15.13% | 4.72% | 0.81% | 13,275 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| KN | 2026-W20 | 90.85% | - | 8.86% | - | 2,798 |  |
| KN | 2026-W21 | 90.07% | -0.86% | 10.01% | +12.92% | 2,438 |  |
| ER | 2026-W20 | 90.21% | - | 23.81% | - | 1,890 |  |
| ER | 2026-W21 | 91.07% | +0.96% | 22.60% | -5.08% | 1,770 |  |
| CK | 2026-W20 | 94.21% | - | 32.27% | - | 2,281 |  |
| CK | 2026-W21 | 94.77% | +0.59% | 35.66% | +10.53% | 2,103 |  |
| GN | 2026-W20 | 93.70% | - | 19.10% | - | 1,508 |  |
| GN | 2026-W21 | 94.61% | +0.97% | 17.15% | -10.20% | 1,242 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 95.87% | - | 16.04% | - | 11,628 |  |
| Paid | 2026-W21 | 95.96% | +0.09% | 15.34% | -4.35% | 11,414 |  |
| Referral | 2026-W20 | 75.79% | - | 25.02% | - | 2,078 |  |
| Referral | 2026-W21 | 76.27% | +0.62% | 25.93% | +3.61% | 1,913 |  |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 96.04% | - | 13.39% | - | 1.45% | - | 1.95% | - | 1,591 |  |
| Paid | 2026-W21 | 94.87% | -1.22% | 12.96% | -3.19% | 1.58% | +9.22% | 2.89% | +48.57% | 1,520 |  |
| Referral | 2026-W20 | 76.54% | - | 21.11% | - | 19.35% | - | 1.47% | - | 341 |  |
| Referral | 2026-W21 | 81.18% | +6.06% | 18.53% | -12.24% | 17.06% | -11.86% | 0.88% | -39.82% | 340 | ⚠️ |

**Analysis:** The WL Fraud Approval Rate change of +0.30 pp in 2026-W21 falls within normal operating variance and requires no immediate action. While L2 deep-dives revealed notable Referral channel volatility in KN (declining) and MR (improving), these segments represent minimal volume (<3% combined) and do not materially impact the overall metric. Standard monitoring should continue with attention to KN Referral duplicate patterns if the trend persists.

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 91.57% | - | 7.93% | - | 6.69% | - | 0.19% | - | 2,599 |  |
| Paid | 2026-W21 | 91.28% | -0.32% | 8.77% | +10.60% | 7.61% | +13.61% | 0.09% | -55.32% | 2,327 |  |
| Referral | 2026-W20 | 81.41% | - | 21.11% | - | 17.09% | - | 1.01% | - | 199 |  |
| Referral | 2026-W21 | 64.86% | -20.32% | 36.04% | +70.74% | 34.23% | +100.37% | 0.00% | -100.00% | 111 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: MR Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 97.67% | - | 4.52% | - | 0.09% | - | 1.62% | - | 2,277 |  |
| Paid | 2026-W21 | 97.15% | -0.53% | 4.20% | -7.07% | 0.32% | +265.03% | 1.96% | +20.58% | 2,807 |  |
| Referral | 2026-W20 | 83.22% | - | 16.78% | - | 13.99% | - | 0.70% | - | 143 |  |
| Referral | 2026-W21 | 92.02% | +10.58% | 10.11% | -39.78% | 5.85% | -58.16% | 1.60% | +128.19% | 188 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-05-26*
