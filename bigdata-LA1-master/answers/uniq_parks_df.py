import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("thach") \
    .getOrCreate()

df = spark.read.csv(sys.argv[1], header=True, encoding="UTF-8")
result = df.select("Nom_parc").filter(df['Nom_parc']!= '').orderBy("Nom_parc").collect()

for elem in result:
	print(elem['Nom_parc'].encode('UTF-8') )


spark.stop()