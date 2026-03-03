# Python for Data Engineers – 4‑Hour Exercises


![Logo](./logo.png)


> Copy any block into a `.py` file and run in VS Code. Where needed, scripts auto-create small sample data.


---

## Module 1 – Exercise: CSV Parsing & Cleaning

```python
from pathlib import Path
import csv

DATA = Path('data'); DATA.mkdir(exist_ok=True)
SRC = DATA / 'customers.csv'
OUT = DATA / 'customers_clean.csv'

if not SRC.exists():
    with SRC.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['first_name','last_name','email','city'])
        w.writerows([
            ['Aarav','Patel','AARAV.PATEL@EXAMPLE.COM','Vadodara'],
            ['Ishaan','Shah','ishaan.shah@example.com',''],
            ['Rohan','Mehta','rohan.mehta@example.com','Ahmedabad'],
        ])

with SRC.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    r['email'] = r['email'].lower()
    r['city'] = r['city'] or 'UNKNOWN'
    r['full_name'] = f"{r['first_name']} {r['last_name']}"

with OUT.open('w', newline='', encoding='utf-8') as f:
    fields = ['first_name','last_name','full_name','email','city']
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(rows)

print('Cleaned file written to', OUT.resolve())
```


---

## Module 1 – Exercise: JSON Flattening to Line Items

```python
from pathlib import Path
import json, csv

DATA = Path('data'); DATA.mkdir(exist_ok=True)
SRC = DATA / 'orders.json'
OUT = DATA / 'orders_flat.csv'

sample = {
    'orders': [
        {'id': 1, 'customer': {'id': 'C100', 'city': 'Vadodara'}, 'lines': [
            {'sku': 'P1', 'qty': 2, 'price': 99.0}
        ]},
        {'id': 2, 'customer': {'id': 'C101', 'city': None}, 'lines': [
            {'sku': 'P2', 'qty': 1, 'price': 149.0},
            {'sku': 'P3', 'qty': 3, 'price': 20.0}
        ]}
    ]
}
if not SRC.exists():
    SRC.write_text(json.dumps(sample, indent=2), encoding='utf-8')

data = json.loads(SRC.read_text(encoding='utf-8'))
rows = []
for o in data.get('orders', []):
    for line in o.get('lines', []):
        amount = float(line['qty']) * float(line['price'])
        rows.append({'order_id': o['id'], 'customer_id': o['customer']['id'],
                     'city': o['customer']['city'] or 'UNKNOWN', 'sku': line['sku'],
                     'qty': int(line['qty']), 'price': float(line['price']),
                     'amount': round(amount, 2)})

with OUT.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader(); writer.writerows(rows)
print('Flattened rows written to', OUT.resolve())
```


---

## Module 1 – Exercise: Schema Validation & Null Handling

```python
from pathlib import Path
import csv
from typing import Any, Dict

DATA = Path('data')
SRC = DATA / 'orders_flat.csv'
ERR = DATA / 'validation_errors.csv'

schema = {
    'order_id': int,
    'customer_id': str,
    'city': str,
    'sku': str,
    'qty': int,
    'price': float,
    'amount': float,
}

def coerce(v: str, typ):
    if typ is int: return int(v)
    if typ is float: return float(v)
    return str(v) if v is not None else ''

if not SRC.exists():
    raise SystemExit('orders_flat.csv not found. Run json_flatten.py first.')

errors = []; valid = []
with SRC.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        row_errors = []; clean: Dict[str, Any] = {}
        for col, typ in schema.items():
            val = row.get(col)
            if val is None or val == '':
                row_errors.append(f'Missing {col}'); continue
            try:
                clean[col] = coerce(val, typ)
            except Exception:
                row_errors.append(f'Bad type for {col}: {val!r}')
        if row_errors: errors.append({'line': i, 'errors': '; '.join(row_errors)})
        else: valid.append(clean)

if errors:
    with ERR.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['line','errors'])
        w.writeheader(); w.writerows(errors)
    print('Validation errors written to', ERR.resolve())
else:
    print('No validation errors!')
print('Valid rows:', len(valid))
```


---

## Module 1 – Exercise: pandas Transformation & Aggregation

