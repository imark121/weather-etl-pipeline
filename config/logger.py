import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if logger already exists
    if logger.handlers:
        return logger

    # Format — shows time, file name, level, message
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Handler 1 — prints to terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Handler 2 — writes to a log file
    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler("logs/etl.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger