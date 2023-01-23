#!/usr/bin/python
#This script searches each line of sentencesunique.txt on the internet, using a locally run searx instance, and outputs a file for each search containing the links from that search.
#This requires Bueatiful Soup 4, and urllib to be installed

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

searchfile = open("sentencesunique.txt", "r")
searches = searchfile.readlines()
searchfile.close()
searches = [i.replace("’", "'").replace("%", "%25").replace(" ", "%20").replace("'", "%27").replace(",", "%2C").replace('"', "%22").replace(";", "%3B").replace(":", "%3A").replace("!", "%21").replace("@", "%40").replace("#", "%23").replace("$", "%24").replace("^", "%5E").replace("&", "%26").replace("*", "%2A").replace("(", "%28").replace(")", "%29").replace("+", "%2B").replace("{", "%7B").replace("}", "%7D").replace("[", "%5B").replace("]", "%5D").replace("|", "%7C").replace("\\", "%5C").replace("<", "%3C").replace(">", "%3E").replace("?", "%3F").replace("`", "%60").strip() for i in searches]
diclen = len(searches)
ind = 0
unicodeErrors = 0
for i in searches:
    if len(i) > 200:
        filename = i[0:200]
    else:
        filename = i
    outf = open("outputs5/" + filename, "w")
    nxtpg = True
    j = 1
    while nxtpg:
        nxtpg = False
        url = 'http://127.0.0.1:8888/search?q=' + i + '&categories=general&pageno=' + str(j) + '&language=en-US'
        try:
            response = urllib.request.urlopen(url)
            webContent = response.read()
            soup = BeautifulSoup(str(webContent), 'html.parser')
            links = soup.find_all('a')
            nxtpg = len(links) >= 10
            for k in links:
                outf.write(k.get('href') + "\n")
            j += 1
        except UnicodeEncodeError:
            unicodeErrors += 1
            print("unicode error")
    outf.close()
    print(str(ind/diclen*100) + "% done with searches. Search query: " + i)
    ind += 1
print("unicode errors: " + str(unicodeErrors))
