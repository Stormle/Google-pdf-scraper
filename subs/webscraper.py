import time
import requests
import re
def googleSearch(query, loops):
	g_clean = []
	#Loop for each page of search results
	for loopcount in range(loops):
		time.sleep(2)
		url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(
			query) + "&start=" + str((loopcount) * 10) + "&filter=0"

		dataX = requests.get(url)
		regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
		url2 = re.findall(regex, str(dataX.text))
		for i in url2:
			#Check if the URL contains either of the words ".pdf" or "document". Skip if it's link by Google.
			if ".pdf" in i[0]:
				if not "google" in i[0]:
					splitup = str(i[0]).split("&")
					a = ""
					for temp1 in splitup:
						#Splitting the URL and reconstructing it to end with the essential part. Necessary for downloading the file later on.
						a += temp1
						if ".pdf" in a:
							break
					if ".pdf" in i[0]:
						print("Found: " + a)
						g_clean.append(a)
					if not ".pdf" in str(str(i[0]).split("&")[0]):
						print("link contained a &-symbol too soon and we lost the filetype. Adding to list anyway:" + a)
			elif "document" in i[0]:
				#Alternative "document" -route
				if not "google" in i[0]:
					#Tidying the link up, checking for duplicates and removing unnecessary characters.
					parsedlink = str(i[0].split("--")).strip("[]'")
					iffound = False
					for i2 in g_clean:
						if parsedlink == i2:
							iffound = True
							break
					if not iffound:
						print("Found: " + str(parsedlink))
						g_clean.append(str(parsedlink))

	print("Done with " + query + "!")
	return g_clean