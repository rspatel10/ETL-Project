"""
Main entry point for ETL pipeline.
Orchestrates extract, transform, and load steps.
"""

from sales_pipeline import SalesPipeline
from db_loader import DBLoader


def main():
    """Run the sales ETL pipeline."""
    pipeline = SalesPipeline(source_path="sales.csv")
    loader = DBLoader(output_path="output.csv")

    # Extract and transform
    data = pipeline.extract()
    transformed = pipeline.transform(data)

    # Load
    loader.load_to_csv(transformed)


if __name__ == "__main__":
    main()
