"""
Database loader module.
Handles loading transformed data into the database.
"""

import pandas as pd


class DBLoader:
    """Loads data into database or output file."""

    def __init__(self, output_path=None):
        self.output_path = output_path or "output.csv"

    def load_to_csv(self, data: pd.DataFrame):
        """Save DataFrame to CSV file."""
        data.to_csv(self.output_path, index=False)
        print(f"Data loaded to {self.output_path}")
