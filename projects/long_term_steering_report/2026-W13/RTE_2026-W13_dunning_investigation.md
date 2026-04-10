# Dunning Investigation: RTE 2026-W13

**Metric:** Dunning Ship Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 43.89% → 43.89% (+0.00pp)  
**Volume:** 21,143 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate remained flat at 43.89% week-over-week (0.00pp change), with volume increasing slightly from 20,396 to 21,143 eligible orders during the transition from Post-Payday to Mid-Cycle phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.65% → 93.38% | -0.27pp | ⚠️ |
| Discount % | 17.95% → 18.11% | +0.16pp | ✅ |
| PC2 | 43.41% → 43.31% | -0.10pp | ⚠️ |
| Ship Rate | 43.89% → 43.89% | +0.00pp | ✅ |

**Key Findings:**
- Pre-Dunning AR declined slightly by 0.27pp (93.65% → 93.38%), indicating marginally lower account readiness entering the dunning process
- YE (Yemen) saw the largest Ship Rate decline among high-volume countries, dropping 1.38pp (61.69% → 60.31%) despite being the highest-performing market
- Low-tier markets showed strong improvements: TK surged +16.33pp (8.33% → 24.66%), TV improved +11.44pp (13.76% → 25.20%), and TZ gained +7.79pp (22.15% → 29.94%)
- FJ (Fiji), the largest market by volume (14,680 orders), remained stable with only +0.07pp improvement (42.72% → 42.79%)
- CF (Central African Republic) volume declined 5.7% with Ship Rate dropping 0.80pp (31.83% → 31.03%)

**Action:** Monitor – The overall metric is stable with no significant degradation. Continue tracking YE performance given its high-tier status and recent decline, while observing if low-tier market improvements sustain.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W12 | Post-Payday | 20,396 | 43.89% | 93.65% | 17.95% | 43.41% |
| 2026-W13 | Mid-Cycle | 21,143 | 43.89% | 93.38% | 18.11% | 43.31% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 13,953 | 42.72% | 14,680 | 42.79% | 5.2% | Medium |
| YE | 3,472 | 61.69% | 3,525 | 60.31% | 1.5% | High |
| CF | 2,180 | 31.83% | 2,056 | 31.03% | -5.7% | Medium |
| TO | 295 | 19.66% | 326 | 25.15% | 10.5% | Low |
| TZ | 158 | 22.15% | 177 | 29.94% | 12.0% | Low |
| TK | 120 | 8.33% | 146 | 24.66% | 21.7% | Low |
| TV | 109 | 13.76% | 123 | 25.20% | 12.8% | Low |
| TT | 109 | 33.03% | 110 | 30.00% | 0.9% | Medium |

---


---

*Report: 2026-04-10*
