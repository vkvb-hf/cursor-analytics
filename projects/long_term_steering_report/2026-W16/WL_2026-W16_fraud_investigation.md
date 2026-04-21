# Fraud Investigation: WL 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 93.28% → 92.95% (-0.35%)  
**Volume:** 14,308 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined slightly from 93.28% to 92.95% (-0.33pp) in W16, a change that is **not statistically significant** and remains within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL 8-Week Trend | FAR within historical range (92.70%-94.34%) | -0.33pp | ✅ |
| L1: Country Scan | No country exceeds ±2.5% threshold | Max: ER +1.28% | ✅ |
| L1: Channel Category | Referral underperforms vs Paid | -1.86% | ✅ |
| L2: CG Referral | FAR drop with elevated Dup Block | -4.60%, Dup Block +42.91% | ⚠️ |
| L2: KN Referral | Significant FAR decline, Dup Rate spike | -16.91%, Dup Rate +91.81% | ⚠️ |
| L2: ER Referral | FAR improved despite flag | +3.02% | ✅ |

**Key Findings:**
- **KN Referral channel shows severe degradation:** FAR dropped 16.91% (84.54% → 70.25%) with Duplicate Rate nearly doubling (+91.81%) and Dup Block Rate increasing 76.42% to 27.27%
- **CG Referral channel declining:** FAR fell 4.60% (83.92% → 80.06%) driven by Dup Rate increase (+24.19%) and Dup Block surge (+42.91% to 18.69%)
- **Paid channels remain stable across all countries:** Changes within ±0.5pp, indicating the overall WL decline is driven entirely by Referral channel performance
- **Overall volume decreased 5.5%** (15,143 → 14,308), with Referral channels seeing proportionally larger volume drops
- **PF Block Rate elevated in CG Paid:** Increased 60.34% (1.94% → 3.12%), though low absolute impact

**Action:** **Investigate** — The KN Referral channel requires immediate attention due to the 16.91% FAR decline and 91.81% Duplicate Rate spike, suggesting potential referral abuse or a single bad actor. Review specific referral sources in KN and CG for anomalous patterns.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 92.95% | 17.14% | 5.26% | 0.96% | 14,308 | -0.35% ← REPORTED CHANGE |
| 2026-W15 | 93.28% | 15.74% | 4.98% | 0.69% | 15,143 | +0.44% |
| 2026-W14 | 92.88% | 15.25% | 4.84% | 0.82% | 13,279 | +0.19% |
| 2026-W13 | 92.70% | 15.44% | 4.99% | 0.79% | 14,388 | -0.35% |
| 2026-W12 | 93.02% | 15.90% | 4.82% | 0.42% | 15,072 | -1.40% |
| 2026-W11 | 94.34% | 14.70% | 4.06% | 0.35% | 16,393 | +0.54% |
| 2026-W10 | 93.83% | 15.76% | 4.45% | 0.44% | 17,314 | +0.39% |
| 2026-W09 | 93.47% | 15.24% | 4.63% | 0.54% | 16,425 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| ER | 2026-W15 | 92.83% | - | 22.17% | - | 2,539 |  |
| ER | 2026-W16 | 94.02% | +1.28% | 22.92% | +3.38% | 2,408 |  |
| KN | 2026-W15 | 91.43% | - | 7.35% | - | 2,707 |  |
| KN | 2026-W16 | 90.66% | -0.84% | 9.08% | +23.56% | 2,323 |  |
| MR | 2026-W15 | 96.87% | - | 4.59% | - | 2,748 |  |
| MR | 2026-W16 | 96.19% | -0.70% | 5.52% | +20.29% | 2,230 |  |
| CK | 2026-W15 | 92.98% | - | 27.56% | - | 2,591 |  |
| CK | 2026-W16 | 92.37% | -0.65% | 28.31% | +2.71% | 2,413 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.33% | - | 14.11% | - | 12,767 |  |
| Paid | 2026-W16 | 96.16% | -0.18% | 15.40% | +9.11% | 12,091 |  |
| Referral | 2026-W15 | 76.89% | - | 24.45% | - | 2,376 |  |
| Referral | 2026-W16 | 75.46% | -1.86% | 26.61% | +8.83% | 2,217 |  |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 94.63% | - | 12.40% | - | 2.40% | - | 1.94% | - | 1,750 |  |
| Paid | 2026-W16 | 94.39% | -0.25% | 11.06% | -10.81% | 1.56% | -35.10% | 3.12% | +60.34% | 1,926 |  |
| Referral | 2026-W15 | 83.92% | - | 15.80% | - | 13.08% | - | 0.27% | - | 367 |  |
| Referral | 2026-W16 | 80.06% | -4.60% | 19.63% | +24.19% | 18.69% | +42.91% | 0.00% | -100.00% | 321 | ⚠️ |

**Analysis:** The WL-level FAR decline of 0.33pp is not significant and masks localized issues in the Referral channel, particularly in KN where FAR dropped 16.91% due to a near-doubling of duplicate submission rates. While the Paid channel (84% of volume) remains healthy across all countries, the Referral channel deterioration in KN and CG warrants investigation into potential referral fraud or quality issues with specific referral partners. No immediate escalation is required, but the KN Referral anomaly should be root-caused before W17 reporting.

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.66% | - | 21.28% | - | 2.27% | - | 0.48% | - | 2,068 |  |
| Paid | 2026-W16 | 97.16% | +0.51% | 22.52% | +5.85% | 1.69% | -25.46% | 0.70% | +44.26% | 2,007 |  |
| Referral | 2026-W15 | 76.01% | - | 26.11% | - | 22.93% | - | 0.42% | - | 471 |  |
| Referral | 2026-W16 | 78.30% | +3.02% | 24.94% | -4.51% | 21.45% | -6.47% | 0.00% | -100.00% | 401 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 92.00% | - | 6.64% | - | 5.72% | - | 0.60% | - | 2,500 |  |
| Paid | 2026-W16 | 91.78% | -0.24% | 7.90% | +19.00% | 6.86% | +19.88% | 0.36% | -39.45% | 2,202 |  |
| Referral | 2026-W15 | 84.54% | - | 15.94% | - | 15.46% | - | 0.00% | - | 207 |  |
| Referral | 2026-W16 | 70.25% | -16.91% | 30.58% | +91.81% | 27.27% | +76.42% | 1.65% | - | 121 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-21*
