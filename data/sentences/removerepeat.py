#!/usr/bin/python
#This script removes duplicates from sentences.txt and outputs them to the file sentencesunique.txt.

sefile = open("sentences.txt", "r")
lines = sefile.readlines()
sefile.close()
lines = set(lines)
uniquefile = open("sentencesunique.txt", "w")
for i in lines:
    uniquefile.write(i)
uniquefile.close()
