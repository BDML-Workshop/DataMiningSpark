import findspark
import matplotlib.pyplot as plt

#findspark.init('/home/pascalfares/DataMiningSpark/sparkhome/spark-3.0.1-bin-hadoop2.7')
findspark.init('/opt/spark/spark-3.0.1-bin-hadoop2.7')
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("QuickStart").getOrCreate()
sc = spark.sparkContext

def countByCentre(raw_data, dosample=False):
    splited_row = raw_data.map(lambda line: line.split(","))
    keyCentre = splited_row.map(lambda rl: (rl[1], 1)).filter(lambda c: c[0] != 'IdCentre')
    count = keyCentre.reduce(lambda c1,c2: (c1[0],c1[1]+c2[1]))
    print(count)
    reducekeys = keyCentre.reduceByKey(lambda a,b:a +b)
    count = reducekeys.reduce(lambda c1,c2: ('count',c1[1]+c2[1]))
    print(count)
    return reducekeys


print(sc)
print(spark)

raw_data = sc.textFile("Admission_n_2020.csv")
lid_centre_count = countByCentre(raw_data).collect()
print(countByCentre(raw_data).collect())

X= [c[0] for c in lid_centre_count]
Y= [c[1] for c in lid_centre_count]
print(X)
print(Y)
plt.plot(X,Y, 'o-')
patches, texts =  plt.pie(Y)
plt.legend(patches, X)
plt.show()

spark.stop()


