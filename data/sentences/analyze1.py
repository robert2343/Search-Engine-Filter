#!/usr/bin/python
#This script counts each domain name in the outputs5 directory and writes the output to stdout in the format that is read by the search and jsonconvert scripts

import os

def compare(e):
    return int(e.split()[0])

blacklist = ["searx.github.io",
            "/",
            "/about",
            "/preferences",
            "127.0.0.1:8888",
            "searx.space",
            "https://github.com/searx/searx",
            "https://github.com/searx/searx/issues",
            ""
            ]

files = os.listdir("outputs5")
domains = {}
for i in files:
    currfile = open("outputs5/" + i, "r")
    lines = currfile.readlines()
    currfile.close()
    for j in lines:
        domain = ""
        try:
            domain = j.split("/")[2].strip()
        except:
            domain = j.strip()
        if domain.strip() not in blacklist and j.strip() not in blacklist:
            try:
                domains[domain] += 1
            except:
                domains[domain] = 1
anaoutl = []
for i in domains:
    anaoutl.append(str(domains[i]) + " " + i.replace("\n", ""))

anaoutl.sort(key=compare)
for i in anaoutl:
    print(i)
