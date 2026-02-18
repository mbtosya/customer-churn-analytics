import logging
import sys

from pipelines.extract import run_extract
from pipelines.load_raw import run_load_raw
from pipelines.setup_db import create_database
from pipelines.setup_schema import run_schema
from pipelines.staging import run_staging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s")

def main():
    try:
        logging.info("Starting pipeline...")

        create_database()
        run_schema()
        run_extract()
        run_load_raw()
        run_staging()

        logging.info("Pipeline finished.")

    except Exception as e:
        logging.exception("Pipeline failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
