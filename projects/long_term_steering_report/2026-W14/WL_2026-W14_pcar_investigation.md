# PCAR Investigation: WL 2026-W14

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 97.07% → 97.03% (-0.04%)  
**Volume:** 11,373 orders

## Executive Summary

**Overall:** PCAR metric experienced a marginal decline of -0.04 percentage points (97.07% → 97.03%) in W14, representing a minor week-over-week decrease on a volume of 11,373 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Stable trend with recovery from W07 low (94.85%) | -0.04pp WoW | ✅ |
| Country Breakdown | AO exceeds ±2.5% threshold | -3.13pp | ⚠️ |
| Payment Method | Minor fluctuations within normal range | -0.37pp to +0.16pp | ✅ |
| Volume | Decreased from 13,604 to 11,373 orders | -16.4% volume drop | ⚠️ |

**Key Findings:**
- **AO country is the primary driver of concern:** AO showed a significant decline of -3.13pp (87.96% → 85.21%) with the highest volume (15,776 orders), exceeding the ±2.5% threshold
- **Volume reduction:** Order volume dropped notably from 13,604 (W13) to 11,373 (W14), a ~16% decrease week-over-week
- **Payment methods remain stable:** Apple Pay showed minor decline (-0.37pp), while Credit Card (+0.09pp) and PayPal (+0.16pp) improved slightly
- **Overall trend remains healthy:** Despite the -0.04pp dip, PCAR has recovered significantly from the W07 low of 94.85% and remains above 97%
- **GN secondary watch:** GN declined -1.25pp (93.5% → 92.33%) though still within acceptable threshold

**Action:** **Investigate** - Focus investigation on AO country to understand the -3.13pp decline. Monitor volume trends and assess if the 16% volume drop is seasonal or indicative of a larger issue.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.03% | 11,373 | -0.04% ← REPORTED CHANGE |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | +0.50% |
| 2026-W08 | 96.86% | 16,585 | +2.12% |
| 2026-W07 | 94.85% | 16,452 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 85.21% | 87.96% | -3.13% | 15,776 | ⚠️ |
| GN | 92.33% | 93.5% | -1.25% | 14,333 |  |
| ER | 89.23% | 89.92% | -0.77% | 67,730 |  |
| CK | 93.82% | 94.15% | -0.35% | 42,176 |  |
| KN | 88.21% | 87.61% | +0.68% | 11,048 |  |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Apple Pay | 96.65% | 97.0% | -0.37% | 3,461 |
| PaymentMethod | Others | 100.0% | 100.0% | +0.00% | 3 |
| PaymentMethod | Credit Card | 97.0% | 96.91% | +0.09% | 6,574 |
| PaymentMethod | Paypal | 98.13% | 97.97% | +0.16% | 1,335 |

---

*Report: 2026-04-09*
