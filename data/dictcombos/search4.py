#!/usr/bin/python
#This script searches nearly 1 million random combinatons of dictionary words on the internet, using a locally run searx instance, and outputs a file for each search containing the links from that search.
#This requires Bueatiful Soup 4, urllib, and NLTK to be installed

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import nltk
import random

allwords = nltk.corpus.words.words()
searchterms = 1000000
searches = []
for i in range(searchterms):
    n = random.randint(1, 11)
    sstring = ""
    for j in range(n):
        if j < n - 1:
            sstring += allwords[random.randint(0, len(allwords) - 1)] + "%20"
        else:
            sstring += allwords[random.randint(0, len(allwords) - 1)]
    searches.append(sstring)
searches = list(set(searches))
diclen = len(searches)
ind = 0
for i in searches:
    if len(i) > 200:
        filename = i[0:200]
    else:
        filename = i
    outf = open("outputs4/" + filename, "w")
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
