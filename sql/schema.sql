CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS raw.customer_churn (
    clientnum INTEGER,
    attrition_flag TEXT,
    customer_age INTEGER,
    gender TEXT,
    dependent_count INTEGER,
    education_level TEXT,
    marital_status TEXT,
    income_category TEXT,
    card_category TEXT,
    months_on_book INTEGER,
    total_relationship_count INTEGER,
    months_inactive_12_mon INTEGER,
    contacts_count_12_mon INTEGER,
    credit_limit NUMERIC,
    total_revolving_bal NUMERIC,
    avg_open_to_buy NUMERIC,
    total_amt_chng_q4_q1 NUMERIC,
    total_trans_amt NUMERIC,
    total_trans_ct INTEGER,
    total_ct_chng_q4_q1 NUMERIC,
    avg_utilization_ratio NUMERIC,
    naive_bayes_score_1 NUMERIC,
    naive_bayes_score_2 NUMERIC,
    ingestion_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_customer_churn_attrition
ON raw.customer_churn (attrition_flag);

CREATE INDEX IF NOT EXISTS idx_customer_churn_clientnum
ON raw.customer_churn (clientnum);

DROP TABLE IF EXISTS staging.customer_churn;

CREATE TABLE staging.customer_churn (
    snapshot_date DATE,
    clientnum INTEGER,
    is_churned INTEGER,
    customer_age INTEGER,
    gender TEXT,
    dependent_count INTEGER,
    education_level TEXT,
    marital_status TEXT,
    income_category TEXT,
    card_type TEXT,
    tenure_months INTEGER,
    product_count INTEGER,
    inactive_months_last_12m INTEGER,
    contact_events_last_12m INTEGER,
    credit_limit NUMERIC,
    revolving_balance NUMERIC,
    spending_change_q4_q1 NUMERIC,
    transaction_amount_last_12m NUMERIC,
    transaction_count_last_12m INTEGER,
    transaction_count_change_q4_q1 NUMERIC,
    credit_utilization_ratio NUMERIC,
    inactivity_ratio NUMERIC,
    transaction_intensity NUMERIC,

    PRIMARY KEY (snapshot_date, clientnum)
);

CREATE INDEX IF NOT EXISTS idx_staging_churn
ON staging.customer_churn (is_churned);

