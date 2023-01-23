# Internet Search Improvement Project
This project is about filtering out websites from search results that you already know about. You already know that Facebook and Youtube exist. What is the use in seeing them in search engine results?

## Data Files
I have generated data on what websites show up the most often over a wide range of web searches.
I have one where I searched each word in the dictionary in NLTK, one where I searched randomized sentences from [this site](https://randomwordgenerator.com/sentence.php), one where I searched randomized phrases from [this site](https://randomwordgenerator.com/phrase.php), and one where I searched nearly 1 million random combinations of dictionary words from NLTK.
On Jan 3, 2022, I added another one called random\_sentences2, where the search queries are generated using the code from "method 1" on [this site](https://www.pythonpool.com/generate-random-sentence-in-python/).
I used 1000 random sentences for random sentences 2.
They are called "dictionary\_words", "dictionary\_combinations", "random\_sentences", and "random\_phrases".
The data files contain many lines, where each line is of the following format:
\[number of times the domain occured in the initial searches\] \[the domain\]
for example, a file might contain the following lines:
```
305 github.com
670 reddit.com
1002 facebook.com
```
This means that github was found 305 times, reddit was found 670 times, and facebook was found 1002 times in searching.
The scripts mentioned below read data of this format. The generated ones can be used, you can generate your own with your own search data set, or you can manually write your own.
The scripts, use a threshold to determine whether a site is a "small site" or a "large site".
When you write your own, you can make some sites higher than a specific number, and some lower than a specific number.
The scripts and other information used to generate the data files can be found in the directory called "data", with each dataset in a subdirectory.
Some of the files require a local [searx](https://searx.github.io/searx/) instance to reproduce.

## HoHSer Browser addon
There is a browser addon called [HoHSer](https://github.com/pistom/hohser), which can be installed on Google Chromium/Chrome, Microsoft Edge, and Mozilla Firefox (and possibly other browsers that support the extensions of these ones).
This is a good option if you want to use Duckduckgo, Qwant, Google, Yahoo, Bing, Startpage, Ecosia, Yandex, or OneSearch as your search engine, since it is integrated directly into the browser.
You can add domains to note or hide manually through the browser addon, or you can add a list of domains as JSON format. See the JSON Format Script section to see how to convert the data files to json with a given threshold

## Script and Searx
If you want to use [searx](https://searx.github.io/searx/) as your search engine, you can use the script. You can run it from the command line, and pass data files to be used as arguments.
The -b switch generates html from the output and opens it in a browser, and the -t switch can be used to change the threshold. The -t switch must be followed by an integer number.
The script currently uses the [searx instance from disroot](https://search.disroot.org/), but the url in the python script can be changed to any searx instance.

## JSON Format Script
As mentioned eariler, the HoHSer browser addon takes JSON. The script named jsonconvert will convert from the format mentioned above for data files to the json required for HoHSer, and it will only include the sites that are above the threshold.

For both scripts, the default threshold value is 100.

## Dependencies
[Python 3.9](https://www.python.org/) or more recent is necessary to run the scripts.
Other recent versions such as 3.8 or 3.7 may work as well.
[The Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io/en/latest/) and [urllib](https://docs.python.org/3/library/urllib.html) Python libraries must be installed.
[NLTK](https://www.nltk.org/) is necessary to regenerate some of the data files that I have provided.
[Essential Generators](https://pypi.org/project/essential-generators/) is necessary to regenerate random\_sentences2.

## Feedback
Please post any constructive criticism or bugs in the issues section on the [gitlab page](https://gitlab.com/123456robert/search-engine-filter). :)
