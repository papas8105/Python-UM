''' Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the
comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
other is the actual data you need to process for the assignment.

    Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: http://python-data.dr-chuck.net/comments_288508.json (Sum ends with 52)

You do not need to save these files to your folder since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. 
'''
import json
import urllib
import re
url      = raw_input('Enter Location: ')
if re.search('^http',url) or len(url)<3 or len(url) == 0:
	url  = 'http://python-data.dr-chuck.net/comments_288508.json'
print 'Retrieving ' + url
data     = urllib.urlopen(url).read()
print 'Retrieved ' + str(len(data)) + ' characters'
data     = json.loads(data)
comments = data['comments']
l        = []
for comment in comments:
        l.append(comment['count'])
print 'Count: ', len(l)
print 'Sum  : ', sum(l)
