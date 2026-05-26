# Fraud Investigation: US-HF 2026-W21

**Metric:** Fraud Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.33% → 92.04% (-0.31%)  
**Volume:** 15,797 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 92.33% to 92.04% (-0.29 pp) in W21, representing a minor fluctuation that is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within historical range (89.25%-92.33%) | -0.29 pp | ✅ |
| L1: Country Scan | No countries exceeding ±2.5% threshold | -0.31% (US) | ✅ |
| L1: Channel Category | No categories exceeding threshold | Paid -0.56%, Referral +1.54% | ✅ |
| Duplicate Rate | Slight increase in duplicates | +0.72 pp (24.38%) | ⚠️ |
| Duplicate Block Rate | Increased blocking | +0.57 pp (5.94%) | ⚠️ |

**Key Findings:**
- FAR decline of -0.29 pp is well within normal weekly volatility observed over the 8-week period (range: 89.25% to 92.33%)
- Volume decreased by 8.4% (17,246 → 15,797 customers), which may contribute to rate fluctuation
- Duplicate Rate increased from 23.66% to 24.38% (+0.72 pp), with corresponding Duplicate Block Rate rising from 5.37% to 5.94% (+0.57 pp)
- Referral channel shows lower FAR (69.40%) compared to Paid channel (96.01%), but Referral improved +1.54% while Paid declined -0.56%
- PF Block Rate remained stable at 1.05% (+0.04 pp), indicating no policy filter anomalies

**Action:** Monitor — No investigation required. The decline is not statistically significant and no segments breach alerting thresholds.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W21 | 92.04% | 24.38% | 5.94% | 1.05% | 15,797 | -0.31% ← REPORTED CHANGE |
| 2026-W20 | 92.33% | 23.66% | 5.37% | 1.01% | 17,246 | +2.14% |
| 2026-W19 | 90.39% | 21.07% | 4.85% | 2.26% | 18,264 | -1.87% |
| 2026-W18 | 92.12% | 21.35% | 4.94% | 0.67% | 18,191 | +0.97% |
| 2026-W17 | 91.23% | 26.49% | 6.63% | 0.94% | 17,203 | +1.84% |
| 2026-W16 | 89.59% | 27.20% | 7.75% | 1.35% | 20,445 | +0.38% |
| 2026-W15 | 89.25% | 25.73% | 6.58% | 2.96% | 20,211 | -2.56% |
| 2026-W14 | 91.60% | 25.27% | 6.26% | 0.85% | 16,706 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W20 | 92.33% | - | 23.66% | - | 17,246 |  |
| US | 2026-W21 | 92.04% | -0.31% | 24.38% | +3.02% | 15,797 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W20 | 96.54% | - | 22.36% | - | 14,668 |  |
| Paid | 2026-W21 | 96.01% | -0.56% | 22.87% | +2.29% | 13,444 |  |
| Referral | 2026-W20 | 68.35% | - | 31.07% | - | 2,578 |  |
| Referral | 2026-W21 | 69.40% | +1.54% | 32.98% | +6.14% | 2,353 |  |

---



*Report: 2026-05-26*
