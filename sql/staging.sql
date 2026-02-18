TRUNCATE TABLE staging.customer_churn;

INSERT INTO staging.customer_churn (
    snapshot_date,
    clientnum,
    is_churned,

    customer_age,
    gender,
    dependent_count,
    education_level,
    marital_status,
    income_category,
    card_type,

    tenure_months,
    product_count,
    inactive_months_last_12m,
    contact_events_last_12m,

    credit_limit,
    revolving_balance,
    spending_change_q4_q1,
    transaction_amount_last_12m,
    transaction_count_last_12m,
    transaction_count_change_q4_q1,
    credit_utilization_ratio
)
SELECT
    CURRENT_DATE AS snapshot_date,
    clientnum,

    CASE
        WHEN attrition_flag = 'Attrited Customer' THEN 1
        ELSE 0
    END AS is_churned,

    customer_age,
    gender,
    dependent_count,
    education_level,
    marital_status,
    income_category,
    card_category AS card_type,

    months_on_book AS tenure_months,
    total_relationship_count AS product_count,
    months_inactive_12_mon AS inactive_months_last_12m,
    contacts_count_12_mon AS contact_events_last_12m,

    credit_limit,
    total_revolving_bal AS revolving_balance,
    -- avg_open_to_buy excluded due to redundancy with credit_limit and revolving balance
    total_amt_chng_q4_q1 AS spending_change_q4_q1,
    total_trans_amt AS transaction_amount_last_12m,
    total_trans_ct AS transaction_count_last_12m,
    total_ct_chng_q4_q1 AS transaction_count_change_q4_q1,
    avg_utilization_ratio AS credit_utilization_ratio

    -- Behavioral features

FROM raw.customer_churn
WHERE
    clientnum IS NOT NULL
    AND months_on_book >= 0
    AND total_relationship_count >= 0
    AND months_inactive_12_mon >= 0
    AND credit_limit >= 0
    AND total_trans_amt >= 0
    AND total_trans_ct >= 0
    AND avg_utilization_ratio BETWEEN 0 AND 1;