```python
from pathlib import Path
import pandas as pd

DATA = Path('data')
SRC = DATA / 'orders_flat.csv'
OUT = Path('out'); OUT.mkdir(exist_ok=True)

if not SRC.exists():
    raise SystemExit('orders_flat.csv not found. Run json_flatten.py first.')

orders = pd.read_csv(SRC)
orders['amount'] = pd.to_numeric(orders['amount'], errors='coerce').fillna(0)

by_city = orders.groupby('city', as_index=False)['amount'].sum().sort_values('amount', ascending=False)
by_sku = orders.groupby('sku', as_index=False).agg(qty=('qty','sum'), revenue=('amount','sum')).sort_values('revenue', ascending=False)

by_city.to_csv(OUT / 'revenue_by_city.csv', index=False)
by_sku.to_csv(OUT / 'revenue_by_sku.csv', index=False)
print('Wrote outputs to', OUT.resolve())
```


---

## Module 2 – Exercise: OOP ETL with Logging & Retries

```python
from __future__ import annotations
import argparse, csv, logging, time
from pathlib import Path
from typing import Iterable, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s - %(message)s')
logger = logging.getLogger('etl')

def retry(times: int = 3, delay: float = 0.5):
    def deco(fn):
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(1, times+1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    logger.warning('%s failed (%d/%d): %s', fn.__name__, attempt, times, e)
                    time.sleep(delay)
            raise last
        return wrapper
    return deco

class CSVExtractor:
    def __init__(self, path: Path):
        self.path = path
    @retry(2, 0.2)
    def extract(self) -> Iterable[Dict[str, str]]:
        logger.info('Extracting from %s', self.path)
        with self.path.open(newline='', encoding='utf-8') as f:
            yield from csv.DictReader(f)

class Transformer:
    def transform(self, row: Dict[str, str]) -> Dict[str, str]:
        r = dict(row)
        r['city'] = r.get('city') or 'UNKNOWN'
        if 'qty' in r and 'price' in r:
            try:
                r['amount'] = str(round(float(r['qty']) * float(r['price']), 2))
            except Exception:
                r['amount'] = r.get('amount', '0')
        return r

class CSVSink:
    def __init__(self, path: Path, fieldnames: list[str]):
        self.path = path
        self.fieldnames = fieldnames
        self.path.parent.mkdir(parents=True, exist_ok=True)
    @retry(2, 0.2)
    def load(self, rows: Iterable[Dict[str, str]]):
        logger.info('Loading to %s', self.path)
        with self.path.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=self.fieldnames)
            w.writeheader()
            for r in rows: w.writerow(r)
        return self.path

def run_pipeline(src: Path, out: Path):
    extractor = CSVExtractor(src)
    transformer = Transformer()
    rows = list(extractor.extract())
    if not rows: raise ValueError('No input rows')
    if 'amount' not in rows[0]: rows = [transformer.transform(r) for r in rows]
    sink = CSVSink(out, list(rows[0].keys()))
    sink.load(rows); logger.info('ETL completed: %s', out.resolve())

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', default='data/orders_flat.csv')
    ap.add_argument('--out', default='out/etl_output.csv')
    args = ap.parse_args(); run_pipeline(Path(args.src), Path(args.out))
```


---

## Module 2 – Exercise: Logging & Exception Handling

```python
import logging
from pathlib import Path

LOG_FILE = Path('app.log')
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    handlers=[logging.FileHandler(LOG_FILE, encoding='utf-8'), logging.StreamHandler()])
logger = logging.getLogger('demo')

try:
    logger.info('Starting task')
    x = 10 / 2
    logger.debug('Intermediate value x=%s', x)
    if x == 5: raise ValueError('Simulated application error')
except ZeroDivisionError:
    logger.exception('Division by zero!')
except Exception as e:
    logger.exception('Unhandled error: %s', e)
else:
    logger.info('Task succeeded')
finally:
    logger.info('Task finished (success or fail)')
print('Logs written to', LOG_FILE.resolve())
```


---

## Module 2 – Exercise: Minimal Airflow DAG (Optional)

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print('Hello from Airflow task')

dag = DAG('simple_etl', start_date=datetime(2025,1,1), schedule_interval='@daily', catchup=False)
hello = PythonOperator(task_id='hello', python_callable=say_hello, dag=dag)
```
