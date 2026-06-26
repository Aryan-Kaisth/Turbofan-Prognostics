# src/logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def configure_logging(log_level: int = logging.INFO) -> None:
    """Sets up the global logging configuration for the entire project.

    Configures the root logger with two handlers:
    1. A RotatingFileHandler that saves logs to '../logs/system.log' (1MB limit, 5 backups, UTF-8).
    2. A StreamHandler that prints clean, aligned logs to the terminal (sys.stderr).

    Args:
        log_level (int): The logging threshold (e.g., logging.INFO, logging.DEBUG). 
        Defaults to logging.INFO.

    Returns:
        None. Modifies global logging behavior and creates a '/logs' directory if missing.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE_DIR / "logs"
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE = LOG_DIR / "system.log"

    root_logger = logging.getLogger()
    
    if root_logger.hasHandlers():
        return

    root_logger.setLevel(log_level)

    # File Stream Configuration
    file_formatter = logging.Formatter(
        "[{asctime}] [{filename}:{lineno}] {name} - {levelname} - {message}", 
        datefmt="%Y-%m-%d %H:%M:%S",
        style='{'
    )
    file_handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=1 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)

    # Terminal Stream Configuration
    console_formatter = logging.Formatter(
        "[{asctime}] [{filename}:{lineno}] {levelname:7} - {message}", 
        datefmt="%H:%M:%S",
        style='{'
    )
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)