# Fraud Investigation: US-HF 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.28% → 89.67% (+0.44%)  
**Volume:** 20,489 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for US-HF improved slightly from 89.28% to 89.67% (+0.44 pp) in 2026-W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Overall | FAR +0.44 pp | 89.28% → 89.67% | ✅ |
| L1: Country (US) | No country >±2.5% threshold | +0.44 pp | ✅ |
| L1: Channel - Paid | FAR -1.56 pp | 95.25% → 93.77% | ✅ |
| L1: Channel - Referral | FAR +10.12 pp | 61.81% → 68.07% | ⚠️ |
| L2: US Referral - PF Block | PF Block -58.29% | 12.71% → 5.30% | ⚠️ |

**Key Findings:**
- Referral channel FAR increased significantly by +10.12 pp (61.81% → 68.07%), flagged as anomalous, driven primarily by a sharp decrease in PF Block rate (-58.29%, from 12.71% to 5.30%)
- Duplicate Rate increased across both channels: Paid (+6.32%) and Referral (+10.24%), with overall Dup Rate rising from 25.90% to 27.64%
- Duplicate Block rate increased substantially in Paid channel (+64.20%, from 2.90% to 4.75%) but FAR still declined slightly in that channel
- Overall volume increased modestly (+1.3%, 20,223 → 20,489 customers) week-over-week
- The +0.44 pp FAR improvement follows a -2.53 pp decline the prior week, suggesting normalization toward the 8-week average (~90%)

**Action:** Monitor – The overall change is not significant. However, continue monitoring the Referral channel's PF Block rate reduction to ensure the FAR improvement reflects legitimate approval increases rather than a policy or system change that may impact fraud prevention effectiveness.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.67% | 27.64% | 8.17% | 1.37% | 20,489 | +0.44% ← REPORTED CHANGE |
| 2026-W15 | 89.28% | 25.90% | 6.72% | 2.97% | 20,223 | -2.53% |
| 2026-W14 | 91.60% | 25.40% | 6.39% | 0.86% | 16,718 | +3.45% |
| 2026-W13 | 88.54% | 25.05% | 6.67% | 3.59% | 17,570 | -1.50% |
| 2026-W12 | 89.89% | 24.63% | 6.29% | 2.72% | 17,509 | +0.16% |
| 2026-W11 | 89.75% | 23.85% | 6.16% | 2.92% | 19,064 | -2.04% |
| 2026-W10 | 91.62% | 24.67% | 5.92% | 1.22% | 20,597 | -0.08% |
| 2026-W09 | 91.68% | 24.00% | 5.89% | 1.16% | 23,222 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W15 | 89.28% | - | 25.90% | - | 20,223 |  |
| US | 2026-W16 | 89.67% | +0.44% | 27.64% | +6.73% | 20,489 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.25% | - | 25.26% | - | 16,612 |  |
| Paid | 2026-W16 | 93.77% | -1.56% | 26.85% | +6.32% | 17,226 |  |
| Referral | 2026-W15 | 61.81% | - | 28.83% | - | 3,611 |  |
| Referral | 2026-W16 | 68.07% | +10.12% | 31.78% | +10.24% | 3,263 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.25% | - | 25.26% | - | 2.90% | - | 0.85% | - | 16,612 |  |
| Paid | 2026-W16 | 93.77% | -1.56% | 26.85% | +6.32% | 4.75% | +64.20% | 0.62% | -27.33% | 17,226 |  |
| Referral | 2026-W15 | 61.81% | - | 28.83% | - | 24.29% | - | 12.71% | - | 3,611 |  |
| Referral | 2026-W16 | 68.07% | +10.12% | 31.78% | +10.24% | 26.17% | +7.76% | 5.30% | -58.29% | 3,263 | ⚠️ |

**Analysis:** The 2026-W16 FAR increase of +0.44 pp for US-HF is within normal fluctuation and not statistically significant. The primary driver appears to be improved approval rates in the Referral channel due to a substantial reduction in PF Block rate (-58.29%), which warrants continued observation to confirm this change aligns with expected business outcomes and does not indicate a degradation in fraud controls.

---



*Report: 2026-04-22*
