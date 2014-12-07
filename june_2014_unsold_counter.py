import csv

#lets define a dictonary to hold our results
all_decades = {}

with open('june_2014_dp_analysis.csv', 'r') as dpa:
	reader = csv.reader(dpa)

	for row in reader:

		decade = row[0]

		#i noticed there are line breaks in the prices, so lets strip them out using the .strip() method
		price = row[1].strip()

		#make sure this decade has a key in the dictonary
		if decade not in all_decades:
			all_decades[decade] = {}
			print(all_decades[decade])
			#so now it is a dictonary with each decade as its own dictonary


		#lets see if for this decade we have this price as a key already
		if price not in all_decades[decade]:
			#set it to one because it has one hit sofar (the first one)
			all_decades[decade][price] = 1
		else:
			#otherwise it already exists so just bump up the counter
			all_decades[decade][price] = all_decades[decade][price] + 1


#lets sort it and save it out we are using the sorted function that returns the dictonary sorted ascending by the key name

dp_analysis_by_price=csv.writer(open('june_2014_dp_analysis_by_price.csv' , 'w'))


for key in sorted(all_decades):

	#so now all the years are sorted now lets sort the prices for each one

	for price_key in sorted(all_decades[key]):

		#and write out the CSV file row for thisone
		dp_analysis_by_price.writerow([ key, price_key,  all_decades[key][price_key] ])
