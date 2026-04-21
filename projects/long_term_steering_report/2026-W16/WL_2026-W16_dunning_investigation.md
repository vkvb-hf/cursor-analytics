# Dunning Investigation: WL 2026-W16

**Metric:** Dunning Ship Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 31.08% → 31.89% (+0.81pp)  
**Volume:** 8,332 eligible orders  
**Payday Phase:** Pre-Payday → Payday

## Executive Summary

## Executive Summary

**Overall:** Dunning Ship Rate improved from 31.08% to 31.89% (+0.81pp, +2.6% relative) in W16, driven primarily by strong gains in AO and GN that offset a decline in CK, during the transition from Pre-Payday to Payday phase.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 90.00% → 89.88% | -0.1% | ✅ Stable |
| Discount % | 17.93% → 18.09% | +0.9% | ✅ Stable |
| PC2 | 51.36% → 40.27% | -21.6% | ⚠️ Significant Drop |
| Ship Rate | 31.08% → 31.89% | +2.6% | ✅ Improved |

**Key Findings:**
- **GN** showed the strongest relative improvement (+27.9% Ship Rate) with stable Pre-Dunning AR (+0.9%) and reduced discounting (-4.7%), suggesting improved customer payment behavior during Payday
- **AO** delivered solid gains (+6.4% Ship Rate) driven by a significant PC2 increase (+38.1%) and reduced discounting (-16.1%), indicating effective dunning optimization
- **CK** declined (-6.4% Ship Rate) despite being the #1 contributor by volume, with discount rates increasing significantly (+15.2%) suggesting aggressive discounting failed to convert
- **Cluster-level PC2 dropped sharply (-21.6%)** yet overall Ship Rate still improved, indicating mix shift effects—higher-performing countries (AO, GN) maintained stronger conversion
- **Volume increased 8.1%** (7,705 → 8,332) with notable growth in CK (+15.9%) and KN (+21.5%), though KN remains a low-tier performer

**Action:** **Monitor** – The overall improvement is positive and aligns with expected Payday phase benefits. Continue tracking CK's elevated discount rates and declining Ship Rate; if CK deterioration persists into W17, escalate for discount strategy review.

---

---

## L0: Cluster-Level Metrics

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 7,705 | 31.08% | - | 90.00% | - | 17.93% | - | 51.36% | - |
| 2026-W16 | Payday | 8,332 | 31.89% | ↑+2.6% | 89.88% | →-0.1% | 18.09% | →+0.9% | 40.27% | ↓-21.6% |

---

## L1: Country-Level Analysis

### CK (Rank #1 by Contribution)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 1,438 | 47.08% | - | 93.91% | - | 25.78% | - | 49.26% | - |
| 2026-W16 | Payday | 1,667 | 44.09% | ↓-6.4% | 93.32% | →-0.6% | 29.69% | ↑+15.2% | 47.35% | ↓-3.9% |

**Analysis:** The +0.81pp improvement in Dunning Ship Rate reflects healthy Payday-phase performance, with AO and GN demonstrating that reduced discounting paired with stable approval rates can drive meaningful conversion gains. However, CK's countertrend of increased discounting without corresponding Ship Rate improvement warrants close monitoring. The significant cluster-level PC2 decline (-21.6%) did not materially impact overall outcomes, suggesting the metric mix favored higher-converting segments this week.

### AO (Rank #2 by Contribution | #2 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 1,109 | 66.37% | - | 87.06% | - | 17.22% | - | 31.81% | - |
| 2026-W16 | Payday | 1,134 | 70.63% | ↑+6.4% | 87.79% | →+0.8% | 14.45% | ↓-16.1% | 43.94% | ↑+38.1% |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

### GN (Rank #3 by Contribution | #1 by Change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
|------|--------------|--------|-----------|------|----------------|------|------------|--------|-----|-------|
| 2026-W15 | Pre-Payday | 495 | 28.89% | - | 93.32% | - | 23.95% | - | 51.21% | - |
| 2026-W16 | Payday | 509 | 36.94% | ↑+27.9% | 94.19% | →+0.9% | 22.83% | ↓-4.7% | 50.68% | →-1.0% |

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
| CK | ↓-6.4% | →-0.6% | ↑+15.2% | ↓-3.9% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| AO | ↑+6.4% | →+0.8% | ↓-16.1% | ↑+38.1% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |
| GN | ↑+27.9% | →+0.9% | ↓-4.7% | →-1.0% | Pre-Payday → Payday | [AI_SUMMARY_PLACEHOLDER] |

---

## Mix Shift Analysis (Simpson's Paradox Detection)

| Country | Prev Volume | Prev SR | Curr Volume | Curr SR | Volume Δ % | SR Tier |
|---------|-------------|---------|-------------|---------|------------|---------|
| ER | 2,345 | 24.18% | 2,522 | 25.10% | 7.5% | Low |
| CK | 1,438 | 47.08% | 1,667 | 44.09% | 15.9% | Medium |
| AO | 1,109 | 66.37% | 1,134 | 70.63% | 2.3% | High |
| MR | 1,061 | 0.19% | 1,120 | 0.36% | 5.6% | Low |
| CG | 732 | 23.63% | 742 | 24.39% | 1.4% | Low |
| KN | 525 | 18.48% | 638 | 18.03% | 21.5% | Low |
| GN | 495 | 28.89% | 509 | 36.94% | 2.8% | Low |

---


---

*Report: 2026-04-21*
