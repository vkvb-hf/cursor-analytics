# Fraud Investigation: RTE 2026-W19

**Metric:** Fraud Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 93.86% → 94.24% (+0.40%)  
**Volume:** 41,588 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 93.86% to 94.24% (+0.38pp) in W19, a change that is not statistically significant and remains within the normal 8-week range of 93.83%-94.67%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | FAR within 8-week range | +0.38pp | ✅ |
| L1: Country Scan | 4 countries exceed ±2.5% threshold | TT +24.32%, TZ +16.21%, TV +20.41%, TO +12.19% | ⚠️ |
| L1: Channel Category | Referral channel declining | -4.14% | ⚠️ |
| L2: Country Deep-Dive | Paid channel driving improvements across flagged countries | TT Paid +29.16%, TZ Paid +16.12% | ⚠️ |
| L2: Referral Performance | Consistent Referral degradation with rising Dup Block | FJ -4.53%, YE -5.25% | ⚠️ |

**Key Findings:**
- **TT Paid channel surged +29.16pp** in FAR while Dup Rate decreased 26.78%, suggesting improved fraud detection calibration or cleaner traffic in this segment
- **Referral channel shows systemic weakness** across multiple countries: FJ (-4.53%), YE (-5.25%), with Dup Block rates increasing significantly (FJ +37.59%, YE +22.19%)
- **TV experienced dramatic Dup Rate spike (+160.93% in Paid)** despite FAR improvement, indicating potential duplicate abuse that is being caught but warrants monitoring
- **Small market volatility** is evident—flagged countries (TT, TZ, TV, TO) have volumes under 900, making percentage swings appear larger than their actual impact (~2,324 combined vs. 41,588 total)
- **Overall volume declined 1.5%** (42,241 → 41,588), with FJ (largest market) down 3.4%

**Action:** **Monitor** — The RTE-level change is not significant and overall FAR remains healthy. Continue monitoring the Referral channel degradation and rising Dup Block rates across markets. If Referral FAR declines persist for 2+ consecutive weeks, escalate for channel quality investigation.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W19 | 94.24% | 16.29% | 4.87% | 0.28% | 41,588 | +0.40% ← REPORTED CHANGE |
| 2026-W18 | 93.86% | 14.56% | 3.90% | 0.25% | 42,241 | -0.11% |
| 2026-W17 | 93.96% | 16.44% | 4.61% | 0.35% | 44,555 | -0.37% |
| 2026-W16 | 94.31% | 15.44% | 4.26% | 0.31% | 45,927 | -0.38% |
| 2026-W15 | 94.67% | 14.51% | 4.03% | 0.30% | 45,712 | +0.04% |
| 2026-W14 | 94.63% | 14.01% | 4.08% | 0.18% | 41,364 | +0.53% |
| 2026-W13 | 94.13% | 14.37% | 3.92% | 0.26% | 43,918 | +0.32% |
| 2026-W12 | 93.83% | 14.42% | 4.17% | 0.21% | 45,541 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| TT | 2026-W18 | 74.91% | - | 7.85% | - | 853 |  |
| TT | 2026-W19 | 93.13% | +24.32% | 7.67% | -2.29% | 873 | ⚠️ |
| FJ | 2026-W18 | 95.45% | - | 14.86% | - | 29,366 |  |
| FJ | 2026-W19 | 95.17% | -0.29% | 16.12% | +8.45% | 28,374 |  |
| TZ | 2026-W18 | 78.84% | - | 11.62% | - | 482 |  |
| TZ | 2026-W19 | 91.62% | +16.21% | 9.31% | -19.86% | 537 | ⚠️ |
| TV | 2026-W18 | 74.86% | - | 6.49% | - | 370 |  |
| TV | 2026-W19 | 90.14% | +20.41% | 12.02% | +85.30% | 416 | ⚠️ |
| TO | 2026-W18 | 80.18% | - | 8.29% | - | 434 |  |
| TO | 2026-W19 | 89.96% | +12.19% | 12.05% | +45.25% | 498 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TT, TZ, TV, TO

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 96.31% | - | 13.35% | - | 33,981 |  |
| Paid | 2026-W19 | 97.73% | +1.47% | 14.40% | +7.87% | 33,258 |  |
| Referral | 2026-W18 | 83.75% | - | 19.54% | - | 8,260 |  |
| Referral | 2026-W19 | 80.29% | -4.14% | 23.81% | +21.83% | 8,330 | ⚠️ |

---

## L2: CF Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 97.89% | - | 12.78% | - | 0.34% | - | 0.00% | - | 4,703 |  |
| Paid | 2026-W19 | 98.69% | +0.81% | 13.56% | +6.09% | 0.25% | -26.55% | 0.00% | - | 4,802 |  |
| Referral | 2026-W18 | 81.89% | - | 17.19% | - | 15.45% | - | 0.00% | - | 2,071 |  |
| Referral | 2026-W19 | 78.70% | -3.90% | 22.84% | +32.85% | 20.19% | +30.68% | 0.00% | - | 2,080 | ⚠️ |

