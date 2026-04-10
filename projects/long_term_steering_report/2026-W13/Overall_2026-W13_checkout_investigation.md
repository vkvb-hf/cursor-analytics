# Payment Conversion Rate (Checkout) - Overall Summary

**Week:** 2026-W13  
**Generated:** 2026-04-10 14:20  
**Clusters:** HF-INTL, HF-NA, RTE, US-HF, WL

---

### Overall Summary

Payment Conversion Rate (Checkout) performance was mixed across clusters in 2026-W13, with three clusters showing improvement (US-HF +0.59pp, HF-INTL +0.41pp, HF-NA +0.28pp) and two declining (RTE -0.82pp, WL -0.31pp). The most critical concern is the Adyen_CreditCard integration failures observed across multiple clusters, including a complete collapse to 3.85% success rate in HF-NA and 100% gap rate on new volume in US-HF.

### Cluster Highlights

- **US-HF:** PCR improved by +0.59pp to 26.77%, driven by a +4.21pp surge in Click Submit Form conversion following a dramatic reduction in CC_NO_PREPAID_ERR validations (250 → 2 occurrences).
- **HF-INTL:** PCR improved by +0.41pp to 34.88%, with gains at Select Payment Method (+1.00pp) offset by a -1.30pp decline at Successful Checkout due to a 75% increase in PVS failures.
- **WL:** PCR declined by -0.31pp to 30.03%, primarily driven by GN's -4.57pp PCR drop with significant frontend validation issues at Select Payment Method (-3.90pp) and FE Validation Passed (-3.79pp).
- **HF-NA:** PCR improved by +0.28pp to 28.63%, with strong Click Submit Form gains (+2.55pp) masking a critical Adyen_CreditCard failure where success rate collapsed from 90.66% to 3.85%.
- **RTE:** PCR declined by -0.82pp to 37.81%, driven by a -2.07pp drop in Select Payment Method conversion and Braintree_CreditCard volume collapse (4,329 → 125 attempts) with an -8.72pp success rate decline.

---

*Auto-generated from 5 cluster reports.*
