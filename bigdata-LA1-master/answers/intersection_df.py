import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("thach") \
    .getOrCreate()

df1 = spark.read.csv(sys.argv[1], header=True)
df2 = spark.read.csv(sys.argv[2], header=True)
 
parks1 = df1.select("Nom_parc").filter(df1['Nom_parc'] != '')
parks2 = df2.select("Nom_parc").filter(df2['Nom_parc'] != '')
result = parks1.join(parks2, "Nom_parc").distinct().orderBy('Nom_parc', ascending=True).collect()
for elem in result:
	print(elem['Nom_parc'])


spark.stop()