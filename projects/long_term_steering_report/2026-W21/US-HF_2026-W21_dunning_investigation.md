# Dunning Investigation: US-HF 2026-W21

**Metric:** Dunning Ship Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 46.44% → 45.53% (-0.91pp)  
**Volume:** 12,995 eligible orders  
**Payday Phase:** Payday → Post-Payday

## Executive Summary

**Overall:** Dunning Ship Rate declined by 0.91pp (46.44% → 45.53%) in US-HF from W20 to W21, coinciding with the transition from Payday to Post-Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 92.92% → 92.71% | -0.21pp | ✅ Stable |
| Discount % | 14.35% → 13.86% | -0.49pp | ✅ Favorable (lower discounts) |
| PC2 | 50.41% → 50.54% | +0.13pp | ✅ Stable |
| Ship Rate | 46.44% → 45.53% | -0.91pp | ⚠️ Declined |

**Key Findings:**
- Ship Rate declined 2.0% despite favorable movement in Discount % (↓3.4%) which typically correlates with improved ship rates
- Pre-Dunning AR remained essentially stable (→-0.2%), ruling out upstream approval issues as a driver
- PC2 held steady (→+0.3%), indicating no significant change in payment completion behavior
- The decline aligns with the Payday → Post-Payday phase transition, suggesting cyclical consumer cash flow impact
- Volume increased slightly (+0.8%, +100 orders), with no evidence of Simpson's Paradox mix shift effects

**Action:** Monitor — The decline appears driven by expected Post-Payday cyclical effects rather than operational issues. Continue tracking into W22 to confirm recovery as the next payday approaches.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 12,895 | 46.44% | - | 92.92% | - | 14.35% | - | 50.41% | - |
| 2026-W21 | Post-Payday | 12,995 | 45.53% | →-2.0% | 92.71% | →-0.2% | 13.86% | ↓-3.4% | 50.54% | →+0.3% |

---

## L1: Country-Level Analysis

### US (Rank #1 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W20 | Payday | 12,895 | 46.44% | - | 92.92% | - | 14.35% | - | 50.41% | - |
| 2026-W21 | Post-Payday | 12,995 | 45.53% | →-2.0% | 92.71% | →-0.2% | 13.86% | ↓-3.4% | 50.54% | →+0.3% |

**Analysis:** The 0.91pp decline in US-HF Dunning Ship Rate is primarily attributable to the natural Payday → Post-Payday phase transition, as all controllable funnel metrics (Pre-Dunning AR, Discount %, PC2) remained stable or moved favorably. This pattern is consistent with expected consumer payment behavior during post-payday periods and does not indicate an underlying operational issue requiring immediate intervention.


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
| US | →-2.0% | →-0.2% | ↓-3.4% | →+0.3% | Payday → Post-Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| US | 12,895 | 46.44% | 12,995 | 45.53% | 0.8% | Medium |

---


---

*Report: 2026-05-26*
