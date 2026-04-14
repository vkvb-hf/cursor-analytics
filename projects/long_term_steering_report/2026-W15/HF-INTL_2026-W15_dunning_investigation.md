# Dunning Investigation: HF-INTL 2026-W15

**Metric:** Dunning Ship Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 70.88% → 65.77% (-5.11pp)  
**Volume:** 27,443 eligible orders  
**Payday Phase:** Pre-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined significantly from 70.88% to 65.77% (-5.11pp) week-over-week, coinciding with a transition from Mid-Cycle to Pre-Payday phase and a 25% reduction in eligible order volume (36,664 → 27,443).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 94.31% → 95.28% | +0.97pp | ✅ |
| Discount % | 13.33% → 13.52% | +0.19pp | ✅ |
| PC2 | 42.48% → 45.94% | +3.46pp | ⚠️ |
| Ship Rate | 70.88% → 65.77% | -5.11pp | ⚠️ |

**Key Findings:**
- All 10 countries experienced volume declines except NO, which grew 35.9% and improved Ship Rate by +3.15pp (79.22% → 82.37%)
- DK saw the largest volume drop (-54.5%) with Ship Rate declining -8.20pp (76.00% → 67.80%)
- GB and FR, the two highest-volume markets, both declined sharply: GB -7.85pp (65.01% → 57.16%) and FR -7.96pp (69.98% → 62.02%)
- Pre-Payday timing correlates with depressed performance across most markets despite stable Pre-Dunning AR and Discount rates
- PC2 increased +3.46pp, suggesting more orders required a second payment collection attempt

**Action:** Investigate — The broad-based decline across major markets (GB, FR, DE) warrants deeper analysis into Pre-Payday consumer behavior patterns and PC2 failure reasons.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W14 | Mid-Cycle | 36,664 | 70.88% | 94.31% | 13.33% | 42.48% |
| 2026-W15 | Pre-Payday | 27,443 | 65.77% | 95.28% | 13.52% | 45.94% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| GB | 8,725 | 65.01% | 6,323 | 57.16% | -27.5% | High |
| FR | 7,647 | 69.98% | 5,350 | 62.02% | -30.0% | High |
| AU | 5,850 | 66.10% | 5,023 | 64.74% | -14.1% | High |
| DE | 4,512 | 74.73% | 3,167 | 67.38% | -29.8% | High |
| BE | 3,221 | 90.50% | 2,003 | 87.62% | -37.8% | High |
| NZ | 1,302 | 61.29% | 1,133 | 69.55% | -13.0% | High |
| DK | 1,229 | 76.00% | 559 | 67.80% | -54.5% | High |
| IE | 1,149 | 65.88% | 885 | 62.15% | -23.0% | High |
| NO | 943 | 79.22% | 1,282 | 82.37% | 35.9% | High |
| SE | 808 | 71.66% | 696 | 61.49% | -13.9% | High |

---


---

*Report: 2026-04-14*
