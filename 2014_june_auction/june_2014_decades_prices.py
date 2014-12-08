import json, csv

dp_analysis = open('june_2014_results_with_dates.json')
data = json.load(dp_analysis)
dp_analysis.close()

dp_analysis=csv.writer(open('june_2014_dp_analysis.csv' , 'w'))

for item in data:
	if "decade" in data[item] and "price" in data[item]:
		dp_analysis.writerow([data[item]['decade'], data[item]['price']])

for item in data:
	if "decade" in data[item] and "price" in data[item]:
		item.count("Unsold")
		print(item.count)
	