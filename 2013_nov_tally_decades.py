import csv
import collections

counts = collections.Counter()

tally_d = {}

with open('2013_nov_dp_analysis.csv', 'r') as td:
	csv_read = csv.reader(td)
	sort_td = sorted(csv_read)
	for row in sort_td:
		decade = row[0]

		if decade not in tally_d:
			tally_d[decade] = 1
		else:
			tally_d[decade] = tally_d[decade] + 1

get_it=csv.writer(open('2013_nov_decade_tally.csv', 'w'))

for decade in sorted(tally_d):
		get_it.writerow([decade, tally_d[decade]])

