# Python for Data Engineers – Hands-On Examples
### 4-Hour Condensed Program | Module 1 & 2

---

## 🟢 BEGINNER EXAMPLES

---

### Beginner Example 1 – Reading & Writing CSV Files

**Topic:** File Handling – CSV Read/Write  
**Objective:** Read a CSV file, print its contents, and write a filtered output.

```python
import csv

# ---------- READ ----------
print("=== Sales Data ===")
with open("sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    for row in rows:
        print(row)

# ---------- FILTER & WRITE ----------
high_sales = [r for r in rows if float(r["amount"]) > 500]

with open("high_sales.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "amount"])
    writer.writeheader()
    writer.writerows(high_sales)

print(f"\n✅ {len(high_sales)} high-value records written to high_sales.csv")
```

**Sample `sales.csv`:**
```
id,name,amount
1,Alice,300
2,Bob,750
3,Carol,900
4,Dave,120
```

**Expected Output:**
```
=== Sales Data ===
{'id': '1', 'name': 'Alice', 'amount': '300'}
...
✅ 2 high-value records written to high_sales.csv
```

**Key Concepts:** `csv.DictReader`, `csv.DictWriter`, list comprehension, file encoding

---

### Beginner Example 2 – Parsing JSON Data

**Topic:** File Handling – JSON Read/Write  
**Objective:** Load a JSON file, extract fields, and save processed output.

```python
import json

# ---------- LOAD ----------
with open("employees.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total employees: {len(data['employees'])}")

# ---------- EXTRACT ACTIVE EMPLOYEES ----------
active = [
    {"name": e["name"], "dept": e["department"]}
    for e in data["employees"]
    if e["active"] is True
]

print("\nActive Employees:")
for emp in active:
    print(f"  - {emp['name']} ({emp['dept']})")

# ---------- WRITE OUTPUT ----------
with open("active_employees.json", "w", encoding="utf-8") as f:
    json.dump(active, f, indent=2)

print("\n✅ Saved active_employees.json")
```

**Sample `employees.json`:**
```json
{
  "employees": [
    {"name": "Alice", "department": "Engineering", "active": true},
    {"name": "Bob",   "department": "HR",          "active": false},
    {"name": "Carol", "department": "Data",         "active": true}
  ]
}
```

**Key Concepts:** `json.load()`, `json.dump()`, filtering lists, JSON structure

---

### Beginner Example 3 – Basic Exception Handling & Logging

**Topic:** Exception Handling & Logging  
**Objective:** Safely read a file with error handling and structured logging.

```python
import logging

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("data_reader")

def read_sales_file(filepath: str) -> list:
    """Reads a CSV-like sales file safely."""
    try:
        logger.info(f"Opening file: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        logger.info(f"Successfully read {len(lines)} lines.")
        return lines
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except PermissionError:
        logger.critical(f"Permission denied: {filepath}")
        return []

# Test
data = read_sales_file("sales.csv")
data_missing = read_sales_file("missing_file.csv")
```

**Expected Log Output:**
```
2026-02-23 10:00:01 | INFO    | Opening file: sales.csv
2026-02-23 10:00:01 | INFO    | Successfully read 5 lines.
2026-02-23 10:00:01 | INFO    | Opening file: missing_file.csv
2026-02-23 10:00:01 | ERROR   | File not found: missing_file.csv
```

**Key Concepts:** `logging.basicConfig`, log levels (INFO/ERROR/CRITICAL), `try/except`, safe file reading

---

## 🟡 INTERMEDIATE EXAMPLES

---

### Intermediate Example 1 – OOP ETL Pipeline (Extractor, Transformer, Loader)

**Topic:** OOP Pipeline Design  
**Objective:** Build a clean ETL pipeline using object-oriented classes.

```python
import csv
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger("etl_pipeline")

# ---------- EXTRACTOR ----------
class Extractor:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def extract(self) -> list[dict]:
        logger.info(f"Extracting from {self.filepath}")
        with open(self.filepath, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

# ---------- TRANSFORMER ----------
class Transformer:
    def transform(self, records: list[dict]) -> list[dict]:
        logger.info("Transforming records...")
        transformed = []
        for r in records:
            transformed.append({
                "customer_id": int(r["id"]),
                "customer_name": r["name"].strip().title(),
                "sale_amount": round(float(r["amount"]), 2),
                "is_premium": float(r["amount"]) > 500
            })
        logger.info(f"Transformed {len(transformed)} records.")
        return transformed

# ---------- LOADER ----------
class Loader:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def load(self, data: list[dict]) -> None:
        logger.info(f"Loading data to {self.output_path}")
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        logger.info("✅ Load complete.")

# ---------- PIPELINE RUNNER ----------
def run_pipeline(source: str, destination: str):
    extractor  = Extractor(source)
    transformer = Transformer()
    loader     = Loader(destination)

    raw_data    = extractor.extract()
    clean_data  = transformer.transform(raw_data)
    loader.load(clean_data)

# Run
run_pipeline("sales.csv", "output.json")
```

