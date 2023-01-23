#!/usr/bin/python
#This script finds random phrases from the site https://randomwordgenerator.com/sentence.php and outputs them to the file sentences.txt.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

outfile = open("sentences.txt", "w")
maxloops = 100
for i in range(maxloops):
    print("loop " + str(i + 1) + " of " + str(maxloops))
    #browser = webdriver.Firefox()
    chop = webdriver.ChromeOptions()
    chop.add_extension("/home/robert/se/ublock.zip")
    browser = webdriver.Chrome(options=chop)
    browser.implicitly_wait(5)
    #xtendir = "/home/robert/.mozilla/firefox/ge7c7jjy.default-esr/extensions/"
    #xtendir = "/home/robert/.mozilla/firefox/2kwfga0o.default-release-1635564517899/extensions/"
    #xtens = os.listdir(xtendir)
    #for j in xtens:
    #    browser.install_addon(xtendir + j, temporary=True)
    browser.get("https://randomwordgenerator.com/sentence.php")
    element = browser.find_element_by_xpath("//*[@id=\"qty\"]")
    element.send_keys(Keys.DELETE)
    element.send_keys("50")
    element.send_keys(Keys.RETURN)
    for j in range(1, 51):
        try:
            phrase = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div/div[2]/div/ol/li[" + str(j) + "]/div/span")
            outfile.write(phrase.text + "\n")
        except:
            print("failed on " + str(j))
    browser.quit()
outfile.close()
