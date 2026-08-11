import logging
import os


os.makedirs("logs", exist_ok=True)


logger = logging.getLogger("SysWatch")
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler(
    "logs/syswatch.log"
)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)


file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_critical(message):
    logger.critical(message)