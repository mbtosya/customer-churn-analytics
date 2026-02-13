from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_CSV = RAW_DIR / "BankChurners.csv"
DATASET_NAME = "sakshigoyal7/credit-card-customers"
ZIP_PATH = RAW_DIR / "credit-card-customers.zip"

