import json
import re
p = re.compile('[0-9]{4}')

artist_count = {
	
}

with open("june_2014_results.json") as json_file:
	json_data = json.load(json_file)
	#print(json_data)

	for a_work in json_data:
		#print(a_work)
		# if (json_data[a_work]["title"]):

		if "artist" in json_data[a_work]:

			if json_data[a_work]['artist'] in artist_count:

				artist_count[json_data[a_work]['artist']] = artist_count[json_data[a_work]['artist']] + 1 
			else:

				artist_count[json_data[a_work]['artist']] = 0
			json_data[a_work]["artist_count"]=artist_count[json_data[a_work]['artist']]

		if "title" in json_data[a_work]:
			#print(json_data[a_work]['title'])

			title = json_data[a_work]['title']
			#print(title)
			m = p.findall(title)
			if len(m) > 0:
				#print(m[0])

				json_data[a_work]["date"]=m[0]

with open('june_2014_results_with_dates.json' , 'w') as f:
 	f.write(json.dumps(json_data, indent=4))