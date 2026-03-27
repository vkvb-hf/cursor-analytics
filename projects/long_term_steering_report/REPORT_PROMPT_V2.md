# Weekly Payments Metrics Steering Report Prompt

## Instructions for Creating Weekly Reports

### Input Requirements
1. Read "Payments P0 Metrics.md" to understand metric definitions
2. Read the current week's metrics TSV file (YYYY-WXX_metrics.tsv)
3. Input structure: Metric Name -> Summary.txt

### Report Structure

Create a weekly payments metrics steering table with the following columns:
- **Metrics** (metric name only)
- **Anomaly/Callout** (important insights for each metric, cell content must not exceed 1000 characters)
- **Notes** (empty cell to be filled later)

### Metric Groups (in order)
1. Payment Page Visit to Success (frontend, backend)
2. Select to Success
3. Duplicate Rate/Duplicate Block Rate
4. Payment Fraud Block Rate
5. Reactivation Rate
6. AR Pre Dunning
7. Acceptance LL0 (Initial Charge)
8. Acceptance LL0 and LL1+ (Recurring Charge)
9. Ship Rate/Recovery W0
10. Recovery W12 - DW21
11. Dunning Profit

### Report Requirements

**Format Requirements:**
- **IMPORTANT: Use proper Markdown bullet points (`-`) NOT unicode bullets (`•`)**
- Use `<br>` for line breaks within table cells
- Use unicode arrows: ↑ (green up arrow) for increases, ↓ (red down arrow) for decreases
- Keep all content in table cells under 1000 characters

**Content Requirements:**
- Always show the performance of Reporting Clusters: ['Overall', 'HF-NA', 'HF-INTL', 'US-HF', 'RTE', 'WL'] 
- **Main comparison: Show progression from previous week to current week (format: "prev% to current%" not "current vs prev")**
- **CRITICAL: Order must be FROM (previous week) TO (current week) to show the direction of change**
- Check with previous month values to make trend statements
- Show significance scores for each change
- Use proper market naming: (BU) Brand-Country format (e.g., (US) HelloFresh-US)
- Consolidate different dimensions of the same metric for a market
- Group findings by metric categories
- Highlight major improvements and concerns
- Highlight where (business units/dimensions) for the significant differences
- Avoid repetitive information
- For Ship Rate, Recovery W0, Recovery W12, Dunning Profit: Only report on Good Customers Performance

**Key Insights Section:**
- Add above the table
- Maximum 1000 characters
- **Use proper Markdown bullet points (`-`) NOT unicode bullets**
- Include 3-4 key insights covering:
  - Critical issues
  - Positive trends
  - Risk shifts
  - Emerging concerns

### Example Format

```markdown
# YYYY-WXX Weekly Payments Metrics Steering

## Key Insights
- **Critical Issues:** [Key problem areas with impact]
- **Positive Trends:** [Major improvements]
- **Risk Shifts:** [Strategic changes observed]
- **Emerging Concerns:** [New issues to watch]

| Metrics | Anomaly/Callout | Notes |
| :--- | :--- | :--- |
| **Payment Page Visit to Success** | **Current Week vs Prev Week:**<br>- **Overall**: 31.36% to 31.52% (↑0.53%, not significant, volume: 213.3K)<br>- **HF-NA**: 31.36% to 31.52% (↑0.53%, not significant, volume: 213.3K)<br>- **HF-INTL**: 31.36% to 31.52% (↑0.53%, not significant, volume: 213.3K)<br>- **RTE**: 31.36% to 31.52% (↑0.53%, not significant, volume: 213.3K)<br>- **WL**: 31.36% to 31.52% (↑0.53%, not significant, volume: 213.3K)<br><br>**Deep Insights**<br>- **Overall** has a drop because of {dimension_name}, 19.28% to 19.64% (1.82% increase, volume impacted:457.3K)<br>- **HF-INTL** shows a decrease because of {dimension_name}, 19.28% to 19.64% (1.82% increase, volume impacted:457.3K) and drop in the below markets:<br>- GB: 36.05% to 38.45% (6.64% increase, volume impacted:121.7K)<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)<br><br>**Comparison vs Prev Year**<br>- **Current Week vs Prev Year Week**: 38.97% to 34.14% (↓12.40%, volume: 35.3K)<br>- **Current Quarter vs Prev Year Quarter**: 38.72% to 33.23% (↓14.20%, volume: 172.2K) - sustained quarterly decline across RTE and WL clusters| |
| **Select to Success** | **Current Week vs Prev Week:**<br>- **Overall**: 66.85% to 67.51% (↑0.97%, significant, volume: 1.4K)<br>...<br><br>**Deep Insights**<br>- {insights}<br><br>**Long Term Impact**<br>- No significant long-term impact (all changes <10%)<br><br>**Comparison vs Prev Year**<br>- **Current Week vs Prev Year Week**: 78.21% to 67.51% (↓13.68%, volume: 19.7K) - broad-based payment method degradation| |
```

### Important Notes
- **Always use `-` for bullet points in Markdown, never use unicode bullets**
- Consolidate insights for the same market/metric combination
- Focus on high significance scores (typically 4-10)
- Include both positive and negative changes
- Ensure readability by grouping related insights
- When using bullet points in table cells, start with `-` followed by a space
- **Long Term Impact section should include noteworthy callouts only (not all comparisons)**

### Table Structure Guidelines

**Main Table Content (Current Week vs Prev Week):**
- Report all Reporting Clusters: Overall, HF-NA, HF-INTL, US-HF, RTE, WL
- Include Deep Insights section with detailed breakdown by business units and dimensions

**Long Term Impact Section:**
The **Long Term Impact** section should appear after **Deep Insights** for **ALL metrics** and includes:
- **Current Month vs Prev Month**: Month-over-month sequential trends
- **Current Quarter vs Prev Quarter**: Quarter-over-quarter sequential trends

**Important Threshold Rule:**
- **Only include callouts when absolute percentage difference is >10%**
- If no comparison exceeds 10% threshold, write: "No significant long-term impact (all changes <10%)"
- This focuses attention on truly material sequential shifts indicating gradual changes

**Comparison vs Prev Year Section:**
The **Comparison vs Prev Year** section should appear after **Long Term Impact** for **ALL metrics** and includes:
- **Current Week vs Prev Year Week**: Year-over-year weekly changes
- **Current Month vs Prev Year Month**: Year-over-year monthly trends
- **Current Quarter vs Prev Year Quarter**: Year-over-year quarterly trends

**Important Threshold Rule:**
- **Only include callouts when absolute percentage difference is >10%**
- If no comparison exceeds 10% threshold, write: "No significant year-over-year impact (all changes <10%)"
- This highlights major year-over-year shifts requiring attention

**Deduplication Rule (applies to both sections):**
- If an impact appears in multiple time periods (e.g., both month and quarter exceed 10%), only report it in the broader time period (quarter)
- Goal: Identify gradual decline/improvement patterns without repetition
- Mention the sustained nature of the trend (e.g., "sustained across monthly and quarterly comparisons")

### Current Week Template
current week: YYYY-WXX

