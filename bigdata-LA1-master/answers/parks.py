import csv
import sys


with open(sys.argv[1], mode='r') as infile:
    reader = csv.reader(infile)
    Trees = list(reader)

total = 0
for elem in Trees	:
	if elem[6] != '' and elem[6] != 'Nom_parc':
		total = total + 1

print(total) 