#!/usr/bin/env python3
"""
Livy MCP Server for DDI Pays Pipelines

EMR Hosts: live-01, live-02, live-03, live-04
Spark Profiles: analytics (12g), generic_etl (16g/32g), generic_etl_heavy (32g/64g)
"""

import json
import base64
import subprocess
import time
import os
from datetime import datetime, timedelta
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("livy-jobs")

EMR_HOSTS = {
    "live-01": "http://ddi-payments-live-01.emr.bi.hellofresh.io:8998",
    "live-02": "http://ddi-payments-live-02.emr.bi.hellofresh.io:8998",
    "live-03": "http://ddi-payments-live-03.emr.bi.hellofresh.io:8998",
    "live-04": "http://ddi-payments-live-04.emr.bi.hellofresh.io:8998",
}

SPARK_CONFIGS = {
    "analytics": {
        "spark.submit.master": "yarn",
        "spark.sql.broadcastTimeout": 1200,
        "spark.yarn.appMasterEnv.PYSPARK_PYTHON": "/opt/pyspark-venvs/payments/bin/python",
        "spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON": "/opt/pyspark-venvs/payments/bin/python",
        "spark.driver.memory": "12g",
        "spark.executor.memory": "12g",
    },
    "generic_etl": {
        "spark.submit.master": "yarn",
        "spark.yarn.queue": "default",
        "spark.yarn.appMasterEnv.PYSPARK_PYTHON": "/opt/pyspark-venvs/payments/bin/python",
        "spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON": "/opt/pyspark-venvs/payments/bin/python",
        "spark.jars.packages": "org.apache.spark:spark-avro_2.12:3.4.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0",
        "spark.sql.broadcastTimeout": 3600,
        "spark.driver.memory": "16g",
        "spark.executor.memory": "32g",
        "spark.driver.maxResultSize": "32g",
        "spark.sql.shuffle.partitions": 8000,
        "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
        "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        "spark.sql.parquet.mergeSchema": "false",
        "spark.sql.execution.pythonUDF.arrow.enabled": "true",
    },
    "generic_etl_heavy": {
        "spark.submit.deployMode": "cluster",
        "spark.submit.master": "yarn",
        "spark.yarn.queue": "default",
        "spark.yarn.appMasterEnv.PYSPARK_PYTHON": "/opt/pyspark-venvs/payments/bin/python",
        "spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON": "/opt/pyspark-venvs/payments/bin/python",
        "spark.jars.packages": "org.apache.spark:spark-avro_2.12:3.4.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0",
        "spark.sql.broadcastTimeout": 3600,
        "spark.driver.memory": "32g",
        "spark.executor.memory": "64g",
        "spark.driver.maxResultSize": "32g",
        "spark.sql.shuffle.partitions": 8000,
        "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
        "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        "spark.sql.parquet.mergeSchema": "false",
        "spark.sql.execution.pythonUDF.arrow.enabled": "true",
    },
}

# Path to ddi-pays-pipelines repo
DDI_PAYS_PIPELINES_PATH = "/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines"


def _detect_etl_type(etl_name: str) -> str:
    """Check if ETL exists in generic_etls folder, otherwise assume analytics."""
    generic_etls_path = os.path.join(DDI_PAYS_PIPELINES_PATH, "ddi_pays_pipelines", "generic_etls")
    
    # Check for direct file
    if os.path.exists(os.path.join(generic_etls_path, f"{etl_name}.py")):
        return "generic"
    
    # Check for folder with same name
    if os.path.isdir(os.path.join(generic_etls_path, etl_name)):
        return "generic"
    
    # Check generic_etl_runner/etls.py for registered ETLs
    etls_file = os.path.join(DDI_PAYS_PIPELINES_PATH, "ddi_pays_pipelines", "generic_etl_runner", "etls.py")
    if os.path.exists(etls_file):
        with open(etls_file, 'r') as f:
            content = f.read()
            if f"add_generic_etl('{etl_name}'" in content:
                return "generic"
    
    return "analytics"


