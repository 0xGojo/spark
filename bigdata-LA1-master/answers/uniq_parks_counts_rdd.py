from pyspark import SparkContext, SparkConf
import sys

sc = SparkContext()
data = sc.textFile(sys.argv[1])
header = data.first()
lines = data.filter(lambda row : row != header) 
parts = lines.map(lambda l: l.split(",")).filter(lambda p: p[len(p) - 7] != '' )

def appendParkName (element):
	if element[len(element) - 7].find('"') > -1 :
		return ((element[len(element) - 8] + element[len(element) - 7]).replace('"', ''), 1)
	else :
		return (element[len(element) - 7].replace('"', ''), 1)


treeInParks = parts.map(appendParkName)
countTreeEachPark = treeInParks.reduceByKey(lambda a, b : a + b).sortBy(lambda a: a[0])
for elem in countTreeEachPark.collect():
	print(elem[0].encode('utf-8') + ": " + str(elem[1]))

