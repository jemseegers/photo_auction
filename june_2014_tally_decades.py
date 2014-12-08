import csv
import collections

counts = collections.Counter()

# #lets define a dictonary to hold our results
# tally_d = {}

with open('june_2014_dp_analysis.csv', 'r') as td:
	csv_read = csv.reader(td)
	sort_td = sorted(csv_read)
	#print("the number of records", len(sort_td))
	for row in sort_td:
		if row[0].isdigit():
			if row[0] in sort_td:
				sort_td[row[0]] = + 1
			else:
				sort_td[row[0]] = 1
		
			print(row)

