import os
import logging
from logging.handlers import TimedRotatingFileHandler

# Ensure logs directory exists
LOG_DIR = os.path.join(os.getcwd(), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

def setup_logger(name: str):
    """
    Configures a logger with both console and timed rotating file handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent double logging if logger is reused
    if logger.hasHandlers():
        return logger

    # Formatter for logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Timed Rotating File Handler (Rotates daily, keeps 7 days)
    file_handler = TimedRotatingFileHandler(
        LOG_FILE,
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    # Customize the rotating file suffix to include dates
    file_handler.suffix = "%Y-%m-%d.log"
    logger.addHandler(file_handler)

    return logger

# Primary logger for the application
app_logger = setup_logger("AI-Script-Analyzer")
