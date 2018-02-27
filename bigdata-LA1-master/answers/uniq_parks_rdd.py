from pyspark import SparkContext
import sys

sc = SparkContext()
data = sc.textFile(sys.argv[1])
header = data.first()
lines = data.filter(lambda row : row != header) 
parks = lines.map(lambda l: l.split(",")).filter(lambda p: p[len(p) - 7] != '')

def appendParkName (element):
	if element[len(element) - 7].find('"') > -1 :
		return (element[len(element) - 8] + ", " + element[len(element) - 7]).replace('"', '')
	else :
		return element[len(element) - 7].replace('"', '')

treeInParks = parks.map(appendParkName)
uniquePark = treeInParks.distinct().sortBy(lambda a: a[0])
sortedResults = uniquePark.collect()
for elem in sortedResults:
	print(elem)
