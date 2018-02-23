import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("thach") \
    .getOrCreate()

df = spark.read.csv(sys.argv[1], header=True)
result = df.select('Nom_parc').distinct().filter(df['Nom_parc']!= '').orderBy("Nom_parc").collect()

for elem in result:
	print(elem['Nom_parc'].encode('utf-8'))


spark.stop()