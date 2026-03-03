"""
Sales data ETL pipeline.
Handles extraction and transformation of sales data.
"""

import pandas as pd
from base import BaseETL


class SalesPipeline(BaseETL):
    """ETL pipeline for sales data."""

    def __init__(self, source_path=None):
        self.source_path = source_path or "sales.csv"

    def extract(self):
        """Extract sales data from CSV file."""
        return pd.read_csv(self.source_path)

    def transform(self, data):
        """Transform sales data (add revenue, clean, aggregate)."""
        df = data.copy()
        if "quantity" in df.columns and "price" in df.columns:
            df["revenue"] = df["quantity"] * df["price"]
        return df

    def load(self, data):
        """Load is handled by db_loader; this pipeline only extracts and transforms."""
        return data
