import urllib
from BeautifulSoup import *

url = raw_input('Enter =')
#http://www.dr-chuck.com/page1.htm
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html) 

#Retrieve all <a> of the anchor tags
tags = soup('a')

for tag in tags:
	#Look at the parts of a tag
	print 'TAG:', tag
	print 'URL:',tag.get('href', None)
	#print 'Conntent:',tag.Conntent[0]
	#print 'Attrs:',tag.Attrs