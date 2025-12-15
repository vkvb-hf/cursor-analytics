# Payments P0 Metrics ([Table](https://tableau.hellofresh.io/views/PaymentsP0metrics_17284783585740/PaymentsP0Metrics) / [Chart](https://tableau.hellofresh.io/views/PaymentsP0metrics_17284783585740/TrendofP0Metrics) / [Sheet](https://docs.google.com/spreadsheets/d/1mBc1VhdlsOq35mpPBJR8LwTqgJyvn6o3EBzcfyti5T4/edit?gid=308499628#gid=308499628))

1. ## Activation (Paid \+ Referrals) [Elizaveta Dmitrieva](mailto:elizaveta.dmitrieva@hellofresh.com)

   1. ### Checkout Funnel (Frontend)

      1. **Payment Page Visit to Success (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
         Conversion rate from checkout page visit to successful checkout.
         **Formula:** Successful Checkouts / Payment Page Visits
      2. **Select to Success (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
         Conversion rate from selecting a payment method to successful checkout.
         **Formula:** Successful Checkouts / Payment Method Selections

   2. ### Checkout Funnel (Backend)

      1. **Payment Page Visit to Success (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**

2. ## Reactivations  [Elizaveta Dmitrieva](mailto:elizaveta.dmitrieva@hellofresh.com)

   1. ### Reactivation Funnel

      1. **Reactivation Success Rate (Ratio) [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
         Percentage of reactivated customers who clicked CTA.
         **Formula:** Reactivated Customers / Reactivation Attempts

3. ## Fraud [Visal Kumar Vazhavandan Baskar](mailto:visal.kumar@hellofresh.com)[Cagdas Ozek](mailto:aoez@hellofresh.com)

   1. ### Voucher Fraud

      1. **Duplicate Rate (Ratio) [Anna Bauhofer](mailto:abau@hellofresh.com)**
         Percentage of checkout attempts identified as duplicate accounts.
         **Formula:** Duplicate Accounts / Checkout Attempts
      2. **Duplicate Block Rate (Ratio) [Anna Bauhofer](mailto:abau@hellofresh.com)**
         Percentage of blocked duplicate checkout attempts
         **Formula:** Blocked Duplicate Accounts / Checkout Attempts

   2. ### Payment Fraud

      1. **Payment Fraud Block Rate (Ratio) [Anna Bauhofer](mailto:abau@hellofresh.com)**
         Percentage of fraudulent checkout attempts blocked at checkout.
         **Formula:** Blocked Fraud Checkouts / Checkout Attempts

4. ## Recurring Payments

   1. ### Total Box Candidates [Tatiana Anikina](mailto:tatiana.anikina@hellofresh.com)

      1. **Acceptance Rate Before Risk Assessment (Pre-Dunning)	 (Ratio) [Zeeshan Akram](mailto:zeeshan.akram@hellofresh.com)**
         Percentage of paid orders before the dunning process.
         **Formula:** Paid Orders Before Dunning / Total Orders
      2. **Final Acceptance Rate (Post-Dunning) (Ratio) [Zeeshan Akram](mailto:zeeshan.akram@hellofresh.com)[Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Percentage of paid orders after the dunning process.
         **Formula:** Paid Orders After Dunning / Total Orders
      3. **LL0 (Initial charges): Final Acceptance Rate [Khaled ElSayed](mailto:khaled.elsayed@hellofresh.com)**
         (Same as Final Acceptance Rate AR but specific to initial charges).
         **Formula:** Paid Initial Orders After Dunning / Total Initial Orders

   2. ### Boxes Shipped [Tatiana Anikina](mailto:tatiana.anikina@hellofresh.com)[Cagdas Ozek](mailto:aoez@hellofresh.com)

      1. **Ship Rate after Dunning Decision (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Percentage of unpaid orders that were shipped.
         **Formula:** Shipped Unpaid Orders / Unpaid Orders
      2. **Recovery Rate (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Percentage of shipped unpaid orders that were recovered
         **Formula:** Recovered Orders / Shipped Unpaid Orders
      3. **Dunning Net Profit (12wk lag) (Monetary) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Net profit from recoveries of shipped unpaid orders.
         **Formula:** Recovered Revenue \- Costs of Shipped Unpaid Orders
      4. **Dunning Avg Net Profit (12wk lag) (Monetary) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Average net profit from recoveries of shipped unpaid orders over all orders with prediction.
         **Formula:** (Recovered Revenue \- Costs of Shipped Unpaid Orders) / ~~Shipped Unpaid~~ Orders with Prediction
      5. **Dunning Bad Debt (12wk lag) (Monetary) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Total amount written off as bad debt after 6 months.
         **Formula:** Unpaid Amount After 6 months
      6. **Dunning Bad Debt Rate (12wk lag) (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Total amount written off as bad debt after ~~6 months~~ 12 weeks / Shipped Order Revenue.
         **Formula:** Unpaid Amount After ~~6 months~~ 12 weeks / Shipped Order Revenue
      7. **Profit Coverage Rate (Ratio) [Hasan Yagiz Söylemez](mailto:hasan.soeylemez@hellofresh.com)**
         Represents the proportion of actual net profit from recoveries relative to the theoretical maximum, calculated by scaling holdout group recoveries to the entire audience.
         **Formula:** Dunning Net Profit / Potential Maximum Dunning Net Profit

   3. ### Chargebacks [Anna Bauhofer](mailto:abau@hellofresh.com)[Visal Kumar Vazhavandan Baskar](mailto:visal.kumar@hellofresh.com)

      1. **Chargeback Rate (13w lag) (Ratio)**
         Percentage of transactions that resulted in a chargeback.
         **Formula:** Chargeback Transactions / Total Transactions

5. ## Cash Credits [Tatiana Anikina](mailto:tatiana.anikina@hellofresh.com)

   1. ### Top-Ups \- *out of scope for now*

      1. **Cash Credits Added Through Top-Ups (Monetary)**
         Total amount added via customer top-ups.
         **Formula:** Sum of Top-Up Transactions

6. ## Payment Costs [Cagdas Ozek](mailto:aoez@hellofresh.com)

   1. ### Payment Processing \- *out of scope for now*

      1. **Fees as % of GR	 (Ratio)**
         Percentage of total payments spent on processing fees.
         **Formula:** Total Payment Processing Fees / Total Payments Processed
      2. **Cost Per Order (Monetary)**
         Average payment processing cost per order.
         **Formula:** Total Payment Costs / Total Orders

## Formula Component Definitions

* **Successful Checkouts**: Number of checkouts successfully completed.
* **Payment Page Visits**: Total visits to the checkout page.
* **Payment Method Selections**: Instances where a payment method is chosen at checkout page.
* **Duplicate Accounts**: Number of accounts flagged as duplicates (both pre/post checkout).
* **Checkout Attempts**: Total checkout attempts (*Place Order click*) made by customers.
* **Blocked Duplicate Accounts**: Duplicate accounts prevented from completing checkout due to high discount.
* **Blocked Fraud Checkouts**: Checkout attempts blocked due to suspected payment fraud.
* **Reactivated Customers**: Customers who successfully reactivated their account with a valid payment method
* **Reactivation Attempts**: Total number of customers clicked reactivation CTA
* **Paid Orders Before Dunning**: Orders successfully paid before logistics cutoff prior to packaging
* **Total Orders**: All orders created and got ready for payment during a specific period.
* **Paid Orders After Dunning**: Orders successfully paid (post-dunning) including the recovered orders
* **Paid Initial Orders After Dunning**: Initial orders successfully paid (post-dunning) including the recovered orders
* **Total Initial Orders**: All initial orders attempted.
* **Shipped Unpaid Orders**: Orders shipped despite not being paid initially.
* **Unpaid Orders**: Orders not being paid initially.
* **Recovered Orders**: Shipped unpaid orders that were recovered
* **Recovered Revenue \- Costs of Shipped Unpaid Orders**: Profit from recovered unpaid orders including the cost of goods.
* **Unpaid Amount After 6 months**: Outstanding debt after six months.
* **Chargeback Transactions**: Transactions that resulted in chargebacks.
* **Total Transactions**: All payment transactions processed.
* **Sum of Top-Up Transactions**: Total value of top-up payments made.
* **Total Payment Processing Fees**: Fees paid for processing payments.
* **Total Payments Processed**: Total amount of payments handled.
* **Total Payment Costs**: Overall costs related to payment processing.
* **Potential Maximum Dunning Net Profit:** The estimated upper limit of net profit that could be achieved if unpaid orders were perfectly predicted and shipped only to customers who would eventually pay. This is calculated by extrapolating the net profit of recovered payments in the holdout group to the entire audience, providing a benchmark for evaluating dunning efficiency.

---
