import logging
import sys

from pipelines.extract import run_extract
from pipelines.setup_db import create_database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s")

def main():
    try:
        logging.info("Starting pipeline...")

        create_database()
        run_extract()

        logging.info("Pipeline finished.")

    except Exception as e:
        logging.exception("Pipeline failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
