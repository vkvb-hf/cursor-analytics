# Fraud Investigation: HF-INTL 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 92.14% → 92.06% (-0.09%)  
**Volume:** 45,438 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined marginally from 92.14% to 92.06% (-0.09pp) in 2026-W15, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | -0.09pp WoW | Within ±0.5pp range | ✅ |
| L1: Country Scan | 3 countries exceed ±2.5% threshold | AT +4.34%, NZ -2.91%, LU -2.96% | ⚠️ |
| L1: Channel Category | Stable performance | Paid +0.48%, Referral -0.10% | ✅ |
| L2: Referral Channel | Multiple flags across countries | Dup Block increases driving declines | ⚠️ |

**Key Findings:**
- **AT Referral improvement (+25.91pp FAR):** Driven by significant decrease in Duplicate Rate (-37.61%) and Duplicate Block Rate (-41.88%), suggesting improved customer quality or reduced repeat fraud attempts
- **NZ Referral decline (-21.15pp FAR):** Caused by sharp increase in Duplicate Block Rate (+51.20%) and Duplicate Rate (+32.54%), indicating heightened duplicate fraud activity in this channel
- **LU Paid channel decline (-3.28pp FAR):** Small volume market (61 customers) saw FAR drop from 100% to 96.72%, driven by new PF Block activity (+1.64pp)
- **Referral channel consistently underperforms:** Across all countries, Referral FAR (76.49%) significantly trails Paid channel (97.71%), with Duplicate Block rates 20-40x higher
- **Volume increased +6.3%:** Overall volume rose from 42,760 to 45,438 customers, with GB and DE contributing the largest absolute increases

**Action:** **Monitor** — The overall FAR change is not statistically significant and within normal variance. Continue monitoring NZ Referral channel for sustained Duplicate Block increases; no immediate escalation required.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 92.06% | 33.28% | 6.87% | 0.28% | 45,438 | -0.09% |
| 2026-W15 | 92.14% | 30.86% | 6.70% | 0.24% | 42,760 | +0.51% ← REPORTED CHANGE |
| 2026-W14 | 91.67% | 29.96% | 6.99% | 0.22% | 37,168 | -0.11% |
| 2026-W13 | 91.77% | 30.39% | 6.49% | 0.27% | 46,643 | -0.19% |
| 2026-W12 | 91.95% | 30.52% | 6.77% | 0.19% | 44,679 | +0.24% |
| 2026-W11 | 91.73% | 29.86% | 7.05% | 0.15% | 49,904 | -0.70% |
| 2026-W10 | 92.37% | 29.80% | 6.39% | 0.22% | 52,827 | -0.01% |
| 2026-W09 | 92.38% | 29.13% | 6.24% | 0.37% | 54,947 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| DE | 2026-W14 | 93.48% | - | 29.66% | - | 7,071 |  |
| DE | 2026-W15 | 94.16% | +0.73% | 29.52% | -0.47% | 9,056 |  |
| GB | 2026-W14 | 92.83% | - | 39.34% | - | 8,845 |  |
| GB | 2026-W15 | 93.21% | +0.41% | 40.82% | +3.76% | 10,499 |  |
| AT | 2026-W14 | 90.18% | - | 22.91% | - | 611 |  |
| AT | 2026-W15 | 94.09% | +4.34% | 17.99% | -21.47% | 728 | ⚠️ |
| AU | 2026-W14 | 92.32% | - | 36.05% | - | 2,982 |  |
| AU | 2026-W15 | 91.53% | -0.86% | 36.87% | +2.29% | 3,436 |  |
| DK | 2026-W14 | 88.77% | - | 25.39% | - | 1,095 |  |
| DK | 2026-W15 | 90.30% | +1.73% | 29.72% | +17.08% | 1,598 |  |
| NZ | 2026-W14 | 89.42% | - | 35.71% | - | 728 |  |
| NZ | 2026-W15 | 86.82% | -2.91% | 34.83% | -2.47% | 933 | ⚠️ |
| LU | 2026-W14 | 97.40% | - | 0.00% | - | 77 |  |
| LU | 2026-W15 | 94.52% | -2.96% | 0.00% | - | 73 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, NZ, LU

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.24% | - | 30.20% | - | 27,150 |  |
| Paid | 2026-W15 | 97.71% | +0.48% | 31.34% | +3.75% | 31,542 |  |
| Referral | 2026-W14 | 76.57% | - | 29.31% | - | 10,018 |  |
| Referral | 2026-W15 | 76.49% | -0.10% | 29.53% | +0.77% | 11,218 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 98.10% | - | 19.66% | - | 0.21% | - | 0.00% | - | 473 |  |
| Paid | 2026-W15 | 98.24% | +0.14% | 17.08% | -13.14% | 0.53% | +149.82% | 0.35% | - | 568 |  |
| Referral | 2026-W14 | 63.04% | - | 34.06% | - | 33.33% | - | 0.00% | - | 138 |  |
| Referral | 2026-W15 | 79.38% | +25.91% | 21.25% | -37.61% | 19.38% | -41.88% | 0.00% | - | 160 | ⚠️ |

