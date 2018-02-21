import csv
import sys
from collections import Counter
with open(sys.argv[1], mode='r') as infile:
    reader = csv.reader(infile)
    Trees = list(reader)
parks = []
total = 0

for elem in Trees:
	if elem[6] != '' and elem[6] != 'Nom_parc':
		parks.append(elem[6].decode('utf-8'))
		
for elem in sorted(Counter(parks).items()) :
	print(elem[0] + ":" + str(elem[1]))
	
