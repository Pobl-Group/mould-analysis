"""
Produces a CSV with the mould analysis dataset.

Takes a CSV input and applies fuzzy lookup logic, producing an output CSV with the mould analysis dataset.

Typical usage:
    `python3 main.py`
"""

import configparser
from datetime import datetime
import logging

import pandas as pd

from steps.fuzzy_lookup import get_fuzzy_lookup


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def run(config: dict) -> None:
    """
    Main run function.
    """

    job = "mould-analysis-dataset"

    fh = logging.FileHandler(f"{config['logging_path']}{job}.log")
    fh.setLevel(logging.INFO)
    LOGGER.addHandler(fh)

    start = datetime.now()
    # denote new instance
    LOGGER.info("---")
    LOGGER.info(f"start_time: {start}")

    key_words = config["key_words"].split(",")
    stop_words = config["stop_words"].split(",")

    try:

        df = pd.read_csv(config["input_file_path"])

        fuzzy_df = get_fuzzy_lookup(df, key_words, stop_words)

        fuzzy_df.to_csv(config["output_file_path"], index=False)

    except Exception as e:
        LOGGER.error(f"{job} raised an error:", exc_info=True)

    end = datetime.now()
    time_taken = end - start
    time_taken = time_taken.total_seconds()

    LOGGER.info(f"time_taken: {time_taken}")
    LOGGER.info(end)


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config.ini")

    run(config["parameters"])
