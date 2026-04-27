# Fraud Investigation: RTE 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.25% → 94.05% (-0.21%)  
**Volume:** 45,711 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 94.25% to 94.05% (-0.20pp) in 2026-W17, a change that is **not statistically significant** with stable volume of 45,711 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR Trend | 8-week trend shows gradual decline from 94.95% (W10) to 94.05% (W17) | -0.21pp WoW | ⚠️ |
| L1: Country Scan | TK flagged at -6.18pp; CF at -1.46pp; TO at -2.23pp | TK exceeds ±2.5% threshold | ⚠️ |
| L1: Channel Category | Paid -0.07pp; Referral -0.56pp | Minor declines, within normal range | ✅ |
| L2: TK Deep-Dive | Paid FAR ↓6.04pp, Referral FAR ↓5.68pp; Dup Block ↑57.78% (Paid) | Both channels impacted by duplicate blocking | ⚠️ |
| L2: CF Deep-Dive | Referral FAR ↓3.96pp; Dup Rate ↑19.27%; Dup Block ↑23.37% | Referral channel degradation | ⚠️ |
| L2: TO Deep-Dive | Paid FAR ↓3.54pp; Dup Rate ↑108.36%; Dup Block ↑83.96% | Significant duplicate surge in Paid channel | ⚠️ |

**Key Findings:**
- **TK experienced the largest FAR decline (-6.18pp)** driven by sharp increases in duplicate blocking across both Paid (+57.78%) and Referral (+55.82%) channels, though volume is low (321 customers)
- **Duplicate Rate increased globally** from 15.58% to 16.66% (+1.08pp), with the most severe spikes in TT (+61.45%), TO (+39.91%), and TK (+18.40%)
- **TO Paid channel** showed a dramatic 108.36% increase in duplicate rate, driving Dup Block up 83.96% and FAR down 3.54pp
- **CF Referral channel** declined 3.96pp in FAR, correlating with a 19.27% increase in duplicate rate and 23.37% increase in duplicate blocking
- **Overall impact is limited** as the flagged countries (TK, TO) represent low volumes (<1,000 combined), while high-volume FJ (32,361) remained stable at -0.05pp

**Action:** **Monitor** - The overall FAR change is not significant and high-volume markets remain stable. Continue monitoring duplicate rate trends, particularly in TK and TO, for potential escalation if the pattern persists into W18.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 94.05% | 16.66% | 4.90% | 0.37% | 45,711 | -0.21% ← REPORTED CHANGE |
| 2026-W16 | 94.25% | 15.58% | 4.39% | 0.31% | 45,893 | -0.45% |
| 2026-W15 | 94.68% | 14.57% | 4.09% | 0.31% | 45,729 | +0.04% |
| 2026-W14 | 94.64% | 14.05% | 4.12% | 0.18% | 41,374 | +0.54% |
| 2026-W13 | 94.13% | 14.40% | 3.96% | 0.25% | 43,924 | +0.32% |
| 2026-W12 | 93.83% | 14.45% | 4.20% | 0.21% | 45,551 | -0.60% |
| 2026-W11 | 94.40% | 14.50% | 3.87% | 0.21% | 48,692 | -0.58% |
| 2026-W10 | 94.95% | 13.95% | 3.72% | 0.16% | 50,484 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| CF | 2026-W16 | 93.66% | - | 14.35% | - | 7,255 |  |
| CF | 2026-W17 | 92.29% | -1.46% | 16.46% | +14.75% | 6,772 |  |
| YE | 2026-W16 | 93.91% | - | 18.92% | - | 4,006 |  |
| YE | 2026-W17 | 94.54% | +0.67% | 20.23% | +6.90% | 4,044 |  |
| TK | 2026-W16 | 91.64% | - | 11.05% | - | 371 |  |
| TK | 2026-W17 | 85.98% | -6.18% | 13.08% | +18.40% | 321 | ⚠️ |
| FJ | 2026-W16 | 94.68% | - | 16.19% | - | 31,327 |  |
| FJ | 2026-W17 | 94.63% | -0.05% | 16.74% | +3.41% | 32,361 |  |
| TT | 2026-W16 | 93.40% | - | 6.29% | - | 1,287 |  |
| TT | 2026-W17 | 91.57% | -1.95% | 10.16% | +61.45% | 807 |  |
| TO | 2026-W16 | 90.69% | - | 8.58% | - | 548 |  |
| TO | 2026-W17 | 88.67% | -2.23% | 12.00% | +39.91% | 450 |  |
| TV | 2026-W16 | 92.26% | - | 7.30% | - | 452 |  |
| TV | 2026-W17 | 93.92% | +1.80% | 7.79% | +6.64% | 411 |  |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.06% | - | 14.32% | - | 37,305 |  |
| Paid | 2026-W17 | 96.99% | -0.07% | 15.26% | +6.58% | 36,979 |  |
| Referral | 2026-W16 | 82.07% | - | 21.04% | - | 8,588 |  |
| Referral | 2026-W17 | 81.61% | -0.56% | 22.57% | +7.28% | 8,732 |  |

