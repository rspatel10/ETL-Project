import pandas as pd
import sqlite3
import logging

class IPLDataPipeline:

    def __init__(self, csv_path, db_name="ipl.db"):
        self.csv_path = csv_path
        self.db_name = db_name

    def extract(self):
        logging.info("Starting data extraction")
        try:
            df = pd.read_csv(self.csv_path)
            logging.info(f"Extracted {len(df)} records")
            return df
        except Exception as e:
            logging.error(f"Extraction failed: {e}")
            raise

    def transform(self, df):
        logging.info("Starting transformation")

        # Important match events
        df['is_boundary'] = df['total_runs'].apply(lambda x: 1 if x >= 4 else 0)
        df['is_wicket'] = df['is_wicket'].astype(int)

        logging.info("Transformation completed")
        return df

    def load(self, df):
        logging.info("Loading data into database")
        conn = sqlite3.connect(self.db_name)
        df.to_sql("ball_by_ball", conn, if_exists="replace", index=False)
        conn.close()
        logging.info("Data successfully loaded")

    def run(self):
        df = self.extract()
        df = self.transform(df)
        self.load(df)
if __name__ == "__main__":
    logging.basicConfig(
        filename="ipl_pipeline.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    pipeline = IPLDataPipeline("Ball_by_Ball.csv")
    pipeline.run()  
    print("ETL Pipeline executed successfully!")

