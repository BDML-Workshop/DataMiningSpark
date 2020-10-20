# Mastering Big Data Analytics with PySpark [Machine Learning & Data Mining Workshop]
This is the code repository for the lab the 2 first sessions "Machine Learning & Data Mining Workshop".

Theses hand-on are mainly inspired by this workshop : https://github.com/PacktPublishing/Mastering-Big-Data-Analytics-with-PySpark Authored by: [Danny Meijer](https://www.linkedin.com/in/dannydatascientist). It is in fact a fork with adaptation to windows 10 and add some parts issued form our courses in [Cnam Liban](http://www.cnam-liban.fr).
[Ingénierie de la fouille et de la visualisation de données massives](http://cedric.cnam.fr/vertigo/Cours/RCP216/)
and
[Cours de bases de données documentaires et distribuées](http://b3d.bdpedia.fr/)


## About the WorkShop

[ ] adapt this paragraph

PySpark helps you perform data analysis at-scale; it enables you to build more scalable analyses and pipelines. This course starts by introducing you to PySpark's potential for performing effective analyses of large datasets. You'll learn how to interact with Spark from Python and connect Jupyter to Spark to provide rich data visualizations. After that, you'll delve into various Spark components and its architecture.

You'll learn to work with Apache Spark and perform ML tasks more smoothly than before. Gathering and querying data using Spark SQL, to overcome challenges involved in reading it. You'll use the DataFrame API to operate with Spark MLlib and learn about the Pipeline API. Finally, we provide tips and tricks for deploying your code and performance tuning.

By the end of this course, you will not only be able to perform efficient data analytics but will have also learned to use PySpark to easily analyze large datasets at-scale in your organization.

## What You Will Learn

* Gain knowledge of vital Data Analytics concepts via practical use cases
* Create elegant data visualizations using Jupyter
* Run, process, and analyze large chunks of datasets using PySpark
* Utilize Spark SQL to easily load big data into DataFrames
* Create fast and scalable Machine Learning applications using MLlib with Spark
* Perform exploratory Data Analysis in a scalable way
* Achieve scalable, high-throughput and fault-tolerant processing of data streams using Spark Streaming


## Instructions and Navigation
### Assumed Knowledge
This course will greatly appeal to data science enthusiasts, data scientists, or anyone who is familiar with Machine Learning concepts and wants to scale out his/her work to work with big data.

If you find it difficult to analyze large datasets that keep growing, then theses two first sessions are  the perfect guide for you!

A working knowledge of Python, installing and manipulatng some systeme admin in wondows 10 or Linux assumed.

## Technical Requirements 
#### Minimum Hardware Requirements
For successful completion of theses sessions, students will require the computer systems with at least the following:

OS: Windows entreprise or professional 10 build > 1903, any Linux distro (preferred), Mac (be autonome)
Processor: Any processor from the last few years
Memory: 2GB RAM
Storage: 300MB for the Integrated Development Environment (IDE) and 1GB for cache

#### Recommended Hardware Requirements 
For an optimal experience with hands-on labs and other practical activities, we recommend the following configuration:

OS: Windows entreprise or professional 10 build > 1903,  or Mac
Processor: Core i5 or better (or AMD equivalent)
Memory: 8GB RAM or better
Storage:  2GB free for build caches and dependencies

#### Software Requirements

Operating system: Windows 10, Linux or mac


## Follow the instructions below to download the data belonging to the course as well as

### setting up your interactive development environment.

There is a bundled script that will help you in all theses steps, but to be able to launch the script we need first to install python, and java (needed for Spark), you will not use Java but it is needed for running spark

#### We will use powershell, verify that it is installed on your windows 10

#### Step1 : Install Java

First verify if java installed, if not install it

#### Step 2 : Install python 

First verify that python is installed, if not install it

#### Step 3: install git

### Downloading Data for this Course

Once you have cloned this repository locally, simply navigate to the folder you have
 stored the repo in and run: 
 
 #### in the folder <repoFolder>/BDA
```python download_and_install_pyspark.py```

This will install an environnement to be used on a shell or powershell terminal and jupyter lab (will use to simplify things only jupyter lab)

#### in the folder <repoFolder>/BDA
```python download_data.py```

This will populate the `data-sets` folder in your repo with a number of data sets that
 will be used throughout the course.



### Instructions for use

There are 2 ways to access jupyter lab if theses two sessions:
1. Through the bundled `run_me.py` script (recommended to use)
2. Through the CLI (only for advanced users)

#### Using the bundled script to run jupyter lab

The easiest way to run the container that belongs to this two sessions is by running
 ```python run_me.py``` from the git repository. This will automatically
 install all necessary softwares and python modules for you, set up envirement variables, download the data, and launch jupyter lab

#### Using CLI

[ ] TODO


#### To Stop the session

[ ] TODO

