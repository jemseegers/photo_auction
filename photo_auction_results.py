# what is this project?
# i want to webscrape the data off the auction results, write them into a file
# then i will separate out the unsold works, collect the artist names and count the number of times an artist appears
# for the works that did sell, i want to separate  them out by the price for which they sold
# down the line I would like to do this for different years to see the trends
# now i'm thinking to do comparative with swann? uk v. us - on second thought, baby steps
# these are all the auctions that contain photographs for sale from dreweatts:

# Photographs & Photobooks - 06 June 2014 - only photo lots
	# http://www.dreweatts.com/cms/pages/auction/36045

from bs4 import BeautifulSoup
import requests

all_lots = {
		
}

with open("lots.txt") as lots_urls:
	for each_lot in lots_urls:
		lot_requests = requests.get(each_lot)
		lot_html = lot_requests.text
		soup = BeautifulSoup(lot_html)
		#print(lot_html)



		all_links = soup.find_all("div" , attrs = {"class" : "wide-right-column" })
		for div_link in all_links:
			#print(div_link.text)

			artist = div_link.find("h4")
			artist = artist.text
			#print(artist)

			title = div_link.find("h5")
			title = title.text
			print(title)

#i don't know how to make all the artists appear in the json file
#it's only getting the second artist
# import json

# with open('artist_names.json' , 'w') as f:
# 	f.write(json.dumps(artist))

	

# Affordable Prints, Paintings and Photographs - 01 May 2014 - only photo lots		
	# http://www.dreweatts.com/cms/pages/auction/20630
		# http://www.dreweatts.com/cms/pages/lot/20630/118
		# http://www.dreweatts.com/cms/pages/lot/20630/119
		# http://www.dreweatts.com/cms/pages/lot/20630/120
		# http://www.dreweatts.com/cms/pages/lot/20630/121
		# http://www.dreweatts.com/cms/pages/lot/20630/122
		# http://www.dreweatts.com/cms/pages/lot/20630/123
		# http://www.dreweatts.com/cms/pages/lot/20630/124
		# http://www.dreweatts.com/cms/pages/lot/20630/125
		# http://www.dreweatts.com/cms/pages/lot/20630/126
		# http://www.dreweatts.com/cms/pages/lot/20630/127
		# http://www.dreweatts.com/cms/pages/lot/20630/128
		# http://www.dreweatts.com/cms/pages/lot/20630/129
		# http://www.dreweatts.com/cms/pages/lot/20630/130
		# http://www.dreweatts.com/cms/pages/lot/20630/131
		# http://www.dreweatts.com/cms/pages/lot/20630/132
		# http://www.dreweatts.com/cms/pages/lot/20630/133
		# http://www.dreweatts.com/cms/pages/lot/20630/134
		# http://www.dreweatts.com/cms/pages/lot/20630/135
		# http://www.dreweatts.com/cms/pages/lot/20630/136
		# http://www.dreweatts.com/cms/pages/lot/20630/137
		# http://www.dreweatts.com/cms/pages/lot/20630/138
		# http://www.dreweatts.com/cms/pages/lot/20630/139
		# http://www.dreweatts.com/cms/pages/lot/20630/140
		# http://www.dreweatts.com/cms/pages/lot/20630/141
		# http://www.dreweatts.com/cms/pages/lot/20630/142
		# http://www.dreweatts.com/cms/pages/lot/20630/143
		# http://www.dreweatts.com/cms/pages/lot/20630/144
		# http://www.dreweatts.com/cms/pages/lot/20630/145
		# http://www.dreweatts.com/cms/pages/lot/20630/146
		# http://www.dreweatts.com/cms/pages/lot/20630/147
		# http://www.dreweatts.com/cms/pages/lot/20630/148
		# http://www.dreweatts.com/cms/pages/lot/20630/149
		# http://www.dreweatts.com/cms/pages/lot/20630/150
		# http://www.dreweatts.com/cms/pages/lot/20630/151
		# http://www.dreweatts.com/cms/pages/lot/20630/152
		# http://www.dreweatts.com/cms/pages/lot/20630/153
		# http://www.dreweatts.com/cms/pages/lot/20630/154
		# http://www.dreweatts.com/cms/pages/lot/20630/155
		# http://www.dreweatts.com/cms/pages/lot/20630/156
		# http://www.dreweatts.com/cms/pages/lot/20630/157
		# http://www.dreweatts.com/cms/pages/lot/20630/158
		# http://www.dreweatts.com/cms/pages/lot/20630/159
		# http://www.dreweatts.com/cms/pages/lot/20630/160
		# http://www.dreweatts.com/cms/pages/lot/20630/161
		# http://www.dreweatts.com/cms/pages/lot/20630/162
		# http://www.dreweatts.com/cms/pages/lot/20630/163
		# http://www.dreweatts.com/cms/pages/lot/20630/164
		# http://www.dreweatts.com/cms/pages/lot/20630/165
		# http://www.dreweatts.com/cms/pages/lot/20630/166
		# http://www.dreweatts.com/cms/pages/lot/20630/167
		# http://www.dreweatts.com/cms/pages/lot/20630/168
		# http://www.dreweatts.com/cms/pages/lot/20630/169
		# http://www.dreweatts.com/cms/pages/lot/20630/170
		# http://www.dreweatts.com/cms/pages/lot/20630/171
		# http://www.dreweatts.com/cms/pages/lot/20630/172
		# http://www.dreweatts.com/cms/pages/lot/20630/173
		# http://www.dreweatts.com/cms/pages/lot/20630/174
		# http://www.dreweatts.com/cms/pages/lot/20630/175
		# http://www.dreweatts.com/cms/pages/lot/20630/176
		# http://www.dreweatts.com/cms/pages/lot/20630/177
		# http://www.dreweatts.com/cms/pages/lot/20630/178
		# http://www.dreweatts.com/cms/pages/lot/20630/179
		# http://www.dreweatts.com/cms/pages/lot/20630/180
		# http://www.dreweatts.com/cms/pages/lot/20630/181


