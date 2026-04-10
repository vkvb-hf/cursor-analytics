# Dunning Investigation: US-HF 2026-W13

**Metric:** Dunning Ship Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 47.68% → 45.08% (-2.60pp)  
**Volume:** 13,814 eligible orders  
**Payday Phase:** Mid-Cycle

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 47.68% to 45.08% (-2.60pp) week-over-week during the Mid-Cycle payday phase, with volume remaining stable at 13,814 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.80% → 92.85% | +0.05pp | ✅ |
| Discount % | 15.17% → 16.31% | +1.14pp | ⚠️ |
| PC2 | 50.88% → 51.11% | +0.23pp | ✅ |
| Ship Rate | 47.68% → 45.08% | -2.60pp | ⚠️ |

**Key Findings:**
- Ship Rate declined -2.60pp despite stable Pre-Dunning Approval Rate (92.85%) and slight PC2 improvement (+0.23pp)
- Discount percentage increased by +1.14pp (15.17% → 16.31%), indicating more aggressive discounting was required but failed to maintain ship rates
- Volume remained essentially flat (-0.1% change, 13,822 → 13,814 orders), ruling out volume-driven mix shift
- Payday phase shifted from Post-Payday to Mid-Cycle, which typically correlates with reduced customer liquidity
- No Simpson's Paradox detected—US is the only country and shows true performance decline

**Action:** Investigate — The -2.60pp decline during Mid-Cycle warrants deeper analysis into payment failure reasons and customer payment behavior patterns, particularly given that increased discounting did not offset the decline.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Pre-Dunning AR | Discount % | PC2 |
|------|--------------|--------|-----------|----------------|------------|-----|
| 2026-W12 | Post-Payday | 13,822 | 47.68% | 92.80% | 15.17% | 50.88% |
| 2026-W13 | Mid-Cycle | 13,814 | 45.08% | 92.85% | 16.31% | 51.11% |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,822 | 47.68% | 13,814 | 45.08% | -0.1% | Medium |

---


---

*Report: 2026-04-10*
