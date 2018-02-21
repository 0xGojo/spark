from pyspark import SparkContext
import sys

print("thach dep trai")
sc = SparkContext()
def proccess(i) :
	data = sc.textFile(sys.argv[i])
	header = data.first()
	lines = data.filter(lambda row : row != header)
	parks = lines.map(lambda l: l.split(",")).filter(lambda p: p[len(p) - 7] != '' and p[len(p) - 7] != '<Null>')
	return parks.map(appendParkName).distinct()

def appendParkName (element):
	if element[len(element) - 7].find('"') > -1 :
		return (element[len(element) - 8] + element[len(element) - 7]).replace('"', '')
	else :
		return element[len(element) - 7].replace('"', '')


park15 = proccess(1)
park16 = proccess(2)

parks = park15.intersection(park16)
results = parks.sortBy(lambda a: a[0])
sortedResults = results.collect()
for elem in sortedResults:
	print(elem.encode('utf-8').strip().replace('"', ''))
