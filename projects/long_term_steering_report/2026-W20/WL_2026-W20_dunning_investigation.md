# Dunning Investigation: WL 2026-W20

**Metric:** Dunning Ship Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 32.85% → 31.84% (-1.01pp)  
**Volume:** 8,075 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 1.01pp (32.85% → 31.84%) week-over-week despite transitioning into Payday phase, driven primarily by significant declines in CK and GN that offset gains in ER.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | Stable | +0.1% | ✅ |
| Discount % | Increased | +2.0% | ⚠️ |
| PC2 | Declined | -22.9% | ⚠️ |
| Ship Rate | Declined | -3.1% | ⚠️ |

**Key Findings:**
- **PC2 collapsed at cluster level:** PC2 dropped sharply from 50.98% to 39.31% (-22.9%), indicating significant payment conversion issues that directly impacted ship rate despite stable approval rates
- **CK drove largest negative contribution:** Despite being a high-performing market (44.89% SR), CK declined 7.5% with discount % spiking +11.7%, suggesting aggressive discounting failed to convert to shipments
- **ER showed counter-trend improvement:** ER improved ship rate by +15.3% (24.29% → 28.00%) during Payday phase with stable discounting (-0.7%), partially offsetting cluster decline
- **GN experienced steepest relative decline:** GN fell 12.3% (38.86% → 34.08%) despite strong approval rates (95.56%) and increased discounting (+9.2%), pointing to payment-side friction
- **Mix shift toward low-SR markets:** MR (+10.6%), CG (+10.9%), and KN (+15.9%) all grew in volume share while AO (highest SR at 70.10%) contracted by -5.5%

**Action:** Investigate — The severe PC2 decline (-22.9%) combined with increased discounting failing to improve conversion suggests a systemic payment processing issue that warrants immediate root cause analysis, particularly in CK and GN markets.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 7,727 | 32.85% | - | 89.79% | - | 16.26% | - | 50.98% | - |
| 2026-W20 | Payday | 8,075 | 31.84% | ↓-3.1% | 89.84% | →+0.1% | 16.59% | →+2.0% | 39.31% | ↓-22.9% |

---

## L1: Country-Level Analysis

### ER (Rank #1 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 2,355 | 24.29% | - | 89.33% | - | 16.35% | - | 43.69% | - |
| 2026-W20 | Payday | 2,414 | 28.00% | ↑+15.3% | 89.66% | →+0.4% | 16.24% | →-0.7% | 42.07% | ↓-3.7% |

**Analysis:** The 1.01pp decline in Dunning Ship Rate during W20 is primarily attributable to a dramatic collapse in PC2 conversion (-22.9%) at the cluster level, which overwhelmed modest gains from ER's Payday-driven improvement. The pattern of increased discounting (+2.0%) failing to improve ship rates—particularly evident in CK (+11.7% discount, -7.5% SR) and GN (+9.2% discount, -12.3% SR)—indicates the bottleneck lies in payment completion rather than offer attractiveness. Additionally, unfavorable mix shift toward low-performing markets (MR, CG, KN) amplified the aggregate decline, suggesting potential Simpson's Paradox effects that warrant deeper segmented analysis.

### CK (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 1,481 | 48.55% | - | 93.00% | - | 25.03% | - | 44.88% | - |
| 2026-W20 | Payday | 1,557 | 44.89% | ↓-7.5% | 93.22% | →+0.2% | 27.95% | ↑+11.7% | 46.61% | ↑+3.9% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W19 | Pre-Payday | 404 | 38.86% | - | 94.92% | - | 18.92% | - | 49.74% | - |
| 2026-W20 | Payday | 402 | 34.08% | ↓-12.3% | 95.56% | →+0.7% | 20.67% | ↑+9.2% | 50.93% | →+2.4% |

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
| ER | ↑+15.3% | →+0.4% | →-0.7% | ↓-3.7% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| CK | ↓-7.5% | →+0.2% | ↑+11.7% | ↑+3.9% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↓-12.3% | →+0.7% | ↑+9.2% | →+2.4% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,355 | 24.29% | 2,414 | 28.00% | 2.5% | Low |
| CK | 1,481 | 48.55% | 1,557 | 44.89% | 5.1% | Medium |
| AO | 1,172 | 70.05% | 1,107 | 70.10% | -5.5% | High |
| MR | 979 | 0.31% | 1,083 | 0.09% | 10.6% | Low |
| CG | 726 | 22.73% | 805 | 21.61% | 10.9% | Low |
| KN | 610 | 16.56% | 707 | 15.28% | 15.9% | Low |
| GN | 404 | 38.86% | 402 | 34.08% | -0.5% | Medium |

---


---

*Report: 2026-05-19*
