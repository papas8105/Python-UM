'''
 Following Links in Python

In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the
anchor tags, scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.
'''
import urllib
from BeautifulSoup import *
import re
url=raw_input("Enter URL: ")
if len(url) < 3:
	url = 'http://python-data.dr-chuck.net/known_by_Brandi.html'
count=int(raw_input("Enter count:"))
position=int(raw_input("Enter position:"))
#7 times 18 position
ls = []
for ii in range(count):
    print "Retrieving:",url
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    for tag in tags:
        ls.append(tag)
    url = ls[position-1].get('href', None)
    ls = []
print '\n\n'
s = re.findall('_+.+_+(.+)\.',url)
print 'The last name retrieved from the process was: ', str(s[0])
