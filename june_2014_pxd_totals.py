import csv
import collections

counts = collections.Counter()

#lets define a dictonary to hold our results
tally_d = {}

with open('june_2014_dp_analysis.csv', 'r') as td:
	csv_read = csv.reader(td)
	sort_td = sorted(csv_read)
	
	for row in sort_td:
		decade = row[0]
		price = row[1]

		if price == "Unsold":
			price = 0
		price = int(price)

		if decade not in tally_d:
			tally_d[decade] = price
		else:
			
			tally_d[decade] = tally_d[decade] + price

get_it=csv.writer(open('june_2014_pxd_totals.csv', 'w'))

for decade in sorted(tally_d):
		get_it.writerow([decade, tally_d[decade]])

