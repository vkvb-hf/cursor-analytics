# Dunning Investigation: HF-NA 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 48.18% → 48.10% (-0.08pp)  
**Volume:** 18,193 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate for HF-NA remained essentially flat in 2026-W16, declining marginally by -0.08pp (48.18% → 48.10%) despite transitioning into Payday phase, with volume increasing by 10.5% to 18,193 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.18% → 93.11% | -0.07pp | ✅ |
| Discount % | 15.06% → 15.85% | +0.79pp | ⚠️ |
| PC2 | 51.03% → 51.97% | +0.94pp | ✅ |
| Ship Rate | 48.18% → 48.10% | -0.08pp | ✅ |

**Key Findings:**
- CA experienced a significant Ship Rate decline of -6.5% (52.98% → 49.55%) despite stable Pre-Dunning AR and improved PC2, making it the primary detractor from cluster performance
- US showed positive momentum with Ship Rate improving +2.1% (46.72% → 47.68%), partially offsetting CA's decline
- Discount % increased across both countries (CA: +2.8%, US: +6.6%), which typically correlates negatively with Ship Rate, yet US still improved—suggesting other positive factors at play
- Mix shift dynamics: US (lower SR tier) grew volume by 11.8% while high-performing CA grew only 6.5%, contributing to overall cluster stagnation
- The transition to Payday phase did not yield the expected uplift, particularly in CA where performance deteriorated significantly

**Action:** **Investigate** — CA's -6.5% Ship Rate decline warrants immediate root cause analysis. The disconnect between improving PC2 (+1.6%) and declining Ship Rate suggests potential issues with payment method availability, checkout friction, or segment-specific behavior changes during Payday.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 16,459 | 48.18% | - | 93.18% | - | 15.06% | - | 51.03% | - |
| 2026-W16 | Payday | 18,193 | 48.10% | →-0.2% | 93.11% | →-0.1% | 15.85% | ↑+5.2% | 51.97% | →+1.8% |

---

## L1: Country-Level Analysis

### CA (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 3,839 | 52.98% | - | 93.49% | - | 18.7% | - | 50.32% | - |
| 2026-W16 | Payday | 4,087 | 49.55% | ↓-6.5% | 93.58% | →+0.1% | 19.23% | ↑+2.8% | 51.12% | →+1.6% |

**Analysis:** The HF-NA cluster's flat week-over-week performance masks divergent country dynamics: CA's substantial -6.5% Ship Rate decline was largely offset by US's +2.1% improvement. CA's deterioration during what should be a favorable Payday phase—despite stable authorization rates and improved PC2—points to potential conversion barriers that require deeper investigation into payment funnel mechanics and customer segment behavior.

### US (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,620 | 46.72% | - | 93.09% | - | 13.95% | - | 51.24% | - |
| 2026-W16 | Payday | 14,106 | 47.68% | →+2.1% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.22% | →+1.9% |

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
| CA | ↓-6.5% | →+0.1% | ↑+2.8% | →+1.6% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| US | →+2.1% | →-0.1% | ↑+6.6% | →+1.9% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,620 | 46.72% | 14,106 | 47.68% | 11.8% | Medium |
| CA | 3,839 | 52.98% | 4,087 | 49.55% | 6.5% | High |

---


---

*Report: 2026-04-21*
