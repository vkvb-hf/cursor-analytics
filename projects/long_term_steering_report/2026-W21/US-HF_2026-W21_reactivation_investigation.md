# Reactivation Investigation: US-HF 2026-W21

**Metric:** Reactivation Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 90.2% → 88.72% (-1.64%)  
**Volume:** 12,683 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** US-HF Reactivation Rate declined from 90.2% to 88.72% (-1.64 pp) in 2026-W21, representing a significant week-over-week drop on volume of 12,683 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate at 8-week low | -1.64 pp | ⚠️ |
| L1: Country Breakdown | US threshold (±2.5%) | -1.64 pp | ✅ |
| L1: PaymentMethod | Apple Pay threshold | -3.84 pp | ⚠️ |
| L1: PaymentMethod | Others threshold | +33.33 pp | ⚠️ |
| Mix Shift | Volume stability | -14.2% | ✅ |

**Key Findings:**
- US Reactivation Rate of 88.72% is the lowest point in the 8-week trend window, breaking below the previously stable ~90% range
- Apple Pay shows the most significant decline at -3.84 pp (82.78% vs 86.08%), flagged as exceeding threshold with 1,957 orders affected
- Order volume dropped substantially from 14,787 to 12,683 (-14.2%), though mix shift impact remains stable within the Medium AR tier
- Credit Card (largest segment at 8,818 orders) declined -1.25 pp, contributing to overall metric pressure
- No individual country exceeded the ±2.5% threshold for deep-dive investigation

**Action:** Investigate – Focus on Apple Pay payment method performance; the -3.84 pp decline warrants review of payment processing issues or user experience changes specific to this payment channel.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 88.72% | 12,683 | -1.64% ← REPORTED CHANGE |
| 2026-W20 | 90.2% | 14,787 | -0.60% |
| 2026-W19 | 90.74% | 17,431 | +0.11% |
| 2026-W18 | 90.64% | 13,634 | +1.04% |
| 2026-W17 | 89.71% | 15,063 | -0.40% |
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | -0.57% |
| 2026-W14 | 90.99% | 14,736 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 88.72% | 90.20% | -1.64% | 12,683 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 82.78% | 86.08% | -3.84% | 1,957 | ⚠️ |
| Paypal | 91.56% | 93.15% | -1.71% | 1,907 |  |
| Credit Card | 89.42% | 90.55% | -1.25% | 8,818 |  |
| Others | 100.0% | 75.0% | +33.33% | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 14,787 | 12,683 | -14.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
