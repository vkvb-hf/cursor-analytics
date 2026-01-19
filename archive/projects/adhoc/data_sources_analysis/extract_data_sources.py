#!/usr/bin/env python3
"""
Extract all data sources (tables and parquet files) from SQL queries and Python ETL files
in analytics_etl/queries and generic_etls, and generate CSVs with pipeline name, data source, 
type, and internal/external classification.

For generic_etls:
1. Parse Python files to find parquet_configs and template variable substitutions
2. Find the SQL files referenced in the Python files
3. Map template variables to their actual parquet sources
4. Extract all data sources from the SQL files
"""

import os
import re
import csv
import ast
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any

# Base directory - ddi-pays-pipelines repo
DDI_PAYS_PIPELINES_DIR = Path("/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines/ddi_pays_pipelines")

# Directories to process
QUERY_DIRS = {
    "analytics_etl": {
        "sql_dir": DDI_PAYS_PIPELINES_DIR / "analytics_etl" / "queries",
        "py_dir": None,
    },
    "generic_etls": {
        "sql_dir": DDI_PAYS_PIPELINES_DIR / "generic_etls" / "queries",
        "py_dir": DDI_PAYS_PIPELINES_DIR / "generic_etls",
    },
}

# Output directory - this script's location
OUTPUT_DIR = Path(__file__).parent

# Regex patterns for SQL files
TABLE_PATTERN = re.compile(
    r'\b(?:FROM|JOIN|INNER\s+JOIN|LEFT\s+JOIN|RIGHT\s+JOIN|FULL\s+JOIN|CROSS\s+JOIN|LEFT\s+OUTER\s+JOIN|RIGHT\s+OUTER\s+JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)',
    re.IGNORECASE
)

TEMPLATE_VAR_PATTERN = re.compile(
    r'\b(?:FROM|JOIN|INNER\s+JOIN|LEFT\s+JOIN|RIGHT\s+JOIN|FULL\s+JOIN|CROSS\s+JOIN|LEFT\s+OUTER\s+JOIN|RIGHT\s+OUTER\s+JOIN)\s+\{([a-zA-Z_][a-zA-Z0-9_]*)\}',
    re.IGNORECASE
)

PARQUET_BACKTICK_PATTERN = re.compile(
    r'parquet\.`([^`]+)`',
    re.IGNORECASE
)

S3_PARQUET_PATTERN = re.compile(
    r"(?:FROM|JOIN|INNER\s+JOIN|LEFT\s+JOIN|RIGHT\s+JOIN)\s+['\"]?(s3[a]?://[^'\"\s\)]+)['\"]?",
    re.IGNORECASE
)

# Pattern to match read_text for SQL queries
PY_SQL_QUERY_PATTERN = re.compile(
    r'pkg_resources\.read_text\s*\(\s*queries\s*,\s*["\']([^"\']+\.sql)["\']',
    re.IGNORECASE
)


def extract_tables_from_sql(sql_content: str) -> set:
    """Extract table references from SQL content."""
    tables = set()
    matches = TABLE_PATTERN.findall(sql_content)
    for match in matches:
        table = match.strip()
        if table and not table.startswith('(') and not table.endswith('.sql'):
            tables.add(table.lower())
    return tables


def extract_template_vars_from_sql(sql_content: str) -> set:
    """Extract template variable references from SQL content."""
    template_vars = set()
    matches = TEMPLATE_VAR_PATTERN.findall(sql_content)
    for match in matches:
        var = match.strip()
        if var:
            template_vars.add(var)
    return template_vars


def extract_parquet_from_sql(sql_content: str) -> set:
    """Extract parquet file references from SQL content."""
    parquets = set()
    
    backtick_matches = PARQUET_BACKTICK_PATTERN.findall(sql_content)
    for match in backtick_matches:
        if match:
            parquets.add(match)
    
    s3_matches = S3_PARQUET_PATTERN.findall(sql_content)
    for match in s3_matches:
        if match and 'parquet' in match.lower():
            parquets.add(match)
    
    return parquets


