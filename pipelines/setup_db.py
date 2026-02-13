import logging

from sqlalchemy import create_engine, text

from config import DB_NAME


def create_database():
    logging.info("Checking whether the database exists...")
    engine = create_engine("postgresql://localhost/postgres")

    with engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT 1 FROM pg_database WHERE datname=:name"
            ),
            {"name": DB_NAME},
        )

        if not result.scalar():
            logging.info(f"Creating database: {DB_NAME}")
            conn.execute(text("COMMIT"))
            conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
        else:
            logging.info("Database already exists.")
