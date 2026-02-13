import logging
import os
import subprocess
import zipfile

from pipelines.config import DATASET_NAME, RAW_CSV, RAW_DIR, ZIP_PATH


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

def run_extract():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    download_dataset()
    unzip_dataset()
    logging.info("Raw data ready.")
