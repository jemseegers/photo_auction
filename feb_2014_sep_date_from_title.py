import json
import re
p = re.compile('[0-9]{4}')

with open("feb_2014_results.json") as json_file:
	json_data = json.load(json_file)
	#print(json_data)

	for a_work in json_data:
		#print(a_work)
		# if (json_data[a_work]["title"]):
		if "title" in json_data[a_work]:
			#print(json_data[a_work]['title'])

			title = json_data[a_work]['title']
			print(title)
			m = p.findall(title)
			if len(m) > 0:
				print(m[0])