**Analysis:** The -0.09pp decline in HF-INTL Fraud Approval Rate represents normal week-over-week fluctuation and does not warrant immediate intervention. While country-level variations exist (notably AT's improvement and NZ's decline in the Referral channel), these are primarily driven by Duplicate Block rate movements in low-to-moderate volume segments. The 8-week trend shows FAR remains stable between 91.67% and 92.38%, confirming this week's performance is consistent with historical patterns.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 97.69% | - | 35.77% | - | 0.77% | - | 0.38% | - | 2,340 |  |
| Paid | 2026-W15 | 97.63% | -0.06% | 35.90% | +0.36% | 0.66% | -14.72% | 0.62% | +61.08% | 2,744 |  |
| Referral | 2026-W14 | 72.74% | - | 37.07% | - | 26.17% | - | 0.47% | - | 642 |  |
| Referral | 2026-W15 | 67.34% | -7.42% | 40.75% | +9.93% | 31.07% | +18.73% | 0.29% | -38.15% | 692 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 95.70% | - | 8.60% | - | 0.00% | - | 0.00% | - | 93 |  |
| Paid | 2026-W15 | 97.52% | +1.90% | 9.09% | +5.68% | 0.00% | - | 1.65% | - | 121 |  |
| Referral | 2026-W14 | 69.57% | - | 21.74% | - | 21.74% | - | 0.00% | - | 23 |  |
| Referral | 2026-W15 | 60.00% | -13.75% | 36.00% | +65.60% | 32.00% | +47.20% | 0.00% | - | 25 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 98.33% | - | 29.15% | - | 0.44% | - | 0.09% | - | 5,732 |  |
| Paid | 2026-W15 | 98.47% | +0.15% | 29.30% | +0.51% | 0.50% | +15.03% | 0.09% | +8.81% | 7,375 |  |
| Referral | 2026-W14 | 72.74% | - | 31.81% | - | 26.36% | - | 0.30% | - | 1,339 |  |
| Referral | 2026-W15 | 75.25% | +3.45% | 30.46% | -4.26% | 24.39% | -7.48% | 0.06% | -80.09% | 1,681 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: DK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 98.51% | - | 25.83% | - | 0.33% | - | 0.33% | - | 604 |  |
| Paid | 2026-W15 | 98.70% | +0.19% | 30.73% | +18.97% | 0.33% | -1.63% | 0.33% | -1.63% | 921 |  |
| Referral | 2026-W14 | 76.78% | - | 24.85% | - | 21.18% | - | 0.00% | - | 491 |  |
| Referral | 2026-W15 | 78.88% | +2.73% | 28.36% | +14.14% | 19.79% | -6.55% | 0.00% | - | 677 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: LU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 100.00% | - | 0.00% | - | 0.00% | - | 0.00% | - | 64 |  |
| Paid | 2026-W15 | 96.72% | -3.28% | 0.00% | - | 0.00% | - | 1.64% | - | 61 | ⚠️ |
| Referral | 2026-W14 | 84.62% | - | 0.00% | - | 0.00% | - | 0.00% | - | 13 |  |
| Referral | 2026-W15 | 83.33% | -1.52% | 0.00% | - | 0.00% | - | 0.00% | - | 12 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NL Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 90.98% | - | 29.47% | - | 6.76% | - | 0.08% | - | 1,242 |  |
| Paid | 2026-W15 | 92.30% | +1.45% | 29.75% | +0.94% | 6.39% | -5.57% | 0.17% | +117.32% | 1,143 |  |
| Referral | 2026-W14 | 92.14% | - | 21.61% | - | 6.68% | - | 0.00% | - | 509 |  |
| Referral | 2026-W15 | 88.89% | -3.53% | 24.55% | +13.61% | 9.32% | +39.51% | 0.00% | - | 558 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 99.68% | - | 21.04% | - | 0.32% | - | 0.00% | - | 309 |  |
| Paid | 2026-W15 | 98.91% | -0.77% | 22.85% | +8.64% | 0.00% | -100.00% | 0.73% | - | 827 |  |
| Referral | 2026-W14 | 80.70% | - | 19.88% | - | 17.54% | - | 0.00% | - | 171 |  |
| Referral | 2026-W15 | 85.28% | +5.67% | 17.26% | -13.20% | 13.45% | -23.32% | 0.00% | - | 394 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.36% | - | 35.52% | - | 0.36% | - | 1.46% | - | 549 |  |
| Paid | 2026-W15 | 96.66% | +0.32% | 30.88% | -13.07% | 0.56% | +52.71% | 0.97% | -33.19% | 719 |  |
| Referral | 2026-W14 | 68.16% | - | 36.31% | - | 29.05% | - | 0.56% | - | 179 |  |
| Referral | 2026-W15 | 53.74% | -21.15% | 48.13% | +32.54% | 43.93% | +51.20% | 0.93% | +67.29% | 214 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| AT | ↑ +4.34% | Referral ↑ +25.91% | ↓ -21.47% | ↓ -39.29% | → - | [AI_SUMMARY_PLACEHOLDER] |
| NZ | ↓ -2.91% | Referral ↓ -21.15% | → -2.47% | ↑ +41.61% | ↓ -21.97% | [AI_SUMMARY_PLACEHOLDER] |
| LU | ↓ -2.96% | Paid ↓ -3.28% | → - | → - | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-22*
