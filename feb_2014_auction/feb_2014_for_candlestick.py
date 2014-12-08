import csv
from statistics import median

all_decades = {}

with open('feb_2014_dp_analysis.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:

		decade = row[0]

		price = row[1].strip()
		if price == "Unsold":
			price = 0
		price = int(price)

		if decade not in all_decades:
			all_decades[decade] = { "total": 0, "total price": 0, "low": 100000000, "median": 0, "average": 0, "high":0, "values":[]}
			
		if price > all_decades[decade]["high"]:
			all_decades[decade]["high"] = price

		if price < all_decades[decade]["low"] and price != 0:
			all_decades[decade]["low"] = price

		all_decades[decade]["total"] = all_decades[decade]["total"]+1
		all_decades[decade]["total price"] = all_decades[decade]["total price"] + price

		if price != 0:
			all_decades[decade]["values"].append(price)


for_candlestick=csv.writer(open('feb_2014_candlestick.csv' , 'w'))

for decade in sorted(all_decades):
	average = all_decades[decade]["total price"]/all_decades[decade]["total"]
	for_candlestick.writerow([decade, all_decades[decade]["total price"], all_decades[decade]["total"], all_decades[decade]["high"], all_decades[decade]["low"], average, median(all_decades[decade]["values"])])