**Key Concepts:** Class design, single responsibility principle, method chaining via pipeline, logging at each stage, `list[dict]` typing

---

### Intermediate Example 2 – pandas Data Validation & Transformation

**Topic:** pandas & NumPy | Data Validation & Quality Checks  
**Objective:** Load a dataset, perform quality checks (nulls, types, schema), and apply vectorized transformations.

```python
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger("data_validator")

# ---------- LOAD ----------
df = pd.read_csv("sales.csv")
logger.info(f"Loaded {len(df)} rows, {len(df.columns)} columns.")

# ---------- SCHEMA VALIDATION ----------
required_columns = {"id", "name", "amount"}
missing_cols = required_columns - set(df.columns)
if missing_cols:
    raise ValueError(f"Missing columns: {missing_cols}")
logger.info("✅ Schema check passed.")

# ---------- NULL CHECK ----------
null_counts = df.isnull().sum()
if null_counts.any():
    logger.warning(f"Null values found:\n{null_counts[null_counts > 0]}")
else:
    logger.info("✅ No null values found.")

# ---------- TYPE ENFORCEMENT ----------
df["id"]     = df["id"].astype(int)
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Drop rows where 'amount' could not be cast
invalid_rows = df[df["amount"].isna()]
if not invalid_rows.empty:
    logger.warning(f"Dropping {len(invalid_rows)} rows with invalid 'amount'.")
df.dropna(subset=["amount"], inplace=True)

# ---------- VECTORIZED TRANSFORMATIONS ----------
df["amount_inr"]  = df["amount"] * 83.5          # USD to INR (NumPy broadcast)
df["tax"]         = np.where(df["amount"] > 500, df["amount"] * 0.18, 0)
df["name"]        = df["name"].str.strip().str.title()
df["is_premium"]  = df["amount"] > 500

# ---------- SUMMARY ----------
logger.info(f"\n{df.to_string(index=False)}")
logger.info(f"\nTotal Revenue (USD): ${df['amount'].sum():.2f}")
logger.info(f"Premium Customers:   {df['is_premium'].sum()}")

df.to_csv("validated_sales.csv", index=False)
logger.info("✅ Saved validated_sales.csv")
```

**Key Concepts:** Schema validation, null detection, type coercion, `np.where` vectorization, `str` accessor, derived columns

---

## 🔴 ADVANCED EXAMPLE

---

### Advanced Example 1 – Resilient Orchestrated Pipeline with Retries, Logging & DAG Simulation

**Topic:** Pipeline Orchestration | Retries | Error Handling | DAG Scheduling  
**Objective:** Simulate an Airflow-style DAG using Python with task dependencies, retry logic, structured logging, and pipeline monitoring — without needing Airflow installed.

