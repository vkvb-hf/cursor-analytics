# Reactivation Investigation: HF-NA 2026-W22

**Metric:** Reactivation Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 89.43% → 90.67% (+1.39%)  
**Volume:** 18,981 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate improved significantly from 89.43% to 90.67% (+1.24 pp) in W22, representing a positive recovery after the prior week's decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.41%-90.67%) | +1.24 pp | ✅ |
| L1: Country Breakdown | No countries exceed ±2.5% threshold | US +1.39%, CA +0.92% | ✅ |
| L1: Payment Method | "Others" flagged but volume=1 | -100.00% | ⚠️ |
| L1: Payment Provider | No data available | N/A | ✅ |
| Mix Shift Analysis | Both countries stable impact | CA +33.4% vol growth | ✅ |

**Key Findings:**
- Both US (+1.39%) and CA (+0.92%) contributed positively to the overall improvement, with US driving the majority of volume (13,381 orders)
- CA experienced significant volume growth (+33.4% from 4,198 to 5,600 orders) while maintaining a higher reactivation rate (92.41%)
- Credit Card payments showed the strongest improvement (+1.63%) with the highest volume (13,386 orders)
- The "Others" payment method flag is a false positive with only 1 order affected
- Current W22 rate (90.67%) represents the highest point in the 8-week trend period

**Action:** Monitor — The improvement reflects normal fluctuation within historical range, with no countries exceeding threshold for deep-dive investigation.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 90.67% | 18,981 | +1.39% ← REPORTED CHANGE |
| 2026-W21 | 89.43% | 16,881 | -0.90% |
| 2026-W20 | 90.24% | 18,775 | -0.46% |
| 2026-W19 | 90.66% | 22,007 | +0.20% |
| 2026-W18 | 90.48% | 19,213 | +0.14% |
| 2026-W17 | 90.35% | 20,799 | +1.05% |
| 2026-W16 | 89.41% | 23,973 | -0.92% |
| 2026-W15 | 90.24% | 26,178 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 92.41% | 91.57% | +0.92% | 5,600 |  |
| US | 89.95% | 88.72% | +1.39% | 13,381 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 0.0% | 100.0% | -100.00% | 1 | ⚠️ |
| Paypal | 93.08% | 92.56% | +0.57% | 2,848 |  |
| Apple Pay | 85.94% | 85.14% | +0.95% | 2,746 |  |
| Credit Card | 91.14% | 89.68% | +1.63% | 13,386 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 12,683 | 13,381 | +5.5% | Stable |
| CA | Medium (>85%) | 4,198 | 5,600 | +33.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
