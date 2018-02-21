import csv
import sys

with open(sys.argv[1], mode='r') as infile:
    reader = csv.reader(infile)
    Trees = list(reader)
print(len(Trees) - 1)