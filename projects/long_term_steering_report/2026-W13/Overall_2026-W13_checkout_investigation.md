# Payment Conversion Rate (Checkout) - Overall Summary

**Week:** 2026-W13  
**Generated:** 2026-04-10 08:05  
**Clusters:** HF-INTL, HF-NA, RTE, US-HF, WL

---

### Overall Summary

Payment Conversion Rate (Checkout) showed mixed performance globally in 2026-W13, with three clusters improving (US-HF +0.59pp, HF-INTL +0.41pp, HF-NA +0.28pp) and two declining (RTE -0.82pp, WL -0.31pp). The most critical concern is the Adyen_CreditCard integration failure in HF-NA, where success rate collapsed from 90.66% to 3.85% (-86.82pp), requiring immediate investigation.

### Cluster Highlights

- **US-HF:** PCR improved by +0.59pp (26.18% → 26.77%), driven by a +4.21pp surge in Click Submit Form conversion following the near-elimination of CC_NO_PREPAID_ERR validation errors (250 → 2 occurrences).
- **HF-INTL:** PCR improved by +0.41pp (34.47% → 34.88%), with gains in Select Payment Method (+1.00pp) partially offset by a -1.30pp decline at Successful Checkout due to increased PVS "Refused" and "Cancelled" errors.
- **WL:** PCR declined by -0.31pp (30.34% → 30.03%), primarily driven by GN country's -4.57pp drop and ProcessOut gateway degradation across CreditCard (-1.62pp) and ApplePay (-3.29pp) methods.
- **HF-NA:** PCR improved by +0.28pp (28.35% → 28.63%), led by a +2.55pp uplift in Click Submit Form, though Adyen_CreditCard experienced a catastrophic failure dropping from 90.66% to 3.85% success rate.
- **RTE:** PCR declined by -0.82pp (38.63% → 37.81%), driven by a -2.07pp drop at Select Payment Method in FJ and CF markets, compounded by Braintree_ApplePay success rate degradation (-4.40pp).

---

*Auto-generated from 5 cluster reports.*
