#!/usr/bin/python
#This script removes duplicates from phrases.txt and outputs them to the file phrasesunique.txt.

sefile = open("phrases.txt", "r")
lines = sefile.readlines()
sefile.close()
lines = set(lines)
uniquefile = open("phrasesunique.txt", "w")
for i in lines:
    uniquefile.write(i)
uniquefile.close()
