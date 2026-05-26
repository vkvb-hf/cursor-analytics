# Fraud Investigation: HF-NA 2026-W21

**Metric:** Fraud Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.06% → 91.99% (-0.07%)  
**Volume:** 21,730 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** Fraud Approval Rate declined marginally from 92.06% to 91.99% (-0.07pp) in W21, a statistically insignificant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Trend | 8-week stability check | -0.07pp | ✅ |
| L1: Country Scan | US, CA threshold ±2.5% | US -0.31pp, CA +0.69pp | ✅ |
| L1: Channel Scan | Paid, Referral threshold | Paid -0.39pp, Referral +2.06pp | ✅ |
| L2: CA Deep-Dive | Channel breakdown | Referral +3.41pp | ⚠️ |

**Key Findings:**
- HF-NA FAR remains stable at ~92%, with W21 showing the smallest week-over-week change (-0.07pp) in the 8-week window
- Duplicate Rate increased across both countries (US +3.02%, CA +3.26%) but did not materially impact FAR
- CA Referral channel showed notable FAR improvement (+3.41pp) driven by decreased Duplicate Rate (-10.01%) and reduced Duplicate Block Rate (-8.61pp)
- Volume declined 5.3% WoW (22,937 → 21,730), primarily from US (-8.4% volume drop)
- PF Block Rate in CA Paid increased +21.75% but from a small base (1.46% → 1.78%), minimal impact on overall FAR

**Action:** Monitor — No significant degradation detected. Continue standard weekly monitoring; track CA Referral improvement trend and elevated Duplicate Rates across channels.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W21 | 91.99% | 25.75% | 5.58% | 1.37% | 21,730 | -0.07% ← REPORTED CHANGE |
| 2026-W20 | 92.06% | 24.86% | 5.32% | 1.28% | 22,937 | +1.64% |
| 2026-W19 | 90.57% | 22.31% | 5.04% | 2.02% | 24,209 | -1.29% |
| 2026-W18 | 91.76% | 23.07% | 5.16% | 0.93% | 24,395 | +1.20% |
| 2026-W17 | 90.67% | 27.56% | 6.71% | 1.18% | 23,794 | +1.04% |
| 2026-W16 | 89.74% | 27.65% | 7.31% | 1.54% | 27,326 | +0.09% |
| 2026-W15 | 89.66% | 26.29% | 6.25% | 2.72% | 27,665 | -1.47% |
| 2026-W14 | 91.00% | 25.83% | 6.26% | 1.34% | 23,577 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W20 | 92.33% | - | 23.66% | - | 17,246 |  |
| US | 2026-W21 | 92.04% | -0.31% | 24.38% | +3.02% | 15,797 |  |
| CA | 2026-W20 | 91.23% | - | 28.48% | - | 5,691 |  |
| CA | 2026-W21 | 91.86% | +0.69% | 29.41% | +3.26% | 5,933 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 96.59% | - | 23.42% | - | 19,311 |  |
| Paid | 2026-W21 | 96.21% | -0.39% | 24.43% | +4.34% | 18,323 |  |
| Referral | 2026-W20 | 67.90% | - | 32.54% | - | 3,626 |  |
| Referral | 2026-W21 | 69.30% | +2.06% | 32.84% | +0.93% | 3,407 |  |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 96.75% | - | 26.75% | - | 0.47% | - | 1.46% | - | 4,643 |  |
| Paid | 2026-W21 | 96.78% | +0.04% | 28.74% | +7.42% | 0.51% | +8.14% | 1.78% | +21.75% | 4,879 |  |
| Referral | 2026-W20 | 66.79% | - | 36.16% | - | 25.95% | - | 4.87% | - | 1,048 |  |
| Referral | 2026-W21 | 69.07% | +3.41% | 32.54% | -10.01% | 23.72% | -8.61% | 4.27% | -12.27% | 1,054 | ⚠️ |

**Analysis:** The W21 Fraud Approval Rate change of -0.07pp is not statistically significant and falls well within normal operating variance. The 8-week trend shows FAR oscillating between 89.66% and 92.06%, with current performance at the higher end of this range. No country or channel exceeded investigation thresholds, and the flagged CA Referral improvement (+3.41pp) represents a positive trend requiring no immediate action.

---



*Report: 2026-05-26*