---

## L2: CF Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 98.37% | - | 12.67% | - | 0.19% | - | 0.00% | - | 5,215 |  |
| Paid | 2026-W17 | 98.83% | +0.47% | 13.76% | +8.57% | 0.26% | +35.84% | 0.00% | - | 4,607 |  |
| Referral | 2026-W16 | 81.62% | - | 18.63% | - | 16.32% | - | 0.00% | - | 2,040 |  |
| Referral | 2026-W17 | 78.38% | -3.96% | 22.22% | +19.27% | 20.14% | +23.37% | 0.00% | - | 2,165 | ⚠️ |

**Analysis:** The 0.20pp decline in FAR for 2026-W17 is within normal weekly fluctuation and not statistically significant. The primary driver across flagged markets (TK, CF, TO) is elevated duplicate detection and blocking, suggesting either increased fraudulent retry attempts or potential sensitivity in duplicate detection rules. Given the low volume of affected markets and stability in the dominant FJ market (70% of volume), no immediate action is required beyond continued monitoring of duplicate rate trends.

---

## L2: TK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 92.69% | - | 10.63% | - | 6.64% | - | 0.33% | - | 301 |  |
| Paid | 2026-W17 | 87.10% | -6.04% | 11.69% | +9.99% | 10.48% | +57.78% | 0.40% | +21.37% | 248 | ⚠️ |
| Referral | 2026-W16 | 87.14% | - | 12.86% | - | 11.43% | - | 0.00% | - | 70 |  |
| Referral | 2026-W17 | 82.19% | -5.68% | 17.81% | +38.51% | 17.81% | +55.82% | 0.00% | - | 73 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 94.06% | - | 4.99% | - | 4.28% | - | 0.00% | - | 421 |  |
| Paid | 2026-W17 | 90.73% | -3.54% | 10.39% | +108.36% | 7.87% | +83.96% | 0.00% | - | 356 | ⚠️ |
| Referral | 2026-W16 | 79.53% | - | 20.47% | - | 18.90% | - | 0.00% | - | 127 |  |
| Referral | 2026-W17 | 80.85% | +1.66% | 18.09% | -11.66% | 18.09% | -4.30% | 0.00% | - | 94 |  |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: TZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 95.69% | - | 6.46% | - | 3.52% | - | 0.00% | - | 511 |  |
| Paid | 2026-W17 | 94.83% | -0.90% | 6.52% | +0.91% | 4.27% | +21.21% | 0.00% | - | 445 |  |
| Referral | 2026-W16 | 68.38% | - | 32.35% | - | 30.88% | - | 0.74% | - | 136 |  |
| Referral | 2026-W17 | 74.00% | +8.22% | 26.00% | -19.64% | 26.00% | -15.81% | 0.00% | -100.00% | 100 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: YE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.74% | - | 17.08% | - | 1.44% | - | 0.00% | - | 3,401 |  |
| Paid | 2026-W17 | 97.90% | +0.17% | 18.75% | +9.74% | 1.63% | +13.32% | 0.00% | - | 3,430 |  |
| Referral | 2026-W16 | 72.40% | - | 29.26% | - | 26.45% | - | 0.00% | - | 605 |  |
| Referral | 2026-W17 | 75.73% | +4.61% | 28.50% | -2.58% | 24.27% | -8.24% | 0.00% | - | 614 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TK | ↓ -6.18% | Paid ↓ -6.04%, Referral ↓ -5.68% | ↑ +18.40% | ↑ +60.98% | ↑ +15.58% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-27*
