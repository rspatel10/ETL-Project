"""
Base module for ETL pipeline.
Contains abstract base class and shared utilities.
"""

from abc import ABC, abstractmethod


class BaseETL(ABC):
    """Abstract base class for ETL pipelines."""

    @abstractmethod
    def extract(self):
        """Extract data from source."""
        pass

    @abstractmethod
    def transform(self, data):
        """Transform extracted data."""
        pass

    @abstractmethod
    def load(self, data):
        """Load transformed data to destination."""
        pass

    def run(self):
        """Execute full ETL pipeline."""
        data = self.extract()
        transformed = self.transform(data)
        self.load(transformed)
