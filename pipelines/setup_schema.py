import logging
from pathlib import Path

from sqlalchemy import create_engine, text

from config import DB_URL, SCHEMA_PATH


def run_schema():
    logging.info("Setting up database schema...")

    engine = create_engine(DB_URL)


    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Schema file not found: {SCHEMA_PATH}")

    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()

    with engine.connect() as conn:
        conn.execute(text(schema_sql))
        conn.commit()

    logging.info("Schema setup complete.")