```python
import csv
import json
import time
import logging
import functools
from datetime import datetime
from typing import Callable, Any

# ─────────────────────────────────────────────
# LOGGING SETUP
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pipeline.log", encoding="utf-8")
    ]
)
logger = logging.getLogger("orchestrator")

# ─────────────────────────────────────────────
# RETRY DECORATOR
# ─────────────────────────────────────────────
def retry(max_attempts: int = 3, delay: float = 1.0, exceptions=(Exception,)):
    """Decorator: retry a task on failure with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            task_logger = logging.getLogger(func.__name__)
            for attempt in range(1, max_attempts + 1):
                try:
                    task_logger.info(f"Attempt {attempt}/{max_attempts}")
                    result = func(*args, **kwargs)
                    task_logger.info("✅ Task succeeded.")
                    return result
                except exceptions as e:
                    task_logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        sleep_time = delay * (2 ** (attempt - 1))  # exponential backoff
                        task_logger.info(f"Retrying in {sleep_time:.1f}s...")
                        time.sleep(sleep_time)
                    else:
                        task_logger.error("❌ All attempts exhausted. Task FAILED.")
                        raise
        return wrapper
    return decorator

# ─────────────────────────────────────────────
# PIPELINE STATE TRACKER
# ─────────────────────────────────────────────
class PipelineMonitor:
    def __init__(self, dag_id: str):
        self.dag_id = dag_id
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.task_log: list[dict] = []

    def record(self, task_name: str, status: str, duration: float, error: str = None):
        entry = {
            "dag_id": self.dag_id,
            "run_id": self.run_id,
            "task": task_name,
            "status": status,
            "duration_sec": round(duration, 3),
            "error": error
        }
        self.task_log.append(entry)
        logger.info(f"[MONITOR] {task_name} → {status} ({duration:.2f}s)")

    def summary(self):
        logger.info("\n" + "="*55)
        logger.info(f"  DAG: {self.dag_id} | Run: {self.run_id}")
        logger.info("="*55)
        for t in self.task_log:
            icon = "✅" if t["status"] == "SUCCESS" else "❌"
            logger.info(f"  {icon} {t['task']:<25} {t['status']:<10} {t['duration_sec']}s")
        failed = [t for t in self.task_log if t["status"] == "FAILED"]
        logger.info(f"\n  Total Tasks: {len(self.task_log)} | Failed: {len(failed)}")
        logger.info("="*55)
        return self.task_log

# ─────────────────────────────────────────────
# TASK DEFINITIONS (simulating Airflow operators)
# ─────────────────────────────────────────────
@retry(max_attempts=3, delay=0.5, exceptions=(FileNotFoundError, ValueError))
def task_extract(filepath: str) -> list[dict]:
    """T1: Extract – Read CSV source data."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))
    if not data:
        raise ValueError("Source file is empty!")
    return data

@retry(max_attempts=2, delay=0.3)
def task_validate(records: list[dict]) -> list[dict]:
    """T2: Validate – Schema & null checks."""
    required = {"id", "name", "amount"}
    for i, r in enumerate(records):
        missing = required - set(r.keys())
        if missing:
            raise ValueError(f"Row {i}: missing fields {missing}")
        if not r.get("amount"):
            raise ValueError(f"Row {i}: null amount")
    return records

def task_transform(records: list[dict]) -> list[dict]:
    """T3: Transform – Clean and enrich data."""
    result = []
    for r in records:
        result.append({
            "id":         int(r["id"]),
            "name":       r["name"].strip().title(),
            "amount":     round(float(r["amount"]), 2),
            "amount_inr": round(float(r["amount"]) * 83.5, 2),
            "is_premium": float(r["amount"]) > 500,
            "processed_at": datetime.now().isoformat()
        })
    return result

def task_load(records: list[dict], output_path: str) -> str:
    """T4: Load – Write output to JSON."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)
    return output_path

# ─────────────────────────────────────────────
# DAG RUNNER (simulates Airflow DAG execution)
# ─────────────────────────────────────────────
def run_dag(source: str, output: str):
    monitor = PipelineMonitor(dag_id="sales_etl_pipeline")
    logger.info(f"\n🚀 Starting DAG: {monitor.dag_id} | Run: {monitor.run_id}\n")

    pipeline = [
        ("extract",   lambda: task_extract(source)),
        ("validate",  None),  # depends on extract output
        ("transform", None),  # depends on validate output
        ("load",      None),  # depends on transform output
    ]

    data = None
    tasks_in_order = [
        ("T1_extract",   lambda: task_extract(source),      None),
        ("T2_validate",  lambda d: task_validate(d),        "data"),
        ("T3_transform", lambda d: task_transform(d),       "data"),
        ("T4_load",      lambda d: task_load(d, output),    "data"),
    ]

    for task_name, task_fn, input_key in tasks_in_order:
        start = time.time()
        try:
            data = task_fn(data) if input_key else task_fn()
            monitor.record(task_name, "SUCCESS", time.time() - start)
        except Exception as e:
            monitor.record(task_name, "FAILED", time.time() - start, str(e))
            logger.error(f"💥 Pipeline halted at {task_name}: {e}")
            break

    return monitor.summary()

# ─────────────────────────────────────────────
# ENTRYPOINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    run_dag(source="sales.csv", output="final_output.json")
```

**What This Demonstrates:**

| Feature | Implementation |
|---|---|
| DAG simulation | Sequential task runner with dependency chain |
| Retry logic | `@retry` decorator with exponential backoff |
| Logging | File + console handlers, per-task loggers |
| Monitoring | `PipelineMonitor` tracks status, duration, errors |
| OOP design | Extractor/Transformer/Loader via task functions |
| Error propagation | Pipeline halts gracefully on unrecoverable failure |
| Orchestration concept | Mirrors Airflow's `dag >> t1 >> t2 >> t3` model |

**Sample Pipeline Log:**
```
2026-02-23 10:00:00 | INFO     | T1_extract   → SUCCESS    0.01s
2026-02-23 10:00:00 | INFO     | T2_validate  → SUCCESS    0.00s
2026-02-23 10:00:00 | INFO     | T3_transform → SUCCESS    0.00s
2026-02-23 10:00:00 | INFO     | T4_load      → SUCCESS    0.01s

  Total Tasks: 4 | Failed: 0
```

---

## 📋 Quick Reference – Example Summary

| # | Level | Topic | Key Skills |
|---|-------|-------|------------|
| 1 | 🟢 Beginner | CSV Read/Write | `csv.DictReader`, file handling |
| 2 | 🟢 Beginner | JSON Parsing | `json.load/dump`, filtering |
| 3 | 🟢 Beginner | Exception Handling & Logging | `try/except`, `logging` levels |
| 4 | 🟡 Intermediate | OOP ETL Pipeline | Classes, ETL pattern, SRP |
| 5 | 🟡 Intermediate | pandas Validation & Transforms | Schema checks, `np.where`, vectorization |
| 6 | 🔴 Advanced | Orchestrated Pipeline + Retries | DAG simulation, decorators, monitoring |

---
*Python for Data Engineers – 4-Hour Condensed Program | Module 1 & 2*
