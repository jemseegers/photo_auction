from bs4 import BeautifulSoup
import requests
import re
p = re.compile('[0-9]+\s')

all_lots = {
		
}

with open("2012_may_auction.txt") as lots_urls:
	for each_lot in lots_urls:
		lot_requests = requests.get(each_lot)
		lot_html = lot_requests.text
		soup = BeautifulSoup(lot_html)
		#print(lot_html)
		all_lots[each_lot] = {}

		all_links = soup.find_all("div" , attrs = {"class" : "wide-right-column" })
		for div_link in all_links:
			#print(div_link.text)

			artist = div_link.find("h4")
			artist = artist.text
			#print(artist)
			all_lots[each_lot]["artist"] = artist

			title = div_link.find("h5")
			title = title.text
			#print(title)
			all_lots[each_lot]["title"] = title

		p_in_div = soup.find_all("div" , attrs = {"class" : "right-column" })
		for p_link in p_in_div:
			#print(p_link.text)

			price = p_link.find("p", attrs ={"class" : "price sold"})
			price = price.text

			m = p.search(price)

			if m == None:
				#print("No interest")
				all_lots[each_lot]["price"] = "Unsold"
			else :
				#print(m.group(0))
				#print(price)
				all_lots[each_lot]["price"] = m.group(0)

import json

with open('2012_may_results.json' , 'w') as f:
 	f.write(json.dumps(all_lots, indent=4))
