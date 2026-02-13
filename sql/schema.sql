CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS raw.customer_churn (
    clientnum BIGINT,
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
    naive_bayes_1 NUMERIC,
    naive_bayes_2 NUMERIC,
    ingestion_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_customer_churn_attrition
ON raw.customer_churn (attrition_flag);

CREATE INDEX IF NOT EXISTS idx_customer_churn_clientnum
ON raw.customer_churn (clientnum);


CREATE TABLE IF NOT EXISTS staging.customer_churn (
    clientnum BIGINT PRIMARY KEY,
    churned INTEGER,
    months_inactive_12_mon INTEGER,
    contacts_count_12_mon INTEGER,
    total_trans_amt NUMERIC,
    total_trans_ct INTEGER,
    avg_utilization_ratio NUMERIC
);
