import logging

from sqlalchemy import create_engine

from config import DB_URL, RAW_CSV


def run_load_raw():
    logging.info("Loading raw data into PostgreSQL...")

    engine = create_engine(DB_URL)
    conn = engine.raw_connection()

    try:
        cursor = conn.cursor()

        try:
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
                        naive_bayes_1,
                        naive_bayes_2
                    )
                    FROM STDIN
                    WITH CSV HEADER
                    """,
                    f,
                )


            conn.commit()

        finally:
            cursor.close()

    finally:
        conn.close()

    logging.info("Raw data loaded.")
