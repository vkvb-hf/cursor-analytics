# Fraud Investigation: HF-NA 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.71% → 89.82% (+0.12%)  
**Volume:** 27,400 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) increased slightly from 89.71% to 89.82% (+0.12pp) in W16, a statistically non-significant change within normal weekly volatility.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within 8-week range (89.11%-91.58%) | +0.12pp | ✅ |
| L1: Country Scan | No country exceeds ±2.5% threshold | US +0.44%, CA -0.69% | ✅ |
| L1: Channel Category Scan | Referral channel exceeds threshold | +5.77% | ⚠️ |
| L2: CA Deep-Dive | CA Referral FAR declined, PF Block spiked | FAR -4.31%, PF Block +42.70% | ⚠️ |
| L2: US Deep-Dive | US Referral FAR improved significantly | FAR +10.12%, PF Block -58.29% | ⚠️ |

**Key Findings:**
- Duplicate Rate increased across all segments, rising from 26.46% to 28.10% (+1.64pp) at the regional level, with US Referral showing +10.24% increase
- US Referral channel showed significant FAR improvement (+10.12%) driven by a sharp decrease in PF Block rate (-58.29%), suggesting a policy or threshold change
- CA Referral channel moved in the opposite direction with FAR declining -4.31% and PF Block rate spiking +42.70%, indicating divergent fraud controls between countries
- US Paid channel experienced a substantial increase in Duplicate Block rate (+64.20%), from 2.90% to 4.75%, partially offsetting FAR gains
- Overall volume remained stable at 27,400 customers (-1.0% vs prior week)

**Action:** Monitor - The regional FAR change is not significant, but the opposing trends in US and CA Referral channels warrant continued observation. If US Referral's improved FAR correlates with increased fraud losses or CA's PF Block spike persists, escalate for policy review.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.82% | 28.10% | 7.72% | 1.60% | 27,400 | +0.12% ← REPORTED CHANGE |
| 2026-W15 | 89.71% | 26.46% | 6.40% | 2.73% | 27,682 | -1.40% |
| 2026-W14 | 90.98% | 25.98% | 6.40% | 1.36% | 23,595 | +2.10% |
| 2026-W13 | 89.11% | 25.95% | 6.22% | 3.32% | 24,576 | -1.35% |
| 2026-W12 | 90.33% | 25.53% | 6.01% | 2.49% | 24,830 | +0.07% |
| 2026-W11 | 90.26% | 24.95% | 5.88% | 2.65% | 26,801 | -1.38% |
| 2026-W10 | 91.52% | 25.45% | 5.83% | 1.39% | 27,713 | -0.06% |
| 2026-W09 | 91.58% | 24.86% | 5.79% | 1.26% | 30,551 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W15 | 89.28% | - | 25.90% | - | 20,223 |  |
| US | 2026-W16 | 89.67% | +0.44% | 27.64% | +6.73% | 20,489 |  |
| CA | 2026-W15 | 90.87% | - | 28.01% | - | 7,459 |  |
| CA | 2026-W16 | 90.25% | -0.69% | 29.47% | +5.24% | 6,911 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.49% | - | 25.45% | - | 22,691 |  |
| Paid | 2026-W16 | 94.44% | -1.10% | 27.00% | +6.08% | 22,769 |  |
| Referral | 2026-W15 | 63.43% | - | 31.08% | - | 4,991 |  |
| Referral | 2026-W16 | 67.09% | +5.77% | 33.53% | +7.91% | 4,631 | ⚠️ |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.13% | - | 25.97% | - | 0.61% | - | 1.89% | - | 6,079 |  |
| Paid | 2026-W16 | 96.54% | +0.42% | 27.44% | +5.64% | 0.72% | +18.56% | 1.82% | -3.68% | 5,543 |  |
| Referral | 2026-W15 | 67.68% | - | 36.96% | - | 27.32% | - | 2.97% | - | 1,380 |  |
| Referral | 2026-W16 | 64.77% | -4.31% | 37.72% | +2.06% | 29.46% | +7.83% | 4.24% | +42.70% | 1,368 | ⚠️ |

**Analysis:** The W16 FAR increase of +0.12pp is within normal operating variance and does not indicate a systemic issue at the regional level. However, the Referral channel shows notable divergence between US (+10.12% FAR improvement) and CA (-4.31% FAR decline), driven by significant swings in PF Block rates that suggest potential policy inconsistencies or model behavior differences between countries. Continued monitoring of Referral channel performance and duplicate rate trends is recommended for W17.

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.25% | - | 25.26% | - | 2.90% | - | 0.85% | - | 16,612 |  |
| Paid | 2026-W16 | 93.77% | -1.56% | 26.85% | +6.32% | 4.75% | +64.20% | 0.62% | -27.33% | 17,226 |  |
| Referral | 2026-W15 | 61.81% | - | 28.83% | - | 24.29% | - | 12.71% | - | 3,611 |  |
| Referral | 2026-W16 | 68.07% | +10.12% | 31.78% | +10.24% | 26.17% | +7.76% | 5.30% | -58.29% | 3,263 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-22*
