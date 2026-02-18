import logging
import subprocess
import zipfile

import pandas as pd

from config import DATASET_NAME, RAW_CSV, RAW_DIR, ZIP_PATH


def download_dataset():
    if ZIP_PATH.exists():
        logging.info("Dataset already downloaded.")
        return

    logging.info("Downloading dataset from Kaggle...")

    try:
        subprocess.run(
            [
                "kaggle",
                "datasets",
                "download",
                "-d",
                DATASET_NAME,
                "-p",
                str(RAW_DIR),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        logging.error("Kaggle download failed. Ensure your API key is configured correctly.")
        raise

def unzip_dataset():

    if RAW_CSV.exists():
        logging.info("Raw data already exists.")
        return

    if not ZIP_PATH.exists():
        raise FileNotFoundError("Dataset zip not found.")

    logging.info("Unzipping dataset...")

    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(RAW_DIR)

def validate_raw_data():
    logging.info("Validating raw dataset...")

    df = pd.read_csv(RAW_CSV)

    if df.empty:
        raise ValueError("Dataset is empty.")

    logging.info(f"Rows: {len(df)}")
    logging.info(f"Columns: {len(df.columns)}")

    core_columns = ["CLIENTNUM", "Attrition_Flag"]
    missing = [c for c in core_columns if c not in df.columns]

    if missing:
        raise ValueError(f"Missing core columns: {missing}")

    logging.info("Raw dataset validation passed.")

# Rename naive bayes columns to avoid duplicate column error during table creation as the original names are truncated and become identical.
def standardize_columns():
    logging.info("Standardizing column names...")

    df = pd.read_csv(RAW_CSV)

    # Check if already standardized
    if "bayes_1" in df.columns and "bayes_2" in df.columns:
        logging.info("Columns already standardized.")
        return

    rename_map = {}

    for col in df.columns:
        col_lower = col.lower()

        if "naive_bayes" in col_lower:
            if col_lower.endswith("_1"):
                rename_map[col] = "naive_bayes_score_1"
            elif col_lower.endswith("_2"):
                rename_map[col] = "naive_bayes_score_2"

    if rename_map:
        df.rename(columns=rename_map, inplace=True)

        if df.columns.duplicated().any():
            raise ValueError("Duplicate columns detected after standardization.")

        df.to_csv(RAW_CSV, index=False)
        logging.info(f"Renamed {len(rename_map)} columns.")
    else:
        logging.warning("Naive Bayes columns not found in source.")


def run_extract():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    download_dataset()
    unzip_dataset()
    standardize_columns()
    validate_raw_data()

    logging.info("Raw data ready.")
