# Steering Report - 2026-W17 (v3)

**Week:** 2026-W17  
**Generated:** 2026-04-28 14:43

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 96.54% to 96.34% (↓0.21%, not sig., vol: 225.5)
- **HF-NA**: 93.86% to 93.94% (↑0.09%, not sig., vol: 18.6)
- **HF-INTL**: 97.13% to 96.67% (↓0.48%, not sig., vol: 163.4)
- **US-HF**: 92.75% to 92.67% (↓0.08%, not sig., vol: 12.9)
- **RTE**: 97.20% to 97.05% (↓0.16%, not sig., vol: 67.4)
- **WL**: 97.59% to 97.02% (↓0.58%, not sig., vol: 63.1)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: BE (↓14%), CH (↑6%)
  - RTE: TT (↓5%)
**Dimensions:**
[2.5% - 19%]
  - RTE: PM Others (↓5%)
  - HF-NA: PM Others (↑4%), FinalTokenType false (↑4%)
**Low Volume (denom < 50):** 1 segment excluded

### Overall Summary

Payment Checkout Approval Rate remained broadly stable across all clusters in 2026-W17, with changes ranging from -0.58pp to +0.09pp, none reaching statistical significance. The most significant concern is BE in HF-INTL, which experienced a -13.63pp decline driven by BcmcMobile/Adyen pathway degradation, requiring investigation.

### Cluster Highlights

- **US-HF:** Stable at 92.67% (-0.08pp), with no dimensions exceeding thresholds and the decline within normal weekly variance.
- **HF-INTL:** Declined to 96.67% (-0.47pp), driven by BE dropping -13.63pp due to BcmcMobile payment method at 69.71% approval rate via Adyen.
- **WL:** Declined to 97.02% (-0.58pp), with ER showing the largest country-level drop at -1.93pp but remaining below investigation threshold.
- **HF-NA:** Improved marginally to 93.94% (+0.09pp), with CA up +0.29pp and US essentially flat at -0.08pp.
- **RTE:** Stable at 97.05% (-0.15pp), with TT exceeding threshold at -5.00pp due to IDeal/Adyen degradation, though impact limited by 39.1% volume drop.

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

Payment Conversion Rate (Checkout) declined across all clusters in 2026-W17, with the most severe drop in RTE (-8.79pp) and significant declines in WL (-3.78pp), HF-INTL (-1.00pp), US-HF (-0.79pp), and HF-NA (-0.29pp). The consistent pattern across all clusters points to a systemic issue at the Select Payment Method step, where users are viewing payment options but abandoning before selection, despite improved downstream PSP success rates.

### Cluster Highlights

- **US-HF:** PCR declined -0.79pp (25.83% → 25.04%) driven by a -1.42pp drop in Select Payment Method conversion and a -24.7% reduction in payment visits, while all payment method success rates improved significantly.
- **HF-INTL:** PCR declined -1.00pp (37.09% → 36.09%) with NL experiencing the most severe degradation (-6.44pp PCR, -9.26pp Select Payment Method), partially offset by GB improvement (+2.06pp).
- **WL:** PCR declined -3.78pp (35.83% → 32.05%) driven by Select Payment Method (-3.27pp) and Click Submit Form (-2.31pp) drops, with CG experiencing the largest country-level decline (-12.90pp).
- **HF-NA:** PCR declined modestly -0.29pp (27.55% → 27.26%) with US underperforming (-0.79pp) while CA improved (+0.91pp), and improved fraud approval rates (+0.88pp) partially offsetting upstream funnel losses.
- **RTE:** PCR declined sharply -8.79pp (48.92% → 40.13%) driven almost entirely by a -9.27pp collapse in Select Payment Method conversion, with TT experiencing the most severe impact (-18.51pp PCR).

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

Reactivation Rate showed mixed performance across clusters in 2026-W17, with significant declines in WL (-1.68pp to 85.35%) and RTE (-2.05pp to 87.33%) offsetting a significant improvement in HF-NA (+1.05pp to 90.35%). The most critical concern is the RTE cluster where YE experienced a 351.6% volume surge coupled with a 13.10pp rate collapse driven by increased card validity issues and blocked transactions.

### Cluster Highlights

