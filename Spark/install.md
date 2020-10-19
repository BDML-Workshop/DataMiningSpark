# How To Install Spark
Installing Spark and getting to work with it can be a daunting task. This section will go deeper into how you can install it and what your options are to start working with it.

First, check if you have the [Java jdk installed](isJava). Then, go to the Spark download page. Keep the default options in the first three steps and you’ll find a downloadable link in step 4. Click to download it.

Second, check if you have the good version of [Python](isPython)

Next, make sure that you untar the directory that appears in your “Downloads” folder. Next, move the untarred folder to /opt/spark for exemple.

##TODO AUTOMATE INSTALL
Write a script for:
[ ] download the version of spark
[ ] Configure environment variables for spark
[ ] download data-set for lab use case
[ ] install all modules
[ ] configure environment variable
[ ] launch juputer lab with pyspark


```bash
$ tar xzf spark-3.0.1-bin-hadoop2.7.tgz
$ mv spark-3.0.1-bin-hadoop2.7 /opt/spark
``` 
**FOR WINDOWS 10 USERS:** use WSL and install a Linux bash to unpack tar files easily

Now that you’re all set to go, open the README file in /opt/spark. You’ll see that you’ll need to run a command to build Spark if you have a version that has not been built yet. So, make sure you run the command:

```bash
$ build/mvn -DskipTests clean package run
```
This might take a while, you will need an internet connection, but after this, you’re all set to go!

# some extra config

## for windows 10

   Add `winutils.exe` File in a directory Hadoop and define `HADOOP_HOME` in "System properties"

## configure some environment variables

export PYTHON_HOME=/opt/spark
export PYSPARK_PYTHON=PATHTOYOURPYTHON3.8
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --ip 0.0.0.0 --port 9999'.

**FOR WINDOWS USERS:**

# Interactive Spark Shell
Next, you can immediately start working in the Spark shell by typing ./bin/pyspark in the same folder in which you left off at the end of the last section. It can take a bit of time, but eventually, you’ll see something like this: