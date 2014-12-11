import csv
from statistics import median

all_decades = {}

with open('2013_nov_dp_analysis.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:

		decade = row[0]

		price = row[1].strip()
		if price == "Unsold":
			price = 0
		price = int(price)

		if decade not in all_decades:
			all_decades[decade] = { "total": 0, "total price": 0, "total sold": 0, "low": 100000000, "median": 0, "average": 0, "high":0, "values":[]}
			
		if price > all_decades[decade]["high"]:
			all_decades[decade]["high"] = price

		if price < all_decades[decade]["low"] and price != 0:
			all_decades[decade]["low"] = price

		all_decades[decade]["total"] = all_decades[decade]["total"]+1
		all_decades[decade]["total price"] = all_decades[decade]["total price"] + price

		if price != 0:
			all_decades[decade]["values"].append(price)


		#trying to get this to be the number of works actually sold, so 
		#how to get it to count the number of occurrences price was above 0?
		if price > 0:
			all_decades[decade]["total sold"] = all_decades[decade]["total sold"]+1


for_candlestick=csv.writer(open('2013_nov_candlestick.csv' , 'w'))

for decade in sorted(all_decades):
	average = all_decades[decade]["total price"]/all_decades[decade]["total sold"]
	for_candlestick.writerow([decade, all_decades[decade]["total price"], all_decades[decade]["total"], all_decades[decade]["total sold"], all_decades[decade]["high"], all_decades[decade]["low"], average, median(all_decades[decade]["values"])])
