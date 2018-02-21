import csv
import sys
from collections import Counter

def getData(i):
	with open(sys.argv[i], mode='r') as infile:
	    reader = csv.reader(infile)
	    Trees = list(reader)
	    parks = set()
	    for elem in Trees:
			if elem[6] != '' and elem[6] != 'Nom_parc':
				parks.add(elem[6].decode('utf-8'))
	return parks

data1 = getData(1)
data2 = getData(2)

for elem in data1.intersection(data2):
	print(elem) 
