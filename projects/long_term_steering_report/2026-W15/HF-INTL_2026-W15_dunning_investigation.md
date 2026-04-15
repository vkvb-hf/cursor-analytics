# Dunning Investigation: HF-INTL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 70.88% → 65.63% (-5.25pp)  
**Volume:** 27,328 eligible orders  
**Payday Phase:** Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined significantly from 70.88% to 65.63% (-5.25pp) week-over-week, coinciding with a transition to Pre-Payday phase and a 25.5% reduction in eligible order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 94.31% → 95.28% | +0.97pp | ✅ |
| Discount % | 13.33% → 13.54% | +0.21pp | ✅ |
| PC2 | 42.48% → 45.95% | +3.47pp | ✅ |
| Ship Rate | 70.88% → 65.63% | -5.25pp | ⚠️ |

**Key Findings:**
- Volume decreased substantially across all major markets, with DK experiencing the largest drop (-54.7%) and BE also declining sharply (-38.1%)
- All top 10 countries except NO and NZ showed Ship Rate declines; GB fell -7.96pp (65.00% → 57.04%) and FR fell -8.32pp (69.98% → 61.66%)
- NO was the only market showing both volume growth (+34.7%) and Ship Rate improvement (+2.98pp to 82.20%)
- Pre-Dunning AR and PC2 metrics both improved, suggesting the conversion breakdown occurs downstream in the funnel
- The Pre-Payday phase timing correlates with reduced customer payment capacity across markets

**Action:** Investigate — The broad-based Ship Rate decline across 8 of 10 major markets, despite improved upstream metrics (Pre-Dunning AR, PC2), warrants deeper analysis into payment timing, customer cash flow constraints during Pre-Payday, and potential operational factors in GB and FR specifically.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W14 | Mid-Cycle | 36,662 | 70.88% | 94.31% | 13.33% | 42.48% |
| 2026-W15 | Pre-Payday | 27,328 | 65.63% | 95.28% | 13.54% | 45.95% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 8,724 | 65.00% | 6,304 | 57.04% | -27.7% | High |
| FR | 7,647 | 69.98% | 5,298 | 61.66% | -30.7% | High |
| AU | 5,850 | 66.10% | 5,023 | 64.74% | -14.1% | High |
| DE | 4,511 | 74.73% | 3,162 | 67.33% | -29.9% | High |
| BE | 3,221 | 90.50% | 1,995 | 87.57% | -38.1% | High |
| NZ | 1,302 | 61.29% | 1,132 | 69.52% | -13.1% | High |
| DK | 1,229 | 76.00% | 557 | 67.68% | -54.7% | High |
| IE | 1,149 | 65.88% | 878 | 61.85% | -23.6% | High |
| NO | 943 | 79.22% | 1,270 | 82.20% | 34.7% | High |
| SE | 808 | 71.66% | 690 | 61.16% | -14.6% | High |

---


---

*Report: 2026-04-15*
