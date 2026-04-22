# Steering Report - 2026-W16 (v3)

**Week:** 2026-W16  
**Generated:** 2026-04-22 11:57

---

## Payment Checkout Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 96.25% to 96.54% (↑0.30%, not sig., vol: 350.5)
- **HF-NA**: 94.08% to 93.86% (↓0.23%, not sig., vol: 54.7)
- **HF-INTL**: 96.12% to 97.13% (↑1.05%, not sig., vol: 392.2)
- **US-HF**: 93.02% to 92.75% (↓0.29%, not sig., vol: 52.6)
- **RTE**: 97.22% to 97.20% (↓0.01%, not sig., vol: 5.7)
- **WL**: 97.37% to 97.59% (↑0.22%, not sig., vol: 24.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: DE (↑4%), BE (↑4%)
  - RTE: TT (↑8%)
  - WL: MR (↑3%)
**Dimensions:**
[2.5% - 19%]
  - HF-INTL: PM Others (↑7%)
  - RTE: PM Others (↑9%)
**Low Volume (denom < 50):** 1 segment excluded

**Overall AI summary:**

### Overall Summary

Payment Checkout Approval Rate remained broadly stable across clusters in 2026-W16, with changes ranging from -0.29pp to +1.01pp. The most significant development was HF-INTL's statistically significant improvement to 97.13%, driven by volume shifts away from underperforming Klarna and BcmcMobile payment methods in DE and BE respectively.

### Cluster Highlights

- **US-HF:** Stable at 92.75% (-0.29pp), a non-significant decline within normal weekly fluctuation with no payment methods or countries flagged.
- **HF-INTL:** Improved significantly by +1.01pp to 97.13%, driven by DE (+4.35pp) and BE (+3.72pp) as volume shifted away from underperforming Klarna via Adyen in DE (-10.81pp) and BcmcMobile via Adyen in BE (-6.61pp).
- **WL:** Stable at 97.59% (+0.22pp), a non-significant improvement with MR flagged but based on only 57 orders making it statistically unreliable.
- **HF-NA:** Stable at 93.86% (-0.23pp), a non-significant decline with both US and CA remaining within normal variance and no material mix shift impact.
- **RTE:** Stable at 97.2% (-0.02pp), with TT showing +7.93pp improvement driven by IDeal via Adyen gains, though overall impact minimal due to low volume (1,223 orders).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Page Visit to Success

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 36.45% to 36.83% (↑1.04%, not sig., vol: 2.4K)
- **HF-NA**: 27.92% to 27.46% (↓1.64%, not sig., vol: 1.2K)
- **HF-INTL**: 37.70% to 37.03% (↓1.78%, not sig., vol: 1.4K)
- **US-HF**: 26.14% to 25.73% (↓1.59%, not sig., vol: 885.1)
- **RTE**: 45.53% to 48.85% (↑7.29%, not sig., vol: 4.1K)
- **WL**: 34.83% to 35.78% (↑2.72%, not sig., vol: 850.3)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TT (↑31%)
  - HF-INTL: LU (↑43%)
[5.0% - 19%]
  - RTE: FJ (↑12%), YE (↓7%), TZ (↑10%)
  - HF-INTL: FR (↓6%), IE (↓13%), NZ (↑10%), DK (↓6%), NO (↓5%)
  - WL: MR (↓7%)

**Overall AI summary:**

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance across clusters in 2026-W16, with RTE improving significantly (+3.33pp) and WL showing moderate gains (+0.97pp), while US-HF (-0.41pp), HF-INTL (-0.66pp), and HF-NA (-0.44pp) all declined. The most significant concern across clusters is the widespread drop in Fraud Service approval rates, particularly in US-HF (-1.04pp) and HF-NA (-0.88pp), which warrants immediate investigation into potential fraud rule changes or model updates.

### Cluster Highlights

- **US-HF:** PCR declined by -0.41pp (26.24% → 25.83%), driven primarily by a -1.04pp drop in Fraud Service approval rate and a -2.14pp decline in Braintree_ApplePay success rate.
- **HF-INTL:** PCR declined by -0.66pp (37.75% → 37.09%), driven by a -1.27pp drop at Select Payment Method, with IE (-7.09pp), GB (-1.80pp), and FR (-1.55pp) most affected.
- **WL:** PCR improved by +0.97pp (34.86% → 35.83%), driven by a +1.01pp gain at Select Payment Method, with CG showing strong improvement (+1.84pp) while MR declined (-1.52pp).
- **HF-NA:** PCR declined by -0.44pp (27.99% → 27.55%), driven by a -0.88pp drop in Fraud Service approval rate concentrated in US (-1.04pp), while Braintree_ApplePay success rate fell -1.75pp.
- **RTE:** PCR improved significantly by +3.33pp (45.59% → 48.92%), driven by a +3.43pp gain at Select Payment Method and a +4.34pp improvement in Braintree_ApplePay success rate, with FJ contributing the largest gains (+5.15pp).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Page Visit to Success (Backend)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 34.58% to 34.74% (↑0.46%, not sig., vol: 1.6K)
- **HF-NA**: 29.59% to 29.18% (↓1.39%, not sig., vol: 1.1K)
- **HF-INTL**: 40.55% to 39.95% (↓1.48%, not sig., vol: 1.4K)
- **US-HF**: 27.68% to 27.36% (↓1.15%, not sig., vol: 680.6)
- **RTE**: 35.56% to 35.97% (↑1.15%, not sig., vol: 1.4K)
- **WL**: 28.80% to 29.52% (↑2.53%, not sig., vol: 1.1K)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TT (↑29%)
  - HF-INTL: LU (↑21%)
[5.0% - 19%]
  - HF-INTL: FR (↓5%), IE (↓9%), NZ (↑10%), DK (↓8%), BE (↓5%)
  - WL: MR (↓7%), CK (↑6%), GN (↑6%), AO (↑5%)
  - RTE: YE (↓5%), TV (↓8%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Reactivation Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 90.71% to 90.01% (↓0.77%, not sig., vol: 744.4)
- **HF-NA**: 90.24% to 89.41% (↓0.91%, not sig., vol: 218.6)
- **HF-INTL**: 91.47% to 91.23% (↓0.27%, not sig., vol: 122.3)
- **US-HF**: 90.47% to 90.07% (↓0.44%, not sig., vol: 83.2)
- **RTE**: 90.41% to 89.16% (↓1.39%, not sig., vol: 257.4)
- **WL**: 89.29% to 86.81% (↓2.77%, not sig., vol: 222.3)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-NA: CA (↓3%)
  - WL: CK (↓6%), MR (↓4%), AO (↓4%)
  - RTE: CF (↓4%), YE (↑7%)
  - HF-INTL: CH (↓5%)
**Dimensions:**
[2.5% - 19%]
  - WL: FinalTokenType false (↓3%), PM Credit Card (↓3%), FinalTokenType true (↑3%)
  - RTE: PM Others (↑13%)
**Low Volume (denom < 50):** 5 segments excluded

**Overall AI summary:**

### Overall Summary

Reactivation Rate declined across most clusters in 2026-W16, with WL experiencing the most significant drop of -2.78% (from 89.29% to 86.81%). The primary concern is the broad-based Credit Card performance degradation, particularly in WL's CK market where all payment methods declined and card validity issues increased substantially.

### Cluster Highlights

- **US-HF:** Declined by -0.44% to 90.07% (not significant), with Credit Card payments showing the largest rate decline at -1.00% while PayPal and Apple Pay improved.
- **HF-INTL:** Declined by -0.26% to 91.23% (not significant), with CH flagged for Apple Pay decline (-20.00%) though impact limited by low volume (55 orders).
- **WL:** Significant decline of -2.78% to 86.81%, driven by CK (-5.69%), AO (-3.83%), and MR (-3.64%), with rising "Expired, Invalid, Closed Card" declines in CK.
- **HF-NA:** Declined by -0.92% to 89.41% (not significant), with CA exceeding threshold at -2.57% due to Credit Card decline (-3.05%) and increased fraud-related declines (+0.88pp).
- **RTE:** Significant decline of -1.38% to 89.16%, primarily driven by CF's -4.03% drop in Credit Card performance and a dramatic -78.2% volume collapse in YE.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Fraud Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 92.64% to 92.53% (↓0.12%, not sig., vol: 163.2)
- **HF-NA**: 89.70% to 89.82% (↑0.14%, not sig., vol: 37.4)
- **HF-INTL**: 92.14% to 92.06% (↓0.09%, not sig., vol: 41.9)
- **US-HF**: 89.28% to 89.68% (↑0.45%, not sig., vol: 92.2)
- **RTE**: 94.68% to 94.42% (↓0.27%, not sig., vol: 126.2)
- **WL**: 93.28% to 92.95% (↓0.35%, not sig., vol: 50.5)

**Deep Insights**
**Business Units:**
[5.0% - 19%]
  - HF-INTL: LU (↓6%)
**Dimensions:**
[+50%]
  - HF-NA: PM Credit Card (↓100%)
  - WL: PM Credit Card (↑51%)
[5.0% - 19%]
  - HF-NA: CC Referral (↑6%)
**Low Volume (denom < 50):** 3 segments excluded

**Overall AI summary:**

### Overall Summary

Fraud Approval Rate remained stable globally in 2026-W16, with all clusters showing statistically insignificant changes ranging from -0.35% to +0.45%. The most significant concern is the systemic Referral channel degradation observed across multiple clusters, with duplicate rates increasing and PF Block rates showing high volatility, particularly in KN Referral (WL) which experienced a critical -16.91pp FAR decline.

### Cluster Highlights

- **US-HF:** FAR improved slightly by +0.45pp to 89.68% (not significant), driven by a sharp -58.26% drop in PF Block Rate within the Referral channel which warrants monitoring.
- **HF-INTL:** FAR declined marginally by -0.09pp to 92.06% (not significant), with systemic Referral channel degradation across all 10 deep-dive countries and duplicate rates rising to 33.28%.
- **WL:** FAR declined by -0.35pp to 92.95% (not significant), but KN Referral requires immediate investigation due to a critical -16.91pp FAR drop with duplicate rates nearly doubling (+91.81%).
- **HF-NA:** FAR improved slightly by +0.14pp to 89.82% (not significant), with divergent Referral channel trends as US Referral improved +10.21pp while CA Referral declined -4.17pp.
- **RTE:** FAR declined by -0.27pp to 94.42% (not significant), with TT showing strong improvement (+4.47pp) while TO Referral declined -9.79pp due to a +72.88% surge in duplicate rates.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Total Duplicate Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 22.75% to 24.52% (↑7.76%, not sig., vol: 10.3K)
- **HF-NA**: 26.78% to 28.35% (↑5.84%, not sig., vol: 1.6K)
- **HF-INTL**: 31.14% to 33.55% (↑7.73%, not sig., vol: 3.5K)
- **US-HF**: 26.17% to 27.86% (↑6.46%, not sig., vol: 1.3K)
- **RTE**: 14.75% to 15.82% (↑7.30%, not sig., vol: 3.4K)
- **WL**: 15.90% to 17.28% (↑8.65%, not sig., vol: 1.2K)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TV (↑75%), TK (↑57%)
[20% - 49%]
  - WL: KN (↑23%)
  - RTE: TT (↓26%), TO (↑47%)
  - HF-INTL: AT (↑28%)
[10.0% - 19%]
  - HF-INTL: DE (↑14%)
  - RTE: CF (↑15%), YE (↑12%), TZ (↑17%)
  - WL: MR (↑20%), GN (↑14%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Total Duplicate Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 5.60% to 6.12% (↑9.18%, not sig., vol: 12.2K)
- **HF-NA**: 6.49% to 7.79% (↑19.99%, not sig., vol: 5.4K)
- **HF-INTL**: 6.76% to 6.93% (↑2.52%, not sig., vol: 1.1K)
- **US-HF**: 6.80% to 8.23% (↑21.09%, not sig., vol: 4.3K)
- **RTE**: 4.17% to 4.61% (↑10.56%, not sig., vol: 5.0K)
- **WL**: 5.03% to 5.31% (↑5.46%, not sig., vol: 774.1)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TV (↑87%), TO (↑56%)
  - HF-INTL: CH (↓54%)
[20% - 49%]
  - HF-NA: US (↑21%)
  - HF-INTL: BE (↑28%), IE (↑28%), NZ (↓25%), NO (↓24%), AT (↑29%)
  - WL: MR (↑23%), KN (↑22%)
  - RTE: TT (↓28%), TK (↑34%)
[10.0% - 19%]
  - RTE: FJ (↑10%), YE (↑17%)
  - HF-INTL: FR (↑19%), AU (↓11%)
  - HF-NA: CA (↑14%)
  - WL: ER (↓19%)
**Dimensions:**
[+50%]
  - HF-NA: CC Paid (↑65%)
[20% - 49%]
  - RTE: CC Paid (↑21%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Fraud Block Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 0.85% to 0.64% (↓24.25%, not sig., vol: 32.3K)
- **HF-NA**: 2.77% to 1.62% (↓41.56%, not sig., vol: 11.3K)
- **HF-INTL**: 0.25% to 0.28% (↑13.90%, not sig., vol: 6.3K)
- **US-HF**: 3.00% to 1.38% (↓54.11%, not sig., vol: 11.0K)
- **RTE**: 0.31% to 0.33% (↑7.57%, not sig., vol: 3.6K)
- **WL**: 0.69% to 0.97% (↑39.10%, not sig., vol: 5.5K)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-NA: US (↓54%)
  - HF-INTL: GB (↑52%), FR (↑51%), NL (↑94%), BE (↑61%), AT (↓100%)
  - WL: GN (↓100%), CG (↑61%), MR (↑53%)
[20% - 49%]
  - HF-INTL: DE (↓30%), IE (↓37%), DK (↓22%), NO (↓21%), LU (↓31%)
  - WL: ER (↑23%), KN (↓23%)
  - RTE: TK (↑21%)
**Dimensions:**
[+50%]
  - HF-INTL: CC Referral (↑85%)
  - RTE: CC Referral (↑97%)
  - HF-NA: CC Referral (↓50%)
[20% - 49%]
  - WL: CC Paid (↑41%)
[10.0% - 19%]
  - HF-NA: CC Paid (↓20%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Payment Approval Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 95.35% to 95.45% (↑0.10%, not sig., vol: 1.9K)
- **HF-NA**: 94.10% to 94.13% (↑0.04%, not sig., vol: 182.0)
- **HF-INTL**: 97.27% to 97.40% (↑0.14%, not sig., vol: 1.1K)
- **US-HF**: 93.76% to 93.82% (↑0.07%, not sig., vol: 306.7)
- **RTE**: 94.87% to 94.81% (↓0.06%, not sig., vol: 255.8)
- **WL**: 91.65% to 91.69% (↑0.04%, not sig., vol: 65.1)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - WL: CustomerQuality Bad (↓21%)
[2.5% - 19%]
  - HF-INTL: CustomerQuality Bad (↓20%), LL a. 0 (↑3%), PP Unknown (↑3%)
  - RTE: CustomerQuality Bad (↓16%), PP Unknown (↓13%)
  - HF-NA: CustomerQuality Bad (↓8%), LL a. 0 (↑3%)
  - WL: LL a. 0 (↑3%), PP Unknown (↑3%)

**Overall AI summary:**

### Overall Summary

Payment Approval Rate remained stable across all clusters in 2026-W16, with changes ranging from -0.06pp to +0.13pp, none of which were statistically significant. All clusters continue positive 8-week trends, with the "Unknown" PaymentProvider showing volatility across multiple clusters but representing negligible volume (<0.5% of orders).

### Cluster Highlights

- **US-HF:** Stable at 93.82% (+0.06pp), with ProcessOut improving +1.88pp and upstream funnel declines offset by effective downstream recovery mechanisms.
- **HF-INTL:** Improved to 97.4% (+0.13pp) on strong volume growth (+8.0% WoW), driven by DE (+11.3%) and GB (+12.7%) volume increases with all countries maintaining high-AR tier performance.
- **WL:** Stable at 91.69% (+0.04pp), continuing an 8-week upward trend from 89.92% with no countries or dimensions exceeding investigation thresholds.
- **HF-NA:** Stable at 94.13% (+0.03pp), with ProcessOut showing the strongest improvement (+0.49pp) while Apple Pay remains the lowest-performing payment method at 89.07%.
- **RTE:** Minor decline to 94.81% (-0.06pp) within normal variance, with "Unknown" provider dropping -12.90pp but impacting only 130 orders (<0.01pp overall effect).

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## AR Pre Dunning

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.26% to 93.24% (↓0.02%, not sig., vol: 348.0)
- **HF-NA**: 92.42% to 92.31% (↓0.12%, not sig., vol: 618.5)
- **HF-INTL**: 94.74% to 94.81% (↑0.07%, not sig., vol: 596.2)
- **US-HF**: 92.22% to 92.10% (↓0.13%, not sig., vol: 564.9)
- **RTE**: 92.83% to 92.65% (↓0.20%, not sig., vol: 854.5)
- **WL**: 90.10% to 90.03% (↓0.08%, not sig., vol: 136.8)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - HF-INTL: CustomerQuality Bad (↓20%)
  - WL: CustomerQuality Bad (↓21%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓15%), LL a. 0 (↑3%)
  - RTE: CustomerQuality Bad (↓15%), PP Unknown (↓13%)
  - HF-INTL: LL a. 0 (↑3%), PP Unknown (↑4%)
  - WL: LL a. 0 (↑3%), PP Unknown (↑3%)

**Overall AI summary:**

### Overall Summary

Acceptance Rate (Overall) remained stable across all clusters in 2026-W16, with changes ranging from -0.19pp to +0.07pp, none of which were statistically significant. All clusters are performing within normal weekly variance with no material concerns or actionable findings requiring escalation.

### Cluster Highlights

- **US-HF:** Declined by -0.13pp to 92.1% with no significant drivers; PaymentProvider "Unknown" showed a -10.77pp drop but on minimal volume (226 orders).
- **HF-INTL:** Improved marginally by +0.07pp to 94.81%; NO showed the largest country decline at -2.03pp but remained below investigation threshold.
- **WL:** Declined by -0.08pp to 90.03%, continuing a positive 8-week trend (+1.84pp since W09) with no dimensional concerns.
- **HF-NA:** Declined by -0.12pp to 92.31% with Credit Card showing the largest segment decline (-0.21pp) across 377,622 orders.
- **RTE:** Declined by -0.19pp to 92.65%; FJ (92% of volume) remained stable and no countries exceeded the ±2.5% threshold.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Acceptance LL0 (Initial Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 91.29% to 91.37% (↑0.09%, not sig., vol: 84.6)
- **HF-NA**: 89.82% to 89.44% (↓0.41%, not sig., vol: 75.0)
- **HF-INTL**: 91.78% to 91.31% (↓0.51%, not sig., vol: 178.3)
- **US-HF**: 89.39% to 88.90% (↓0.55%, not sig., vol: 68.1)
- **RTE**: 91.73% to 92.56% (↑0.90%, not sig., vol: 289.4)
- **WL**: 91.05% to 91.28% (↑0.26%, not sig., vol: 33.8)

**Deep Insights**
**Business Units:**
[2.5% - 19%]
  - HF-INTL: NZ (↓11%), AU (↑3%), NL (↓3%), SE (↑3%), LU (↓5%)
  - WL: CK (↓4%), GN (↑4%), AO (↑3%)
  - RTE: YE (↑3%), TO (↑5%), TV (↑5%)
**Dimensions:**
[2.5% - 19%]
  - RTE: PP Unknown (↓13%)
  - HF-NA: PP Adyen (↓4%)

**Overall AI summary:**

### Overall Summary

Acceptance Rate (Initial Charges) remained broadly stable across all clusters in 2026-W16, with changes ranging from -0.55pp to +0.90pp, none of which were statistically significant. The most notable finding was NZ's -10.84pp decline in HF-INTL driven by a surge in Insufficient Funds declines (+7.48pp) amid a 113% volume increase, warranting continued monitoring.

### Cluster Highlights

- **US-HF:** Declined by -0.55pp (89.39% → 88.9%) within normal variance, with "Unknown" PaymentProvider showing a notable -4.00pp drop on low volume (170 orders).
- **HF-INTL:** Declined by -0.51pp (91.78% → 91.31%) with NZ experiencing a significant -10.84pp drop driven by Insufficient Funds increases via ProcessOut, despite 113% volume growth.
- **WL:** Improved slightly by +0.23pp (91.05% → 91.28%), with CK declining -4.02pp due to credit card/Adyen performance offset by gains in GN (+4.04pp) and AO (+2.64pp).
- **HF-NA:** Declined marginally by -0.42pp (89.82% → 89.44%) with no dimensions exceeding thresholds and all funnel metrics moving in parallel.
- **RTE:** Improved by +0.90pp (91.73% → 92.56%) driven by reduced Insufficient Funds declines in YE, TV, and TO, returning to W12 performance levels.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Acceptance LL0 and LL1+ (Recurring Charge)

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 93.36% to 93.34% (↓0.01%, not sig., vol: 235.4)
- **HF-NA**: 92.51% to 92.41% (↓0.10%, not sig., vol: 501.0)
- **HF-INTL**: 94.86% to 94.97% (↑0.12%, not sig., vol: 942.9)
- **US-HF**: 92.30% to 92.19% (↓0.11%, not sig., vol: 463.3)
- **RTE**: 92.92% to 92.66% (↓0.28%, not sig., vol: 1.1K)
- **WL**: 90.03% to 89.92% (↓0.12%, not sig., vol: 184.1)

**Deep Insights**
**Dimensions:**
[20% - 49%]
  - WL: CustomerQuality Bad (↓21%)
[2.5% - 19%]
  - HF-NA: CustomerQuality Bad (↓15%), PP Unknown (↑7%)
  - HF-INTL: CustomerQuality Bad (↓20%), PP Unknown (↑14%)
  - RTE: CustomerQuality Bad (↓15%)
**Low Volume (denom < 50):** 2 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Ship Rate

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 51.48% to 52.56% (↑2.10%, not sig., vol: 1.6K)
- **HF-NA**: 48.18% to 48.10% (↓0.16%, not sig., vol: 30.0)
- **HF-INTL**: 65.59% to 66.79% (↑1.83%, not sig., vol: 555.9)
- **US-HF**: 46.72% to 47.68% (↑2.06%, not sig., vol: 290.6)
- **RTE**: 42.62% to 43.92% (↑3.06%, not sig., vol: 631.2)
- **WL**: 31.08% to 31.89% (↑2.59%, not sig., vol: 215.9)

**Deep Insights**
**Business Units:**
[+50%]
  - WL: MR (↑89%)
  - RTE: TV (↑110%)
[20% - 49%]
  - WL: GN (↑28%)
[10.0% - 19%]
  - HF-INTL: NZ (↓13%)
  - RTE: TZ (↑13%), TK (↓12%)

**Overall AI summary:**

### Overall Summary

Dunning Recovery Rate improved across most clusters in 2026-W16, with gains ranging from +0.74pp to +1.21pp driven by the Pre-Payday to Payday phase transition. The most significant concern is NZ in HF-INTL, which declined -13.3% counter to expected Payday behavior, and CA in HF-NA, which dropped -6.7% despite increased discounting.

### Cluster Highlights

- **US-HF:** Ship Rate improved +0.89pp (46.72% → 47.61%) driven by Payday phase timing effects that overcame a +6.6% increase in Discount %.
- **HF-INTL:** Ship Rate improved +1.15pp (65.58% → 66.73%) led by NO (+7.3%) and AU (+7.0%), though NZ declined -13.3% requiring investigation.
- **WL:** Ship Rate improved +0.74pp (31.07% → 31.81%) driven by GN (+27.4%) and AO (+6.4%), partially offset by CK declining -6.6% due to elevated discounting.
- **HF-NA:** Ship Rate declined -0.16pp (48.19% → 48.03%) as CA's sharp -6.7% drop offset US's +1.9% improvement despite Payday phase transition.
- **RTE:** Ship Rate improved +1.21pp (42.61% → 43.82%) with broad-based gains across FJ (+3.7%) and YE (+4.2%), supported by a -4.1% reduction in Discount %.

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Recovery W0

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 41.75% to 44.21% (↑5.88%, not sig., vol: 2.4K)
- **HF-NA**: 37.81% to 40.14% (↑6.18%, not sig., vol: 541.2)
- **HF-INTL**: 42.73% to 45.45% (↑6.35%, not sig., vol: 1.3K)
- **US-HF**: 41.49% to 42.28% (↑1.92%, not sig., vol: 129.4)
- **RTE**: 44.05% to 46.05% (↑4.55%, not sig., vol: 411.7)
- **WL**: 39.50% to 41.89% (↑6.05%, not sig., vol: 160.8)

**Deep Insights**
**Business Units:**
[+50%]
  - RTE: TO (↑101%)
  - HF-INTL: CH (↓56%)
[20% - 49%]
  - HF-INTL: FR (↓27%), NO (↑32%), SE (↑33%)
  - HF-NA: CA (↑22%)
[10.0% - 19%]
  - HF-INTL: GB (↑15%), DE (↑14%)
  - WL: CK (↑18%), GN (↑18%), KN (↓18%)
  - RTE: CF (↑17%)
**Low Volume (denom < 50):** 3 segments excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Recovery W12

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: 85.11% to 85.77% (↑0.77%, not sig., vol: 334.1)
- **HF-NA**: 81.02% to 80.57% (↓0.56%, not sig., vol: 55.3)
- **HF-INTL**: 87.99% to 88.94% (↑1.08%, not sig., vol: 236.2)
- **US-HF**: 81.07% to 80.99% (↓0.10%, not sig., vol: 6.9)
- **RTE**: 84.01% to 84.61% (↑0.72%, not sig., vol: 61.2)
- **WL**: 81.81% to 82.74% (↑1.15%, not sig., vol: 32.7)

**Deep Insights**
**Business Units:**
[20% - 49%]
  - RTE: TV (↑33%)
[10.0% - 19%]
  - WL: GN (↑11%)
  - HF-INTL: ES (↑11%)
**Low Volume (denom < 50):** 1 segment excluded

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---

## Dunning Profit

**Anomaly Detection:**

**Prev Week vs Current Week:**
- **Overall**: €9.87 to €10.18 (↑3.10%, not sig., vol: 2.4K)
- **HF-NA**: €11.40 to €11.38 (↓0.18%, not sig., vol: 34.4)
- **HF-INTL**: €9.67 to €10.54 (↑8.96%, not sig., vol: 3.0K)
- **US-HF**: €11.65 to €11.29 (↓3.06%, not sig., vol: 446.4)
- **RTE**: €10.25 to €10.15 (↓0.99%, not sig., vol: 180.7)
- **WL**: €5.51 to €5.22 (↓5.15%, not sig., vol: 361.3)

**Deep Insights**
**Business Units:**
[+50%]
  - HF-INTL: GB (↑60%), ES (↑452%)
  - WL: GN (↑55%)
[20% - 49%]
  - HF-INTL: NZ (↑23%), AT (↓32%), LU (↑39%)
[10.0% - 19%]
  - HF-INTL: AU (↓12%), SE (↑15%), IE (↑13%), NL (↑12%)
  - RTE: YE (↓18%)
  - HF-NA: CA (↑10%)
  - WL: ER (↓11%), CK (↓16%), CG (↓15%)

**Link to detailed github report:** https://github.com/vkvb-hf/cursor-analytics/tree/main/projects/long_term_steering_report/2026-W16

---
