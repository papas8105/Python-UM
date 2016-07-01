'''
You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and
add them up to complete the assignment. 
'''
import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
if len(url)<3:
	url = 'http://python-data.dr-chuck.net/comments_288507.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
    print '\n'

s = 0
for tag in tags:
	x = int(tag.contents[0])
	s = s + x
print 'The total contents sum is: ' , s
