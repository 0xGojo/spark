
import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("thach") \
    .getOrCreate()

df = spark.read.csv(sys.argv[1], header=True)
result = df.filter(df['Nom_parc']!= '').count()

print(result)

spark.stop()