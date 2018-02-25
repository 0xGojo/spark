from pyspark import SparkContext
import sys

sc = SparkContext()
data = sc.textFile(sys.argv[1])
header = data.first()
lines = data.filter(lambda row : row != header) 
parts = lines.map(lambda l: l.split(",")).filter(lambda p: p[len(p) - 7] != '')

def appendParkName (element):
	if element[len(element) - 7].find('"') > -1 :
		return ((element[len(element) - 8] + element[len(element) - 7]).replace('"', ''), 1)
	else :
		return (element[len(element) - 7].replace('"', ''), 1)

treeInParks = parts.map(appendParkName)
countTreeEachPark = treeInParks.reduceByKey(lambda a, b : a + b)
topTenParks = countTreeEachPark.takeOrdered(10, lambda (a, b) : -1 * b)

for elem in topTenParks:
	print(elem[0] + ": " + str(elem[1]))