def _build_py_files(pr_number: Optional[int] = None) -> list:
    if pr_number:
        return [
            f"s3://pays-ddi/binary-repository/ddi_pays_pipelines/PR-{pr_number}/ddi_pays_pipelines-PR_{pr_number}-py3.7.egg",
            f"s3://pays-ddi/binary-repository/ddi_pays_pipelines/PR-{pr_number}/libs.zip",
        ]
    return [
        "s3://pays-ddi/binary-repository/ddi_pays_pipelines/latest/ddi_pays_pipelines-latest-py3.7.egg",
        "s3://pays-ddi/binary-repository/ddi_pays_pipelines/latest/libs.zip",
    ]


def _submit_livy_job(host: str, payload: dict, dry_run: bool = False) -> dict:
    url = f"{host}/batches"
    
    if dry_run:
        return {
            "dry_run": True,
            "url": url,
            "payload": payload,
        }
    
    result = subprocess.run(
        ["curl", "--location", "-g", "-s", "--request", "POST", url,
         "--header", "Content-Type: application/json",
         "--data-raw", json.dumps(payload)],
        capture_output=True, text=True
    )
    
    try:
        response = json.loads(result.stdout)
    except json.JSONDecodeError:
        response = {"raw_output": result.stdout, "error": result.stderr}
    
    return {"submitted": True, "url": url, "response": response}


def _submit_single_job(
    etl_name: str,
    etl_type: str,
    start_date: str,
    end_date: str,
    pr_number: Optional[int],
    emr_host: str,
    spark_profile: str,
    dry_run: bool,
) -> dict:
    """Submit a single job (analytics or generic)."""
    host = EMR_HOSTS.get(emr_host, EMR_HOSTS["live-01"])
    
    if etl_type == "analytics":
        app_name = f"{etl_name}-{pr_number}-run" if pr_number else f"{etl_name}-run"
        conf = SPARK_CONFIGS["analytics"].copy()
        conf["spark.app.name"] = app_name
        args = ["ddi_pays_pipelines.analytics_etl", "--etl", etl_name, "--no-backup"]
    else:
        date_suffix = start_date.replace("-", "")
        app_name = f"{etl_name}-pr-{pr_number}-{date_suffix}" if pr_number else f"{etl_name}-{date_suffix}"
        conf = SPARK_CONFIGS.get(spark_profile, SPARK_CONFIGS["generic_etl"]).copy()
        conf["spark.app.name"] = app_name
        encoded_args = base64.b64encode(json.dumps({}).encode()).decode()
        args = [
            "ddi_pays_pipelines.generic_etl_runner",
            "--etl", etl_name,
            "--etl-start-date-inclusive", start_date,
            "--etl-end-date-inclusive", end_date,
            "--args", encoded_args,
        ]
    
    payload = {
        "conf": conf,
        "file": "s3://pays-ddi/binary-repository/entrypoint.py",
        "args": args,
        "pyFiles": _build_py_files(pr_number),
    }
    
    return _submit_livy_job(host, payload, dry_run)


