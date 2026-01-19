# Atlan MCP Server

Remote MCP server hosted by Atlan for data catalog and governance operations.

## Type

**External/Remote** - No local code required. Hosted at `https://hellofresh.atlan.com/mcp`

## Tools (12 total)

| Tool | Description |
|------|-------------|
| `semantic_search_tool` | Search data assets by meaning |
| `traverse_lineage_tool` | Explore data lineage |
| `update_assets_tool` | Update asset metadata |
| `create_glossaries` | Create business glossaries |
| `create_glossary_categories` | Create glossary categories |
| `create_glossary_terms` | Create glossary terms |
| `create_domains` | Create data domains |
| `create_data_products` | Create data products |
| `create_dq_rules_tool` | Create data quality rules |
| `update_dq_rules_tool` | Update DQ rules |
| `delete_dq_rules_tool` | Delete DQ rules |
| `schedule_dq_rules_tool` | Schedule DQ rule execution |

## Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "Atlan": {
      "url": "https://hellofresh.atlan.com/mcp"
    }
  }
}
```

## Authentication

Authentication is handled through your Atlan account. You may need to authenticate when first connecting.

## Usage Examples

### Search for Data Assets
```
Use semantic_search_tool with:
- query: customer orders table
```

### Explore Lineage
```
Use traverse_lineage_tool with:
- asset_qualified_name: default/schema/table_name
- direction: upstream
```

### Create Glossary Term
```
Use create_glossary_terms with:
- glossary_name: Business Glossary
- term_name: Customer Lifetime Value
- definition: Total revenue from a customer over their relationship
```

### Create Data Quality Rule
```
Use create_dq_rules_tool with:
- asset_qualified_name: default/schema/table_name
- rule_type: completeness
- column: email
```
