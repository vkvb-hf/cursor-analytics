# Dunning Investigation: HF-NA 2026-W18

**Metric:** Dunning Ship Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 48.71% → 48.35% (-0.36pp)  
**Volume:** 18,156 eligible orders  
**Payday Phase:** Post-Payday → Mid-Cycle

## Executive Summary

**Overall:** Dunning Ship Rate for HF-NA declined slightly from 48.71% to 48.35% (-0.36pp) in W18, driven primarily by a significant drop in CA performance that offset modest gains in US.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 93.02% → 93.09% | +0.07pp | ✅ |
| Discount % | 15.44% → 14.1% | -1.34pp | ✅ |
| PC2 | 49.7% → 51.55% | +1.85pp | ✅ |
| Ship Rate | 48.71% → 48.35% | -0.36pp | ⚠️ |

**Key Findings:**
- CA experienced a sharp Ship Rate decline of -6.1% (52.78% → 49.55%) despite favorable metric movements (AR +0.4%, Discount -10.3%), suggesting Payday Phase transition from Post-Payday to Mid-Cycle is the primary driver
- US showed resilience with Ship Rate improving +0.9% (47.58% → 48.00%), supported by strong PC2 increase (+4.6%) and reduced discounting (-8.3%)
- Mix shift detected: CA volume increased +4.2% while its Ship Rate dropped significantly, amplifying negative cluster impact (Simpson's Paradox risk)
- Discount reduction across both countries (-8.3% to -10.3%) did not translate to expected Ship Rate gains, indicating Payday Phase effects dominated
- Pre-Dunning AR remained stable across both countries, ruling out upstream acceptance issues

**Action:** Monitor - The decline is modest (-0.36pp) and primarily attributable to expected Mid-Cycle payday effects in CA. Track W19 to confirm recovery as payday cycle progresses.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 18,211 | 48.71% | - | 93.02% | - | 15.44% | - | 49.7% | - |
| 2026-W18 | Mid-Cycle | 18,156 | 48.35% | →-0.7% | 93.09% | →+0.1% | 14.1% | ↓-8.7% | 51.55% | ↑+3.7% |

---

## L1: Country-Level Analysis

### CA (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 3,971 | 52.78% | - | 93.13% | - | 18.3% | - | 50.71% | - |
| 2026-W18 | Mid-Cycle | 4,139 | 49.55% | ↓-6.1% | 93.48% | →+0.4% | 16.42% | ↓-10.3% | 51.0% | →+0.6% |

**Analysis:** The W18 Ship Rate decline of -0.36pp is primarily driven by CA's -6.1% drop coinciding with the transition from Post-Payday to Mid-Cycle phase, a predictable seasonal pattern affecting customer payment capacity. US performance remained stable with slight improvement, and underlying metrics (Pre-Dunning AR, PC2) showed positive trends, suggesting no systemic issues requiring immediate intervention. Continue monitoring through W19 to confirm expected recovery as the payday cycle advances.

### US (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W17 | Post-Payday | 14,240 | 47.58% | - | 92.99% | - | 14.64% | - | 49.42% | - |
| 2026-W18 | Mid-Cycle | 14,017 | 48.00% | →+0.9% | 92.98% | →-0.0% | 13.42% | ↓-8.3% | 51.71% | ↑+4.6% |

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
| CA | ↓-6.1% | →+0.4% | ↓-10.3% | →+0.6% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |
| US | →+0.9% | →-0.0% | ↓-8.3% | ↑+4.6% | Post-Payday → Mid-Cycle | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 14,240 | 47.58% | 14,017 | 48.00% | -1.6% | Medium |
| CA | 3,971 | 52.78% | 4,139 | 49.55% | 4.2% | High |

---


---

*Report: 2026-05-05*
