import csv
import sys

with open(sys.argv[1], mode='r') as infile:
    reader = csv.reader(infile)
    Trees = list(reader)
output = set()
total = 0

for elem in Trees:
	if elem[6] != '' and elem[6] != 'Nom_parc':
		output.add(elem[6])
		
for elem in sorted(output):
	print(elem)

