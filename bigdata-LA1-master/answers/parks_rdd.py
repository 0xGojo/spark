from pyspark import SparkContext, SparkConf
import sys

sc = SparkContext()
data = sc.textFile(sys.argv[1])
header = data.first()
lines = data.filter(lambda row : row != header) 
numberTrees = lines.map(lambda l: l.split(",")).filter(lambda p: p[len(p) - 7] != '' ).count()

print(numberTrees)

