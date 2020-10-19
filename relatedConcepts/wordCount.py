import sys
 
from pyspark import SparkContext, SparkConf

print(f"read from {sys.argv[1]} count saved to {sys.argv[2]}")
if __name__ == "__main__":
    print(f"read from {sys.argv[1]} count saved to {sys.argv[2]}")
    #create Spark context with necessary configuration
    sc = SparkContext("local[*]","PySpark Word Count Example")
    # read data from text file and split each line into words
    words = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" ")). \
    flatMap(lambda line: line.split("(")). \
    flatMap(lambda line: line.split(")")). \
    flatMap(lambda line: line.split(","))
    # count the occurrence of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
    # save the counts to output
    wordCounts.saveAsTextFile(sys.argv[2])
    wordCounts.foreach(print)
print("Bye")