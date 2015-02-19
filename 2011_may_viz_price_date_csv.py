import json, csv

pxd_viz = {

}

pxd_viz = open('2011_may_results_with_dates.json')
data = json.load(pxd_viz)
pxd_viz.close()

pxd_viz=csv.writer(open('2011_may_pxd_viz_again.csv' , 'w'))

for item in data:

	if "price" in data[item]:
		price = (data[item]["price"])
	if "date" in data[item] and "price" in data[item]:
		pxd_viz.writerow([data[item]['date'], data[item]['price'], data[item]['artist']])