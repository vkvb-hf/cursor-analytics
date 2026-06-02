# Fraud Investigation: WL 2026-W22

**Metric:** Fraud Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 92.95% → 94.14% (+1.28%)  
**Volume:** 14,733 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** Fraud Approval Rate improved significantly from 92.95% to 94.14% (+1.28% or +1.19pp) in 2026-W22, with volume increasing to 14,733 customers reaching fraud service.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (91.70%-94.14%) | +1.28% | ✅ |
| L1: Country Scan | KN exceeds ±2.5% threshold | +2.51% | ⚠️ |
| L1: Channel Scan | Paid & Referral within threshold | +0.95% / +1.26% | ✅ |
| L2: KN Deep-Dive | Referral channel driving change | +15.14% | ⚠️ |
| L2: CK Deep-Dive | Referral FAR declining | -4.77% | ⚠️ |
| L2: CG Deep-Dive | Referral FAR improving significantly | +5.54% | ⚠️ |

**Key Findings:**
- KN is the primary driver of the FAR increase, with Referral channel FAR surging +15.14% (66.36% → 76.40%) accompanied by a -19.28% drop in Duplicate Rate and -29.28% drop in Duplicate Block Rate
- Duplicate Rate across WL decreased from 16.58% to 15.58% (-6.03%), contributing to fewer fraud blocks and higher approval rates
- CK shows a divergent pattern where Referral FAR declined -4.77% (75.34% → 71.74%) due to increased Duplicate Block Rate (+9.12%)
- Overall Duplicate Block Rate decreased from 4.87% to 4.41% (-9.45%) and PF Block Rate decreased from 0.94% to 0.75% (-20.21%), both contributing to improved FAR
- Volume increased by 11.2% (13,248 → 14,733), with KN volume up 22.4% (2,372 → 2,903)

**Action:** Monitor - The FAR improvement appears driven by reduced duplicate activity and lower block rates, particularly in KN Referral channel. Continue monitoring KN and CK Referral channels for sustained trends; no immediate escalation required unless pattern reverses or fraud losses increase.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W22 | 94.14% | 15.58% | 4.41% | 0.75% | 14,733 | +1.28% ← REPORTED CHANGE |
| 2026-W21 | 92.95% | 16.58% | 4.87% | 0.94% | 13,248 | +0.18% |
| 2026-W20 | 92.78% | 17.28% | 5.00% | 0.82% | 13,701 | -0.28% |
| 2026-W19 | 93.04% | 13.86% | 4.43% | 1.01% | 14,277 | +0.10% |
| 2026-W18 | 92.95% | 14.59% | 4.34% | 1.05% | 13,772 | +1.36% |
| 2026-W17 | 91.70% | 17.52% | 5.49% | 1.09% | 13,942 | -1.20% |
| 2026-W16 | 92.82% | 16.61% | 4.72% | 0.92% | 13,988 | -0.47% |
| 2026-W15 | 93.26% | 15.49% | 4.73% | 0.66% | 15,128 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| KN | 2026-W21 | 89.42% | - | 8.98% | - | 2,372 |  |
| KN | 2026-W22 | 91.66% | +2.51% | 8.27% | -7.93% | 2,903 | ⚠️ |
| MR | 2026-W21 | 96.62% | - | 4.55% | - | 2,992 |  |
| MR | 2026-W22 | 97.78% | +1.19% | 4.21% | -7.37% | 3,420 |  |
| ER | 2026-W21 | 90.94% | - | 22.42% | - | 1,766 |  |
| ER | 2026-W22 | 92.33% | +1.53% | 24.08% | +7.40% | 1,852 |  |
| GN | 2026-W21 | 94.44% | - | 16.99% | - | 1,242 |  |
| GN | 2026-W22 | 95.79% | +1.42% | 17.49% | +2.94% | 1,258 |  |

**Countries exceeding ±2.5% threshold:** KN

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 95.70% | - | 15.14% | - | 11,347 |  |
| Paid | 2026-W22 | 96.61% | +0.95% | 14.31% | -5.45% | 12,826 |  |
| Referral | 2026-W21 | 76.54% | - | 25.14% | - | 1,901 |  |
| Referral | 2026-W22 | 77.50% | +1.26% | 24.12% | -4.07% | 1,907 |  |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 94.73% | - | 12.91% | - | 1.58% | - | 2.83% | - | 1,518 |  |
| Paid | 2026-W22 | 94.18% | -0.58% | 13.91% | +7.74% | 2.13% | +34.67% | 3.26% | +15.25% | 1,409 |  |
| Referral | 2026-W21 | 81.42% | - | 17.99% | - | 16.52% | - | 0.88% | - | 339 |  |
| Referral | 2026-W22 | 85.93% | +5.54% | 15.19% | -15.61% | 13.70% | -17.04% | 0.37% | -58.15% | 270 | ⚠️ |

**Analysis:** The +1.28% FAR improvement in 2026-W22 is primarily attributed to decreased duplicate rates and block rates across the portfolio, with KN's Referral channel showing the most significant improvement (+15.14% FAR). The reduction in Duplicate Block Rate (-9.45%) and PF Block Rate (-20.21%) at the aggregate level suggests either improved customer quality or potential loosening of fraud controls that warrants continued observation. Recommend maintaining standard monitoring cadence while tracking downstream fraud loss metrics to ensure the higher approval rate does not correlate with increased fraud exposure.

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 98.96% | - | 36.65% | - | 0.40% | - | 0.00% | - | 1,730 |  |
| Paid | 2026-W22 | 99.17% | +0.21% | 28.13% | -23.25% | 0.17% | -56.76% | 0.00% | - | 2,286 |  |
| Referral | 2026-W21 | 75.34% | - | 30.56% | - | 24.13% | - | 0.00% | - | 373 |  |
| Referral | 2026-W22 | 71.74% | -4.77% | 30.19% | -1.21% | 26.33% | +9.12% | 0.00% | - | 414 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 90.51% | - | 7.86% | - | 6.71% | - | 0.09% | - | 2,265 |  |
| Paid | 2026-W22 | 92.66% | +2.38% | 7.08% | -9.88% | 6.17% | -8.13% | 0.26% | +190.92% | 2,725 |  |
| Referral | 2026-W21 | 66.36% | - | 32.71% | - | 31.78% | - | 0.00% | - | 107 |  |
| Referral | 2026-W22 | 76.40% | +15.14% | 26.40% | -19.28% | 22.47% | -29.28% | 0.56% | - | 178 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| KN | ↑ +2.51% | Referral ↑ +15.14% | ↓ -7.93% | ↓ -8.63% | ↑ +226.83% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-06-02*