# Photo Opportunities - 28 February 2014 - only photo lots
	# http://www.dreweatts.com/cms/pages/auction/36117
		# http://www.dreweatts.com/cms/pages/lot/36117/1
		# http://www.dreweatts.com/cms/pages/lot/36117/10
		# http://www.dreweatts.com/cms/pages/lot/36117/100
		# http://www.dreweatts.com/cms/pages/lot/36117/101
		# http://www.dreweatts.com/cms/pages/lot/36117/102
		# http://www.dreweatts.com/cms/pages/lot/36117/103
		# http://www.dreweatts.com/cms/pages/lot/36117/104
		# http://www.dreweatts.com/cms/pages/lot/36117/105
		# http://www.dreweatts.com/cms/pages/lot/36117/106
		# http://www.dreweatts.com/cms/pages/lot/36117/107
		# http://www.dreweatts.com/cms/pages/lot/36117/108
		# http://www.dreweatts.com/cms/pages/lot/36117/109
		# http://www.dreweatts.com/cms/pages/lot/36117/11
		# http://www.dreweatts.com/cms/pages/lot/36117/110
		# http://www.dreweatts.com/cms/pages/lot/36117/111
		# http://www.dreweatts.com/cms/pages/lot/36117/112
		# http://www.dreweatts.com/cms/pages/lot/36117/113
		# http://www.dreweatts.com/cms/pages/lot/36117/114
		# http://www.dreweatts.com/cms/pages/lot/36117/115
		# http://www.dreweatts.com/cms/pages/lot/36117/116
		# http://www.dreweatts.com/cms/pages/lot/36117/117
		# http://www.dreweatts.com/cms/pages/lot/36117/118
		# http://www.dreweatts.com/cms/pages/lot/36117/119
		# http://www.dreweatts.com/cms/pages/lot/36117/12
		# http://www.dreweatts.com/cms/pages/lot/36117/120
		# http://www.dreweatts.com/cms/pages/lot/36117/121
		# http://www.dreweatts.com/cms/pages/lot/36117/122
		# http://www.dreweatts.com/cms/pages/lot/36117/123
		# http://www.dreweatts.com/cms/pages/lot/36117/124
		# http://www.dreweatts.com/cms/pages/lot/36117/125
		# http://www.dreweatts.com/cms/pages/lot/36117/126
		# http://www.dreweatts.com/cms/pages/lot/36117/127
		# http://www.dreweatts.com/cms/pages/lot/36117/128
		# http://www.dreweatts.com/cms/pages/lot/36117/129
		# http://www.dreweatts.com/cms/pages/lot/36117/13
		# http://www.dreweatts.com/cms/pages/lot/36117/130
		# http://www.dreweatts.com/cms/pages/lot/36117/131
		# http://www.dreweatts.com/cms/pages/lot/36117/132
		# http://www.dreweatts.com/cms/pages/lot/36117/133
		# http://www.dreweatts.com/cms/pages/lot/36117/134
		# http://www.dreweatts.com/cms/pages/lot/36117/135
		# http://www.dreweatts.com/cms/pages/lot/36117/136
		# http://www.dreweatts.com/cms/pages/lot/36117/137
		# http://www.dreweatts.com/cms/pages/lot/36117/138
		# http://www.dreweatts.com/cms/pages/lot/36117/139
		# http://www.dreweatts.com/cms/pages/lot/36117/14
		# http://www.dreweatts.com/cms/pages/lot/36117/140
		# http://www.dreweatts.com/cms/pages/lot/36117/141
		# http://www.dreweatts.com/cms/pages/lot/36117/142
		# http://www.dreweatts.com/cms/pages/lot/36117/143
		# http://www.dreweatts.com/cms/pages/lot/36117/144
		# http://www.dreweatts.com/cms/pages/lot/36117/145
		# http://www.dreweatts.com/cms/pages/lot/36117/146
		# http://www.dreweatts.com/cms/pages/lot/36117/147
		# http://www.dreweatts.com/cms/pages/lot/36117/148
		# http://www.dreweatts.com/cms/pages/lot/36117/149
		# http://www.dreweatts.com/cms/pages/lot/36117/15
		# http://www.dreweatts.com/cms/pages/lot/36117/150
		# http://www.dreweatts.com/cms/pages/lot/36117/151
		# http://www.dreweatts.com/cms/pages/lot/36117/152
		# http://www.dreweatts.com/cms/pages/lot/36117/153
		# http://www.dreweatts.com/cms/pages/lot/36117/154
		# http://www.dreweatts.com/cms/pages/lot/36117/155
		# http://www.dreweatts.com/cms/pages/lot/36117/156
		# http://www.dreweatts.com/cms/pages/lot/36117/157
		# http://www.dreweatts.com/cms/pages/lot/36117/158
		# http://www.dreweatts.com/cms/pages/lot/36117/159
		# http://www.dreweatts.com/cms/pages/lot/36117/16
		# http://www.dreweatts.com/cms/pages/lot/36117/160
		# http://www.dreweatts.com/cms/pages/lot/36117/161
		# http://www.dreweatts.com/cms/pages/lot/36117/162
		# http://www.dreweatts.com/cms/pages/lot/36117/163
		# http://www.dreweatts.com/cms/pages/lot/36117/164
		# http://www.dreweatts.com/cms/pages/lot/36117/165
		# http://www.dreweatts.com/cms/pages/lot/36117/166
		# http://www.dreweatts.com/cms/pages/lot/36117/167
		# http://www.dreweatts.com/cms/pages/lot/36117/169
		# http://www.dreweatts.com/cms/pages/lot/36117/17
		# http://www.dreweatts.com/cms/pages/lot/36117/170
		# http://www.dreweatts.com/cms/pages/lot/36117/171
		# http://www.dreweatts.com/cms/pages/lot/36117/172
		# http://www.dreweatts.com/cms/pages/lot/36117/173
		# http://www.dreweatts.com/cms/pages/lot/36117/174
		# http://www.dreweatts.com/cms/pages/lot/36117/175
		# http://www.dreweatts.com/cms/pages/lot/36117/176
		# http://www.dreweatts.com/cms/pages/lot/36117/177
		# http://www.dreweatts.com/cms/pages/lot/36117/178
		# http://www.dreweatts.com/cms/pages/lot/36117/179
		# http://www.dreweatts.com/cms/pages/lot/36117/18
		# http://www.dreweatts.com/cms/pages/lot/36117/180
		# http://www.dreweatts.com/cms/pages/lot/36117/181
		# http://www.dreweatts.com/cms/pages/lot/36117/182
		# http://www.dreweatts.com/cms/pages/lot/36117/183
		# http://www.dreweatts.com/cms/pages/lot/36117/184
		# http://www.dreweatts.com/cms/pages/lot/36117/185
		# http://www.dreweatts.com/cms/pages/lot/36117/186
		# http://www.dreweatts.com/cms/pages/lot/36117/187
		# http://www.dreweatts.com/cms/pages/lot/36117/188
		# http://www.dreweatts.com/cms/pages/lot/36117/189
		# http://www.dreweatts.com/cms/pages/lot/36117/19
		# http://www.dreweatts.com/cms/pages/lot/36117/190
		# http://www.dreweatts.com/cms/pages/lot/36117/191
		# http://www.dreweatts.com/cms/pages/lot/36117/192
		# http://www.dreweatts.com/cms/pages/lot/36117/193
		# http://www.dreweatts.com/cms/pages/lot/36117/193A
		# http://www.dreweatts.com/cms/pages/lot/36117/194
		# http://www.dreweatts.com/cms/pages/lot/36117/195
		# http://www.dreweatts.com/cms/pages/lot/36117/196
		# http://www.dreweatts.com/cms/pages/lot/36117/197
		# http://www.dreweatts.com/cms/pages/lot/36117/198
		# http://www.dreweatts.com/cms/pages/lot/36117/198A
		# http://www.dreweatts.com/cms/pages/lot/36117/199
		# http://www.dreweatts.com/cms/pages/lot/36117/2
		# http://www.dreweatts.com/cms/pages/lot/36117/20
		# http://www.dreweatts.com/cms/pages/lot/36117/200
		# http://www.dreweatts.com/cms/pages/lot/36117/201
		# http://www.dreweatts.com/cms/pages/lot/36117/202
		# http://www.dreweatts.com/cms/pages/lot/36117/203
		# http://www.dreweatts.com/cms/pages/lot/36117/204
		# http://www.dreweatts.com/cms/pages/lot/36117/205
		# http://www.dreweatts.com/cms/pages/lot/36117/206
		# http://www.dreweatts.com/cms/pages/lot/36117/207
		# http://www.dreweatts.com/cms/pages/lot/36117/208
		# http://www.dreweatts.com/cms/pages/lot/36117/209
		# http://www.dreweatts.com/cms/pages/lot/36117/21
		# http://www.dreweatts.com/cms/pages/lot/36117/210
		# http://www.dreweatts.com/cms/pages/lot/36117/211
		# http://www.dreweatts.com/cms/pages/lot/36117/212
		# http://www.dreweatts.com/cms/pages/lot/36117/213
		# http://www.dreweatts.com/cms/pages/lot/36117/214
		# http://www.dreweatts.com/cms/pages/lot/36117/215
		# http://www.dreweatts.com/cms/pages/lot/36117/216
		# http://www.dreweatts.com/cms/pages/lot/36117/217
		# http://www.dreweatts.com/cms/pages/lot/36117/218
		# http://www.dreweatts.com/cms/pages/lot/36117/219
		# http://www.dreweatts.com/cms/pages/lot/36117/22
		# http://www.dreweatts.com/cms/pages/lot/36117/220
		# http://www.dreweatts.com/cms/pages/lot/36117/221
		# http://www.dreweatts.com/cms/pages/lot/36117/222
		# http://www.dreweatts.com/cms/pages/lot/36117/223
		# http://www.dreweatts.com/cms/pages/lot/36117/224
		# http://www.dreweatts.com/cms/pages/lot/36117/225
		# http://www.dreweatts.com/cms/pages/lot/36117/226
		# http://www.dreweatts.com/cms/pages/lot/36117/227
		# http://www.dreweatts.com/cms/pages/lot/36117/228
		# http://www.dreweatts.com/cms/pages/lot/36117/229
		# http://www.dreweatts.com/cms/pages/lot/36117/23
		# http://www.dreweatts.com/cms/pages/lot/36117/230
		# http://www.dreweatts.com/cms/pages/lot/36117/231
		# http://www.dreweatts.com/cms/pages/lot/36117/232
		# http://www.dreweatts.com/cms/pages/lot/36117/233
		# http://www.dreweatts.com/cms/pages/lot/36117/234
		# http://www.dreweatts.com/cms/pages/lot/36117/235
		# http://www.dreweatts.com/cms/pages/lot/36117/236
		# http://www.dreweatts.com/cms/pages/lot/36117/237
		# http://www.dreweatts.com/cms/pages/lot/36117/238
		# http://www.dreweatts.com/cms/pages/lot/36117/239
		# http://www.dreweatts.com/cms/pages/lot/36117/24
		# http://www.dreweatts.com/cms/pages/lot/36117/240
		# http://www.dreweatts.com/cms/pages/lot/36117/241
		# http://www.dreweatts.com/cms/pages/lot/36117/242
		# http://www.dreweatts.com/cms/pages/lot/36117/243
		# http://www.dreweatts.com/cms/pages/lot/36117/244
		# http://www.dreweatts.com/cms/pages/lot/36117/245
		# http://www.dreweatts.com/cms/pages/lot/36117/246
		# http://www.dreweatts.com/cms/pages/lot/36117/247
		# http://www.dreweatts.com/cms/pages/lot/36117/248
		# http://www.dreweatts.com/cms/pages/lot/36117/249
		# http://www.dreweatts.com/cms/pages/lot/36117/25
		# http://www.dreweatts.com/cms/pages/lot/36117/250
		# http://www.dreweatts.com/cms/pages/lot/36117/251
		# http://www.dreweatts.com/cms/pages/lot/36117/252
		# http://www.dreweatts.com/cms/pages/lot/36117/253
		# http://www.dreweatts.com/cms/pages/lot/36117/254
		# http://www.dreweatts.com/cms/pages/lot/36117/255
		# http://www.dreweatts.com/cms/pages/lot/36117/256
		# http://www.dreweatts.com/cms/pages/lot/36117/257
		# http://www.dreweatts.com/cms/pages/lot/36117/258
		# http://www.dreweatts.com/cms/pages/lot/36117/259
		# http://www.dreweatts.com/cms/pages/lot/36117/26
		# http://www.dreweatts.com/cms/pages/lot/36117/260
		# http://www.dreweatts.com/cms/pages/lot/36117/261
		# http://www.dreweatts.com/cms/pages/lot/36117/262
		# http://www.dreweatts.com/cms/pages/lot/36117/263
		# http://www.dreweatts.com/cms/pages/lot/36117/264
		# http://www.dreweatts.com/cms/pages/lot/36117/265
		# http://www.dreweatts.com/cms/pages/lot/36117/266
		# http://www.dreweatts.com/cms/pages/lot/36117/267
		# http://www.dreweatts.com/cms/pages/lot/36117/268
		# http://www.dreweatts.com/cms/pages/lot/36117/269
		# http://www.dreweatts.com/cms/pages/lot/36117/27
		# http://www.dreweatts.com/cms/pages/lot/36117/270
		# http://www.dreweatts.com/cms/pages/lot/36117/271
		# http://www.dreweatts.com/cms/pages/lot/36117/272
		# http://www.dreweatts.com/cms/pages/lot/36117/273
		# http://www.dreweatts.com/cms/pages/lot/36117/274
		# http://www.dreweatts.com/cms/pages/lot/36117/275
		# http://www.dreweatts.com/cms/pages/lot/36117/276
		# http://www.dreweatts.com/cms/pages/lot/36117/277
		# http://www.dreweatts.com/cms/pages/lot/36117/278
		# http://www.dreweatts.com/cms/pages/lot/36117/279
		# http://www.dreweatts.com/cms/pages/lot/36117/28
		# http://www.dreweatts.com/cms/pages/lot/36117/280
		# http://www.dreweatts.com/cms/pages/lot/36117/281
		# http://www.dreweatts.com/cms/pages/lot/36117/282
		# http://www.dreweatts.com/cms/pages/lot/36117/283
		# http://www.dreweatts.com/cms/pages/lot/36117/284
		# http://www.dreweatts.com/cms/pages/lot/36117/285
		# http://www.dreweatts.com/cms/pages/lot/36117/286
		# http://www.dreweatts.com/cms/pages/lot/36117/287
		# http://www.dreweatts.com/cms/pages/lot/36117/288
		# http://www.dreweatts.com/cms/pages/lot/36117/289
		# http://www.dreweatts.com/cms/pages/lot/36117/29
		# http://www.dreweatts.com/cms/pages/lot/36117/290
		# http://www.dreweatts.com/cms/pages/lot/36117/291
		# http://www.dreweatts.com/cms/pages/lot/36117/292
		# http://www.dreweatts.com/cms/pages/lot/36117/293
		# http://www.dreweatts.com/cms/pages/lot/36117/294
		# http://www.dreweatts.com/cms/pages/lot/36117/295
		# http://www.dreweatts.com/cms/pages/lot/36117/296
		# http://www.dreweatts.com/cms/pages/lot/36117/297
		# http://www.dreweatts.com/cms/pages/lot/36117/298
		# http://www.dreweatts.com/cms/pages/lot/36117/299
		# http://www.dreweatts.com/cms/pages/lot/36117/3
		# http://www.dreweatts.com/cms/pages/lot/36117/30
		# http://www.dreweatts.com/cms/pages/lot/36117/300
		# http://www.dreweatts.com/cms/pages/lot/36117/301
		# http://www.dreweatts.com/cms/pages/lot/36117/302
		# http://www.dreweatts.com/cms/pages/lot/36117/303
		# http://www.dreweatts.com/cms/pages/lot/36117/304
		# http://www.dreweatts.com/cms/pages/lot/36117/305
		# http://www.dreweatts.com/cms/pages/lot/36117/306
		# http://www.dreweatts.com/cms/pages/lot/36117/307
		# http://www.dreweatts.com/cms/pages/lot/36117/308
		# http://www.dreweatts.com/cms/pages/lot/36117/309
		# http://www.dreweatts.com/cms/pages/lot/36117/31
		# http://www.dreweatts.com/cms/pages/lot/36117/310
		# http://www.dreweatts.com/cms/pages/lot/36117/311
		# http://www.dreweatts.com/cms/pages/lot/36117/312
		# http://www.dreweatts.com/cms/pages/lot/36117/313
		# http://www.dreweatts.com/cms/pages/lot/36117/314
		# http://www.dreweatts.com/cms/pages/lot/36117/314A
		# http://www.dreweatts.com/cms/pages/lot/36117/314B
		# http://www.dreweatts.com/cms/pages/lot/36117/315
		# http://www.dreweatts.com/cms/pages/lot/36117/33
		# http://www.dreweatts.com/cms/pages/lot/36117/34
		# http://www.dreweatts.com/cms/pages/lot/36117/35
		# http://www.dreweatts.com/cms/pages/lot/36117/36
		# http://www.dreweatts.com/cms/pages/lot/36117/37
		# http://www.dreweatts.com/cms/pages/lot/36117/38
		# http://www.dreweatts.com/cms/pages/lot/36117/39
		# http://www.dreweatts.com/cms/pages/lot/36117/4
		# http://www.dreweatts.com/cms/pages/lot/36117/40
		# http://www.dreweatts.com/cms/pages/lot/36117/41
		# http://www.dreweatts.com/cms/pages/lot/36117/42
		# http://www.dreweatts.com/cms/pages/lot/36117/43
		# http://www.dreweatts.com/cms/pages/lot/36117/44
		# http://www.dreweatts.com/cms/pages/lot/36117/45
		# http://www.dreweatts.com/cms/pages/lot/36117/46
		# http://www.dreweatts.com/cms/pages/lot/36117/47
		# http://www.dreweatts.com/cms/pages/lot/36117/48
		# http://www.dreweatts.com/cms/pages/lot/36117/49
		# http://www.dreweatts.com/cms/pages/lot/36117/5
		# http://www.dreweatts.com/cms/pages/lot/36117/50
		# http://www.dreweatts.com/cms/pages/lot/36117/51
		# http://www.dreweatts.com/cms/pages/lot/36117/52
		# http://www.dreweatts.com/cms/pages/lot/36117/53
		# http://www.dreweatts.com/cms/pages/lot/36117/54
		# http://www.dreweatts.com/cms/pages/lot/36117/55
		# http://www.dreweatts.com/cms/pages/lot/36117/56
		# http://www.dreweatts.com/cms/pages/lot/36117/57
		# http://www.dreweatts.com/cms/pages/lot/36117/58
		# http://www.dreweatts.com/cms/pages/lot/36117/59
		# http://www.dreweatts.com/cms/pages/lot/36117/6
		# http://www.dreweatts.com/cms/pages/lot/36117/60
		# http://www.dreweatts.com/cms/pages/lot/36117/61
		# http://www.dreweatts.com/cms/pages/lot/36117/62
		# http://www.dreweatts.com/cms/pages/lot/36117/63
		# http://www.dreweatts.com/cms/pages/lot/36117/64
		# http://www.dreweatts.com/cms/pages/lot/36117/65
		# http://www.dreweatts.com/cms/pages/lot/36117/66
		# http://www.dreweatts.com/cms/pages/lot/36117/67
		# http://www.dreweatts.com/cms/pages/lot/36117/68
		# http://www.dreweatts.com/cms/pages/lot/36117/69
		# http://www.dreweatts.com/cms/pages/lot/36117/7
		# http://www.dreweatts.com/cms/pages/lot/36117/70
		# http://www.dreweatts.com/cms/pages/lot/36117/71
		# http://www.dreweatts.com/cms/pages/lot/36117/72
		# http://www.dreweatts.com/cms/pages/lot/36117/73
		# http://www.dreweatts.com/cms/pages/lot/36117/74
		# http://www.dreweatts.com/cms/pages/lot/36117/75
		# http://www.dreweatts.com/cms/pages/lot/36117/76
		# http://www.dreweatts.com/cms/pages/lot/36117/77
		# http://www.dreweatts.com/cms/pages/lot/36117/78
		# http://www.dreweatts.com/cms/pages/lot/36117/79
		# http://www.dreweatts.com/cms/pages/lot/36117/8
		# http://www.dreweatts.com/cms/pages/lot/36117/80
		# http://www.dreweatts.com/cms/pages/lot/36117/81
		# http://www.dreweatts.com/cms/pages/lot/36117/82
		# http://www.dreweatts.com/cms/pages/lot/36117/83
		# http://www.dreweatts.com/cms/pages/lot/36117/84
		# http://www.dreweatts.com/cms/pages/lot/36117/85
		# http://www.dreweatts.com/cms/pages/lot/36117/86
		# http://www.dreweatts.com/cms/pages/lot/36117/87
		# http://www.dreweatts.com/cms/pages/lot/36117/88
		# http://www.dreweatts.com/cms/pages/lot/36117/89
		# http://www.dreweatts.com/cms/pages/lot/36117/9
		# http://www.dreweatts.com/cms/pages/lot/36117/90
		# http://www.dreweatts.com/cms/pages/lot/36117/91
		# http://www.dreweatts.com/cms/pages/lot/36117/92
		# http://www.dreweatts.com/cms/pages/lot/36117/93
		# http://www.dreweatts.com/cms/pages/lot/36117/94
		# http://www.dreweatts.com/cms/pages/lot/36117/95
		# http://www.dreweatts.com/cms/pages/lot/36117/96
		# http://www.dreweatts.com/cms/pages/lot/36117/97
		# http://www.dreweatts.com/cms/pages/lot/36117/98
		# http://www.dreweatts.com/cms/pages/lot/36117/99


