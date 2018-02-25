from pyspark import SparkContext
import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("thach") \
    .getOrCreate()
df = spark.read.csv(sys.argv[1], header=True)
result = df.groupBy("Nom_parc").count().filter(df['Nom_parc']!= '').orderBy("count", ascending=False).take(10)
for elem in result:
	print(elem['Nom_parc'] + ": " + str(elem['count']))

spark.stop()