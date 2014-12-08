import csv
from statistics import median

#lets define a dictonary to hold our results
all_decades = {}

with open('june_2014_dp_analysis.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:

		decade = row[0]

		#i noticed there are line breaks in the prices, so lets strip them out using the .strip() method
		price = row[1].strip()
		if price == "Unsold":
			price = 0
		price = int(price)

		#make sure this decade has a key in the dictonary
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



#lets sort it and save it out we are using the sorted function that returns the dictonary sorted ascending by the key name

for_candlestick=csv.writer(open('june_2014_candlestick.csv' , 'w'))

for decade in sorted(all_decades):
	average = all_decades[decade]["total price"]/all_decades[decade]["total"]
	for_candlestick.writerow([decade, all_decades[decade]["total price"], all_decades[decade]["total"], all_decades[decade]["high"], all_decades[decade]["low"], average, median(all_decades[decade]["values"])])
