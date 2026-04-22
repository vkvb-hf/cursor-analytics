# Dunning Investigation: HF-NA 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 48.19% → 48.03% (-0.16pp)  
**Volume:** 18,142 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined marginally from 48.19% to 48.03% (-0.16pp) week-over-week, with volume increasing by 10.3% (16,450 → 18,142 orders) during the transition from Pre-Payday to Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.18% → 93.11% | -0.07pp | ✅ |
| Discount % | 15.07% → 15.88% | +0.81pp | ⚠️ |
| PC2 | 51.84% → 51.98% | +0.14pp | ✅ |
| Ship Rate | 48.19% → 48.03% | -0.16pp | ⚠️ |

**Key Findings:**
- **CA drove the cluster decline:** CA Ship Rate dropped significantly (-6.7%, from 53.04% to 49.51%) despite stable Pre-Dunning AR (+0.1%) and PC2 (+0.1%), with increased Discount % (+3.4%) indicating higher-risk orders entering the funnel
- **US showed resilience:** US Ship Rate improved (+1.9%, from 46.72% to 47.61%) even with a notable Discount % increase (+6.6%), suggesting effective dunning execution
- **Mix shift partially masked US gains:** US volume grew faster (+11.6%) than CA (+5.9%), but since US has a lower baseline SR (47.61% vs 49.51%), the volume shift toward the lower-performing country dampened overall improvement
- **Payday phase transition impact:** The move from Pre-Payday to Payday typically improves payment likelihood, yet CA's sharp decline suggests country-specific factors overrode seasonal benefit
- **Root cause for CA:** The combination of stable operational metrics (AR, PC2) with increased discount penetration points to an unfavorable order mix entering dunning rather than execution issues

**Action:** **Investigate** – Deep dive into CA to understand the sharp Ship Rate decline; analyze whether specific customer segments, payment methods, or product categories drove the increased discount % and lower conversion.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 16,450 | 48.19% | - | 93.18% | - | 15.07% | - | 51.84% | - |
| 2026-W16 | Payday | 18,142 | 48.03% | →-0.3% | 93.11% | →-0.1% | 15.88% | ↑+5.4% | 51.98% | →+0.3% |

---

## L1: Country-Level Analysis

### CA (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 3,831 | 53.04% | - | 93.48% | - | 18.75% | - | 51.08% | - |
| 2026-W16 | Payday | 4,056 | 49.51% | ↓-6.7% | 93.58% | →+0.1% | 19.38% | ↑+3.4% | 51.12% | →+0.1% |

**Analysis:** The HF-NA cluster experienced a minor Ship Rate decline (-0.16pp) driven primarily by CA's significant underperformance (-6.7%), which offset gains in US (+1.9%). The increased Discount % across both countries during the Payday phase suggests a shift toward higher-risk orders, though US managed to convert effectively while CA did not. Immediate investigation into CA's dunning performance is recommended to identify segment-specific drivers before the trend compounds in subsequent weeks.

### US (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 12,619 | 46.72% | - | 93.09% | - | 13.95% | - | 52.07% | - |
| 2026-W16 | Payday | 14,086 | 47.61% | →+1.9% | 92.97% | →-0.1% | 14.87% | ↑+6.6% | 52.23% | →+0.3% |

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
| CA | ↓-6.7% | →+0.1% | ↑+3.4% | →+0.1% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| US | →+1.9% | →-0.1% | ↑+6.6% | →+0.3% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,619 | 46.72% | 14,086 | 47.61% | 11.6% | Medium |
| CA | 3,831 | 53.04% | 4,056 | 49.51% | 5.9% | High |

---


---

*Report: 2026-04-22*
