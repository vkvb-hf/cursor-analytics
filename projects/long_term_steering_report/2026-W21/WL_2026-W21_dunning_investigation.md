# Dunning Investigation: WL 2026-W21

**Metric:** Dunning Ship Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 31.72% → 31.71% (-0.01pp)  
**Volume:** 7,741 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

**Overall:** Dunning Ship Rate remained essentially flat week-over-week, declining marginally from 31.72% to 31.71% (-0.01pp) as the portfolio transitioned from Payday to Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 89.82% → 89.49% | -0.4% | ✅ |
| Discount % | 16.58% → 15.74% | -5.1% | ✅ |
| PC2 | 38.42% → 38.15% | -0.7% | ✅ |
| Ship Rate | 31.72% → 31.71% | -0.0% | ✅ |

**Key Findings:**
- **Simpson's Paradox detected:** Most individual countries improved their Ship Rates (CK +7.6%, GN +13.2%, AO +0.6pp), yet the aggregate remained flat due to volume mix shifts
- **ER dragged performance:** ER saw Ship Rate decline by -7.9% (27.76% → 25.57%) despite stable Pre-Dunning AR and improved PC2 (+4.9%), with Discount % increasing (+2.8%) contrary to optimal direction
- **CK strong recovery:** CK improved Ship Rate by +7.6% driven primarily by a significant -27.4% reduction in Discount %, suggesting more selective/effective discounting strategy
- **Volume shift to low-performers:** ER (low SR tier) lost 12.7% volume while MR (0.43% SR) gained 7.0% and KN (15.91% SR) gained 9.3%, diluting aggregate performance
- **GN top performer:** Achieved +13.2% Ship Rate improvement with balanced metric movements (Discount -4.5%, PC2 +2.9%)

**Action:** Monitor – The flat aggregate masks healthy underlying country-level improvements; investigate ER's discount strategy as it moved contrary to expected behavior despite Post-Payday phase

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 8,048 | 31.72% | - | 89.82% | - | 16.58% | - | 38.42% | - |
| 2026-W21 | Post-Payday | 7,741 | 31.71% | →-0.0% | 89.49% | →-0.4% | 15.74% | ↓-5.1% | 38.15% | →-0.7% |

---

## L1: Country-Level Analysis

### CK (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 1,546 | 44.83% | - | 93.22% | - | 27.96% | - | 45.6% | - |
| 2026-W21 | Post-Payday | 1,495 | 48.23% | ↑+7.6% | 92.89% | →-0.4% | 20.29% | ↓-27.4% | 45.98% | →+0.8% |

**Analysis:** The Dunning Ship Rate stability at 31.71% during the Post-Payday transition masks meaningful country-level divergence, with CK and GN showing strong improvements (+7.6% and +13.2% respectively) offset by ER's -7.9% decline and unfavorable volume mix shifts toward lower-performing segments. The reduction in overall Discount % (-5.1%) aligns with Post-Payday best practices and contributed to individual country gains. Continued monitoring is recommended with specific attention to ER's counter-trend discount increase and the volume migration toward low Ship Rate tiers (MR, KN).

### ER (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 2,406 | 27.76% | - | 89.66% | - | 16.21% | - | 39.66% | - |
| 2026-W21 | Post-Payday | 2,100 | 25.57% | ↓-7.9% | 89.66% | →+0.0% | 16.67% | ↑+2.8% | 41.61% | ↑+4.9% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 402 | 34.08% | - | 95.55% | - | 20.67% | - | 49.02% | - |
| 2026-W21 | Post-Payday | 412 | 38.59% | ↑+13.2% | 95.18% | →-0.4% | 19.74% | ↓-4.5% | 50.46% | ↑+2.9% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]


---

## Decision Framework

**How Ship Rate relates to other metrics:**

| Metric | Relationship | If metric ↑ | If metric ↓ |
|--------|--------------|-------------|-------------|
| Pre-Dunning AR | Positive | Ship Rate ↑ | Ship Rate ↓ |
| Discount % | Negative | Ship Rate ↓ | Ship Rate ↑ |
| PC2 | Positive | Ship Rate ↑ | Ship Rate ↓ |

**Root Cause Derivation:**

| Country | Ship Rate | Pre-Dunning AR | Discount % | PC2 | Payday Phase | Root Cause |
|---------|-----------|----------------|------------|-----|--------------|------------|
| CK | ↑+7.6% | →-0.4% | ↓-27.4% | →+0.8% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| ER | ↓-7.9% | →+0.0% | ↑+2.8% | ↑+4.9% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↑+13.2% | →-0.4% | ↓-4.5% | ↑+2.9% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,406 | 27.76% | 2,100 | 25.57% | -12.7% | Low |
| CK | 1,546 | 44.83% | 1,495 | 48.23% | -3.3% | Medium |
| AO | 1,105 | 70.14% | 1,051 | 70.69% | -4.9% | High |
| MR | 1,079 | 0.00% | 1,155 | 0.43% | 7.0% | Low |
| CG | 803 | 21.42% | 755 | 22.12% | -6.0% | Low |
| KN | 707 | 15.28% | 773 | 15.91% | 9.3% | Low |
| GN | 402 | 34.08% | 412 | 38.59% | 2.5% | Medium |

---


---

*Report: 2026-05-26*
