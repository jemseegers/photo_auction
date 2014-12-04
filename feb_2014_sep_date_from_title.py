import json
import re
p = re.compile('[0-9]{4}')
d = re.compile('[0-9]{3}')

artist_count = {
	
}

with open("feb_2014_results.json") as json_file:
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

		if "date" in json_data[a_work]:
			date = json_data[a_work]['date']

			dec = d.findall(date)
			if len(dec) > 0:

					if dec[0]=="185" : 
						json_data[a_work]["decade"]= '1850s'
					if dec[0]=="186" :
						json_data[a_work]["decade"]= '1860s'
					if dec[0]=="187" :
						json_data[a_work]["decade"]= '1870s'
					if dec[0]=="188" :
						json_data[a_work]["decade"]= '1880s'
					if dec[0]=="189" :
						json_data[a_work]["decade"]= '1890s'
					if dec[0]=="190" :
						json_data[a_work]["decade"]= '1900s aughts'
					if dec[0]=="191" :
						json_data[a_work]["decade"]= '1910s'
					if dec[0]=="192" :
						json_data[a_work]["decade"]= '1920s'
					if dec[0]=="193" :
						json_data[a_work]["decade"]= '1930s'
					if dec[0]=="194" :
						json_data[a_work]["decade"]= '1940s'
					if dec[0]=="195" :
						json_data[a_work]["decade"]= '1950s'
					if dec[0]=="196" :
						json_data[a_work]["decade"]= '1960s'
					if dec[0]=="197" :
						json_data[a_work]["decade"]= '1970s'
					if dec[0]=="198" :
						json_data[a_work]["decade"]= '1980s'
					if dec[0]=="199" :
						json_data[a_work]["decade"]= '1990s'
					if dec[0]=="200" :
						json_data[a_work]["decade"]= '2000s aughts'
					if dec[0]=="201" :
						json_data[a_work]["decade"]= '2010s'	

with open('feb_2014_results_with_dates.json' , 'w') as f:
 	f.write(json.dumps(json_data, indent=4))