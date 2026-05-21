import logging
import os

LOG_DIR = "app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename="app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()