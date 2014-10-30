# these are all the auctions that contain photographs for sale from dreweatts:
	# http://www.dreweatts.com/cms/pages/auction/36045
	# http://www.dreweatts.com/cms/pages/auction/20630
	# http://www.dreweatts.com/cms/pages/auction/36117
	# http://www.dreweatts.com/cms/pages/auction/36093
	# http://www.dreweatts.com/cms/pages/auction/36043
	# http://www.dreweatts.com/cms/pages/auction/35995
	# http://www.dreweatts.com/cms/pages/auction/35931
	# http://www.dreweatts.com/cms/pages/auction/35919
	# http://www.dreweatts.com/cms/pages/auction/45162
	# http://www.dreweatts.com/cms/pages/auction/35854
	# http://www.dreweatts.com/cms/pages/auction/35852
	# http://www.dreweatts.com/cms/pages/auction/13422
	# http://www.dreweatts.com/cms/pages/auction/35764
	# http://www.dreweatts.com/cms/pages/auction/45050
	# http://www.dreweatts.com/cms/pages/auction/40052
	# http://www.dreweatts.com/cms/pages/auction/45038
	# http://www.dreweatts.com/cms/pages/auction/45033
	# http://www.dreweatts.com/cms/pages/auction/35719
	# http://www.dreweatts.com/cms/pages/auction/40048
	# http://www.dreweatts.com/cms/pages/auction/12710

#this is the "writing out data to json" code from the dropbox
	# import json

	# #getting an empty list ready to store my artworks into it
	# artworks = []

	# #pseudo scrapping code loop goes here 
	# while scrapping == True:
		
	# 	#more pseudo code working with request and beautiful here

	# 	a_work = { "title" : "The title i got from beautiful soup", "artist" : "The artist name i got from beautiful soup" }

	# 	#okay now add it into our list
	# 	artworks.append(a_work)

	# #okay all done, going to write it out to a formated JSON file
	# with open('scraped_artworks.json', 'w') as f:

	# 	f.write(json.dumps(artworks,indent=4))

#this is the "beautiful soup demo" code from the dropbox
	#now we can "query" the soup variable for the paterns we are looking for
		# all_links = soup.find_all("a", attrs = {"class": "titleLink"})

		# for a_link in all_links:

		# 	#print out the url of each link and the text
		# 	print(a_link.text)
		# 	print(a_link['href'])

		# #find all the spans with class titleCell
		# all_title_cells = soup.find_all("span", attrs = {"class": "titleCell"})

		# for a_title_cell in all_title_cells:

		# 	artist = a_title_cell.find("span", attrs = {"class": "imageArtist"})

		# 	#now we have the arist span, we just want the text of the link so do another find
		# 	print (artist.find("a").text)

		# 	#lets get the title of the work
		# 	title = a_title_cell.find("a", attrs = {"class": "titleLink"})

		# 	#if it is not found None is returned so lets make sure we found something
		# 	if title != None: 
		# 		print (title.text)

		# #lets find the "Next" link
		# next_link = soup.find("a",text="Next")

		# print ("The next page is:")
		# print (next_link)