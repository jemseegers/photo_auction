import csv
import collections

trying = {}

with open('2011_may_pxd_viz.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:
		date = row[0]
		price = row[1].strip()
		#how am i doing this wrong?

		if price == "Unsold":
			price = 0
		price = int(price)

		if date not in trying:
			trying[date] = date

		if int(price) not in trying:
			trying[price] = int(price)

convert_to_zero=csv.writer(open('2011_may_converted.csv' , 'w'))

for item in sorted(trying):
	convert_to_zero.writerow([date, price])