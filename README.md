# Customer Churn Analytics

This project develops an end-to-end churn analytics system designed to simulate a banking data environment.
The system integrates automated data pipelines, layered SQL transformations, and interpretable machine learning models to monitor customer behavior and identify churn risk. By combining business KPIs, behavioral segmentation, and predictive modeling, the system provides actionable insights to guide targeted and cost-efficient retention strategies.

## Business Objective

Customer attrition is a major source of revenue loss in retail banking, as acquiring new customers is significantly more expensive than retaining existing ones. Customer acquisition usually involves significant upfront investments through subsidized credit products, promotional savings rates, and sign-up bonuses. These strategies often result in delayed profitability, making long-term customer retention critical for recovering acquisition costs and generating sustainable value.

Customer value in retail banking typically increases over time as relationships deepen, trust grows, and customers adopt a broader range of financial products such as credit, savings, and investments. As interaction and activity expand, customers tend to concentrate financial activity in one institution, increasing the institution's share of customer financial activity and reducing attrition risk. At the same time, the institution accumulates richer behavioral data, enabling more accurate risk assessment and targeted product offerings, which increase profitability.

This lifecycle dynamic makes early detection of disengagement particularly important, as attrition in early stages can prevent long-term value creation. Sustainable growth requires continuously managing the balance between acquisition and retention, rather than relying solely on expansion. Effective retention strategies rely on continuous monitoring of customer engagement to enable targeted and cost-efficient interventions that stabilize revenue streams and support long-term growth.

## Project Goals

The objective of this project is to build a structured churn analytics framework that supports proactive customer retention through behavioral analysis, segmentation, and predictive modeling. Key goals include:
#### Understanding customer behavior
- Analyze customer behavior through engagement, transaction activity, and credit utilization patterns.
- Identify behavioral changes across the customer lifecycle that precede disengagement and churn.
#### Churn driver identification
- Quantify the impact of inactivity and declining engagement on churn risk.
- Detect high-risk customer segments and key behavioral drivers of churn.
#### Customer segmentation
- Group customers based on engagement, product usage, and churn risk.
- Identify high-value but vulnerable customers for targeted intervention.
#### Predictive analytics
- Develop interpretable models to estimate churn probability and proxy measures of customer value.
- Compare alternative approaches using structured evaluation.
#### Monitoring and decision support
- Define KPIs to track retention, engagement, and behavioral trends.
- Develop structured reporting and visualization to enable continuous monitoring and evaluation of retention strategies based on risk, value, and intervention cost.

## System Architecture

## Tech Stack
- Python
- SQL

## Dataset

The project uses the [Credit Card Customer Churn](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers/) dataset from Kaggle, which features:

- Customer demographics
- Transaction behavior
- Engagement signals
- Credit utilization

## Data Pipeline

The pipeline automates:

1. Dataset download from Kaggle
2. Raw data validation
3. Loading into PostgreSQL using COPY

The pipeline is idempotent and reproducible.

## Exploratory Data Analysis

EDA was performed on the raw dataset to identify key drivers of churn. Detailed findings are available in [EDA documentation](docs/eda.md).

## Key Insights

## Setup
The project has been developed on macOS and is compatible with Windows and Linux.
### Prerequisites
- Python installed
- Conda installed
- PostgreSQL installed and running locally
- Kaggle account with API credentials configured

### Installation

#### 1. Clone the repository:

```bash
git clone https://github.com/mbtosya/customer-retention-analytics.git
cd customer-retention-analytics
```
#### 2. Create and activate the Conda environment:
```bash
conda create -n churn-analytics python=3.10
conda activate churn-analytics
```
#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
#### 4. Configure Kaggle API:
1. Download your Kaggle API key from your Kaggle account settings.
2. Place the file in:

**macOS / Linux:**
```
~/.kaggle/kaggle.json
```
Set appropriate permissions (Optional, recommended):
```bash
chmod 600 ~/.kaggle/kaggle.json
```
**Windows:**
```
C:\Users\<your-username>\.kaggle\kaggle.json
```
#### 5. Start PostgreSQL:
Make sure your local PostgreSQL instance is running.
You can test the connection with:
```bash
psql postgres
```
Exit with:
```bash
\q
```
#### 6. Run the pipeline:
```bash
python run_pipeline.py
```