**Analysis:** The +0.38pp FAR improvement in W19 reflects positive movement in smaller markets (TT, TZ, TV, TO) primarily driven by the Paid channel, offsetting continued weakness in the Referral channel where duplicate activity and blocking rates are increasing. Given the statistical insignificance of the overall change and the low volume of flagged countries, no immediate action is required beyond standard monitoring of Referral channel performance trends.

---

## L2: FJ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 97.39% | - | 13.79% | - | 1.39% | - | 0.37% | - | 24,183 |  |
| Paid | 2026-W19 | 97.84% | +0.46% | 14.60% | +5.81% | 1.24% | -11.28% | 0.44% | +19.31% | 23,457 |  |
| Referral | 2026-W18 | 86.36% | - | 19.83% | - | 12.14% | - | 0.29% | - | 5,183 |  |
| Referral | 2026-W19 | 82.45% | -4.53% | 23.37% | +17.82% | 16.70% | +37.59% | 0.24% | -15.67% | 4,917 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 80.30% | - | 6.69% | - | 4.46% | - | 0.00% | - | 269 |  |
| Paid | 2026-W19 | 89.37% | +11.30% | 11.63% | +73.77% | 9.63% | +115.97% | 0.00% | - | 301 | ⚠️ |
| Referral | 2026-W18 | 77.78% | - | 17.46% | - | 17.46% | - | 0.00% | - | 63 |  |
| Referral | 2026-W19 | 88.64% | +13.96% | 12.50% | -28.41% | 9.09% | -47.93% | 0.00% | - | 88 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 81.10% | - | 6.85% | - | 4.66% | - | 0.00% | - | 365 |  |
| Paid | 2026-W19 | 92.25% | +13.75% | 10.25% | +49.65% | 7.50% | +61.03% | 0.00% | - | 400 | ⚠️ |
| Referral | 2026-W18 | 75.36% | - | 15.94% | - | 15.94% | - | 0.00% | - | 69 |  |
| Referral | 2026-W19 | 80.61% | +6.97% | 19.39% | +21.61% | 19.39% | +21.61% | 0.00% | - | 98 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 74.22% | - | 6.98% | - | 4.99% | - | 0.00% | - | 702 |  |
| Paid | 2026-W19 | 95.86% | +29.16% | 5.11% | -26.78% | 3.18% | -36.28% | 0.00% | - | 724 | ⚠️ |
| Referral | 2026-W18 | 78.15% | - | 11.92% | - | 10.60% | - | 0.00% | - | 151 |  |
| Referral | 2026-W19 | 79.87% | +2.20% | 20.13% | +68.90% | 20.13% | +90.02% | 0.00% | - | 149 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TV Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 74.77% | - | 4.98% | - | 3.43% | - | 0.00% | - | 321 |  |
| Paid | 2026-W19 | 89.31% | +19.45% | 13.01% | +160.93% | 9.54% | +178.32% | 0.29% | - | 346 | ⚠️ |
| Referral | 2026-W18 | 75.51% | - | 16.33% | - | 12.24% | - | 0.00% | - | 49 |  |
| Referral | 2026-W19 | 94.29% | +24.86% | 7.14% | -56.25% | 4.29% | -65.00% | 0.00% | - | 70 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 82.08% | - | 7.75% | - | 5.33% | - | 0.00% | - | 413 |  |
| Paid | 2026-W19 | 95.31% | +16.12% | 5.36% | -30.86% | 4.02% | -24.57% | 0.00% | - | 448 | ⚠️ |
| Referral | 2026-W18 | 59.42% | - | 34.78% | - | 34.78% | - | 0.00% | - | 69 |  |
| Referral | 2026-W19 | 73.03% | +22.91% | 29.21% | -16.01% | 26.97% | -22.47% | 0.00% | - | 89 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 97.82% | - | 15.21% | - | 1.16% | - | 0.00% | - | 3,025 |  |
| Paid | 2026-W19 | 98.78% | +0.98% | 19.17% | +26.08% | 0.72% | -37.82% | 0.00% | - | 2,780 |  |
| Referral | 2026-W18 | 74.21% | - | 26.12% | - | 23.80% | - | 0.00% | - | 605 |  |
| Referral | 2026-W19 | 70.32% | -5.25% | 31.94% | +22.31% | 29.08% | +22.19% | 0.00% | - | 839 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TT | ↑ +24.32% | Paid ↑ +29.16% | → -2.29% | → +1.54% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TZ | ↑ +16.21% | Paid ↑ +16.12%, Referral ↑ +22.91% | ↓ -19.86% | ↓ -18.05% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TV | ↑ +20.41% | Paid ↑ +19.45%, Referral ↑ +24.86% | ↑ +85.30% | ↑ +88.35% | → - | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑ +12.19% | Paid ↑ +13.75%, Referral ↑ +6.97% | ↑ +45.25% | ↑ +52.51% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-12*
