import csv
import collections

trying = {}

with open('2011_may_viz_again.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:
		date = row[0]
		price = row[1].strip()
		#how am i doing this wrong?

		if price == "Unsold":
			price = 0
		price = int(price)

		#is this date in the dictonary yet?
		if date not in trying:
			#no, so set it to zero with the date as the key
			trying[date] = 0


		#now add the price to this date
		trying[date] = trying[date] + price


convert_to_zero=csv.writer(open('2011_may_converted.csv' , 'w'))


#so now sort the diconary by the key (the date) and each item var will be a date. So write out the date and the value for that year
for item in sorted(trying):
	convert_to_zero.writerow([item, trying[item]] )