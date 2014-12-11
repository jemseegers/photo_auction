import json, csv

dp_analysis = open('2011_may_results_with_dates.json')
data = json.load(dp_analysis)
dp_analysis.close()

dp_analysis=csv.writer(open('2011_may_dp_analysis.csv' , 'w'))

for item in data:
	if "decade" in data[item] and "price" in data[item]:
		#print(data[item]["decade"])
		#print(data[item]["price"])
		#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		dp_analysis.writerow([data[item]['decade'], data[item]['price']])
	# print(data[item])
	# print(data[item]["decade"])
	