def parse_python_file_for_parquet_mapping(py_file: Path) -> Dict[str, Any]:
    """
    Parse a Python file to extract:
    1. parquet_configs - list of {path, base_table_name}
    2. template_to_base_table - mapping from template var to base_table_name
    3. base_table_to_path - mapping from base_table_name to parquet path
    4. sql_files - set of SQL files referenced
    """
    result = {
        'parquet_configs': [],
        'template_to_base_table': {},  # {template_var: base_table_name}
        'base_table_to_path': {},  # {base_table_name: parquet_path}
        'sql_files': set(),
        'all_s3_paths': set()
    }
    
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            py_content = f.read()
    except Exception as e:
        print(f"Error reading {py_file}: {e}")
        return result
    
    # Extract SQL files via regex (handles both string literals and f-strings)
    sql_matches = PY_SQL_QUERY_PATTERN.findall(py_content)
    result['sql_files'] = set(sql_matches)
    
    # Also try to find f-string patterns like f"{query_source}.sql"
    # First find query_source assignments
    query_source_pattern = re.compile(r'query_source\s*=\s*["\']([^"\']+)["\']')
    query_source_matches = query_source_pattern.findall(py_content)
    for qs in query_source_matches:
        result['sql_files'].add(f"{qs}.sql")
    
    # Also check for direct .sql file references in strings
    sql_file_pattern = re.compile(r'["\']([a-zA-Z_][a-zA-Z0-9_]*\.sql)["\']')
    for match in sql_file_pattern.findall(py_content):
        result['sql_files'].add(match)
    
    # Parse with AST
    try:
        tree = ast.parse(py_content)
        
        # Walk through all nodes to find parquet_configs and table_replacements
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == 'parquet_configs':
                            # Extract parquet configs
                            if isinstance(node.value, ast.List):
                                for elem in node.value.elts:
                                    if isinstance(elem, ast.Dict):
                                        config = {}
                                        for k, v in zip(elem.keys, elem.values):
                                            if isinstance(k, ast.Constant):
                                                if k.value == 'path':
                                                    config['path'] = _extract_string(v)
                                                elif k.value == 'base_table_name':
                                                    config['base_table_name'] = _extract_string(v)
                                        if config.get('path') and config.get('base_table_name'):
                                            result['parquet_configs'].append(config)
                                            result['base_table_to_path'][config['base_table_name']] = config['path']
                        
                        elif target.id == 'table_replacements':
                            # Extract table_replacements dict
                            # Format: {'{temp_xxx_table}': table_mapping['base_table_name'], ...}
                            if isinstance(node.value, ast.Dict):
                                for k, v in zip(node.value.keys, node.value.values):
                                    if isinstance(k, ast.Constant) and isinstance(k.value, str):
                                        placeholder = k.value
                                        # Extract variable name from '{var_name}'
                                        if placeholder.startswith('{') and placeholder.endswith('}'):
                                            var_name = placeholder[1:-1]
                                            # Get the base_table_name from the subscript
                                            if isinstance(v, ast.Subscript):
                                                if isinstance(v.slice, ast.Constant):
                                                    base_table = v.slice.value
                                                    result['template_to_base_table'][var_name] = base_table
        
        # Also extract S3 paths via regex for fallback
        s3_pattern = re.compile(r's3://[a-zA-Z0-9\-_./]+', re.IGNORECASE)
        for match in s3_pattern.findall(py_content):
            if 'topics/' in match:
                result['all_s3_paths'].add(match)
                
    except SyntaxError as e:
        print(f"Syntax error parsing {py_file}: {e}")
    
    return result


