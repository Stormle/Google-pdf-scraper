# Google pdf-scraper
Google's "filetype:pdf" just doesn't work well and many results are left behind. This program scrapes search results for pdf files better than Google does and dumps download links in to a text file.


<b>GoogleSearch</b>
The syntax for the command googleSearch is:
 ```bash
googleSearch([search term as it would appear in a URL], [number of pages you want to scrape])
```
Search is done with the "repeat the search with the omitted results included" setting enabled.
There is a 2 second delay between each request to keep Google happy. I do not condone spamming requests.