- **US-HF:** Stable at 89.71% (-0.36pp), a non-significant decline within normal fluctuation with PayPal showing the largest payment method decrease (-1.49%) on 2,532 orders.
- **HF-INTL:** Stable at 90.74% (-0.54pp), a non-significant decline with minor flags in LU (-8.33%) and NO (-3.16%) both driven by low-volume payment method issues.
- **WL:** Declined significantly to 85.35% (-1.68pp), continuing a two-week downward trend driven by Credit Card degradation in GN (-7.90%) and AO (-5.96%) with increased "Expired, Invalid, Closed Card" decline reasons.
- **HF-NA:** Improved significantly to 90.35% (+1.05pp), driven by CA's strong Credit Card recovery (+7.29pp) and reduced fraud-related declines (-1.38pp).
- **RTE:** Declined significantly to 87.33% (-2.05pp), the lowest in 8 weeks, primarily caused by YE's volume surge (+351.6%) coinciding with Credit Card rate collapse (-15.34pp) and sharp increases in expired/blocked card declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.44% to 92.59% (↑0.16%, not sig., vol: 200.7)
- **HF-NA**: 89.77% to 90.84% (↑1.19%, not sig., vol: 284.2)
- **HF-INTL**: 91.99% to 92.23% (↑0.26%, not sig., vol: 108.5)
- **US-HF**: 89.62% to 91.44% (↑2.03%, not sig., vol: 351.8)
- **RTE**: 94.33% to 94.05% (↓0.29%, not sig., vol: 133.4)
- **WL**: 92.89% to 91.88% (↓1.08%, not sig., vol: 154.3)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - RTE: TK (↓6%)
**Dimensions:**
[+50%]
  - WL: PM Credit Card (↓100%)
