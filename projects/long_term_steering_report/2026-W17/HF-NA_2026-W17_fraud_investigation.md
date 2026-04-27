# Fraud Investigation: HF-NA 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.71% → 90.84% (+1.25%)  
**Volume:** 23,950 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) improved from 89.71% to 90.84% (+1.13 pp) in 2026-W17, representing a significant positive shift on reduced volume (23,950 customers, down from 27,288).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Trend | FAR within 8-week range (89.10%-91.53%) | +1.13 pp | ✅ |
| L1: Country Scan | No country exceeds ±2.5% threshold | US +2.06 pp, CA -0.86 pp | ✅ |
| L1: Channel Scan | Referral Dup Rate spike +12.94% | Paid +2.17 pp, Referral -2.24 pp | ⚠️ |
| L2: CA Referral | FAR declined -7.88%, Dup Block +19.42% | Significant degradation | ⚠️ |

**Key Findings:**
- US drove the overall FAR improvement with a +2.06 pp increase (89.60% → 91.44%), while volume decreased by 15% (20,427 → 17,298)
- CA Referral channel shows significant degradation: FAR dropped -7.88 pp (65.06% → 59.93%) with Dup Rate surging +11.29% and Dup Block rising +19.42 pp to 34.18%
- Paid channel performing strongly across both countries with FAR at 96.23% (NA) and 97.16% (CA), both showing improvement
- Overall Dup Rate increased slightly to 27.96% (+0.08 pp) while PF Block decreased to 1.27% (-0.29 pp), contributing to FAR improvement
- Volume declined 12% week-over-week (27,288 → 23,950), which may partially explain rate improvements

**Action:** Investigate — The CA Referral channel requires immediate attention due to the -7.88 pp FAR decline and 34.18% Dup Block rate, suggesting potential fraud pattern or policy issue specific to this segment.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 90.84% | 27.96% | 7.11% | 1.27% | 23,950 | +1.25% ← REPORTED CHANGE |
| 2026-W16 | 89.71% | 27.88% | 7.50% | 1.56% | 27,288 | +0.03% |
| 2026-W15 | 89.69% | 26.42% | 6.37% | 2.73% | 27,679 | -1.43% |
| 2026-W14 | 90.99% | 25.96% | 6.38% | 1.35% | 23,590 | +2.12% |
| 2026-W13 | 89.10% | 25.91% | 6.19% | 3.31% | 24,575 | -1.35% |
| 2026-W12 | 90.32% | 25.53% | 6.01% | 2.48% | 24,830 | +0.08% |
| 2026-W11 | 90.25% | 24.94% | 5.87% | 2.64% | 26,801 | -1.39% |
| 2026-W10 | 91.53% | 25.44% | 5.81% | 1.39% | 27,707 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W16 | 89.60% | - | 27.42% | - | 20,427 |  |
| US | 2026-W17 | 91.44% | +2.06% | 26.84% | -2.11% | 17,298 |  |
| CA | 2026-W16 | 90.05% | - | 29.25% | - | 6,861 |  |
| CA | 2026-W17 | 89.27% | -0.86% | 30.86% | +5.51% | 6,652 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 94.19% | - | 26.89% | - | 22,708 |  |
| Paid | 2026-W17 | 96.23% | +2.17% | 25.99% | -3.36% | 19,676 |  |
| Referral | 2026-W16 | 67.49% | - | 32.77% | - | 4,580 |  |
| Referral | 2026-W17 | 65.98% | -2.24% | 37.01% | +12.94% | 4,274 |  |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 96.14% | - | 27.36% | - | 0.69% | - | 1.76% | - | 5,516 |  |
| Paid | 2026-W17 | 97.16% | +1.06% | 28.08% | +2.65% | 0.36% | -47.39% | 1.51% | -14.30% | 5,242 |  |
| Referral | 2026-W16 | 65.06% | - | 37.03% | - | 28.62% | - | 3.94% | - | 1,345 |  |
| Referral | 2026-W17 | 59.93% | -7.88% | 41.21% | +11.29% | 34.18% | +19.42% | 4.18% | +6.19% | 1,410 | ⚠️ |

**Analysis:** The +1.13 pp FAR improvement in 2026-W17 is primarily driven by strong US Paid channel performance and reduced PF Block rates, keeping the metric within normal 8-week variance. However, the CA Referral channel exhibits concerning degradation with a -7.88 pp FAR drop and elevated duplicate blocking (34.18%), warranting focused investigation into potential fraud patterns or duplicate detection rule changes affecting this specific segment.

---



*Report: 2026-04-27*
