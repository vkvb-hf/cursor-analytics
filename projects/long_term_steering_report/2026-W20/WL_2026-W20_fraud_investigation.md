# Fraud Investigation: WL 2026-W20

**Metric:** Fraud Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 93.08% → 92.86% (-0.24%)  
**Volume:** 13,761 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) declined slightly from 93.08% to 92.86% (-0.22pp) in 2026-W20, a change deemed not statistically significant with stable volume of 13,761 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability | -0.24% (within normal range 91.73%-93.26%) | ✅ |
| L1: Country | Any country ±2.5% | No countries exceeded threshold | ✅ |
| L1: Channel Category | Any category ±2.5% | Referral -4.06% (75.49% from 78.69%) | ⚠️ |
| L2: AO Referral | Deep-dive | FAR -14.14%, Dup Rate +70.67% | ⚠️ |
| L2: GN Referral | Deep-dive | FAR -9.68%, Dup Rate +47.20% | ⚠️ |
| L2: ER Referral | Deep-dive | FAR -3.24%, Dup Rate +17.35% | ⚠️ |
| L2: CG Paid | Deep-dive | FAR +3.02% (improvement) | ✅ |

**Key Findings:**
- **Referral channel is the primary driver of FAR decline:** Global Referral FAR dropped -4.06pp (78.69% → 75.49%) while Paid improved +0.56pp (95.44% → 95.97%)
- **AO Referral shows severe degradation:** FAR plummeted -14.14pp (79.45% → 68.21%) with duplicate rate surging +70.67% and duplicate blocks increasing +55.91%
- **GN Referral also significantly impacted:** FAR declined -9.68pp (82.64% → 74.64%) with duplicate rate up +47.20% and duplicate blocks up +43.04%
- **Duplicate rates increased across multiple markets:** WL-level duplicate rate rose from 13.98% to 17.62% (+26.04%), with Referral channels disproportionately affected
- **CG showed positive movement:** Paid channel FAR improved +3.02pp with reduced blocking rates, partially offsetting declines elsewhere

**Action:** **Investigate** — The concentrated Referral channel degradation across AO, GN, and ER markets, driven by significant duplicate rate increases, warrants immediate investigation into potential coordinated fraudulent activity or referral program abuse.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W20 | 92.86% | 17.62% | 5.37% | 0.87% | 13,761 | -0.24% ← REPORTED CHANGE |
| 2026-W19 | 93.08% | 13.98% | 4.54% | 1.02% | 14,285 | +0.13% |
| 2026-W18 | 92.96% | 14.70% | 4.44% | 1.05% | 13,780 | +1.34% |
| 2026-W17 | 91.73% | 17.62% | 5.57% | 1.10% | 13,946 | -1.18% |
| 2026-W16 | 92.83% | 16.64% | 4.75% | 0.93% | 13,988 | -0.47% |
| 2026-W15 | 93.26% | 15.52% | 4.77% | 0.66% | 15,128 | +0.44% |
| 2026-W14 | 92.85% | 15.14% | 4.74% | 0.81% | 13,275 | +0.21% |
| 2026-W13 | 92.66% | 15.37% | 4.92% | 0.79% | 14,382 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| CG | 2026-W19 | 90.73% | - | 14.70% | - | 1,952 |  |
| CG | 2026-W20 | 92.81% | +2.29% | 14.91% | +1.39% | 1,932 |  |
| GN | 2026-W19 | 95.27% | - | 13.91% | - | 1,459 |  |
| GN | 2026-W20 | 93.70% | -1.65% | 19.16% | +37.74% | 1,508 |  |
| AO | 2026-W19 | 90.84% | - | 23.46% | - | 699 |  |
| AO | 2026-W20 | 89.29% | -1.71% | 28.82% | +22.82% | 878 |  |
| KN | 2026-W19 | 91.07% | - | 7.70% | - | 2,598 |  |
| KN | 2026-W20 | 90.64% | -0.47% | 9.36% | +21.57% | 2,853 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 95.44% | - | 12.64% | - | 12,277 |  |
| Paid | 2026-W20 | 95.97% | +0.56% | 16.13% | +27.62% | 11,672 |  |
| Referral | 2026-W19 | 78.69% | - | 22.16% | - | 2,008 |  |
| Referral | 2026-W20 | 75.49% | -4.06% | 25.95% | +17.08% | 2,089 | ⚠️ |

---

## L2: AO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 97.31% | - | 24.66% | - | 0.22% | - | 0.00% | - | 446 |  |
| Paid | 2026-W20 | 99.16% | +1.91% | 25.25% | +2.38% | 0.00% | -100.00% | 0.17% | - | 598 |  |
| Referral | 2026-W19 | 79.45% | - | 21.34% | - | 20.16% | - | 0.00% | - | 253 |  |
| Referral | 2026-W20 | 68.21% | -14.14% | 36.43% | +70.67% | 31.43% | +55.91% | 0.36% | - | 280 | ⚠️ |

**Analysis:** While the overall WL FAR decline of -0.22pp is not statistically significant, the investigation reveals a concerning pattern in the Referral channel across multiple markets. AO and GN Referral segments show severe FAR drops (-14.14pp and -9.68pp respectively) coupled with substantial duplicate rate increases, suggesting potential referral fraud or abuse that is being appropriately caught by duplicate blocking mechanisms. The Fraud team should investigate the source of increased duplicate submissions in Referral channels, particularly in AO and GN, to determine if policy adjustments or enhanced monitoring are needed.

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 93.29% | - | 13.12% | - | 2.71% | - | 3.02% | - | 1,624 |  |
| Paid | 2026-W20 | 96.10% | +3.02% | 13.45% | +2.55% | 1.51% | -44.32% | 2.01% | -33.34% | 1,591 | ⚠️ |
| Referral | 2026-W19 | 78.05% | - | 22.56% | - | 20.73% | - | 0.61% | - | 328 |  |
| Referral | 2026-W20 | 77.42% | -0.81% | 21.70% | -3.81% | 19.94% | -3.81% | 1.47% | +140.47% | 341 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 92.99% | - | 20.05% | - | 2.43% | - | 2.32% | - | 1,726 |  |
| Paid | 2026-W20 | 94.24% | +1.35% | 23.36% | +16.55% | 2.23% | -8.56% | 1.96% | -15.28% | 1,528 |  |
| Referral | 2026-W19 | 76.32% | - | 23.68% | - | 21.58% | - | 0.26% | - | 380 |  |
| Referral | 2026-W20 | 73.84% | -3.24% | 27.79% | +17.35% | 24.52% | +13.64% | 0.82% | +210.63% | 367 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W19 | 98.38% | - | 12.81% | - | 0.17% | - | 0.00% | - | 1,171 |  |
| Paid | 2026-W20 | 99.40% | +1.04% | 16.80% | +31.12% | 0.26% | +51.29% | 0.00% | - | 1,161 |  |
| Referral | 2026-W19 | 82.64% | - | 18.40% | - | 16.32% | - | 0.00% | - | 288 |  |
| Referral | 2026-W20 | 74.64% | -9.68% | 27.09% | +47.20% | 23.34% | +43.04% | 0.29% | - | 347 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-05-19*