[20% - 49%]
  - RTE: PM Unknown (↑33%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Fraud Approval Rate performance was mixed across clusters in 2026-W17, with US-HF (+2.03%) and HF-NA (+1.19%) showing significant improvements while WL declined significantly (-1.08%). The most critical concern is the deteriorating Referral channel performance across multiple clusters, with WL's CK Referral FAR dropping 11.79pp alongside a 31.25% surge in duplicate rates, and similar patterns emerging in CA Referral (-8.12% FAR) and HF-INTL's NZ Referral (-5.39pp).

### Cluster Highlights

- **US-HF:** FAR improved significantly by +2.03% to 91.44%, driven by Paid channel gains (+2.34pp to 95.90%) and reduced PF Block rates, though Referral duplicate rate spiked +13.19% warranting monitoring.
- **HF-INTL:** FAR remained stable at 92.23% (+0.26%, not significant), with NZ showing the largest decline (-4.62pp) driven by Referral channel deterioration while DK (+3.47pp) and IE (+2.62pp) improved.
- **WL:** FAR declined significantly by -1.08% to 91.88%, driven by Referral channel deterioration (-4.59pp) with CK Referral showing critical FAR collapse (-11.79pp) and duplicate rate surge (+31.25%).
- **HF-NA:** FAR improved significantly by +1.19% to 90.84%, led by US Paid channel strength (+2.03%), though CA Referral requires investigation due to FAR decline (-8.12%) and elevated duplicate block rate (34.18%).
- **RTE:** FAR remained stable at 94.05% (-0.29%, not significant), with TK exceeding threshold (-6.18pp) due to duplicate block surges in both channels, though low volume (321 customers) amplifies volatility.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 24.46% to 25.19% (↑2.97%, not sig., vol: 3.7K)
- **HF-NA**: 28.13% to 28.18% (↑0.17%, not sig., vol: 40.5)
- **HF-INTL**: 33.50% to 34.93% (↑4.27%, not sig., vol: 1.8K)
- **US-HF**: 27.65% to 27.02% (↓2.29%, not sig., vol: 393.3)
- **RTE**: 15.70% to 16.77% (↑6.85%, not sig., vol: 3.1K)
- **WL**: 17.01% to 18.32% (↑7.68%, not sig., vol: 1.1K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: LU (↑1567%)
  - RTE: TT (↑60%)
[20% - 49%]
  - HF-INTL: NO (↑35%), SE (↑21%)
  - RTE: TO (↑39%)
[10.0% - 19%]
  - RTE: CF (↑15%), TZ (↓15%), TK (↑20%)
  - WL: KN (↑18%), CK (↑15%), CG (↑14%), AO (↑11%)
  - HF-INTL: AT (↑17%), CH (↓11%)
**Dimensions:**
[10.0% - 19%]
  - HF-NA: CC Referral (↑13%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.90% to 6.03% (↑2.25%, not sig., vol: 2.8K)
- **HF-NA**: 7.55% to 7.16% (↓5.10%, not sig., vol: 1.2K)
- **HF-INTL**: 6.71% to 6.53% (↓2.64%, not sig., vol: 1.1K)
- **US-HF**: 7.99% to 6.99% (↓12.56%, not sig., vol: 2.2K)
- **RTE**: 4.40% to 4.93% (↑12.01%, not sig., vol: 5.5K)
- **WL**: 4.97% to 6.16% (↑23.93%, not sig., vol: 3.4K)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TK (↑63%)
  - HF-INTL: CH (↑96%), LU (↓77%)
[20% - 49%]
  - RTE: CF (↑42%), TT (↑44%), TO (↑30%)
  - HF-NA: CA (↑22%)
  - WL: CK (↑45%), MR (↑38%), KN (↑25%), CG (↑20%)
  - HF-INTL: BE (↓26%), IE (↓23%), NO (↑49%), DK (↓30%), NZ (↑46%)
[10.0% - 19%]
  - HF-NA: US (↓13%)
  - HF-INTL: AU (↑15%)
  - RTE: TZ (↓11%)
**Dimensions:**
[20% - 49%]
  - HF-NA: CC Paid (↓50%)
  - WL: CC Paid (↑40%)
[10.0% - 19%]
  - RTE: CC Paid (↑18%)
  - HF-NA: CC Referral (↑19%)
  - WL: CC Referral (↑15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.62% to 0.63% (↑1.33%, not sig., vol: 1.7K)
- **HF-NA**: 1.57% to 1.28% (↓18.41%, not sig., vol: 4.4K)
- **HF-INTL**: 0.25% to 0.35% (↑41.83%, not sig., vol: 17.5K)
- **US-HF**: 1.36% to 0.97% (↓28.51%, not sig., vol: 4.9K)
- **RTE**: 0.31% to 0.37% (↑19.26%, not sig., vol: 8.7K)
- **WL**: 0.95% to 1.15% (↑21.02%, not sig., vol: 3.0K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: GB (↑79%), AU (↑161%), IE (↓100%), NO (↓100%), NZ (↑86%)
  - WL: ER (↑292%), AO (↓100%)
  - RTE: TZ (↓100%)
[20% - 49%]
  - HF-NA: US (↓29%)
  - HF-INTL: DE (↓40%), BE (↓27%), DK (↓43%)
  - WL: KN (↓46%)
[10.0% - 19%]
  - RTE: FJ (↑16%), TK (↑17%)
  - HF-INTL: FR (↑16%)
**Dimensions:**
[+50%]
  - HF-INTL: CC Paid (↑51%)
  - WL: CC Referral (↑233%)
  - HF-NA: CC Referral (↓66%)
[20% - 49%]
  - RTE: CC Paid (↑30%), CC Referral (↓30%)
  - HF-NA: CC Paid (↑34%)
  - HF-INTL: CC Referral (↑24%)
[10.0% - 19%]
  - WL: CC Paid (↑15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.45% to 95.42% (↓0.02%, not sig., vol: 417.3)
- **HF-NA**: 94.13% to 94.03% (↓0.11%, not sig., vol: 547.4)
- **HF-INTL**: 97.39% to 97.43% (↑0.03%, not sig., vol: 267.0)
- **US-HF**: 93.82% to 93.80% (↓0.02%, not sig., vol: 102.9)
- **RTE**: 94.81% to 94.83% (↑0.02%, not sig., vol: 92.3)
- **WL**: 91.69% to 91.67% (↓0.02%, not sig., vol: 25.7)

**Deep Insights**
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓6%)
  - RTE: CustomerQuality Bad (↓3%)
**Low Volume (denom < 50):** 4 segments excluded

### Overall Summary

Payment Approval Rate remained stable globally in 2026-W17, with all five clusters showing statistically non-significant changes ranging from -0.11pp to +0.04pp. The only notable concern was MR in the WL cluster, which exceeded the ±2.5% threshold with a -3.04pp decline driven by increased "Refused" declines in credit card transactions through Braintree.

### Cluster Highlights

- **US-HF:** Stable at 93.80% (-0.02pp), with Post-Dunning AR showing the largest funnel degradation at -0.17pp while the 8-week upward trend from 93.38% remains intact.
- **HF-INTL:** Improved marginally to 97.43% (+0.04pp), continuing an 8-week positive trajectory with no countries exceeding alert thresholds despite CH declining -1.24pp on low volume.
- **WL:** Stable at 91.67% (-0.02pp) overall, but MR requires monitoring after a -3.04pp decline (83.54% → 81.00%) driven by +2.27pp increase in refused credit card transactions.
- **HF-NA:** Declined slightly to 94.03% (-0.11pp), with CA showing a -0.41pp drop and Post-Dunning AR weakness at -0.27pp, though the 8-week trend remains positive.
- **RTE:** Stable at 94.83% (+0.02pp), with no countries exceeding thresholds and Credit Card payments improving +0.33pp to 95.09% across 235,932 orders.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.24% to 93.15% (↓0.09%, not sig., vol: 1.7K)
- **HF-NA**: 92.31% to 92.19% (↓0.13%, not sig., vol: 640.8)
- **HF-INTL**: 94.81% to 94.63% (↓0.19%, not sig., vol: 1.5K)
- **US-HF**: 92.10% to 92.07% (↓0.03%, not sig., vol: 113.5)
- **RTE**: 92.64% to 92.75% (↑0.12%, not sig., vol: 515.6)
- **WL**: 90.02% to 90.10% (↑0.08%, not sig., vol: 141.1)

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

Acceptance Rate (Overall) remained stable across all clusters in 2026-W17, with changes ranging from -0.19pp to +0.12pp, none of which were statistically significant. The most notable finding was the provider migration in NO (HF-INTL) where ProcessOut volume dropped to zero with traffic shifting to Unknown provider, resulting in a +4.53pp improvement driven by reduced "Insufficient Funds" declines.

### Cluster Highlights

- **US-HF:** Stable at 92.07% (-0.03pp), with all payment methods and providers operating within normal thresholds and no actionable concerns.
- **HF-INTL:** Declined marginally to 94.63% (-0.19pp), though NO improved significantly (+4.53pp) following a ProcessOut to Unknown provider migration that reduced Insufficient Funds declines by 3.78pp.
- **WL:** Improved slightly to 90.1% (+0.08pp), with stable performance across all countries and no dimensions exceeding alert thresholds.
- **HF-NA:** Declined to 92.19% (-0.13pp), with CA showing the largest country movement at -0.47pp and "Others" payment method declining -1.05pp on 105K orders.
- **RTE:** Improved to 92.75% (+0.12pp), with all countries within normal range and FJ maintaining stable performance at 93.81% representing 90% of volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.26% to 92.01% (↑0.83%, not sig., vol: 770.8)
- **HF-NA**: 89.33% to 90.32% (↑1.11%, not sig., vol: 202.1)
- **HF-INTL**: 91.22% to 91.80% (↑0.64%, not sig., vol: 204.8)
- **US-HF**: 88.73% to 89.24% (↑0.57%, not sig., vol: 75.1)
- **RTE**: 92.41% to 93.20% (↑0.85%, not sig., vol: 260.4)
- **WL**: 91.27% to 92.15% (↑0.96%, not sig., vol: 111.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: FR (↑3%), NZ (↑6%), CH (↓6%), LU (↓8%)
  - HF-NA: CA (↑3%)
  - WL: ER (↑3%)
  - RTE: TK (↓4%), TV (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: PP Adyen (↑10%)
  - HF-INTL: PM Credit Card (↓6%)
**Low Volume (denom < 50):** 5 segments excluded

### Overall Summary

Acceptance Rate (Initial Charges) improved across all five clusters in 2026-W17, with gains ranging from +0.57% (US-HF) to +1.11% (HF-NA), though only HF-NA's improvement was statistically significant. The most notable finding is the complete migration away from ProcessOut across multiple clusters (US-HF, HF-INTL, WL, HF-NA, RTE), coinciding with improved acceptance rates, suggesting a deliberate provider shift that warrants continued monitoring.

### Cluster Highlights

- **US-HF:** Improved by +0.57% to 89.24% (not significant), with Credit Card payment method flagged at -7.42% decline but limited impact due to low volume (160 orders).
- **HF-INTL:** Improved by +0.64% to 91.8% (not significant), though LU (-7.94%) and CH (-5.66%) declined significantly due to Apple Pay and Braintree performance issues alongside ProcessOut exiting.
- **WL:** Improved by +0.96% to 92.15% (not significant), driven by ER's +2.53% gain from reduced Insufficient Funds declines and Unknown provider performance improvement following ProcessOut exit.
- **HF-NA:** Improved by +1.11% to 90.32% (significant), driven by CA's +2.73% gain as Adyen volume surged (+12.27% AR) following ProcessOut migration and Insufficient Funds declined -2.15pp.
- **RTE:** Improved by +0.85% to 93.2% (not significant), with TK (-3.57%) and TV (-2.78%) flagged for Insufficient Funds increases but representing only ~2.4% of total volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.34% to 93.21% (↓0.14%, not sig., vol: 2.5K)
- **HF-NA**: 92.41% to 92.26% (↓0.17%, not sig., vol: 824.7)
- **HF-INTL**: 94.97% to 94.75% (↓0.23%, not sig., vol: 1.8K)
- **US-HF**: 92.20% to 92.16% (↓0.04%, not sig., vol: 152.7)
- **RTE**: 92.66% to 92.72% (↑0.06%, not sig., vol: 255.0)
- **WL**: 89.91% to 89.94% (↑0.03%, not sig., vol: 52.0)

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
- **Overall**: 52.47% to 53.37% (↑1.70%, not sig., vol: 1.3K)
- **HF-NA**: 48.04% to 48.73% (↑1.45%, not sig., vol: 264.7)
- **HF-INTL**: 66.70% to 68.33% (↑2.45%, not sig., vol: 777.9)
- **US-HF**: 47.59% to 47.65% (↑0.13%, not sig., vol: 18.3)
- **RTE**: 43.81% to 42.97% (↓1.92%, not sig., vol: 389.6)
- **WL**: 31.81% to 31.30% (↓1.63%, not sig., vol: 132.9)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↑96%)
[20% - 49%]
  - RTE: TO (↑25%), TK (↓44%)
[10.0% - 19%]
  - HF-INTL: SE (↑11%)
  - WL: GN (↑14%)
  - RTE: TZ (↑13%), TT (↑15%), TV (↓11%)

### Overall Summary

Dunning Recovery Rate showed mixed performance globally in 2026-W17, with three clusters improving (HF-INTL +1.63pp, HF-NA +0.69pp, US-HF +0.06pp) and two declining (RTE -0.84pp, WL -0.51pp) during the Post-Payday phase. The most significant finding is HF-INTL's strong +1.63pp improvement driven by GB (+8.3%) and SE (+11.2%), while NO experienced a concerning -9.6% decline due to a +26.1% spike in discount rates requiring investigation.

### Cluster Highlights

- **US-HF:** Stable at 47.65% (+0.06pp) with PC2 improving +3.9% while discount rates decreased -1.8%, indicating healthy underlying performance despite Post-Payday timing.
- **HF-INTL:** Improved by +1.63pp to 68.33%, driven by GB (+8.3%) and SE (+11.2%) through reduced discounting, partially offset by NO's -9.6% decline from aggressive discount increases (+26.1%).
- **WL:** Declined by -0.51pp to 31.30% due to Simpson's Paradox as high-performing AO volume dropped -10.1% while lower-performing ER gained +5.1% share, masking individual country improvements.
- **HF-NA:** Improved by +0.69pp to 48.73%, driven primarily by CA's +6.0% Ship Rate gain attributed to -6.8% discount reduction and +2.8% PC2 improvement.
- **RTE:** Declined by -0.84pp to 42.98% despite favorable funnel metrics, primarily due to Payday-to-Post-Payday transition impact on FJ (-2.6%) and severe TK deterioration (-43.7%) on small volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 44.29% to 41.57% (↓6.15%, not sig., vol: 2.6K)
- **HF-NA**: 40.20% to 38.85% (↓3.35%, not sig., vol: 298.5)
- **HF-INTL**: 45.55% to 41.49% (↓8.92%, not sig., vol: 1.9K)
- **US-HF**: 42.28% to 40.95% (↓3.14%, not sig., vol: 213.2)
- **RTE**: 46.10% to 45.34% (↓1.66%, not sig., vol: 144.3)
- **WL**: 42.04% to 38.90% (↓7.46%, not sig., vol: 190.7)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: CH (↑100%)
[20% - 49%]
  - WL: GN (↓20%), CG (↓22%)
  - RTE: TZ (↑34%)
[10.0% - 19%]
  - HF-INTL: DE (↓19%), FR (↓12%), BE (↓12%), SE (↓12%), AT (↓20%)
  - RTE: TO (↑11%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W17

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 85.77% to 84.17% (↓1.86%, not sig., vol: 841.6)
- **HF-NA**: 80.56% to 74.66% (↓7.32%, not sig., vol: 707.4)
- **HF-INTL**: 88.94% to 90.05% (↑1.25%, not sig., vol: 316.4)
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
- **Overall**: €10.18 to €6.20 (↓39.06%, not sig., vol: 32.5K)
- **HF-NA**: €11.37 to €3.42 (↓69.90%, not sig., vol: 13.5K)
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
