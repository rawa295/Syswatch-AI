import time

from agent.main import run_monitoring
from logger.logger import log_info
from config.loader import load_config
config = load_config()
interval = config["monitoring"]["interval"]
def start_scheduler():

    log_info("Scheduler started")

    while True:

        run_monitoring()

        time.sleep(interval)


if __name__ == "__main__":
    start_scheduler()