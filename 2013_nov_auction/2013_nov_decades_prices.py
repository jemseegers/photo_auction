import json, csv

dp_analysis = open('2013_nov_results_with_dates.json')
data = json.load(dp_analysis)
dp_analysis.close()

dp_analysis=csv.writer(open('2013_nov_dp_analysis.csv' , 'w'))

for item in data:
	if "decade" in data[item] and "price" in data[item]:
		dp_analysis.writerow([data[item]['decade'], data[item]['price']])
	