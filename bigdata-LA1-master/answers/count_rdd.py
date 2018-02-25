from pyspark import SparkContext
import sys

sc = SparkContext()
data = sc.textFile(sys.argv[1])
header = data.first()
lines = data.filter(lambda row : row != header) 
totalTree = lines.count()
print(totalTree)
