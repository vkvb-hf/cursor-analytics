# Fraud Investigation: RTE 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.33% → 94.05% (-0.29%)  
**Volume:** 45,711 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by -0.29pp from 94.33% to 94.05% in 2026-W17, a change that is **not statistically significant** across 45,711 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | 8-week trend stable (93.83%-94.94% range) | -0.29pp | ✅ |
| L1: Country | TK exceeded ±2.5% threshold | -6.18pp | ⚠️ |
| L1: Channel Category | Paid & Referral within normal range | -0.13pp / -0.70pp | ✅ |
| L2: TK Paid | Significant FAR decline with Dup Block surge | -6.04pp, Dup Block +57.78% | ⚠️ |
| L2: TK Referral | FAR decline with elevated Dup Rate | -5.68pp, Dup Rate +38.51% | ⚠️ |
| L2: TO Paid | FAR decline driven by Dup Rate doubling | -3.54pp, Dup Rate +108.36% | ⚠️ |

**Key Findings:**
- TK shows the largest FAR decline (-6.18pp) driven by both Paid (-6.04pp) and Referral (-5.68pp) channels, with Dup Block rates increasing +57.78% and +55.82% respectively
- Global Dup Rate increased from 15.54% to 16.66% (+1.12pp), continuing a 7-week upward trend from 13.95% in W10
- TO Paid channel experienced a Dup Rate surge of +108.36% (4.99% → 10.39%), driving FAR down -3.54pp
- CF Referral channel saw FAR decline -4.22pp with Dup Rate up +20.68% and Dup Block up +25.07%
- TK has low volume (321 customers), making percentage swings more volatile but still warranting monitoring

**Action:** **Monitor** – The overall RTE change is not significant. Continue monitoring TK and TO for sustained Dup Rate/Block increases over the next 1-2 weeks. Escalate if TK FAR remains below 90% or global Dup Rate exceeds 18%.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 94.05% | 16.66% | 4.90% | 0.37% | 45,711 | -0.29% ← REPORTED CHANGE |
| 2026-W16 | 94.33% | 15.54% | 4.36% | 0.31% | 45,955 | -0.37% |
| 2026-W15 | 94.68% | 14.56% | 4.08% | 0.30% | 45,726 | +0.05% |
| 2026-W14 | 94.64% | 14.05% | 4.12% | 0.18% | 41,374 | +0.54% |
| 2026-W13 | 94.13% | 14.40% | 3.96% | 0.25% | 43,924 | +0.32% |
| 2026-W12 | 93.83% | 14.45% | 4.19% | 0.21% | 45,550 | -0.60% |
| 2026-W11 | 94.40% | 14.50% | 3.87% | 0.21% | 48,691 | -0.58% |
| 2026-W10 | 94.94% | 13.95% | 3.72% | 0.16% | 50,483 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| CF | 2026-W16 | 93.81% | - | 14.20% | - | 7,304 |  |
| CF | 2026-W17 | 92.29% | -1.62% | 16.46% | +15.97% | 6,772 |  |
| FJ | 2026-W16 | 94.74% | - | 16.17% | - | 31,339 |  |
| FJ | 2026-W17 | 94.63% | -0.11% | 16.74% | +3.55% | 32,361 |  |
| YE | 2026-W16 | 94.09% | - | 18.94% | - | 4,007 |  |
| YE | 2026-W17 | 94.54% | +0.48% | 20.23% | +6.79% | 4,044 |  |
| TK | 2026-W16 | 91.64% | - | 11.05% | - | 371 |  |
| TK | 2026-W17 | 85.98% | -6.18% | 13.08% | +18.40% | 321 | ⚠️ |
| TT | 2026-W16 | 93.32% | - | 6.29% | - | 1,287 |  |
| TT | 2026-W17 | 91.57% | -1.87% | 10.16% | +61.45% | 807 |  |
| TO | 2026-W16 | 90.69% | - | 8.58% | - | 548 |  |
| TO | 2026-W17 | 88.67% | -2.23% | 12.00% | +39.91% | 450 |  |
| TV | 2026-W16 | 92.26% | - | 7.30% | - | 452 |  |
| TV | 2026-W17 | 93.92% | +1.80% | 7.79% | +6.64% | 411 |  |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.12% | - | 14.31% | - | 37,369 |  |
| Paid | 2026-W17 | 96.99% | -0.13% | 15.26% | +6.69% | 36,979 |  |
| Referral | 2026-W16 | 82.18% | - | 20.91% | - | 8,586 |  |
| Referral | 2026-W17 | 81.61% | -0.70% | 22.57% | +7.97% | 8,732 |  |

---

## L2: CF Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 98.44% | - | 12.57% | - | 0.21% | - | 0.00% | - | 5,267 |  |
| Paid | 2026-W17 | 98.83% | +0.39% | 13.76% | +9.49% | 0.26% | +24.72% | 0.00% | - | 4,607 |  |
| Referral | 2026-W16 | 81.84% | - | 18.41% | - | 16.10% | - | 0.00% | - | 2,037 |  |
| Referral | 2026-W17 | 78.38% | -4.22% | 22.22% | +20.68% | 20.14% | +25.07% | 0.00% | - | 2,165 | ⚠️ |

**Analysis:** The -0.29pp decline in Fraud Approval Rate is within normal weekly fluctuation and not statistically significant. The primary concern is the localized deterioration in TK (-6.18pp), where both Paid and Referral channels show elevated duplicate detection rates and block rates, though the low volume (321 customers) limits overall RTE impact. Recommend continued monitoring of the upward Dup Rate trend (now at 16.66% globally, up from 13.95% in W10) and specific attention to TK and TO markets.

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
| Paid | 2026-W16 | 97.94% | - | 17.11% | - | 1.44% | - | 0.00% | - | 3,402 |  |
| Paid | 2026-W17 | 97.90% | -0.04% | 18.75% | +9.58% | 1.63% | +13.35% | 0.00% | - | 3,430 |  |
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


*Report: 2026-04-28*
