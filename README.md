# Customer Retention Analytics

End-to-end churn analytics system designed to simulate a banking data environment.

The project has been developed and tested on macOS and is compatible with Windows and Linux.

## Business Objectives

## Project Goals

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
```bash
~/.kaggle/kaggle.json
```
Set appropriate permissions (Optional, recommended):
```bash
chmod 600 ~/.kaggle/kaggle.json
```
Windows:
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
