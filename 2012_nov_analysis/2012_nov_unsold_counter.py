import csv

all_decades = {}

with open('2012_nov_dp_analysis.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:

		decade = row[0]

		price = row[1].strip()

		if decade not in all_decades:
			all_decades[decade] = {}
			
		if price not in all_decades[decade]:
			all_decades[decade][price] = 1
		
		else:
			all_decades[decade][price] = all_decades[decade][price] + 1

dp_analysis_by_price=csv.writer(open('2012_nov_dp_analysis_by_price.csv' , 'w'))


for key in sorted(all_decades):


	for price_key in sorted(all_decades[key]):

		dp_analysis_by_price.writerow([ key, price_key,  all_decades[key][price_key] ])