from pathlib import Path, PurePath
import subprocess
import os
import logging
import re
import webbrowser
from time import sleep


from download_data import download

# TODO: fix docker.errors.APIError: 409 Client Error: Conflict ("Conflict. The container name "/mastering-pyspark-ml"
#  is already in use by container "5e645605bbef237ecabe3366dd512de182ac76505e3ff1cff16fb3d5af748cdf". You have to
#  remove (or rename) that container to be able to reuse that name.")

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)-7s  %(name)-19s  %(message)s", style="%"
)
logger = logging.getLogger("CourseHandler")


def re_search(pattern, text, plural=False):
    """Regex helper to find strings in a body of text"""
    match = [m.group(1) for m in re.finditer(pattern, text)]
    if plural:
        return match
    else:
        if match:
            return match[0]


def look_ahead(iter_item):
    """
    This function can be used to determine if there are items left after the current
    value in the iterable. It passes through all values from the given iterable,
    augmented by the information if there are more values to come after the current
    one. The data is enumerated as to provide an index key as well.

     Passes through all values from the given iterable augmented with a index number
     (i) and a boolean that determines if the current value is the last value.
              - (False) if there are more values after the current one
              - (True) if it is the last value

    :param iter_item: iterable item
    :return: yields index, value, last_flag

    Code example:
    >>> for i, v, last in look_ahead(["this","is","a","test"]):
    ...     print(i, v, last)
    ...     if last:
    ...         print("The End")
    0 this False
    1 is False
    2 a False
    3 test True
    The End

    Inspired by: (http://stackoverflow.com/questions/1630320/what-is-the-pythonic-way-to
    -detect-the-last-element-in-a-python-for-loop)
    """
    # Get an iterator and pull the first value (we are starting from the second value
    ii = iter(iter_item)
    last_value = next(ii)
    last_i = 0

    # Run the iterator to exhaustion. As long as loop is running we have not reached
    # the last value yet
    for i, value in enumerate(ii):
        # Report the *previous* value
        yield i, last_value, False
        last_value = value
        last_i = i + 1

    # Report the last value. Since the loop has finished we have reached the last value
    yield last_i, last_value, True




if __name__ == "__main__":
    logger.info("Welcome to '%s' by %s", "WorkShop BDA", "Pascal Fares")
    logger.info("Course Version: %s", "0.0")
    logger.info("Course Name: %s", "Mastering Big Data Analytics with PySpark [Machine Learning & Data Mining Workshop]")


    logger.info("Installing spark and pysaprk")

    logger.info("Downloading the data")
    #download()

    # Set up the course launch pyspark
    spark_home = 'sparkhome/spark-3.0.1-bin-hadoop2.7'
    os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'
    os.environ['SPARK_HOME'] = str(Path(__file__).resolve().parent / spark_home)
    print(os.environ['SPARK_HOME'])
    os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
    os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'

    subprocess.check_call(os.environ['SPARK_HOME'] + '/bin/pyspark',shell=True)
    
