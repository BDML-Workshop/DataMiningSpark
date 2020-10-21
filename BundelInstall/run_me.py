#! /home/pascalfares/vDMA/bin/python

from pathlib import Path
import sys
import subprocess
import os
import logging

from download_data import download
from sparkDownload import download as download_spark

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)-7s  %(name)-19s  %(message)s", style="%"
)
logger = logging.getLogger("CourseHandler")

if __name__ == "__main__":
    logger.info("Welcome to '%s' by %s", "WorkShop BDA", "Pascal Fares")
    logger.info("Course Version: %s", "0.0")
    logger.info("Course Name: %s",
                "Mastering Big Data Analytics with PySpark [Machine Learning & Data Mining Workshop]")

    logger.info("1. Step 1 : Install Java ")
    subprocess.check_call(['java','--version'])
    logger.info("Installing spark, needed packages and pyspark")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", '-r', 'requirement_me.txt'])
    logger.info("And Downloading the data")
    download_spark()
    
    download()

    # Set up the course launch pyspark
    logger.info("Set up environment of the course and launch pyspark with jupyter lab")
    HOME_PATH = Path(os.environ['HOME'])
    REPO_PATH = HOME_PATH / 'DataMiningSpark'
    BASE_DIR = REPO_PATH
    spark_home = 'sparkhome/spark-3.0.1-bin-hadoop2.7'
    data_examples = spark_home + "/data"
    data_sets = 'data-sets'
    os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'
    os.environ['SPARK_HOME'] = str(BASE_DIR / spark_home)
    os.environ['DATA_SETS'] = str(BASE_DIR / data_sets)
    os.environ['DATA_EXAMPLES'] = str(BASE_DIR / data_examples)
    print(os.environ['SPARK_HOME'])
    os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
    os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'

    # subprocess.check_call(os.environ['SPARK_HOME'] + '/bin/pyspark', shell=True)
    os.system(f"cd ..; {os.environ['SPARK_HOME']+ '/bin/pyspark'}")
    print("Voila ..... Wait a little and Enjoy")