@mcp.tool()
def submit_etl(
    etl_name: str,
    pr_number: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    emr_host: str = "live-01",
    days_per_batch: Optional[int] = None,
    spark_profile: str = "generic_etl",
    dry_run: bool = False,
) -> dict:
    """
    Submit an ETL job to Livy. Auto-detects analytics vs generic based on ETL location in ddi-pays-pipelines.
    
    Args:
        etl_name: Name of the ETL (e.g., 'checkout_funnel_backend', 'customer_cluster_status_agg')
        pr_number: PR number for testing. If None, uses latest/prod build.
        start_date: Start date (YYYY-MM-DD). Default: yesterday. Ignored for analytics ETLs.
        end_date: End date (YYYY-MM-DD). Default: same as start_date.
        emr_host: EMR cluster (live-01, live-02, live-03, live-04)
        days_per_batch: If set, splits date range into batches of this size. If None, runs as single job.
        spark_profile: Spark config (generic_etl, generic_etl_heavy). Only for generic ETLs.
        dry_run: If True, returns job config without executing.
    
    Returns:
        Job submission response(s)
    """
    # Detect ETL type
    etl_type = _detect_etl_type(etl_name)
    
    # Default dates for generic ETLs
    if etl_type == "generic":
        if not start_date:
            start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        if not end_date:
            end_date = start_date
    
    # Analytics ETL - single job, no dates
    if etl_type == "analytics":
        result = _submit_single_job(etl_name, etl_type, "", "", pr_number, emr_host, spark_profile, dry_run)
        return {"etl_type": "analytics", "etl_name": etl_name, **result}
    
    # Generic ETL - check if batching needed
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    total_days = (end - start).days + 1
    
    # Single job if no batching or range fits in one batch
    if not days_per_batch or total_days <= days_per_batch:
        result = _submit_single_job(etl_name, etl_type, start_date, end_date, pr_number, emr_host, spark_profile, dry_run)
        return {"etl_type": "generic", "etl_name": etl_name, "date_range": f"{start_date} to {end_date}", **result}
    
    # Batch mode
    batches = []
    current = start
    batch_num = 1
    
    while current <= end:
        batch_end = min(current + timedelta(days=days_per_batch - 1), end)
        batches.append({
            "batch_num": batch_num,
            "start_date": current.strftime("%Y-%m-%d"),
            "end_date": batch_end.strftime("%Y-%m-%d"),
        })
        current = batch_end + timedelta(days=1)
        batch_num += 1
    
    if dry_run:
        return {
            "dry_run": True,
            "etl_type": "generic",
            "etl_name": etl_name,
            "total_batches": len(batches),
            "days_per_batch": days_per_batch,
            "batches": batches,
        }
    
    results = []
    for batch in batches:
        result = _submit_single_job(
            etl_name, etl_type, batch["start_date"], batch["end_date"],
            pr_number, emr_host, spark_profile, dry_run=False
        )
        results.append({"batch": batch, "result": result})
        if batch["batch_num"] < len(batches):
            time.sleep(5)
    
    return {
        "etl_type": "generic",
        "etl_name": etl_name,
        "total_batches": len(batches),
        "results": results,
    }


@mcp.tool()
def get_livy_batches(emr_host: str = "live-01", limit: int = 20) -> dict:
    """
    Get list of recent Livy batch jobs.
    
    Args:
        emr_host: EMR cluster to query (live-01, live-02, live-03, live-04)
        limit: Maximum number of batches to return (default: 20)
    
    Returns:
        List of recent batch jobs with their status
    """
    host = EMR_HOSTS.get(emr_host, EMR_HOSTS["live-01"])
    result = subprocess.run(["curl", "-s", "-g", f"{host}/batches?size={limit}"], capture_output=True, text=True)
    
    try:
        response = json.loads(result.stdout)
    except json.JSONDecodeError:
        response = {"raw_output": result.stdout, "error": result.stderr}
    
    return {"host": emr_host, "batches": response}


@mcp.tool()
def get_batch_status(batch_id: int, emr_host: str = "live-01") -> dict:
    """
    Get status of a specific Livy batch job.
    
    Args:
        batch_id: The batch ID to check
        emr_host: EMR cluster to query
    
    Returns:
        Batch job status and details
    """
    host = EMR_HOSTS.get(emr_host, EMR_HOSTS["live-01"])
    result = subprocess.run(["curl", "-s", "-g", f"{host}/batches/{batch_id}"], capture_output=True, text=True)
    
    try:
        response = json.loads(result.stdout)
    except json.JSONDecodeError:
        response = {"raw_output": result.stdout, "error": result.stderr}
    
    return {"batch_id": batch_id, "host": emr_host, "status": response}


@mcp.tool()
def kill_batch(batch_id: int, emr_host: str = "live-01") -> dict:
    """
    Kill/cancel a running Livy batch job.
    
    Args:
        batch_id: The batch ID to kill
        emr_host: EMR cluster where the job is running
    
    Returns:
        Result of the kill operation
    """
    host = EMR_HOSTS.get(emr_host, EMR_HOSTS["live-01"])
    result = subprocess.run(["curl", "-s", "-g", "-X", "DELETE", f"{host}/batches/{batch_id}"], capture_output=True, text=True)
    
    try:
        response = json.loads(result.stdout) if result.stdout else {"deleted": True}
    except json.JSONDecodeError:
        response = {"raw_output": result.stdout, "error": result.stderr}
    
    return {"batch_id": batch_id, "host": emr_host, "result": response}


if __name__ == "__main__":
    mcp.run()
