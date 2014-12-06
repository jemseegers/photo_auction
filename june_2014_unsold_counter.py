import csv
from collections import Counter

unsoldxdecade = Counter()
with open('june_2014_dp_analysis.csv', 'r') as dpa:
	reader = csv.reader(dpa)
	for row in reader:
		#print(row)
		print(unsoldxdecade["Unsold"])