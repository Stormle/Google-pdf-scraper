from subs.filedownloader import Downloadfiles
from subs.webscraper import googleSearch
from subs.filewriter import Writetofile
import os, sys
import getpass

print("Starting...")
if not os.path.isdir("/Users/" + getpass.getuser() + "/Documents/pdf-scrape"):
	os.mkdir("/Users/" + getpass.getuser() + "/Documents/pdf-scrape")

resultlist = googleSearch("company+annual+report", 30)

Writetofile(resultlist, "/Users/" + getpass.getuser() + "/Documents/pdf-scrape/data.txt")
