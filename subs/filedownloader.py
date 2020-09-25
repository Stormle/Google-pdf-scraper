import requests

#I ended up having way less links than anticipated so I just downloaded them by hand. Here's my half-working file downloader function.
# It just needs support for links that don't end in .pdf or has redirects. Links should be a list.
def Downloadfiles(links, path):
	for i in links:
		print("test")
		splitup = links.split("/")
		datatowrite = requests.get(links)
		filename1 = splitup[(len(splitup) - 1)]
		if not ".pdf" in filename1:
			filename1 += ".pdf"
		with open(path + filename1, 'wb') as f:
			f.write(datatowrite.content)