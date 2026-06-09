# Dunning Investigation: US-HF 2026-W23

**Metric:** Dunning Ship Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 44.15% → 45.50% (+1.35pp)  
**Volume:** 12,181 eligible orders  
**Payday Phase:** Mid-Cycle → Pre-Payday

## Executive Summary

**Overall:** Dunning Ship Rate improved from 44.15% to 45.50% (+1.35pp) week-over-week, driven by favorable payday phase timing and improved payment conversion metrics.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.41% → 92.70% | +0.3% | ✅ |
| Discount % | 16.95% → 16.02% | -5.5% | ✅ |
| PC2 | 48.67% → 51.46% | +5.7% | ✅ |
| Ship Rate | 44.15% → 45.50% | +3.1% | ✅ |

**Key Findings:**
- US Ship Rate improved by +3.1% (44.15% → 45.50%) as the payday phase shifted from Mid-Cycle to Pre-Payday
- PC2 (payment conversion) showed the strongest improvement at +5.7%, indicating better customer payment behavior ahead of payday
- Discount % decreased by -5.5% (16.95% → 16.02%), suggesting improved ship rates were achieved with less promotional reliance
- Pre-Dunning AR remained stable at ~92.7% (+0.3%), maintaining strong baseline authorization rates
- Volume decreased by -7.6% (13,188 → 12,181 orders), but this did not negatively impact conversion performance

**Action:** Monitor — All metrics trending positively with payday phase transition as the primary driver. Continue tracking into Post-Payday phase to confirm sustained improvement.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 13,188 | 44.15% | - | 92.41% | - | 16.95% | - | 48.67% | - |
| 2026-W23 | Pre-Payday | 12,181 | 45.50% | ↑+3.1% | 92.70% | →+0.3% | 16.02% | ↓-5.5% | 51.46% | ↑+5.7% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W22 | Mid-Cycle | 13,188 | 44.15% | - | 92.41% | - | 16.95% | - | 48.67% | - |
| 2026-W23 | Pre-Payday | 12,181 | 45.50% | ↑+3.1% | 92.70% | →+0.3% | 16.02% | ↓-5.5% | 51.46% | ↑+5.7% |

**Analysis:** The +1.35pp improvement in Dunning Ship Rate for US-HF during 2026-W23 is primarily attributable to the favorable payday phase shift (Mid-Cycle → Pre-Payday), which correlated with a +5.7% increase in PC2 and reduced discount dependency. This represents healthy organic improvement in payment conversion behavior, and no immediate intervention is required beyond continued monitoring through the payday cycle.


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
| US | ↑+3.1% | →+0.3% | ↓-5.5% | ↑+5.7% | Mid-Cycle → Pre-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 13,188 | 44.15% | 12,181 | 45.50% | -7.6% | Medium |

---


---

*Report: 2026-06-09*
