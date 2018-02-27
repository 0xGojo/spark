import csv
import sys

def getData(i):
	with open(sys.argv[i], mode='r') as infile:
		reader = csv.reader(infile)
		Trees = list(reader)
		parks = set()	
		for elem in Trees:
			if elem[6] != '' and elem[6] != 'Nom_parc':
				parks.add(elem[6])
		return parks
data1 = getData(1)
data2 = getData(2)
result = sorted(data1.intersection(data2))
for elem in result:
	print(elem) 
