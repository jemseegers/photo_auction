import csv
import collections

counts = collections.Counter()

#lets define a dictonary to hold our results
tally_d = {}

with open('june_2014_dp_analysis.csv', 'r') as td:
	csv_read = csv.reader(td)
	sort_td = sorted(csv_read)
	#print("the number of records", len(sort_td))
	for row in sort_td:
		decade = row[0]

		if decade not in tally_d:
			tally_d[decade] = 1
		else:
			#otherwise it already exists so just bump up the counter
			tally_d[decade] = tally_d[decade] + 1

get_it=csv.writer(open('june_2014_decade_tally.csv', 'w'))

for decade in sorted(tally_d):
		get_it.writerow([decade, tally_d[decade]])

