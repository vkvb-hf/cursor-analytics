# Steering Report - 2026-W22 (v3)

**Week:** 2026-W22  
**Generated:** 2026-06-02 14:40

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.12% to 95.20% (↑0.08%, not sig., vol: 69.8)
- **HF-NA**: 92.33% to 91.90% (↓0.46%, not sig., vol: 80.8)
- **HF-INTL**: 93.72% to 94.50% (↑0.82%, not sig., vol: 209.3)
- **US-HF**: 90.75% to 90.37% (↓0.43%, not sig., vol: 57.2)
- **RTE**: 97.25% to 97.02% (↓0.23%, not sig., vol: 73.1)
- **WL**: 96.86% to 97.14% (↑0.29%, not sig., vol: 27.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DK (↑6%), SE (↑3%)
  - WL: MR (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: FinalTokenType false (↑4%), PM Others (↑4%)
**Low Volume (denom < 50):** 4 segments excluded

### Overall Summary

Payment Checkout Approval Rate remained broadly stable across all clusters in 2026-W22, with no statistically significant changes observed. The most notable concern is the continued 8-week downward trend in US-HF, which has eroded 2.65pp from 93.02% (W15) to 90.37% (W22) alongside declining order volumes.

### Cluster Highlights

- **US-HF:** Declined by -0.42pp to 90.37% (not significant), with Apple Pay showing the largest drop (-1.08pp) among major payment methods and an ongoing 8-week erosion trend warranting monitoring.
- **HF-INTL:** Improved by +0.83pp to 94.5% (not significant), driven by DK (+6.33pp) recovery via ProcessOut and Mobilepay, though overall volume declined 9.9%.
- **WL:** Improved by +0.29pp to 97.14% (not significant), with MR the only flagged country (-2.70pp) due to ApplePay/Braintree issues on low volume (111 orders).
- **HF-NA:** Declined by -0.47pp to 91.9% (not significant), with neither US (-0.38pp) nor CA (-0.35pp) exceeding investigation thresholds.
- **RTE:** Declined by -0.24pp to 97.02% (not significant), stable with no material changes as no countries or dimensions exceeded thresholds.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.77% to 33.52% (↑2.29%, not sig., vol: 5.0K)
- **HF-NA**: 27.26% to 27.77% (↑1.84%, not sig., vol: 1.1K)
- **HF-INTL**: 34.89% to 36.84% (↑5.58%, not sig., vol: 3.3K)
- **US-HF**: 25.01% to 26.02% (↑4.04%, not sig., vol: 1.8K)
- **RTE**: 38.47% to 38.68% (↑0.55%, not sig., vol: 326.7)
- **WL**: 28.64% to 29.35% (↑2.49%, not sig., vol: 1.0K)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: IE (↑30%)
[5.0% - 19%]
  - WL: KN (↑17%), CK (↓9%), ER (↓5%)
  - HF-INTL: FR (↑8%), AU (↑6%), NO (↓5%), AT (↑8%)
  - RTE: TZ (↑11%), TT (↑6%), TO (↑8%)

### Overall Summary

Payment Conversion Rate (Checkout) improved across all clusters in 2026-W22, with gains ranging from +0.20pp (RTE) to +1.95pp (HF-INTL). A critical backend data logging issue affecting "Payment Method Listed" and "Successful Checkout" metrics (showing 0 values) was detected across all clusters and requires immediate investigation.

### Cluster Highlights

- **US-HF:** PCR improved by +1.01pp to 26.16%, driven primarily by Select Payment Method conversion (+1.20pp), though a backend data anomaly and increased Adyen_CreditCard fraud service gap (+166 transactions) require investigation.
- **HF-INTL:** PCR improved significantly by +1.95pp to 36.88%, led by exceptional gains in IE (+10.86pp) and strong Select Payment Method conversion improvement (+1.77pp) across the cluster.
- **WL:** PCR improved by +0.73pp to 29.39%, driven by improved Fraud Service approval rates (+0.89pp) and FE Validation (+0.78pp), with KN showing strong gains (+3.98pp) while CK declined (-4.15pp).
- **HF-NA:** PCR improved by +0.52pp to 27.90%, with US driving the gain (+1.01pp) through Select Payment Method improvement (+1.20pp), partially offset by CA's decline (-1.18pp) due to Click Submit Form drop (-1.61pp).
- **RTE:** PCR improved marginally by +0.20pp to 38.72%, supported by Fraud Service approval gains (+0.27pp) and Select Payment Method improvement (+0.55pp), though PVS Success declined (-0.29pp) with increased "Cancelled" errors.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 32.21% to 0.00% (↓100.00%, not sig., vol: 0.0)
- **HF-NA**: 28.26% to 0.00% (↓100.00%, not sig., vol: 0.0)
- **HF-INTL**: 36.56% to 0.00% (↓100.00%, not sig., vol: 0.0)
- **US-HF**: 26.01% to 0.00% (↓100.00%, not sig., vol: 0.0)
- **RTE**: 33.71% to 0.00% (↓100.00%, not sig., vol: 0.0)
- **WL**: 26.88% to 0.00% (↓100.00%, not sig., vol: 0.0)

**Deep Insights**
**Low Volume (denom < 50):** 31 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 89.94% to 90.64% (↑0.78%, not sig., vol: 652.2)
- **HF-NA**: 89.43% to 90.67% (↑1.40%, not sig., vol: 265.1)
- **HF-INTL**: 90.58% to 91.07% (↑0.54%, not sig., vol: 198.3)
- **US-HF**: 88.72% to 89.95% (↑1.39%, not sig., vol: 185.7)
- **RTE**: 89.38% to 89.71% (↑0.38%, not sig., vol: 72.0)
- **WL**: 89.48% to 90.86% (↑1.54%, not sig., vol: 128.2)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: FR (↑3%), NO (↓7%), CH (↑11%)
  - WL: AO (↑7%)
  - RTE: TT (↑4%)
**Dimensions:**
[2.5% - 19%]
  - WL: PM Apple Pay (↑5%)
  - RTE: PM Others (↓6%)
**Low Volume (denom < 50):** 6 segments excluded

### Overall Summary

Reactivation Rate improved across all clusters in 2026-W22, with significant gains in US-HF (+1.39%), WL (+1.54%), and HF-NA (+1.39%), while HF-INTL (+0.54%) and RTE (+0.37%) showed modest, non-significant improvements. The most notable concern is NO in HF-INTL, which experienced a -7.29pp decline driven by a +4.18pp spike in expired card declines on Credit Card payments.

### Cluster Highlights

- **US-HF:** Improved significantly by +1.39% to 89.95%, representing a recovery from W21's dip with Credit Card payments driving the strongest gains (+1.66%).
- **HF-INTL:** Improved modestly by +0.54% to 91.07% (not significant), but NO declined -7.29pp due to Credit Card expired card issues requiring monitoring.
- **WL:** Improved significantly by +1.54% to 90.86%, continuing a 5-week upward trend with AO driving gains (+7.45pp) from reduced payment blocks and improved PayPal/Apple Pay performance.
- **HF-NA:** Improved significantly by +1.39% to 90.67%, with both US (+1.39%) and CA (+0.92%) contributing positively and CA showing strong volume growth (+33.4%).
- **RTE:** Stable with marginal improvement of +0.37% to 89.71% (not significant), with low-volume country fluctuations in TZ, TT, TO, and TV not warranting escalation.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.83% to 93.43% (↑0.64%, not sig., vol: 705.3)
- **HF-NA**: 91.75% to 92.47% (↑0.79%, not sig., vol: 178.4)
- **HF-INTL**: 91.81% to 92.55% (↑0.81%, not sig., vol: 286.7)
- **US-HF**: 91.75% to 92.61% (↑0.94%, not sig., vol: 154.6)
- **RTE**: 94.31% to 94.52% (↑0.22%, not sig., vol: 84.9)
- **WL**: 92.95% to 94.14% (↑1.28%, not sig., vol: 187.9)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-INTL: BE (↑6%), LU (↑9%)
  - RTE: TZ (↑7%)
**Dimensions:**
[+50%]
  - HF-INTL: PM Unknown (↑309%), PM Credit Card (↓100%)
  - HF-NA: PM Unknown (↑274%), PM Credit Card (↑173%), PM Apple Pay (↑127%)
  - WL: PM Unknown (↑218%)

### Overall Summary

Fraud Approval Rate improved across all clusters in 2026-W22, with changes ranging from +0.22pp (RTE) to +1.28pp (WL), though only WL's improvement was statistically significant. The most notable finding is the persistent ~25-27pp FAR gap between Paid and Referral channels across all clusters, with Referral channels showing elevated duplicate block rates driving lower approval rates.

### Cluster Highlights

- **US-HF:** FAR improved by +0.94pp to 92.61% (not significant), driven by reduced Prefunded Block Rate (-0.20pp) and Duplicate Block Rate (-0.32pp), with Referral channel continuing to lag Paid by 26.52pp.
- **HF-INTL:** FAR improved by +0.81pp to 92.55% (not significant), with BE showing the largest movement (+5.94pp) driven by a 46.89% decrease in Duplicate Rate.
- **WL:** FAR improved significantly by +1.28pp to 94.14%, primarily driven by KN's Referral channel (+15.14pp FAR) following a -29.28% decrease in Duplicate Block Rate.
- **HF-NA:** FAR improved by +0.79pp to 92.47% (not significant), with both US (+0.94pp) and CA (+0.40pp) showing parallel improvement within normal operating range.
- **RTE:** FAR improved marginally by +0.22pp to 94.52% (not significant), with TZ (+6.82pp) and TK (+4.26pp) exceeding thresholds due to substantial reductions in duplicate detection rates.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 23.38% to 23.24% (↓0.59%, not sig., vol: 640.9)
- **HF-NA**: 25.88% to 25.90% (↑0.06%, not sig., vol: 13.7)
- **HF-INTL**: 33.06% to 32.28% (↓2.37%, not sig., vol: 828.9)
- **US-HF**: 24.46% to 24.39% (↓0.28%, not sig., vol: 46.4)
- **RTE**: 15.78% to 16.24% (↑2.92%, not sig., vol: 1.1K)
- **WL**: 16.78% to 15.69% (↓6.49%, not sig., vol: 950.2)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TZ (↓54%)
  - HF-INTL: CH (↑149%)
[20% - 49%]
  - HF-INTL: BE (↓48%)
  - RTE: TV (↓38%), TK (↓24%)
[10.0% - 19%]
  - WL: CK (↓20%)
  - HF-INTL: IE (↑12%), NO (↑12%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.26% to 5.10% (↓3.11%, not sig., vol: 3.4K)
- **HF-NA**: 5.51% to 5.39% (↓2.27%, not sig., vol: 505.6)
- **HF-INTL**: 6.21% to 5.89% (↓5.18%, not sig., vol: 1.8K)
- **US-HF**: 5.88% to 5.54% (↓5.93%, not sig., vol: 967.0)
- **RTE**: 4.40% to 4.45% (↑1.04%, not sig., vol: 393.3)
- **WL**: 4.93% to 4.44% (↓9.87%, not sig., vol: 1.4K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: BE (↓52%), CH (↑378%), LU (↑192%)
  - RTE: TZ (↓52%)
[20% - 49%]
  - WL: MR (↓35%)
  - HF-INTL: IE (↓36%), NL (↑30%), AT (↑28%)
  - RTE: TV (↓42%), TO (↑21%)
[10.0% - 19%]
  - HF-INTL: DE (↑11%), AU (↓14%), SE (↑18%)
  - RTE: CF (↑11%), YE (↑17%), TK (↓17%)
  - WL: KN (↓10%), GN (↓19%), ER (↓10%)
**Dimensions:**
[20% - 49%]
  - RTE: CC Paid (↑22%)
  - HF-NA: CC Paid (↓21%)
[10.0% - 19%]
  - HF-INTL: CC Paid (↓11%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.60% to 0.57% (↓5.41%, not sig., vol: 5.9K)
- **HF-NA**: 1.35% to 1.12% (↓16.79%, not sig., vol: 3.7K)
- **HF-INTL**: 0.32% to 0.38% (↑17.38%, not sig., vol: 6.1K)
- **US-HF**: 1.04% to 0.83% (↓19.96%, not sig., vol: 3.3K)
- **RTE**: 0.30% to 0.35% (↑15.04%, not sig., vol: 5.7K)
- **WL**: 0.96% to 0.76% (↓20.58%, not sig., vol: 3.0K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: DE (↑120%), AU (↑64%), BE (↓76%), DK (↓61%), NZ (↑58%)
  - WL: KN (↑221%), GN (↓100%), AO (↓100%)
  - RTE: TZ (↓100%)
[20% - 49%]
  - HF-INTL: GB (↓45%), IE (↓27%)
  - WL: MR (↓39%)
[10.0% - 19%]
  - RTE: FJ (↑17%), TK (↓13%)
  - HF-NA: US (↓20%), CA (↓11%)
  - HF-INTL: FR (↑14%), SE (↓12%)
  - WL: ER (↓14%), CG (↑12%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: CC Referral (↑43%)
  - WL: CC Paid (↓22%)
  - HF-NA: CC Referral (↓33%)
[10.0% - 19%]
  - RTE: CC Paid (↑15%), CC Referral (↑13%)
  - HF-INTL: CC Paid (↑12%)
  - WL: CC Referral (↓13%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.35% to 95.23% (↓0.13%, not sig., vol: 2.3K)
- **HF-NA**: 93.64% to 93.43% (↓0.22%, not sig., vol: 1.0K)
- **HF-INTL**: 97.57% to 97.45% (↓0.12%, not sig., vol: 855.9)
- **US-HF**: 93.23% to 92.92% (↓0.33%, not sig., vol: 1.2K)
- **RTE**: 94.84% to 94.94% (↑0.10%, not sig., vol: 400.9)
- **WL**: 91.13% to 90.97% (↓0.18%, not sig., vol: 270.7)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - RTE: PP Unknown (↓20%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓11%), PP Unknown (↓10%)
  - HF-INTL: LL a. 0 (↓4%), CustomerQuality Bad (↑5%)
  - RTE: CustomerQuality Bad (↑7%)
  - WL: CustomerQuality Bad (↓7%)

### Overall Summary

Payment Approval Rate declined marginally across all clusters in 2026-W22, with changes ranging from -0.33pp (US-HF) to +0.11pp (RTE), none of which were statistically significant. The most notable concern is a persistent multi-week downward trend in US-HF and HF-NA, with cumulative declines of -0.83pp and -0.66pp respectively over the past 7-8 weeks, driven by weakening Post-Dunning recovery rates.

### Cluster Highlights

- **US-HF:** Declined by -0.33pp to 92.92% with Post-Dunning AR showing the largest funnel drop (-0.53pp), continuing a 7-week downward trend from 93.75%.
- **HF-INTL:** Declined marginally by -0.12pp to 97.45%, with FirstRunAR showing a larger upstream drop of -0.59pp; AT had the steepest country decline at -0.58pp.
- **WL:** Declined by -0.18pp to 90.97%, with Post-Dunning AR down -0.27pp and Adyen showing the steepest provider decline at -0.66pp.
- **HF-NA:** Declined by -0.22pp to 93.43%, driven by US (-0.31pp) while CA remained stable, with Post-Dunning AR showing the largest funnel decline at -0.40pp.
- **RTE:** Improved slightly by +0.11pp to 94.94%, with all funnel stages and dimensions performing within normal parameters.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.13% to 92.93% (↓0.22%, not sig., vol: 3.6K)
- **HF-NA**: 91.84% to 91.72% (↓0.13%, not sig., vol: 590.5)
- **HF-INTL**: 94.94% to 94.48% (↓0.48%, not sig., vol: 3.4K)
- **US-HF**: 91.58% to 91.27% (↓0.33%, not sig., vol: 1.2K)
- **RTE**: 92.73% to 92.91% (↑0.18%, not sig., vol: 711.8)
- **WL**: 89.28% to 89.34% (↑0.07%, not sig., vol: 106.9)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - WL: KN (↑3%)
**Dimensions:**
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑7%), PP Unknown (↓10%)
  - HF-INTL: LL a. 0 (↓4%), CustomerQuality Bad (↑5%)
  - RTE: CustomerQuality Bad (↑6%), PP Unknown (↓18%)

### Overall Summary

Acceptance Rate (Overall) declined modestly across most clusters in 2026-W22, with changes ranging from -0.48pp (HF-INTL) to +0.19pp (RTE), though none were statistically significant. The most notable concern is the persistent 8-week downward trend observed in US-HF (-0.95pp cumulative) and HF-NA (-0.67pp cumulative), alongside a broad systemic decline across all funnel stages in HF-INTL.

### Cluster Highlights

- **US-HF:** Declined by -0.31pp to 91.27% with an 8-week downward trend; PostDunningAR showed the largest funnel degradation at -0.53pp, suggesting weakening dunning recovery effectiveness.
- **HF-INTL:** Declined by -0.48pp to 94.48% with parallel declines across all funnel stages (-0.12pp to -0.59pp); AT (-1.57pp), LU (-1.41pp), and BE (-1.21pp) led country-level drops but remained within thresholds.
- **WL:** Stable at 89.34% (+0.07pp); KN exceeded the ±2.5% threshold with a +2.65pp improvement driven by PayPal (+6.56pp) and resolution of "Other reasons" declines.
- **HF-NA:** Declined marginally by -0.13pp to 91.72% continuing an 8-week erosion trend; US declined -0.32pp while CA improved +0.51pp, with PostDunningAR showing the largest funnel drop at -0.40pp.
- **RTE:** Improved slightly by +0.19pp to 92.91% with stable performance across all funnel stages and payment methods; no countries exceeded investigation thresholds.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.75% to 90.66% (↓1.19%, not sig., vol: 908.6)
- **HF-NA**: 88.20% to 87.09% (↓1.26%, not sig., vol: 183.5)
- **HF-INTL**: 92.14% to 90.15% (↓2.16%, not sig., vol: 497.8)
- **US-HF**: 86.57% to 85.43% (↓1.31%, not sig., vol: 130.8)
- **RTE**: 93.06% to 92.81% (↓0.27%, not sig., vol: 73.7)
- **WL**: 91.97% to 91.07% (↓0.98%, not sig., vol: 111.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↓4%), AT (↓6%), CH (↓3%)
  - WL: CK (↓8%), ER (↑3%), AO (↓4%)
  - RTE: TZ (↓3%), TO (↓3%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PP ProcessOut (↓3%), PP Braintree (↓3%), PM Credit Card (↓3%), PM Apple Pay (↓3%)
  - WL: PM Credit Card (↓3%), PP Adyen (↓6%)
  - HF-NA: PM Paypal (↓4%), PP Unknown (↓6%)
  - RTE: PP Unknown (↓14%)

### Overall Summary

Acceptance Rate (Initial Charges) declined across all five clusters in 2026-W22, with HF-INTL experiencing the largest drop (-2.16%) and RTE the smallest (-0.27%). The most significant concern is the sustained 7-week downward trend in US-HF (89.64% → 85.43%) combined with systemic ProcessOut credit card processing issues affecting both US-HF and HF-INTL markets.

### Cluster Highlights

- **US-HF:** Declined from 86.57% to 85.43% (-1.32%), continuing a 7-week downward trend driven by Credit Card (-2.51%) and ProcessOut (-2.22%) degradation.
- **HF-INTL:** Significant decline from 92.14% to 90.15% (-2.16%), driven by AT (-5.81%) and DE (-4.39%) where ProcessOut credit card acceptance dropped over 11% with rising Insufficient Funds declines.
- **WL:** Declined from 91.97% to 91.07% (-0.98%, not significant), with CK (-8.24%) experiencing a 24% drop in PayPal/Braintree transactions due to increased Insufficient Funds.
- **HF-NA:** Declined from 88.20% to 87.09% (-1.26%), driven by PayPal underperformance (-4.50%) and a 4-week sustained downward trend from 90.16% in W17.
- **RTE:** Stable decline from 93.06% to 92.81% (-0.27%, not significant), with minor impacts from low-volume markets TZ (-3.41%) and TO (-2.67%).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.19% to 93.03% (↓0.17%, not sig., vol: 2.8K)
- **HF-NA**: 91.95% to 91.87% (↓0.08%, not sig., vol: 358.8)
- **HF-INTL**: 95.05% to 94.63% (↓0.44%, not sig., vol: 3.0K)
- **US-HF**: 91.71% to 91.44% (↓0.29%, not sig., vol: 1.1K)
- **RTE**: 92.71% to 92.91% (↑0.22%, not sig., vol: 778.7)
- **WL**: 89.06% to 89.20% (↑0.15%, not sig., vol: 208.2)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - WL: KN (↑3%)
**Dimensions:**
[20% - 49%]
  - HF-INTL: PP Unknown (↑20%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↑7%), PP Unknown (↓15%)
  - RTE: CustomerQuality Bad (↑6%)
  - HF-INTL: CustomerQuality Bad (↑5%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 53.01% to 53.67% (↑1.26%, not sig., vol: 877.2)
- **HF-NA**: 46.48% to 44.69% (↓3.85%, not sig., vol: 639.5)
- **HF-INTL**: 68.71% to 70.64% (↑2.82%, not sig., vol: 805.0)
- **US-HF**: 45.48% to 44.21% (↓2.79%, not sig., vol: 368.3)
- **RTE**: 44.20% to 44.09% (↓0.24%, not sig., vol: 41.8)
- **WL**: 31.67% to 30.84% (↓2.62%, not sig., vol: 198.1)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - WL: MR (↓41%), CK (↓21%)
  - RTE: TV (↑34%), TT (↓27%), TK (↑22%)
[10.0% - 19%]
  - WL: ER (↑16%), CG (↑14%)

### Overall Summary

Dunning Ship Rate declined modestly across most clusters during the transition from Post-Payday to Mid-Cycle phase in 2026-W22, with HF-INTL being the notable exception showing +1.93pp improvement. The most significant concern is the sharp Discount % increases observed in US-HF (+21.9%), HF-NA (+18.8%), and WL's CK market (+37.3%), which are negatively impacting conversion despite stable upstream authorization rates.

### Cluster Highlights

- **US-HF:** Ship Rate declined by 1.27pp (45.48% → 44.21%) driven primarily by a +21.9% increase in Discount % during the Mid-Cycle phase, representing expected cyclical behavior.
- **HF-INTL:** Ship Rate improved by 1.93pp (68.71% → 70.64%) driven by strong PC2 gains (+6.7%), with FR leading performance (+8.7% SR) while AU was the only detractor (-2.8% SR).
- **WL:** Ship Rate declined by 0.83pp (31.67% → 30.84%) with CK experiencing a severe -20.7% drop driven by a +37.3% Discount % increase that failed to convert to shipments.
- **HF-NA:** Ship Rate declined by 1.79pp (46.48% → 44.69%) driven by substantial Discount % increases (+18.8% cluster-wide), with CA showing the steepest decline (-7.3%) despite improved PC2.
- **RTE:** Ship Rate remained essentially stable at 44.09% (-0.11pp) as strong PC2 improvement (+9.5%) offset increased discount pressure, though TT warrants monitoring after a -27.0% drop on low volume.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 45.65% to 42.63% (↓6.62%, not sig., vol: 2.5K)
- **HF-NA**: 43.79% to 35.74% (↓18.37%, not sig., vol: 1.4K)
- **HF-INTL**: 44.42% to 43.65% (↓1.73%, not sig., vol: 348.5)
- **US-HF**: 44.70% to 36.58% (↓18.17%, not sig., vol: 1.1K)
- **RTE**: 50.34% to 46.73% (↓7.17%, not sig., vol: 539.7)
- **WL**: 45.56% to 42.45% (↓6.84%, not sig., vol: 159.3)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - WL: CK (↓21%), KN (↑29%)
  - HF-INTL: NL (↑28%)
  - RTE: TZ (↓29%)
[10.0% - 19%]
  - HF-NA: US (↓18%), CA (↓20%)
  - HF-INTL: BE (↓16%), IE (↑18%), SE (↑15%), AT (↓20%), CH (↑17%)
  - WL: ER (↓14%), GN (↑20%)
  - RTE: CF (↓11%)
**Low Volume (denom < 50):** 3 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 86.20% to 86.96% (↑0.89%, not sig., vol: 400.6)
- **HF-NA**: 78.96% to 81.46% (↑3.17%, not sig., vol: 271.8)
- **HF-INTL**: 89.33% to 89.67% (↑0.39%, not sig., vol: 98.9)
- **US-HF**: 78.60% to 80.89% (↑2.92%, not sig., vol: 178.1)
- **RTE**: 85.07% to 85.51% (↑0.52%, not sig., vol: 43.5)
- **WL**: 83.89% to 83.27% (↓0.74%, not sig., vol: 19.6)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - HF-INTL: IT (↓23%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €10.63 to €11.19 (↑5.22%, not sig., vol: 3.9K)
- **HF-NA**: €11.44 to €11.42 (↓0.14%, not sig., vol: 24.1)
- **HF-INTL**: €11.48 to €12.45 (↑8.46%, not sig., vol: 2.9K)
- **US-HF**: €11.49 to €11.07 (↓3.62%, not sig., vol: 463.8)
- **RTE**: €9.89 to €10.32 (↑4.34%, not sig., vol: 781.6)
- **WL**: €5.81 to €5.82 (↑0.25%, not sig., vol: 14.9)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: NL (↑135%), ES (↑80%)
[20% - 49%]
  - WL: AO (↑25%)
  - HF-INTL: AT (↑33%), IT (↓44%)
[10.0% - 19%]
  - HF-INTL: FR (↑16%), DE (↑19%), DK (↑11%), CH (↑17%)
  - HF-NA: CA (↑11%)
  - WL: CG (↓12%), GN (↓15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W22

---
