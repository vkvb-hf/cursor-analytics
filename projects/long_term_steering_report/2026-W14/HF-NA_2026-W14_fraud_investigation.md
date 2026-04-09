# Fraud Investigation: HF-NA 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.13% → 90.90% (+1.98%)  
**Volume:** 23,540 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved significantly from 89.13% to 90.90% (+1.98pp) in 2026-W14, representing a recovery toward the baseline levels observed in W07-W10.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within normal range | +1.98pp | ✅ |
| L0: PF Block Rate | Decreased from prior week | 3.33% → 1.48% (-1.85pp) | ✅ |
| L0: Dup Block Rate | Slight increase | 6.32% → 6.85% (+0.53pp) | ✅ |
| L1: Country - US | Exceeds ±2.5% threshold | +3.30pp | ⚠️ |
| L1: Country - CA | Within threshold | -1.20pp | ✅ |
| L1: Channel - Paid | Within threshold | +0.49pp | ✅ |
| L1: Channel - Referral | Exceeds threshold; Dup Rate spike | +6.81pp FAR; +17.19% Dup Rate | ⚠️ |

**Key Findings:**
- US drove the regional FAR improvement with a +3.30pp increase (88.61% → 91.54%), accounting for the majority of the +1.98pp regional change
- PF Block Rate dropped significantly from 3.33% to 1.48% (-1.85pp), contributing to higher approval rates
- Referral channel shows concerning signals: FAR increased +6.81pp but Dup Rate spiked +17.19% (29.78% → 34.90%), suggesting potential abuse pattern
- Overall volume declined by 1,050 customers (24,590 → 23,540), a -4.27% decrease week-over-week
- Canada showed slight FAR decline (-1.20pp) but remains within normal operating range

**Action:** Investigate — The Referral channel's simultaneous FAR increase and Dup Rate spike (+17.19%) warrants deeper analysis to rule out fraudulent referral abuse or policy exploitation.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 90.90% | 26.58% | 6.85% | 1.48% | 23,540 | +1.98% ← REPORTED CHANGE |
| 2026-W13 | 89.13% | 26.05% | 6.32% | 3.33% | 24,590 | -1.30% |
| 2026-W12 | 90.31% | 25.61% | 6.09% | 2.50% | 24,841 | +0.05% |
| 2026-W11 | 90.27% | 25.00% | 5.92% | 2.65% | 26,806 | -1.38% |
| 2026-W10 | 91.53% | 25.50% | 5.87% | 1.40% | 27,721 | -0.06% |
| 2026-W09 | 91.58% | 24.92% | 5.85% | 1.27% | 30,559 | +0.03% |
| 2026-W08 | 91.55% | 24.95% | 6.16% | 1.08% | 28,186 | -1.05% |
| 2026-W07 | 92.52% | 23.92% | 5.50% | 0.89% | 30,135 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W13 | 88.61% | - | 25.13% | - | 17,575 |  |
| US | 2026-W14 | 91.54% | +3.30% | 26.05% | +3.68% | 16,609 | ⚠️ |
| CA | 2026-W13 | 90.43% | - | 28.37% | - | 7,015 |  |
| CA | 2026-W14 | 89.35% | -1.20% | 27.85% | -1.84% | 6,931 |  |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W13 | 95.99% | - | 25.08% | - | 19,523 |  |
| Paid | 2026-W14 | 96.46% | +0.49% | 24.64% | -1.75% | 19,096 |  |
| Referral | 2026-W13 | 62.72% | - | 29.78% | - | 5,067 |  |
| Referral | 2026-W14 | 66.99% | +6.81% | 34.90% | +17.19% | 4,444 | ⚠️ |

---

*Report: 2026-04-09*
