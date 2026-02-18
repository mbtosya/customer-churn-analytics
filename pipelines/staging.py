import logging

from sqlalchemy import create_engine, text

from config import DB_URL, STAGING_SQL_PATH


def run_staging():
    logging.info("Running staging transformations...")

    engine = create_engine(DB_URL)

    if not STAGING_SQL_PATH.exists():
        raise FileNotFoundError(f"Staging SQL not found: {STAGING_SQL_PATH}")

    with open(STAGING_SQL_PATH, "r") as f:
        staging_sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(staging_sql))

        # Data quality monitoring
        raw_result = conn.execute(
            text("SELECT COUNT(*) FROM raw.customer_churn;")
        ).scalar()

        staging_result = conn.execute(
            text("SELECT COUNT(*) FROM staging.customer_churn;")
        ).scalar()

        raw_count = int(raw_result) if raw_result is not None else 0
        staging_count = int(staging_result) if staging_result is not None else 0

    logging.info(f"Raw rows: {raw_count}")
    logging.info(f"Staging rows: {staging_count}")
    logging.info(f"Filtered rows: {raw_count - staging_count}")
    logging.info("Staging layer complete.")
