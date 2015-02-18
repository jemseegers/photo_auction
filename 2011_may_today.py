import json, csv

dp_analysis = open('2011_may_results_with_dates.json')
data = json.load(dp_analysis)
dp_analysis.close()

dp_analysis=csv.writer(open('2011_may_try.csv' , 'w'))

for item in data:
	if "date" in data[item] and "price" in data[item]:
		#print(data[item]["date"])
		#print(data[item]["price"])
		#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		

		if price == "Unsold":
			price = 0
		price = int(price)



		dp_analysis.writerow([data[item]['date'], data[item]['price']])
	# print(data[item])
	# print(data[item]["date"])
	
