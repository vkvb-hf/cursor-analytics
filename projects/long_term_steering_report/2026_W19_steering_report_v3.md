# Steering Report - 2026-W19 (v3)

**Week:** 2026-W19  
**Generated:** 2026-05-12 14:52

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 94.90% to 94.18% (↓0.76%, not sig., vol: 784.0)
- **HF-NA**: 92.45% to 91.02% (↓1.55%, not sig., vol: 321.2)
- **HF-INTL**: 94.18% to 92.95% (↓1.30%, not sig., vol: 439.4)
- **US-HF**: 91.13% to 89.60% (↓1.68%, not sig., vol: 273.7)
- **RTE**: 96.52% to 96.66% (↑0.15%, not sig., vol: 59.4)
- **WL**: 96.02% to 95.28% (↓0.77%, not sig., vol: 81.1)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↓4%), SE (↓4%), NZ (↓3%), LU (↑6%)
  - RTE: TV (↑5%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PM Others (↓12%)
**Low Volume (denom < 50):** 3 segments excluded

### Overall Summary

Payment Checkout Approval Rate declined across most clusters in 2026-W19, with significant drops in US-HF (-1.68%), HF-INTL (-1.31%), and HF-NA (-1.55%), while RTE remained stable (+0.15%). The most critical issue is a Klarna/Adyen integration failure in DE, where Klarna approval rate collapsed from 55.81% to 19.65% (-64.79%), requiring immediate escalation.

### Cluster Highlights

- **US-HF:** Declined significantly from 91.13% to 89.60% (-1.68%), continuing a 3-week downward trend primarily driven by Credit Card (-1.79%) and Apple Pay (-1.68%) performance degradation.
- **HF-INTL:** Declined from 94.18% to 92.95% (-1.31%), driven by a critical Klarna/Adyen failure in DE (-64.79% Klarna approval rate) with SE showing a similar pattern (-8.45% Klarna via Adyen).
- **WL:** Declined from 96.02% to 95.28% (-0.77%, not significant), though a sustained 4-week downward trend (-2.31pp cumulative) driven by Credit Card (-1.08%) warrants monitoring.
- **HF-NA:** Declined from 92.45% to 91.02% (-1.55%), with US driving 79% of volume and experiencing a -1.68% drop while Credit Card payments declined -1.70% across 12,140 orders.
- **RTE:** Stable at 96.66% (+0.15%, not significant), with TV showing notable improvement (+4.60pp) driven by Klarna (+6.44pp) and Adyen (+5.18pp) recovery.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.59% to 32.81% (↑0.67%, not sig., vol: 1.6K)
- **HF-NA**: 25.12% to 25.65% (↑2.14%, not sig., vol: 1.4K)
- **HF-INTL**: 36.44% to 36.26% (↓0.50%, not sig., vol: 346.4)
- **US-HF**: 23.27% to 23.74% (↑2.03%, not sig., vol: 1.0K)
- **RTE**: 37.83% to 38.46% (↑1.68%, not sig., vol: 1.1K)
- **WL**: 29.70% to 29.28% (↓1.43%, not sig., vol: 568.3)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - WL: MR (↑16%), KN (↓11%), CG (↓6%), GN (↓11%)
  - HF-INTL: DE (↓7%), AT (↑10%), CH (↑6%), LU (↓8%)
  - RTE: TO (↑10%), TZ (↑5%), TK (↑8%)

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance globally in 2026-W19, with US-HF (+0.57pp), HF-NA (+0.59pp), and RTE (+0.70pp) improving while HF-INTL (-0.16pp) and WL (-0.42pp) declined. The most significant concern across clusters is deteriorating PVS success rates, with "Insufficient Funds" declines increasing notably in US-HF (+139 cases) and HF-NA (+138 cases), alongside rising "Cancelled" errors in HF-INTL's DE market.

### Cluster Highlights

- **US-HF:** PCR improved by +0.57pp to 23.95%, driven by stronger payment method selection (+1.07pp), though PVS success rate declined -1.53pp with "Insufficient Funds" errors increasing significantly.
- **HF-INTL:** PCR declined by -0.16pp to 36.32%, primarily driven by DE (-2.46pp) where PVS failures increased by 437 cases due to rising "Cancelled" and "RedirectShopper" errors.
- **WL:** PCR declined by -0.42pp to 29.33%, driven by FE validation failures (-0.58pp) with APPLEPAY_DISMISSED errors increasing to 63.7% of all FE errors, particularly impacting GN (-4.06pp).
- **HF-NA:** PCR improved by +0.59pp to 25.81%, driven by early funnel gains in Select Payment Method (+0.79pp) and Click Submit Form (+0.85pp), offsetting downstream PVS challenges.
- **RTE:** PCR improved by +0.70pp to 38.59%, driven primarily by Select Payment Method conversion (+0.85pp) with Braintree_ApplePay success rate improving +1.23pp to 93.09%.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.72% to 32.78% (↑0.19%, not sig., vol: 600.1)
- **HF-NA**: 26.79% to 27.28% (↑1.84%, not sig., vol: 1.3K)
- **HF-INTL**: 39.05% to 38.51% (↓1.38%, not sig., vol: 1.2K)
- **US-HF**: 24.89% to 25.30% (↑1.67%, not sig., vol: 937.9)
- **RTE**: 33.35% to 33.99% (↑1.91%, not sig., vol: 2.1K)
- **WL**: 28.29% to 27.60% (↓2.46%, not sig., vol: 1.2K)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - WL: MR (↑17%), KN (↓10%), CG (↓9%), GN (↓10%), AO (↓6%)
  - HF-INTL: DE (↓6%), NZ (↓8%), SE (↓9%), DK (↓7%), AT (↑9%)
  - RTE: TO (↑9%), TV (↓7%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 89.32% to 89.96% (↑0.72%, not sig., vol: 660.7)
- **HF-NA**: 90.48% to 90.66% (↑0.20%, not sig., vol: 44.3)
- **HF-INTL**: 90.32% to 90.32% (↑0.00%, not sig., vol: 0.0)
- **US-HF**: 90.64% to 90.74% (↑0.11%, not sig., vol: 19.2)
- **RTE**: 87.04% to 89.01% (↑2.26%, not sig., vol: 461.0)
- **WL**: 86.51% to 88.73% (↑2.56%, not sig., vol: 231.5)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: CF (↑7%), YE (↑5%)
  - WL: CK (↑7%), GN (↑5%), AO (↓7%)
  - HF-INTL: NZ (↓4%), SE (↓4%), AT (↓3%), CH (↓6%)
**Dimensions:**
[2.5% - 19%]
  - WL: PM Credit Card (↑3%)
  - RTE: PM Others (↑3%)
**Low Volume (denom < 50):** 7 segments excluded

### Overall Summary

Reactivation Rate improved across most clusters in 2026-W19, with WL (+2.57% to 88.73%) and RTE (+2.26% to 89.01%) showing significant gains while US-HF, HF-INTL, and HF-NA remained stable. The most notable concern is HF-INTL's NZ and SE markets, which experienced Credit Card-driven declines of -4.38% and -4.08% respectively, warranting continued monitoring.

### Cluster Highlights

- **US-HF:** Stable at 90.74% (+0.11%) with Credit Card performance steady at 91.14% on 27.8% higher volume; Apple Pay declined -1.19% but remains within threshold.
- **HF-INTL:** Flat at 90.32% overall, but NZ (-4.38%) and SE (-4.08%) flagged for Credit Card underperformance while low-volume IT and CH anomalies are not material.
- **WL:** Significant improvement to 88.73% (+2.57%) driven by Credit Card gains in CK (+6.97%) and GN (+7.73%), offsetting AO's -7.44% decline on low volume.
- **HF-NA:** Stable at 90.66% (+0.20%) with both US and CA showing modest improvements and no countries exceeding threshold.
- **RTE:** Significant recovery to 89.01% (+2.26%) led by Credit Card improvements in YE (+7.46%) and CF (+7.92%), returning the metric to historical norms.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.67% to 92.63% (↓0.05%, not sig., vol: 56.7)
- **HF-NA**: 91.81% to 91.22% (↓0.64%, not sig., vol: 157.1)
- **HF-INTL**: 91.87% to 91.78% (↓0.10%, not sig., vol: 40.9)
- **US-HF**: 92.19% to 91.34% (↓0.92%, not sig., vol: 170.8)
- **RTE**: 93.86% to 94.24% (↑0.40%, not sig., vol: 168.2)
- **WL**: 92.96% to 92.79% (↓0.18%, not sig., vol: 26.6)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TT (↑24%), TV (↑20%)
[5.0% - 19%]
  - RTE: TZ (↑16%), TO (↑12%), TK (↑12%)
  - HF-INTL: LU (↓14%)
**Dimensions:**
[+50%]
  - RTE: PM Unknown (↑129%)
[5.0% - 19%]
  - HF-NA: CC Referral (↓7%)
**Low Volume (denom < 50):** 2 segments excluded

### Overall Summary

Fraud Approval Rate remained stable across all clusters in 2026-W19, with changes ranging from -0.64% to +0.40%, none statistically significant. The most critical finding is a systemic Referral channel degradation across multiple clusters, with US-HF experiencing an 835% spike in PF Block rate and consistent Dup Block increases impacting Referral FAR in HF-INTL, WL, and HF-NA.

### Cluster Highlights

- **US-HF:** FAR declined by 0.92% to 91.34% (not significant), driven by Referral channel collapse (-7.22pp) due to an 835% surge in PF Block rate requiring immediate investigation.
- **HF-INTL:** FAR stable at 91.78% (-0.10%), though Referral channel dropped -3.00pp across DE, DK, NO, and NL driven by elevated duplicate rates (+13.77% overall).
- **WL:** FAR declined marginally by 0.18% to 92.79% (not significant), with Referral channel degradation (-3.22pp) and rising Dup Block rates across CG, ER, and KN indicating potential referral abuse patterns.
- **HF-NA:** FAR declined by 0.64% to 91.22% (not significant), primarily attributable to US Referral channel deterioration (-9.90pp) from the PF Block spike while Paid channel improved to 96.66%.
- **RTE:** FAR improved by 0.40% to 94.24% (not significant), with strong Paid channel performance (+1.47pp) offset by continued Referral weakness (-4.14%) and rising Dup Block rates.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 21.62% to 23.87% (↑10.40%, not sig., vol: 12.5K)
- **HF-NA**: 23.63% to 25.49% (↑7.86%, not sig., vol: 1.9K)
- **HF-INTL**: 29.63% to 33.38% (↑12.66%, not sig., vol: 5.1K)
- **US-HF**: 21.88% to 24.20% (↑10.61%, not sig., vol: 2.0K)
- **RTE**: 14.86% to 16.39% (↑10.27%, not sig., vol: 4.2K)
- **WL**: 15.02% to 16.08% (↑7.03%, not sig., vol: 1.0K)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: YE (↑29%), TV (↑49%), TT (↓20%), TZ (↓29%), TO (↑26%)
  - WL: KN (↑31%), CG (↑23%), ER (↑21%)
  - HF-INTL: NL (↑41%), NZ (↑21%)
[10.0% - 19%]
  - HF-NA: US (↑11%)
  - HF-INTL: GB (↑10%), DE (↑15%), FR (↑11%), AU (↑15%), BE (↑15%)
  - RTE: CF (↑15%), TK (↑19%)
**Dimensions:**
[20% - 49%]
  - RTE: CC Referral (↑20%)
[10.0% - 19%]
  - HF-INTL: CC Paid (↑11%), CC Referral (↑18%)
  - HF-NA: CC Paid (↑10%)
  - WL: CC Referral (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 4.82% to 5.74% (↑19.10%, not sig., vol: 23.0K)
- **HF-NA**: 5.34% to 5.76% (↑7.82%, not sig., vol: 1.9K)
- **HF-INTL**: 5.45% to 6.73% (↑23.36%, not sig., vol: 9.4K)
- **US-HF**: 5.09% to 5.57% (↑9.28%, not sig., vol: 1.7K)
- **RTE**: 3.98% to 4.90% (↑23.16%, not sig., vol: 9.6K)
- **WL**: 4.61% to 5.39% (↑16.83%, not sig., vol: 2.4K)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: CG (↑107%), ER (↑50%)
  - HF-INTL: DK (↑111%), BE (↑51%), NL (↑57%), NO (↑54%)
  - RTE: TV (↑51%)
[20% - 49%]
  - HF-INTL: DE (↑40%), AT (↑23%)
  - RTE: CF (↑25%), YE (↑47%), TO (↑32%), TZ (↓27%), TK (↑21%)
  - WL: KN (↑34%), CK (↓21%)
[10.0% - 19%]
  - RTE: FJ (↑19%), TT (↓17%)
  - HF-INTL: FR (↑18%), GB (↑12%), AU (↑19%), SE (↑17%), IE (↓11%)
  - WL: MR (↓13%)
**Dimensions:**
[20% - 49%]
  - HF-NA: CC Paid (↑31%)
  - WL: CC Paid (↑34%)
  - RTE: CC Referral (↑32%)
[10.0% - 19%]
  - HF-INTL: CC Paid (↑17%), CC Referral (↑15%)
  - WL: CC Referral (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.59% to 0.80% (↑33.81%, not sig., vol: 40.7K)
- **HF-NA**: 0.97% to 2.26% (↑134.08%, not sig., vol: 32.7K)
- **HF-INTL**: 0.56% to 0.31% (↓44.27%, not sig., vol: 17.8K)
- **US-HF**: 0.70% to 2.41% (↑246.36%, not sig., vol: 45.5K)
- **RTE**: 0.25% to 0.28% (↑11.71%, not sig., vol: 4.8K)
- **WL**: 1.08% to 1.14% (↑5.32%, not sig., vol: 765.5)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-NA: US (↑246%)
  - HF-INTL: AU (↓83%), DK (↓100%), IE (↑52%), LU (↑315%)
[20% - 49%]
  - HF-INTL: GB (↑47%), FR (↓41%), DE (↑41%), NL (↓32%), NZ (↓31%)
  - WL: ER (↑32%)
[10.0% - 19%]
  - RTE: FJ (↑14%)
  - WL: MR (↓11%)
**Dimensions:**
[+50%]
  - HF-NA: CC Referral (↑361%)
[20% - 49%]
  - HF-INTL: CC Paid (↓44%), CC Referral (↓44%)
  - RTE: CC Referral (↓22%)
  - WL: CC Referral (↑21%)
[10.0% - 19%]
  - RTE: CC Paid (↑18%)
  - HF-NA: CC Paid (↑18%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.24% to 95.08% (↓0.17%, not sig., vol: 3.2K)
- **HF-NA**: 93.92% to 93.68% (↓0.26%, not sig., vol: 1.3K)
- **HF-INTL**: 97.29% to 97.29% (↓0.00%, not sig., vol: 0.1)
- **US-HF**: 93.62% to 93.33% (↓0.30%, not sig., vol: 1.3K)
- **RTE**: 94.65% to 94.15% (↓0.52%, not sig., vol: 2.2K)
- **WL**: 91.24% to 91.27% (↑0.04%, not sig., vol: 68.7)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - RTE: TV (↑3%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: CustomerQuality Bad (↑23%)
  - WL: CustomerQuality Bad (↑23%)
  - RTE: PP Unknown (↑31%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑6%), PP Unknown (↓14%)
  - RTE: LL a. 0 (↓3%), CustomerQuality Bad (↑4%)
  - HF-INTL: LL a. 0 (↑3%), PP Unknown (↓3%)

### Overall Summary

Payment Approval Rate remained broadly stable across all clusters in 2026-W19, with changes ranging from -0.53pp to +0.03pp, none of which were statistically significant. The most notable pattern is RTE's continued gradual 8-week decline from 95.18% to 94.15% (-1.03pp cumulative), which warrants ongoing monitoring despite week-over-week changes remaining within normal bounds.

### Cluster Highlights

- **US-HF:** Declined by -0.29pp to 93.33% (not significant), driven by weakened PostDunningAR (-0.45pp) with low-volume segments (Unknown provider, Others payment method) showing larger but immaterial drops.
- **HF-INTL:** Stable at 97.29% with no change week-over-week, as upstream funnel improvements in FirstRunAR (+0.93pp) and PreDunningAR (+0.73pp) offset a slight PostDunningAR decline (-0.18pp).
- **WL:** Stable at 91.27% (+0.03pp), with no countries or payment dimensions exceeding thresholds and MR showing the largest positive movement at +2.06pp on low volume.
- **HF-NA:** Declined by -0.24pp to 93.68% (not significant), with PostDunningAR showing the largest funnel drop (-0.41pp) and US contributing the majority of the decline (-0.27pp).
- **RTE:** Declined by -0.50pp to 94.15% (not significant), continuing an 8-week downward trend with all funnel stages declining consistently (~0.6pp), while TV improved +2.87pp driven by better credit_card and applepay performance.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.75% to 92.89% (↑0.16%, not sig., vol: 3.0K)
- **HF-NA**: 92.11% to 92.01% (↓0.11%, not sig., vol: 553.1)
- **HF-INTL**: 93.93% to 94.62% (↑0.73%, not sig., vol: 5.7K)
- **US-HF**: 91.90% to 91.78% (↓0.13%, not sig., vol: 553.0)
- **RTE**: 92.55% to 92.00% (↓0.59%, not sig., vol: 2.5K)
- **WL**: 89.60% to 89.67% (↑0.08%, not sig., vol: 130.5)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: SE (↑3%), LU (↑6%)
  - RTE: TV (↑5%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: CustomerQuality Bad (↑24%)
  - WL: CustomerQuality Bad (↑22%)
  - RTE: PP Unknown (↑33%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑9%), PP Unknown (↓14%)
  - HF-INTL: LL a. 0 (↑3%), PP Unknown (↓3%)
  - RTE: LL a. 0 (↓3%), CustomerQuality Bad (↑4%)

### Overall Summary

Acceptance Rate (Overall) remained broadly stable across all clusters in 2026-W19, with changes ranging from -0.59pp to +0.69pp, none of which were statistically significant. The most notable finding is a gradual downward trend in US-HF and HF-NA over the past 4-8 weeks, alongside reduced Post-Dunning recovery effectiveness observed across multiple clusters.

### Cluster Highlights

- **US-HF:** Declined by -0.12pp to 91.78%, continuing a gradual 4-week downward trend from 92.22% (W15), with no dimensions exceeding thresholds at meaningful volume.
- **HF-INTL:** Improved by +0.69pp to 94.62%, driven by SE (+2.53pp) and LU (+4.67pp) where reduced "Insufficient Funds" declines via Braintree lifted performance.
- **WL:** Stable at 89.67% (+0.08pp), with no countries exceeding thresholds and all payment methods/providers within normal variance.
- **HF-NA:** Declined by -0.11pp to 92.01%, extending an 8-week gradual erosion trend, with "Unknown" PaymentProvider dropping -13.66pp on minimal volume (436 orders).
- **RTE:** Declined by -0.55pp to 92.0%, with YE showing the largest drop among major markets (-1.80pp) while TV improved significantly (+4.61pp) due to reduced Insufficient Funds declines.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.36% to 92.01% (↑0.71%, not sig., vol: 643.0)
- **HF-NA**: 89.34% to 90.34% (↑1.13%, not sig., vol: 183.4)
- **HF-INTL**: 91.10% to 92.73% (↑1.79%, not sig., vol: 572.6)
- **US-HF**: 88.21% to 89.29% (↑1.23%, not sig., vol: 141.7)
- **RTE**: 92.36% to 92.07% (↓0.32%, not sig., vol: 94.8)
- **WL**: 91.97% to 92.22% (↑0.28%, not sig., vol: 33.8)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↑3%), IE (↑4%), SE (↑4%), CH (↑5%), LU (↑9%)
  - RTE: YE (↓4%), TO (↑10%), TV (↑5%)
  - WL: CK (↑5%), ER (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PP Braintree (↑3%), PM Apple Pay (↑3%), PP Unknown (↓3%)
  - HF-NA: PP ProcessOut (↑3%), PM Credit Card (↑3%), PP Unknown (↓7%)
  - WL: PP Adyen (↑3%)
  - RTE: PP Unknown (↓12%)

### Overall Summary

Acceptance Rate (Initial Charges) improved across most clusters in 2026-W19, with HF-INTL showing the strongest gain (+1.79pp to 92.73%) and RTE experiencing a minor non-significant decline (-0.31pp to 92.07%). The most notable finding is the broad-based reduction in "Insufficient Funds" declines across HF-INTL markets (DE, SE, IE, CH), driving significant improvements in Apple Pay and Braintree performance.

### Cluster Highlights

- **US-HF:** Improved significantly by +1.08pp to 89.29%, driven by Credit Card acceptance gains (+2.72pp) through ProcessOut provider.
- **HF-INTL:** Strong improvement of +1.79pp to 92.73%, led by DE (+3.31pp on 98% volume growth) and reduced Insufficient Funds declines across all flagged markets.
- **WL:** Stable with non-significant change of +0.25pp to 92.22%, with offsetting movements in ER (-2.96pp) and CK (+4.62pp) driven by Insufficient Funds fluctuations.
- **HF-NA:** Improved significantly by +1.12pp to 90.34%, with broad gains across US (+1.23pp) and CA (+1.15pp) driven by Credit Card and ProcessOut performance.
- **RTE:** Slight non-significant decline of -0.31pp to 92.07%, with YE (-3.96pp) offsetting improvements in TV (+5.47pp) and TO (+9.76pp).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.81% to 92.94% (↑0.14%, not sig., vol: 2.4K)
- **HF-NA**: 92.20% to 92.07% (↓0.15%, not sig., vol: 718.6)
- **HF-INTL**: 94.04% to 94.70% (↑0.70%, not sig., vol: 5.3K)
- **US-HF**: 92.00% to 91.85% (↓0.16%, not sig., vol: 665.5)
- **RTE**: 92.57% to 92.00% (↓0.61%, not sig., vol: 2.4K)
- **WL**: 89.43% to 89.47% (↑0.05%, not sig., vol: 68.9)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: SE (↑3%), LU (↑6%)
  - RTE: TV (↑4%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: CustomerQuality Bad (↑24%)
  - WL: CustomerQuality Bad (↑22%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑9%), PP Unknown (↓17%)
  - RTE: CustomerQuality Bad (↑4%)
  - HF-INTL: PP Unknown (↓6%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 55.00% to 53.22% (↓3.25%, not sig., vol: 2.4K)
- **HF-NA**: 48.33% to 47.67% (↓1.36%, not sig., vol: 230.1)
- **HF-INTL**: 72.12% to 68.77% (↓4.64%, not sig., vol: 1.4K)
- **US-HF**: 47.98% to 46.40% (↓3.29%, not sig., vol: 431.3)
- **RTE**: 41.62% to 43.01% (↑3.33%, not sig., vol: 688.2)
- **WL**: 31.05% to 32.96% (↑6.13%, not sig., vol: 475.3)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↑93%)
  - RTE: TV (↓61%)
[20% - 49%]
  - RTE: TO (↑21%)
[10.0% - 19%]
  - HF-INTL: GB (↓13%), SE (↓15%), NL (↓10%)
  - WL: CG (↑18%), KN (↑13%), GN (↓12%)
  - RTE: TK (↓15%), TT (↓20%)

### Overall Summary

Dunning Ship Rate performance was mixed across clusters in 2026-W19, with WL (+1.90pp) and RTE (+1.39pp) improving while HF-INTL (-3.35pp), US-HF (-1.58pp), and HF-NA (-0.66pp) declined during the Mid-Cycle to Pre-Payday transition. The most significant concern is HF-INTL's widespread Discount % increases across GB, DE, and SE, suggesting systemic pricing pressure requiring strategic review of dunning discount timing.

### Cluster Highlights

- **US-HF:** Ship Rate declined by -1.58pp (47.98% → 46.40%) driven by payday phase transition, with all upstream funnel metrics remaining stable.
- **HF-INTL:** Ship Rate dropped -3.35pp (72.12% → 68.77%) primarily driven by elevated Discount % across GB (+6.2%), DE (+10.9%), and SE (+26.7%) during Pre-Payday phase.
- **WL:** Ship Rate improved +1.90pp (31.06% → 32.96%) driven by a dramatic PC2 surge (+583.0%), though ER declined -7.4% due to increased discounting.
- **HF-NA:** Ship Rate declined -0.66pp (48.33% → 47.67%) as US underperformance (-3.3%) offset strong CA improvement (+5.2% driven by -5.9% Discount % reduction).
- **RTE:** Ship Rate improved +1.39pp (41.62% → 43.01%) driven by PC2 gains (+7.0%), though TV experienced severe collapse (-61.2%) requiring investigation.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 44.50% to 47.57% (↑6.91%, not sig., vol: 2.8K)
- **HF-NA**: 39.58% to 39.74% (↑0.41%, not sig., vol: 32.7)
- **HF-INTL**: 46.01% to 50.16% (↑9.03%, not sig., vol: 1.8K)
- **US-HF**: 42.40% to 42.63% (↑0.54%, not sig., vol: 32.6)
- **RTE**: 45.68% to 50.31% (↑10.14%, not sig., vol: 900.7)
- **WL**: 42.33% to 42.01% (↓0.74%, not sig., vol: 19.0)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: FR (↑68%), DK (↑76%)
[20% - 49%]
  - HF-INTL: BE (↑40%), SE (↓31%), NL (↓28%), CH (↓32%)
  - WL: GN (↓31%)
  - RTE: TO (↑39%)
[10.0% - 19%]
  - RTE: FJ (↑14%)
  - HF-INTL: GB (↓13%), DE (↑16%)
  - WL: ER (↑13%), CG (↓19%)
**Low Volume (denom < 50):** 5 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 86.22% to 84.48% (↓2.02%, not sig., vol: 824.1)
- **HF-NA**: 78.97% to 79.49% (↑0.65%, not sig., vol: 66.0)
- **HF-INTL**: 89.62% to 87.56% (↓2.30%, not sig., vol: 453.7)
- **US-HF**: 79.27% to 79.50% (↑0.29%, not sig., vol: 21.1)
- **RTE**: 86.32% to 84.67% (↓1.91%, not sig., vol: 152.0)
- **WL**: 81.80% to 80.59% (↓1.48%, not sig., vol: 44.8)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TK (↓24%)
[10.0% - 19%]
  - HF-INTL: AT (↓11%)
**Low Volume (denom < 50):** 1 segment excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €9.83 to €9.28 (↓5.59%, not sig., vol: 4.2K)
- **HF-NA**: €9.94 to €10.79 (↑8.58%, not sig., vol: 1.6K)
- **HF-INTL**: €10.95 to €9.95 (↓9.12%, not sig., vol: 2.8K)
- **US-HF**: €9.20 to €10.96 (↑19.15%, not sig., vol: 2.7K)
- **RTE**: €9.38 to €8.27 (↓11.79%, not sig., vol: 2.2K)
- **WL**: €5.44 to €4.97 (↓8.55%, not sig., vol: 608.9)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - WL: ER (↓27%), GN (↓23%)
  - RTE: CF (↓23%)
  - HF-INTL: DK (↓43%), NL (↓40%), AT (↓42%), ES (↑23%), CH (↑38%)
[10.0% - 19%]
  - HF-NA: US (↑19%), CA (↓16%)
  - RTE: FJ (↓13%)
  - HF-INTL: FR (↓15%), DE (↓18%), BE (↓19%), NO (↑12%), NZ (↓13%)
  - WL: CK (↑12%), AO (↓15%), CG (↑15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W19

---
