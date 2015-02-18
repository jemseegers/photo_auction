import json

with open("2011_may_results_with_dates.json") as json_file:
	json_data = json.load(json_file)

	for a_work in json_data:

		if "price" in json_data[a_work]:
			price = json_data[a_work]['price']
			
			if price == "Unsold":
				price = 0
		

with open('2011_may_unsold_zero.json' , 'w') as f:
 	f.write(json.dumps(json_data, indent=4))