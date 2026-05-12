# AR Initial (LL0) Investigation: HF-NA 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 89.34% → 90.34% (+1.12%)  
**Volume:** 16,271 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-NA improved from 89.34% to 90.34% (+1.12%) in 2026-W19, representing a significant positive change on volume of 16,271 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +1.03% | ✅ |
| 2_PreDunningAR | Reported Metric | +1.13% | ✅ |
| 3_PostDunningAR | Post-Recovery | +1.15% | ✅ |
| 6_PaymentApprovalRate | Final Approval | +1.20% | ✅ |

**Key Findings:**
- Both countries showed improvement: US +1.23% (11,545 orders) and CA +1.15% (4,726 orders) — no country exceeded the ±2.5% threshold requiring deep-dive
- Credit Card payment method showed notable improvement at +2.58% (9,063 orders), flagged as a positive contributor
- ProcessOut provider improved significantly at +2.78% (8,653 orders), representing over half of total volume
- Unknown payment provider declined -6.75% (256 orders), but low volume limits overall impact
- The entire payment funnel improved consistently (+1.03% to +1.20% across all stages), indicating broad-based improvement rather than isolated recovery efforts

**Action:** Monitor — The improvement is significant and positive, driven by broad gains across countries, payment methods (especially Credit Card), and providers (especially ProcessOut). No anomalies require immediate investigation. Continue monitoring to confirm trend sustainability.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 90.34% | 16,271 | +1.12% ← REPORTED CHANGE |
| 2026-W18 | 89.34% | 15,832 | -0.90% |
| 2026-W17 | 90.15% | 18,081 | +0.86% |
| 2026-W16 | 89.38% | 18,050 | -0.63% |
| 2026-W15 | 89.95% | 16,004 | +0.21% |
| 2026-W14 | 89.76% | 17,053 | +0.63% |
| 2026-W13 | 89.2% | 16,141 | -0.55% |
| 2026-W12 | 89.69% | 21,085 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 92.91% | 91.85% | +1.15% | 4,726 |  |
| US | 89.29% | 88.21% | +1.23% | 11,545 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.83% | 94.72% | -2.00% | 669 |  |
| Apple Pay | 87.79% | 88.25% | -0.52% | 5,178 |  |
| Paypal | 90.45% | 90.51% | -0.07% | 1,361 |  |
| Credit Card | 91.6% | 89.3% | +2.58% | 9,063 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 83.2% | 89.23% | -6.75% | 256 | ⚠️ |
| Adyen | 94.91% | 96.82% | -1.97% | 570 |  |
| Braintree | 88.28% | 88.67% | -0.44% | 6,654 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 138 |  |
| ProcessOut | 91.69% | 89.21% | +2.78% | 8,653 | ⚠️ |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.16% | 88.25% | +1.03% | 16,271 | 15,832 |  |
| 2_PreDunningAR | 90.34% | 89.34% | +1.13% | 16,271 | 15,832 |  |
| 3_PostDunningAR | 90.54% | 89.51% | +1.15% | 16,271 | 15,832 |  |
| 6_PaymentApprovalRate | 90.7% | 89.63% | +1.20% | 16,271 | 15,832 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,934 | 11,545 | +5.6% | Stable |
| CA | Medium (>85%) | 4,898 | 4,726 | -3.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
