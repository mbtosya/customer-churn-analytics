import logging

import pandas as pd
from sqlalchemy import create_engine

from config import DB_URL, RAW_CSV


def get_db_columns(cursor):
    cursor.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'raw'
          AND table_name = 'customer_churn'
        ORDER BY ordinal_position;
        """
    )
    return [row[0] for row in cursor.fetchall()]

def get_csv_columns():
    df = pd.read_csv(RAW_CSV, nrows=0)
    return [col.strip().lower() for col in df.columns]

def format_set(s: set) -> str:
    if not s:
        return "[none]"
    return ", ".join(sorted(s))


def validate_schema(cursor):
    db_columns = get_db_columns(cursor)
    csv_columns = get_csv_columns()
    db_columns_without_ts = [c for c in db_columns if c != "ingestion_ts"]

    # Column count validation
    if len(csv_columns) != len(db_columns_without_ts):
        raise ValueError(
            f"Column count mismatch. CSV={len(csv_columns)}, DB={len(db_columns_without_ts)}"
        )

    # Column presence validation
    missing = set(db_columns_without_ts) - set(csv_columns)
    extra = set(csv_columns) - set(db_columns_without_ts)

    if missing or extra:
        raise ValueError(
            f"Schema mismatch.\n"
            f"Missing columns: {format_set(missing)}\n"
            f"Extra columns: {format_set(extra)}"
        )

    # Column order validation
    if csv_columns != db_columns_without_ts:
        order_diff = [
            (i, csv, db)
            for i, (csv, db) in enumerate(zip(csv_columns, db_columns_without_ts))
            if csv != db
        ]

        details = "\n".join(
            f"Position {i}: CSV='{csv}', DB='{db}'"
            for i, csv, db in order_diff[:5]
        )

        raise ValueError(
            "Column order mismatch.\n" + details
        )


def run_load_raw():
    logging.info("Loading raw data into PostgreSQL...")

    engine = create_engine(DB_URL)
    conn = engine.raw_connection()

    try:
        cursor = conn.cursor()

        validate_schema(cursor)

        cursor.execute("TRUNCATE TABLE raw.customer_churn;")

        with open(RAW_CSV, "r") as f:
            cursor.copy_expert(
                """
                COPY raw.customer_churn (
                    clientnum,
                    attrition_flag,
                    customer_age,
                    gender,
                    dependent_count,
                    education_level,
                    marital_status,
                    income_category,
                    card_category,
                    months_on_book,
                    total_relationship_count,
                    months_inactive_12_mon,
                    contacts_count_12_mon,
                    credit_limit,
                    total_revolving_bal,
                    avg_open_to_buy,
                    total_amt_chng_q4_q1,
                    total_trans_amt,
                    total_trans_ct,
                    total_ct_chng_q4_q1,
                    avg_utilization_ratio,
                    bayes_1,
                    bayes_2
                )
                FROM STDIN WITH CSV HEADER
                """,
                f,
            )

        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM raw.customer_churn;")
        result = cursor.fetchone()
        assert result is not None
        count = result[0]
        logging.info(f"Rows loaded: {count}")

    finally:
        cursor.close()
        conn.close()

    logging.info("Raw data loaded.")

