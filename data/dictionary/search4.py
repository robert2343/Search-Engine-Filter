#!/usr/bin/python
#This script searches each dictionary word on the internet once, using a locally run searx instance, and outputs a file for each search containing the links from that search.
#This requires Bueatiful Soup 4, urllib, and NLTK to be installed

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import nltk

searches = nltk.corpus.words.words()
diclen = len(searches)
ind = 0
for i in searches:
    outf = open("outputs4/" + i, "w")
    nxtpg = True
    j = 1
    while nxtpg:
        nxtpg = False
        url = 'http://127.0.0.1:8888/search?q=' + i + '&categories=general&pageno=' + str(j) + '&language=en-US'
        response = urllib.request.urlopen(url)
        webContent = response.read()
        soup = BeautifulSoup(str(webContent), 'html.parser')
        links = soup.find_all('a')
        nxtpg = len(links) >= 10
        for k in links:
            outf.write(k.get('href') + "\n")
        j += 1
    outf.close()
    print(str(ind/diclen*100) + "% done with searches. Search query: " + i)
    ind += 1
