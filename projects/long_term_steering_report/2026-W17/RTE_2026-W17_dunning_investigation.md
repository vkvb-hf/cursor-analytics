# Dunning Investigation: RTE 2026-W17

**Metric:** Dunning Ship Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 43.82% → 42.98% (-0.84pp)  
**Volume:** 20,285 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate declined from 43.82% to 42.98% (-0.84pp) in W17, coinciding with the transition from Payday to Post-Payday phase across 20,285 eligible orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.76% → 92.86% | +0.1% | ✅ |
| Discount % | 16.8% → 16.12% | -4.0% | ✅ |
| PC2 | 44.21% → 46.6% | +5.4% | ✅ |
| Ship Rate | 43.82% → 42.98% | -1.9% | ⚠️ |

**Key Findings:**
- **FJ drives the decline:** As the largest market (70% of volume), FJ's Ship Rate dropped -2.6% (42.67% → 41.55%) despite stable Pre-Dunning AR and improved PC2 (+2.8%)
- **TK experienced severe deterioration:** Ship Rate collapsed -43.7% (28.26% → 15.91%) on increased volume (+43.5%), suggesting potential quality degradation in new cohorts
- **TO showed strong improvement:** Ship Rate increased +24.9% driven by significant discount reduction (-30.5%) and PC2 improvement (+19.3%)
- **Payday Phase transition impact:** The shift from Payday to Post-Payday appears to be the primary driver, as supporting metrics (AR, Discount, PC2) all moved favorably yet Ship Rate still declined
- **No Simpson's Paradox detected:** Volume shifts were minimal in major markets (FJ -1.3%, YE -0.2%), ruling out mix shift as explanation

**Action:** **Monitor** - The decline aligns with expected Post-Payday seasonality. Supporting metrics are healthy. Watch TK closely given disproportionate degradation on small volume.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 20,571 | 43.82% | - | 92.76% | - | 16.8% | - | 44.21% | - |
| 2026-W17 | Post-Payday | 20,285 | 42.98% | →-1.9% | 92.86% | →+0.1% | 16.12% | ↓-4.0% | 46.6% | ↑+5.4% |

---

## L1: Country-Level Analysis

### FJ (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 14,411 | 42.67% | - | 93.79% | - | 16.69% | - | 46.82% | - |
| 2026-W17 | Post-Payday | 14,218 | 41.55% | ↓-2.6% | 93.81% | →+0.0% | 15.93% | ↓-4.6% | 48.15% | ↑+2.8% |

**Analysis:** The -0.84pp Ship Rate decline appears primarily driven by the Payday to Post-Payday phase transition rather than fundamental funnel deterioration, as Pre-Dunning AR remained stable (+0.1%), discounting decreased (-4.0%), and PC2 improved (+5.4%). FJ accounts for the majority of impact due to its volume dominance, while TK requires monitoring given its outsized -43.7% decline on expanding volume. If the decline persists beyond typical Post-Payday recovery windows, escalation for deeper cohort analysis in FJ and TK would be warranted.

### YE (Rank #2 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 3,265 | 61.29% | - | 87.83% | - | 15.1% | - | 40.23% | - |
| 2026-W17 | Post-Payday | 3,260 | 60.71% | →-0.9% | 88.42% | →+0.7% | 15.28% | →+1.2% | 49.25% | ↑+22.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TK (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 92 | 28.26% | - | 93.65% | - | 17.84% | - | 33.75% | - |
| 2026-W17 | Post-Payday | 132 | 15.91% | ↓-43.7% | 91.98% | →-1.8% | 17.57% | →-1.5% | 38.61% | ↑+14.4% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### TO (Rank #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W16 | Payday | 230 | 23.48% | - | 88.79% | - | 28.2% | - | 26.48% | - |
| 2026-W17 | Post-Payday | 249 | 29.32% | ↑+24.9% | 87.92% | →-1.0% | 19.6% | ↓-30.5% | 31.58% | ↑+19.3% |

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
| FJ | ↓-2.6% | →+0.0% | ↓-4.6% | ↑+2.8% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| YE | →-0.9% | →+0.7% | →+1.2% | ↑+22.4% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TK | ↓-43.7% | →-1.8% | →-1.5% | ↑+14.4% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |
| TO | ↑+24.9% | →-1.0% | ↓-30.5% | ↑+19.3% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| FJ | 14,411 | 42.67% | 14,218 | 41.55% | -1.3% | Medium |
| YE | 3,265 | 61.29% | 3,260 | 60.71% | -0.2% | High |
| CF | 2,261 | 30.38% | 2,043 | 29.81% | -9.6% | Medium |
| TO | 230 | 23.48% | 249 | 29.32% | 8.3% | Low |
| TZ | 144 | 29.17% | 182 | 32.97% | 26.4% | Low |
| TK | 92 | 28.26% | 132 | 15.91% | 43.5% | Low |
| TT | 85 | 38.82% | 103 | 44.66% | 21.2% | Medium |
| TV | 83 | 25.30% | 98 | 22.45% | 18.1% | Low |

---


---

*Report: 2026-04-28*
