# Steering Report - 2026-W17 (v3)

**Week:** 2026-W17  
**Generated:** 2026-04-27 14:44

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 96.54% to 95.92% (↓0.65%, not sig., vol: 702.0)
- **HF-NA**: 93.86% to 93.94% (↑0.09%, not sig., vol: 18.6)
- **HF-INTL**: 97.13% to 95.74% (↓1.43%, not sig., vol: 487.7)
- **US-HF**: 92.75% to 92.67% (↓0.08%, not sig., vol: 12.9)
- **RTE**: 97.20% to 96.76% (↓0.46%, not sig., vol: 194.0)
- **WL**: 97.59% to 96.82% (↓0.78%, not sig., vol: 85.7)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: BE (↓20%)
[2.5% - 19%]
  - HF-INTL: NL (↓11%), SE (↓9%), CH (↑6%)
  - RTE: TT (↓18%), TV (↓10%), TZ (↓3%)
**Dimensions:**
[20% - 49%]
  - RTE: PM Others (↓21%)
[2.5% - 19%]
  - HF-INTL: PM Others (↓17%)
  - HF-NA: PM Others (↑4%), FinalTokenType false (↑4%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Payment Checkout Approval Rate declined across most clusters in 2026-W17, with the most significant drop in HF-INTL (-1.43pp to 95.74%), the only statistically significant change this week. Adyen processing of local European payment methods (BcmcMobile, iDEAL, Klarna) in BE, NL, and SE requires immediate investigation as the common root cause across multiple markets.

### Cluster Highlights

- **US-HF:** Stable at 92.67% (-0.08pp), a non-significant decline within normal operating variance with no dimensions exceeding thresholds.
- **HF-INTL:** Declined significantly by -1.43pp to 95.74%, driven by Adyen-processed local payment methods failing in BE (-20.40pp), NL (-10.95pp), and SE (-9.26pp).
- **WL:** Declined by -0.79pp to 96.82%, a non-significant change with no countries or payment methods exceeding investigation thresholds.
- **HF-NA:** Improved marginally by +0.08pp to 93.94%, a non-significant change with stable performance across US and CA.
- **RTE:** Declined by -0.44pp to 96.76%, with TT (-18.17pp) and TV (-10.47pp) showing IDeal and Klarna degradation via Adyen, though low volumes (3.8% of total) limit overall impact.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 36.83% to 34.18% (↓7.17%, not sig., vol: 14.4K)
- **HF-NA**: 27.46% to 27.19% (↓1.01%, not sig., vol: 547.1)
- **HF-INTL**: 37.03% to 36.03% (↓2.69%, not sig., vol: 1.7K)
- **US-HF**: 25.73% to 24.93% (↓3.09%, not sig., vol: 1.3K)
- **RTE**: 48.83% to 40.05% (↓17.98%, not sig., vol: 10.1K)
- **WL**: 35.78% to 32.03% (↓10.49%, not sig., vol: 3.0K)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - WL: CG (↓27%), ER (↓21%), GN (↓22%)
  - RTE: TT (↓40%), TZ (↓29%), TK (↓25%)
[5.0% - 19%]
  - RTE: FJ (↓17%), CF (↓18%), YE (↓15%), TO (↓15%), TV (↓19%)
  - HF-INTL: GB (↑5%), FR (↓7%), DE (↓6%), NL (↓16%), IE (↑10%)
  - WL: KN (↑9%), CK (↓16%), AO (↓11%)

### Overall Summary

Payment Conversion Rate (Checkout) declined globally across all clusters in 2026-W17, with declines ranging from -0.29pp (HF-NA) to -8.79pp (RTE). The most significant concern is a consistent and severe drop at the Select Payment Method funnel step across all clusters, suggesting a potential systemic UI/UX issue or technical degradation affecting users' ability to initiate checkout.

### Cluster Highlights

- **US-HF:** PCR declined by -0.79pp (25.83% → 25.04%), primarily driven by a -1.42pp drop at Select Payment Method and a severe -7.43pp decline in backend Checkout Attempt rate, indicating significant top-of-funnel friction.
- **HF-INTL:** PCR declined by -1.00pp (37.09% → 36.09%), with NL experiencing the most severe degradation (-6.44pp) driven by a -9.26pp drop at Select Payment Method.
- **WL:** PCR declined by -3.78pp (35.83% → 32.05%), with Select Payment Method (-3.27pp) and Click Submit Form (-2.31pp) as the primary bottlenecks, most severely impacting CG (-14.37pp at payment selection).
- **HF-NA:** PCR declined modestly by -0.29pp (27.55% → 27.26%), driven by US Select Payment Method degradation (-1.42pp) while CA showed improvement (+1.36pp).
- **RTE:** PCR declined severely by -8.79pp (48.92% → 40.13%), with Select Payment Method dropping -9.27pp across all countries, most notably TT (-20.35pp at payment selection).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 34.74% to 33.48% (↓3.63%, not sig., vol: 11.9K)
- **HF-NA**: 29.09% to 29.21% (↑0.42%, not sig., vol: 282.6)
- **HF-INTL**: 40.09% to 39.12% (↓2.42%, not sig., vol: 2.2K)
- **US-HF**: 27.37% to 27.06% (↓1.13%, not sig., vol: 580.2)
- **RTE**: 35.87% to 33.10% (↓7.71%, not sig., vol: 9.7K)
- **WL**: 29.47% to 29.36% (↓0.37%, not sig., vol: 159.2)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TT (↓23%)
[5.0% - 19%]
  - RTE: FJ (↓8%), TZ (↓13%), TK (↓18%), TO (↓7%), TV (↓9%)
  - HF-INTL: FR (↓7%), IE (↑15%), NL (↓10%), NZ (↓10%), BE (↓6%)
  - WL: KN (↑10%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 90.01% to 89.43% (↓0.65%, not sig., vol: 576.2)
- **HF-NA**: 89.41% to 90.35% (↑1.04%, not sig., vol: 216.9)
- **HF-INTL**: 91.23% to 90.74% (↓0.53%, not sig., vol: 215.8)
- **US-HF**: 90.07% to 89.71% (↓0.40%, not sig., vol: 59.8)
- **RTE**: 89.16% to 87.33% (↓2.05%, not sig., vol: 396.4)
- **WL**: 86.81% to 85.35% (↓1.69%, not sig., vol: 132.1)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-NA: CA (↑6%)
  - RTE: YE (↓13%)
  - WL: GN (↓6%), CG (↓3%), MR (↑4%), AO (↓3%)
  - HF-INTL: NO (↓3%)
**Dimensions:**
[20% - 49%]
  - RTE: PM Others (↓24%)
[2.5% - 19%]
  - RTE: PM Apple Pay (↓10%)
  - WL: PM Apple Pay (↓5%)
**Low Volume (denom < 50):** 5 segments excluded

### Overall Summary

Reactivation Rate declined across most clusters in 2026-W17, with WL (-1.68%) and RTE (-2.05%) showing statistically significant drops while HF-NA (+1.05%) was the only cluster to improve significantly. The most critical concern is RTE's YE market, where a 351.6% volume surge coincided with a 13.10pp rate collapse driven by "Expired, Invalid, Closed Card" declines and degraded Credit Card performance.

### Cluster Highlights

- **US-HF:** Declined slightly from 90.07% to 89.71% (-0.36pp), a non-significant change with PayPal showing the largest rate drop (-1.49%) amid a 20.3% volume contraction.
- **HF-INTL:** Declined non-significantly from 91.23% to 90.74% (-0.54%), with low-volume LU (-8.33%) and NO (-3.16%) exceeding thresholds due to Credit Card and PayPal issues respectively.
- **WL:** Declined significantly from 86.81% to 85.35% (-1.68%), driven by Credit Card degradation in GN (-7.90%) and AO (-5.96%) with increased "Expired, Invalid, Closed Card" declines.
- **HF-NA:** Improved significantly from 89.41% to 90.35% (+1.05pp), driven by CA's Credit Card reactivation surge (+7.29pp) and reduced fraud-related declines.
- **RTE:** Declined significantly from 89.16% to 87.33% (-2.05%), primarily caused by YE's volume surge (+351.6%) paired with severe rate collapse (-13.10pp) across Credit Card (-15.34%) and Others (-24.65%) payment methods.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.31% to 92.59% (↑0.30%, not sig., vol: 377.4)
- **HF-NA**: 89.71% to 90.84% (↑1.25%, not sig., vol: 300.4)
- **HF-INTL**: 91.77% to 92.23% (↑0.50%, not sig., vol: 211.8)
- **US-HF**: 89.60% to 91.44% (↑2.05%, not sig., vol: 355.5)
- **RTE**: 94.25% to 94.05% (↓0.21%, not sig., vol: 96.0)
- **WL**: 92.72% to 91.88% (↓0.90%, not sig., vol: 128.2)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-INTL: BE (↑5%)
  - RTE: TK (↓6%)
**Dimensions:**
[+50%]
  - WL: PM Credit Card (↓100%)
[20% - 49%]
  - RTE: PM Unknown (↑33%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Fraud Approval Rate performance was mixed across clusters in 2026-W17, with US-HF and HF-NA showing significant improvements (+1.84pp and +1.13pp respectively) while WL declined (-0.84pp) and other clusters remained stable. The most significant concern is the deteriorating Referral channel performance across multiple clusters, particularly the severe FAR collapse in CK Referral (-11.53pp) within WL and CA Referral (-7.88pp) within HF-NA, both driven by surging duplicate rates.

### Cluster Highlights

- **US-HF:** FAR improved significantly by +1.84pp to 91.44%, driven by Paid channel gains (+2.33pp) and decreased PF Block Rate (-0.38pp), returning to the upper end of the 8-week range.
- **HF-INTL:** FAR stable at 92.23% (+0.46pp, not significant), with BE showing strong improvement (+5.10pp) offset by NZ decline (-4.52pp) due to elevated Referral channel blocking.
- **WL:** FAR declined by -0.84pp to 91.88%, driven by Referral channel degradation (-4.33pp) with CK Referral experiencing severe FAR collapse (-11.53pp) alongside a +30.36% duplicate rate surge.
- **HF-NA:** FAR improved significantly by +1.13pp to 90.84%, led by US Paid channel strength (+2.17pp), though CA Referral requires investigation due to -7.88pp FAR decline and 34.18% Dup Block rate.
- **RTE:** FAR stable at 94.05% (-0.20pp, not significant), with TK flagged for -6.18pp decline driven by duplicate blocking increases, though low volume (321 customers) limits overall impact.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 24.70% to 25.19% (↑1.98%, not sig., vol: 2.5K)
- **HF-NA**: 28.23% to 28.18% (↓0.18%, not sig., vol: 41.7)
- **HF-INTL**: 34.28% to 34.93% (↑1.90%, not sig., vol: 794.3)
- **US-HF**: 27.73% to 27.02% (↓2.56%, not sig., vol: 440.0)
- **RTE**: 15.74% to 16.77% (↑6.55%, not sig., vol: 3.0K)
- **WL**: 17.07% to 18.32% (↑7.32%, not sig., vol: 1.0K)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TT (↑61%)
[20% - 49%]
  - HF-INTL: BE (↓48%), NO (↑35%), SE (↑21%)
  - RTE: TO (↑39%)
[10.0% - 19%]
  - RTE: CF (↑14%), TZ (↓15%), TK (↑20%)
  - WL: KN (↑15%), CK (↑14%), CG (↑14%), AO (↑11%)
  - HF-INTL: AT (↑17%), CH (↓11%)
**Dimensions:**
[10.0% - 19%]
  - HF-NA: CC Referral (↑13%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.97% to 6.03% (↑0.96%, not sig., vol: 1.2K)
- **HF-NA**: 7.59% to 7.16% (↓5.65%, not sig., vol: 1.3K)
- **HF-INTL**: 6.87% to 6.53% (↓4.96%, not sig., vol: 2.1K)
- **US-HF**: 8.03% to 6.99% (↓13.02%, not sig., vol: 2.2K)
- **RTE**: 4.44% to 4.93% (↑11.15%, not sig., vol: 5.1K)
- **WL**: 5.02% to 6.16% (↑22.70%, not sig., vol: 3.2K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: BE (↓59%), CH (↑96%), LU (↓75%)
  - RTE: TK (↑63%)
[20% - 49%]
  - RTE: CF (↑39%), TT (↑44%), TO (↑30%)
  - HF-NA: CA (↑22%)
  - WL: CK (↑44%), MR (↑38%), KN (↑21%), CG (↑20%)
  - HF-INTL: IE (↓23%), NO (↑49%), DK (↓30%), NZ (↑46%), SE (↑20%)
[10.0% - 19%]
  - HF-NA: US (↓13%)
  - HF-INTL: AU (↑15%)
  - RTE: TZ (↓11%)
**Dimensions:**
[20% - 49%]
  - HF-NA: CC Paid (↓50%)
  - WL: CC Paid (↑37%)
[10.0% - 19%]
  - RTE: CC Paid (↑18%)
  - HF-NA: CC Referral (↑18%)
  - WL: CC Referral (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.63% to 0.63% (↓0.20%, not sig., vol: 247.5)
- **HF-NA**: 1.58% to 1.28% (↓18.60%, not sig., vol: 4.4K)
- **HF-INTL**: 0.26% to 0.35% (↑36.14%, not sig., vol: 15.1K)
- **US-HF**: 1.36% to 0.97% (↓28.62%, not sig., vol: 4.9K)
- **RTE**: 0.32% to 0.37% (↑17.39%, not sig., vol: 7.9K)
- **WL**: 0.96% to 1.15% (↑19.95%, not sig., vol: 2.8K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: GB (↑72%), AU (↑160%), IE (↓100%), BE (↓61%), NO (↓100%)
  - WL: ER (↑292%), AO (↓100%)
  - RTE: TZ (↓100%)
[20% - 49%]
  - HF-NA: US (↓29%)
  - HF-INTL: DE (↓40%), DK (↓44%)
  - WL: KN (↓46%)
[10.0% - 19%]
  - RTE: FJ (↑14%), TK (↑17%)
  - HF-INTL: FR (↑13%)
**Dimensions:**
[+50%]
  - WL: CC Referral (↑232%)
  - HF-NA: CC Referral (↓65%)
[20% - 49%]
  - HF-INTL: CC Paid (↑42%), CC Referral (↑24%)
  - RTE: CC Paid (↑28%), CC Referral (↓30%)
  - HF-NA: CC Paid (↑34%)
[10.0% - 19%]
  - WL: CC Paid (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.45% to 95.44% (↓0.01%, not sig., vol: 172.2)
- **HF-NA**: 94.13% to 94.03% (↓0.10%, not sig., vol: 511.2)
- **HF-INTL**: 97.39% to 97.45% (↑0.05%, not sig., vol: 432.3)
- **US-HF**: 93.82% to 93.80% (↓0.02%, not sig., vol: 86.9)
- **RTE**: 94.81% to 94.84% (↑0.03%, not sig., vol: 112.3)
- **WL**: 91.69% to 91.69% (↓0.00%, not sig., vol: 3.9)

**Deep Insights**
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓6%)
  - RTE: CustomerQuality Bad (↓3%)
  - WL: CustomerQuality Bad (↑4%)
**Low Volume (denom < 50):** 4 segments excluded

### Overall Summary

Payment Approval Rate remained stable across all clusters in 2026-W17, with changes ranging from -0.11pp to +0.06pp—none statistically significant. The most notable concern is MR in the WL cluster, which declined -2.98pp (exceeding the ±2.5% threshold) driven by increased "Refused" decline reasons and Credit Card underperformance.

### Cluster Highlights

- **US-HF:** Stable at 93.8% (-0.02pp), with all dimensions within normal ranges and no investigation required.
- **HF-INTL:** Improved marginally to 97.45% (+0.06pp), continuing a 5-week upward trend with Apple Pay and Credit Card showing the strongest gains.
- **WL:** Flat at 91.69% overall, but MR flagged with -2.98pp decline driven by increased "Refused" declines and Braintree underperformance (-2.53pp).
- **HF-NA:** Slight decline to 94.03% (-0.11pp), with CA showing the largest country movement (-0.39pp) while the 8-week trend remains positive.
- **RTE:** Stable at 94.84% (+0.03pp), with no countries exceeding thresholds and Credit Card improving +0.33pp on the largest volume segment.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.24% to 93.15% (↓0.09%, not sig., vol: 1.7K)
- **HF-NA**: 92.31% to 92.19% (↓0.12%, not sig., vol: 633.3)
- **HF-INTL**: 94.81% to 94.63% (↓0.19%, not sig., vol: 1.5K)
- **US-HF**: 92.10% to 92.07% (↓0.03%, not sig., vol: 105.9)
- **RTE**: 92.64% to 92.76% (↑0.12%, not sig., vol: 515.5)
- **WL**: 90.02% to 90.10% (↑0.08%, not sig., vol: 138.8)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: NO (↑5%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓5%)
  - WL: CustomerQuality Bad (↑4%)
**Low Volume (denom < 50):** 4 segments excluded

### Overall Summary

Acceptance Rate (Overall) remained stable across all clusters in 2026-W17, with changes ranging from -0.19pp to +0.13pp, none of which were statistically significant. The most notable finding was NO in HF-INTL showing a +4.53pp improvement driven by a payment provider migration from ProcessOut to Unknown, while ProcessOut showed zero volume across all clusters this week.

### Cluster Highlights

- **US-HF:** Stable at 92.07% (-0.03pp), with "Others" payment method showing the largest segment decline at -0.89pp but remaining within normal variance.
- **HF-INTL:** Declined marginally to 94.63% (-0.19pp), with NO flagged at +4.53pp improvement due to ProcessOut-to-Unknown provider migration reducing Insufficient Funds declines by -3.78pp.
- **WL:** Stable at 90.1% (+0.09pp), with no countries exceeding thresholds and AO showing the strongest improvement at +1.84pp.
- **HF-NA:** Stable at 92.19% (-0.13pp), with CA showing the largest country decline at -0.47pp while US remained flat at +0.02pp.
- **RTE:** Improved marginally to 92.76% (+0.13pp), with all countries and payment dimensions remaining within normal operating parameters.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.35% to 91.98% (↑0.69%, not sig., vol: 651.4)
- **HF-NA**: 89.38% to 89.87% (↑0.55%, not sig., vol: 101.4)
- **HF-INTL**: 91.38% to 91.82% (↑0.48%, not sig., vol: 158.9)
- **US-HF**: 88.80% to 89.01% (↑0.24%, not sig., vol: 31.3)
- **RTE**: 92.47% to 93.34% (↑0.94%, not sig., vol: 291.5)
- **WL**: 91.28% to 92.13% (↑0.93%, not sig., vol: 107.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - WL: ER (↑3%)
  - HF-INTL: NZ (↑6%), CH (↓6%), LU (↓8%)
  - RTE: TK (↓4%), TV (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: PP Adyen (↑9%)
  - HF-INTL: PM Credit Card (↓5%)
**Low Volume (denom < 50):** 5 segments excluded

### Overall Summary

Acceptance Rate (Initial Charges) improved modestly across all clusters in W17, with gains ranging from +0.24% (US-HF) to +0.94% (RTE), though none reached statistical significance. The most notable concern is Braintree payment provider degradation in LU (-12.36%) and CH (-11.59%) within HF-INTL, both showing increased Insufficient Funds declines.

### Cluster Highlights

- **US-HF:** Stable at 89.01% (+0.24%), with Credit Card payment method showing a -7.30% decline on low volume (157 orders) warranting monitoring.
- **HF-INTL:** Improved to 91.82% (+0.48%), though LU (-7.94%) and CH (-6.35%) experienced Braintree-driven declines with elevated Insufficient Funds.
- **WL:** Improved to 92.13% (+0.93%), driven by ER's +2.53% gain from reduced Insufficient Funds (-1.74pp) despite ProcessOut volume dropping to zero.
- **HF-NA:** Improved to 89.87% (+0.55%), with CA outperforming US (+1.59% vs +0.24%) and Adyen showing a flagged +9.47% spike on low volume.
- **RTE:** Improved to 93.34% (+0.94%), continuing a steady upward trend from W13, though TK (-3.57%) and TV (-2.78%) showed PayPal and credit card degradation on minimal volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.34% to 93.22% (↓0.13%, not sig., vol: 2.4K)
- **HF-NA**: 92.41% to 92.28% (↓0.15%, not sig., vol: 713.5)
- **HF-INTL**: 94.97% to 94.75% (↓0.23%, not sig., vol: 1.7K)
- **US-HF**: 92.19% to 92.17% (↓0.02%, not sig., vol: 98.8)
- **RTE**: 92.66% to 92.71% (↑0.06%, not sig., vol: 224.4)
- **WL**: 89.91% to 89.94% (↑0.03%, not sig., vol: 54.0)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: NO (↑5%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓5%)
  - WL: CustomerQuality Bad (↑4%)
**Low Volume (denom < 50):** 4 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 52.48% to 53.47% (↑1.90%, not sig., vol: 1.5K)
- **HF-NA**: 48.05% to 48.81% (↑1.60%, not sig., vol: 292.9)
- **HF-INTL**: 66.70% to 68.46% (↑2.63%, not sig., vol: 840.2)
- **US-HF**: 47.59% to 47.69% (↑0.19%, not sig., vol: 27.3)
- **RTE**: 43.82% to 43.02% (↓1.83%, not sig., vol: 371.7)
- **WL**: 31.81% to 31.38% (↓1.34%, not sig., vol: 109.3)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↑194%)
[20% - 49%]
  - RTE: TO (↑26%), TK (↓44%)
[10.0% - 19%]
  - HF-INTL: SE (↑11%)
  - WL: GN (↑14%)
  - RTE: TZ (↑13%), TT (↑15%), TV (↓14%)

### Overall Summary

Dunning Recovery Rate showed mixed performance globally in 2026-W17, with three clusters improving (HF-INTL +1.76pp, HF-NA +0.78pp, US-HF +0.10pp) and two declining (RTE -0.80pp, WL -0.42pp) during the Post-Payday phase transition. The most significant finding is HF-INTL's strong +1.76pp improvement driven by GB's +4.98pp gain from reduced discounting, while WL's decline was primarily a Simpson's Paradox effect as volume shifted from high-performing AO to lower-performing ER.

### Cluster Highlights

- **US-HF:** Stable at 47.69% (+0.10pp), with PC2 improvement of +3.9% offsetting the Payday to Post-Payday transition.
- **HF-INTL:** Improved by +1.76pp to 68.46%, driven by GB's +4.98pp gain from a 7.8% reduction in Discount % and broad PC2 improvements across markets.
- **WL:** Declined by -0.42pp to 31.39% due to Simpson's Paradox as high-performing AO volume dropped 10.1% while low-performing ER volume increased 5.2%, masking underlying country-level improvements.
- **HF-NA:** Improved by +0.78pp to 48.82%, led by CA's +6.4% Ship Rate gain from reduced discounting (-6.4%) and improved PC2 (+2.8%).
- **RTE:** Declined by -0.80pp to 43.02% despite favorable upstream metrics, with FJ contributing most to the drop due to Post-Payday phase timing effects on its 70% volume share.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 44.29% to 41.41% (↓6.50%, not sig., vol: 2.7K)
- **HF-NA**: 40.19% to 38.77% (↓3.52%, not sig., vol: 314.1)
- **HF-INTL**: 45.55% to 41.27% (↓9.40%, not sig., vol: 2.1K)
- **US-HF**: 42.27% to 40.95% (↓3.10%, not sig., vol: 211.4)
- **RTE**: 46.09% to 45.25% (↓1.82%, not sig., vol: 159.3)
- **WL**: 42.04% to 38.74% (↓7.86%, not sig., vol: 201.7)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: CH (↑100%)
[20% - 49%]
  - HF-INTL: AT (↓20%)
  - WL: GN (↓21%), CG (↓22%)
  - RTE: TZ (↑34%)
[10.0% - 19%]
  - HF-INTL: FR (↓14%), DE (↓19%), BE (↓13%), SE (↓12%)
**Low Volume (denom < 50):** 3 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 85.77% to 84.17% (↓1.86%, not sig., vol: 842.8)
- **HF-NA**: 80.56% to 74.65% (↓7.33%, not sig., vol: 708.4)
- **HF-INTL**: 88.94% to 90.05% (↑1.25%, not sig., vol: 316.3)
- **US-HF**: 80.97% to 72.04% (↓11.04%, not sig., vol: 760.9)
- **RTE**: 84.61% to 78.13% (↓7.67%, not sig., vol: 561.2)
- **WL**: 82.74% to 79.50% (↓3.92%, not sig., vol: 110.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TK (↑23%)
[10.0% - 19%]
  - HF-NA: US (↓11%)
  - RTE: FJ (↓13%), TZ (↑16%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €10.18 to €6.20 (↓39.07%, not sig., vol: 32.5K)
- **HF-NA**: €11.37 to €3.42 (↓69.92%, not sig., vol: 13.5K)
- **HF-INTL**: €10.54 to €11.18 (↑6.05%, not sig., vol: 2.3K)
- **US-HF**: €11.29 to €1.46 (↓87.06%, not sig., vol: 12.6K)
- **RTE**: €10.15 to €0.46 (↓95.50%, not sig., vol: 18.5K)
- **WL**: €5.22 to €3.18 (↓39.16%, not sig., vol: 2.8K)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: FJ (↓115%)
  - HF-NA: US (↓87%)
  - WL: ER (↓109%), CG (↓64%)
  - HF-INTL: IT (↑660%), ES (↓86%)
[20% - 49%]
  - HF-INTL: FR (↑28%), IE (↑25%), LU (↑34%)
  - HF-NA: CA (↓20%)
  - RTE: CF (↓24%)
  - WL: CK (↑22%), AO (↓27%), GN (↑21%)
[10.0% - 19%]
  - HF-INTL: AU (↓15%), DE (↑19%), BE (↑13%), NO (↓19%), AT (↑12%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---
