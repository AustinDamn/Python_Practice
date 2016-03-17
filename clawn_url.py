import urllib
import re

url = raw_input('Enter = ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
	print link

#http://www.py4inf.com/book.htm