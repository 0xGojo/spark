import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("thach") \
    .getOrCreate()

df = spark.read.csv(sys.argv[1], header=True, encoding="UTF-8")

result = df.groupBy("Nom_parc").count().filter(df['Nom_parc']!= '').orderBy("Nom_parc", ascending=True).collect()
for elem in result:
	print(elem['Nom_parc'].encode('UTF-8') + ":" + str(elem['count']))


spark.stop()