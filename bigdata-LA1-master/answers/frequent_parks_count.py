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
		parks.append(elem[6])
		
result = Counter(parks).most_common(10)
for elem in result:
	print(elem[0] + ":" + str(elem[1]))
	
