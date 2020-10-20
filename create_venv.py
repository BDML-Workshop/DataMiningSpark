import os, subprocess, sys
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="{levelname:7s}  {name:19s}  {message}", style="{"
)
logger = logging.getLogger("WorkShopHandler")

HOME_PATH = Path(os.environ['HOME'])
VENV_PATH = HOME_PATH / 'vDMA'

logger.info(f"Step 0: git clone https://github.com/opentrainingcamp/DataMiningSpark.git")

logger.info(f"Step 1: Virtual env")
if not os.path.exists(VENV_PATH):
    logger.info(f"Creating virtual env {str(VENV_PATH)}")
    subprocess.check_call([sys.executable, "-m", "venv", str(VENV_PATH)])
else:
    logger.info(f"Cvirtual env {str(VENV_PATH)} already exist")

logger.info(f"Step 2: activating the virtual environnement")

logger.info("By issuing the folowing command: (copy/paste it) ")

logger.info(f"source {str(VENV_PATH)+'/bin/activate'}")