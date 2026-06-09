# Fraud Investigation: WL 2026-W23

**Metric:** Fraud Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 93.97% → 94.60% (+0.67%)  
**Volume:** 16,174 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) improved by +0.67pp from 93.97% to 94.60% week-over-week, with volume increasing 10.3% (14,659 → 16,174 customers). The change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week trend shows steady improvement from 91.70% to 94.60% | +0.67pp | ✅ |
| L1: Country Scan | No country exceeded ±2.5% threshold | Max: MR +0.79pp | ✅ |
| L1: Channel Category | Paid +0.43pp, Referral +1.50pp | Both positive | ✅ |
| L2: Referral Channel | 7 countries flagged with Dup Block increases | CG -8.37pp, MR -4.85pp | ⚠️ |

**Key Findings:**
- New duplicate detection system activated in W23: Dup Rate jumped from 0% to 14.06% at WL level, with corresponding Dup Block Rate of 3.81%
- Referral channel shows significant volatility across all countries, with FAR changes ranging from -8.37pp (CG) to +5.91pp (AO)
- Paid channel remains stable across all markets (FAR changes <1.5pp), indicating the FAR improvement is primarily driven by MR volume growth (+58.4%)
- CG Referral experienced the largest decline (-8.37pp FAR) with Dup Block Rate rising to 18.81%, suggesting the new duplicate controls are catching previously approved fraud
- PF Block Rate increased substantially in several segments: ER Paid +101.43%, KN Paid +172.26%, MR Referral +330.35%

**Action:** Monitor — The overall FAR improvement is positive and driven by legitimate volume growth in MR. The Referral channel volatility and new duplicate blocking are expected behaviors from newly deployed fraud controls. Continue monitoring Referral performance for stabilization over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W23 | 94.60% | 14.06% | 3.81% | 0.97% | 16,174 | +0.67% ← REPORTED CHANGE |
| 2026-W22 | 93.97% | 0.00% | 0.00% | 0.73% | 14,659 | +1.03% |
| 2026-W21 | 93.01% | 0.00% | 0.00% | 0.92% | 13,245 | +0.23% |
| 2026-W20 | 92.79% | 0.00% | 0.00% | 0.80% | 13,698 | -0.51% |
| 2026-W19 | 93.27% | 0.00% | 0.00% | 1.00% | 14,235 | +0.33% |
| 2026-W18 | 92.96% | 0.00% | 0.00% | 1.05% | 13,770 | +1.38% |
| 2026-W17 | 91.70% | 0.00% | 0.00% | 1.09% | 13,941 | -1.19% |
| 2026-W16 | 92.81% | 0.00% | 0.00% | 0.92% | 13,987 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| MR | 2026-W22 | 97.42% | - | 0.00% | - | 3,416 |  |
| MR | 2026-W23 | 98.19% | +0.79% | 4.54% | - | 5,413 |  |
| CG | 2026-W22 | 92.78% | - | 0.00% | - | 1,676 |  |
| CG | 2026-W23 | 91.22% | -1.69% | 15.42% | - | 1,719 |  |
| ER | 2026-W22 | 92.27% | - | 0.00% | - | 1,849 |  |
| ER | 2026-W23 | 91.36% | -0.98% | 23.41% | - | 1,875 |  |
| AO | 2026-W22 | 89.55% | - | 0.00% | - | 919 |  |
| AO | 2026-W23 | 90.87% | +1.47% | 25.50% | - | 843 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 96.46% | - | 0.00% | - | 12,759 |  |
| Paid | 2026-W23 | 96.87% | +0.43% | 12.90% | - | 14,181 |  |
| Referral | 2026-W22 | 77.26% | - | 0.00% | - | 1,900 |  |
| Referral | 2026-W23 | 78.42% | +1.50% | 22.33% | - | 1,993 |  |

---

