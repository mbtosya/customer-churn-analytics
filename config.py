import getpass
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_CSV = RAW_DIR / "BankChurners.csv"
ZIP_PATH = RAW_DIR / "credit-card-customers.zip"
SCHEMA_PATH = PROJECT_ROOT / "sql" / "schema.sql"
STAGING_SQL_PATH = PROJECT_ROOT / "sql" / "staging.sql"


DATASET_NAME = "sakshigoyal7/credit-card-customers"
DB_NAME = "churn_analytics"

# Make more robust with docker later
DB_USER = os.getenv("DB_USER", getpass.getuser())
DB_URL = os.getenv(
    "DB_URL",
    f"postgresql://{DB_USER}@localhost:5432/churn_analytics"
)
