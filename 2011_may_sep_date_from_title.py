import json
import re
p = re.compile('[0-9]{4}')
d = re.compile('[0-9]{3}')

artist_count = {
	
}

with open("2011_may_results.json") as json_file:
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

					if "185" 
						print('1850s')
					if 186
						print('1860s')
					if 187
						print('1870s')
					if 188
						print('1880s')
					if 189
						print('1890s')
					if 190
						print('1900s aughts')
					if 191
						print('1910s')
					if 192
						print('1920s')
					if 193
						print('1930s')
					if 194
						print('1940s')
					if 195
						print('1950s')
					if 196
						print('1960s')
					if 197
						print('1970s')
					if 198
						print('1980s')
					if 199
						print('1990s')
					if 200
						print('2000s aughts')
					if 201
						print('2010s')


				json_data[a_work]['decade']=dec[0]
					

with open('2011_may_results_with_dates.json' , 'w') as f:
 	f.write(json.dumps(json_data, indent=4))