def _extract_string(node) -> str:
    """Extract string value from an AST node, handling concatenation."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _extract_string(node.left)
        right = _extract_string(node.right)
        if left and right:
            return left + right
    return None


def process_sql_file(sql_file: Path) -> dict:
    """Process a single SQL file and return extracted data sources."""
    result = {
        'tables': set(),
        'template_vars': set(),
        'parquets': set()
    }
    
    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
    except Exception as e:
        print(f"Error reading {sql_file}: {e}")
        return result
    
    result['tables'] = extract_tables_from_sql(sql_content)
    result['template_vars'] = extract_template_vars_from_sql(sql_content)
    result['parquets'] = extract_parquet_from_sql(sql_content)
    
    return result


def classify_source(source: str) -> str:
    """Classify source as internal (payments_hf) or external."""
    if source.lower().startswith('payments_hf.'):
        return 'internal'
    else:
        return 'external'


def process_generic_etls(sql_dir: Path, py_dir: Path) -> List[dict]:
    """Process generic_etls by parsing Python files first, then SQL files."""
    results = []
    processed_sql_files = set()
    
    if not py_dir or not py_dir.exists():
        return results
    
    py_files = list(py_dir.glob("*.py"))
    print(f"Found {len(py_files)} Python files in {py_dir.name}")
    
    for py_file in sorted(py_files):
        if py_file.name.startswith('__'):
            continue
        
        pipeline_name = py_file.stem
        py_result = parse_python_file_for_parquet_mapping(py_file)
        
        # Track SQL files processed
        processed_sql_files.update(py_result['sql_files'])
        
        # Build the complete template_var -> parquet_path mapping
        template_to_parquet = {}
        for template_var, base_table in py_result['template_to_base_table'].items():
            if base_table in py_result['base_table_to_path']:
                template_to_parquet[template_var] = py_result['base_table_to_path'][base_table]
        
        # Collect all data sources for this pipeline
        all_tables = set()
        all_parquets = set()
        unresolved_template_vars = set()
        
        # Add parquet paths from Python configs
        for config in py_result['parquet_configs']:
            if config.get('path'):
                all_parquets.add(config['path'])
        
        # Also add any S3 paths found via regex
        all_parquets.update(py_result['all_s3_paths'])
        
        # Process each SQL file referenced
        for sql_file_name in py_result['sql_files']:
            sql_file_path = sql_dir / sql_file_name
            if sql_file_path.exists():
                sql_result = process_sql_file(sql_file_path)
                all_tables.update(sql_result['tables'])
                all_parquets.update(sql_result['parquets'])
                
                # For each template variable in SQL, try to resolve it to a parquet path
                for template_var in sql_result['template_vars']:
                    if template_var in template_to_parquet:
                        parquet_path = template_to_parquet[template_var]
                        all_parquets.add(parquet_path)
                    else:
                        # Keep track of unresolved template variables
                        unresolved_template_vars.add(template_var)
        
        # Add tables to results
        for table in sorted(all_tables):
            results.append({
                'pipeline_name': pipeline_name,
                'data_source': table,
                'type': 'table',
                'source_category': classify_source(table)
            })
        
        # Add parquet files to results
        for parquet in sorted(all_parquets):
            results.append({
                'pipeline_name': pipeline_name,
                'data_source': parquet,
                'type': 'parquet',
                'source_category': 'external'
            })
        
        # Add unresolved template variables
        for var in sorted(unresolved_template_vars):
            results.append({
                'pipeline_name': pipeline_name,
                'data_source': f'{{{var}}}',
                'type': 'template_variable',
                'source_category': 'external'
            })
    
    # Process remaining SQL files not referenced by Python
    if sql_dir and sql_dir.exists():
        sql_files = list(sql_dir.glob("*.sql"))
        print(f"Found {len(sql_files)} SQL files in {sql_dir.name}")
        
        for sql_file in sorted(sql_files):
            if sql_file.name in processed_sql_files:
                continue
            
            pipeline_name = sql_file.stem
            sql_result = process_sql_file(sql_file)
            
            # Add tables
            for table in sorted(sql_result['tables']):
                results.append({
                    'pipeline_name': pipeline_name,
                    'data_source': table,
                    'type': 'table',
                    'source_category': classify_source(table)
                })
            
            # Add template variables (unresolved)
            for var in sorted(sql_result['template_vars']):
                results.append({
                    'pipeline_name': pipeline_name,
                    'data_source': f'{{{var}}}',
                    'type': 'template_variable',
                    'source_category': 'external'
                })
            
            # Add parquet files
            for parquet in sorted(sql_result['parquets']):
                results.append({
                    'pipeline_name': pipeline_name,
                    'data_source': parquet,
                    'type': 'parquet',
                    'source_category': 'external'
                })
    
    return results


def process_analytics_etl(sql_dir: Path) -> List[dict]:
    """Process analytics_etl SQL files."""
    results = []
    
    if not sql_dir or not sql_dir.exists():
        return results
    
    sql_files = list(sql_dir.glob("*.sql"))
    print(f"Found {len(sql_files)} SQL files in {sql_dir.name}")
    
    for sql_file in sorted(sql_files):
        pipeline_name = sql_file.stem
        sql_result = process_sql_file(sql_file)
        
        # Add tables
        for table in sorted(sql_result['tables']):
            results.append({
                'pipeline_name': pipeline_name,
                'data_source': table,
                'type': 'table',
                'source_category': classify_source(table)
            })
        
        # Add template variables
        for var in sorted(sql_result['template_vars']):
            results.append({
                'pipeline_name': pipeline_name,
                'data_source': f'{{{var}}}',
                'type': 'template_variable',
                'source_category': 'external'
            })
        
        # Add parquet files
        for parquet in sorted(sql_result['parquets']):
            results.append({
                'pipeline_name': pipeline_name,
                'data_source': parquet,
                'type': 'parquet',
                'source_category': 'external'
            })
    
    return results


def write_csv(results: list, output_path: Path):
    """Write results to CSV file."""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['pipeline_name', 'data_source', 'type', 'source_category'])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"CSV written to: {output_path}")
    print(f"Total records: {len(results)}")


def print_summary(results: list, name: str):
    """Print summary statistics."""
    pipelines = set(r['pipeline_name'] for r in results)
    sources = set(r['data_source'] for r in results)
    internal = [r for r in results if r['source_category'] == 'internal']
    external = [r for r in results if r['source_category'] == 'external']
    tables = [r for r in results if r['type'] == 'table']
    parquets = [r for r in results if r['type'] == 'parquet']
    template_vars = [r for r in results if r['type'] == 'template_variable']
    
    print(f"\n=== Summary for {name} ===")
    print(f"Pipelines processed: {len(pipelines)}")
    print(f"Unique data sources: {len(sources)}")
    print(f"Total entries: {len(results)}")
    print(f"  - Tables: {len(tables)}")
    print(f"  - Parquet files: {len(parquets)}")
    print(f"  - Template variables: {len(template_vars)}")
    print(f"  - Internal (payments_hf): {len(internal)}")
    print(f"  - External: {len(external)}")


def main():
    # Process analytics_etl
    print(f"\n{'='*60}")
    print(f"Processing: analytics_etl")
    print(f"{'='*60}")
    
    analytics_results = process_analytics_etl(QUERY_DIRS["analytics_etl"]["sql_dir"])
    analytics_csv = OUTPUT_DIR / "analytics_etl_data_sources.csv"
    write_csv(analytics_results, analytics_csv)
    print_summary(analytics_results, "analytics_etl")
    
    # Process generic_etls
    print(f"\n{'='*60}")
    print(f"Processing: generic_etls")
    print(f"{'='*60}")
    
    generic_results = process_generic_etls(
        QUERY_DIRS["generic_etls"]["sql_dir"],
        QUERY_DIRS["generic_etls"]["py_dir"]
    )
    generic_csv = OUTPUT_DIR / "generic_etls_data_sources.csv"
    write_csv(generic_results, generic_csv)
    print_summary(generic_results, "generic_etls")


if __name__ == "__main__":
    main()