## L2: AO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.70% | - | 0.00% | - | 0.00% | - | 0.00% | - | 614 |  |
| Paid | 2026-W23 | 98.75% | +0.05% | 25.76% | - | 0.00% | - | 0.00% | - | 559 |  |
| Referral | 2026-W22 | 71.15% | - | 0.00% | - | 0.00% | - | 0.00% | - | 305 |  |
| Referral | 2026-W23 | 75.35% | +5.91% | 25.00% | - | 24.30% | - | 0.00% | - | 284 | ⚠️ |

**Analysis:** The +0.67pp FAR improvement is a positive signal driven primarily by strong volume growth in MR (Paid channel), which offset minor declines in other markets. The activation of duplicate detection in W23 is working as intended, blocking previously undetected duplicate applications primarily in the Referral channel across all countries. No immediate action is required, but the Referral channel should be monitored as the new controls stabilize.

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 94.10% | - | 0.00% | - | 0.00% | - | 3.27% | - | 1,407 |  |
| Paid | 2026-W23 | 94.07% | -0.03% | 14.43% | - | 1.79% | - | 3.50% | +7.05% | 1,400 |  |
| Referral | 2026-W22 | 85.87% | - | 0.00% | - | 0.00% | - | 0.37% | - | 269 |  |
| Referral | 2026-W23 | 78.68% | -8.37% | 19.75% | - | 18.81% | - | 0.94% | +152.98% | 319 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 98.95% | - | 0.00% | - | 0.00% | - | 0.00% | - | 2,282 |  |
| Paid | 2026-W23 | 99.30% | +0.35% | 27.56% | - | 0.10% | - | 0.00% | - | 1,992 |  |
| Referral | 2026-W22 | 70.98% | - | 0.00% | - | 0.00% | - | 0.00% | - | 417 |  |
| Referral | 2026-W23 | 74.70% | +5.23% | 27.95% | - | 23.86% | - | 0.00% | - | 415 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 95.48% | - | 0.00% | - | 0.00% | - | 1.03% | - | 1,547 |  |
| Paid | 2026-W23 | 94.34% | -1.19% | 23.18% | - | 2.28% | - | 2.08% | +101.43% | 1,536 |  |
| Referral | 2026-W22 | 75.83% | - | 0.00% | - | 0.00% | - | 0.99% | - | 302 |  |
| Referral | 2026-W23 | 77.88% | +2.70% | 24.48% | - | 20.65% | - | 0.59% | -40.61% | 339 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: GN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 99.52% | - | 0.00% | - | 0.00% | - | 0.00% | - | 1,046 |  |
| Paid | 2026-W23 | 99.81% | +0.29% | 16.38% | - | 0.09% | - | 0.00% | - | 1,062 |  |
| Referral | 2026-W22 | 77.36% | - | 0.00% | - | 0.00% | - | 0.00% | - | 212 |  |
| Referral | 2026-W23 | 81.64% | +5.54% | 20.70% | - | 18.36% | - | 0.00% | - | 256 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 92.61% | - | 0.00% | - | 0.00% | - | 0.23% | - | 2,666 |  |
| Paid | 2026-W23 | 92.36% | -0.27% | 7.43% | - | 6.33% | - | 0.61% | +172.26% | 2,448 |  |
| Referral | 2026-W22 | 76.70% | - | 0.00% | - | 0.00% | - | 0.57% | - | 176 |  |
| Referral | 2026-W23 | 79.47% | +3.61% | 23.18% | - | 20.53% | - | 0.00% | -100.00% | 151 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: MR Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W22 | 97.97% | - | 0.00% | - | 0.00% | - | 1.00% | - | 3,197 |  |
| Paid | 2026-W23 | 98.77% | +0.82% | 4.28% | - | 0.12% | - | 0.91% | -9.42% | 5,184 |  |
| Referral | 2026-W22 | 89.50% | - | 0.00% | - | 0.00% | - | 0.91% | - | 219 |  |
| Referral | 2026-W23 | 85.15% | -4.85% | 10.48% | - | 7.42% | - | 3.93% | +330.35% | 229 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-06-09*
