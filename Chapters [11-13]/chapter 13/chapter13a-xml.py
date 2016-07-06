'''
Welcome Georgios Papadopoulos from Using Python to Access Web Data

Extracting Data from XML

In this assignment you will write a Python program somewhat similar to
http://www.pythonlearn.com/code/geoxml.py. The program will prompt for a URL, 
read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your
testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_288504.xml (Sum ends with 49)
'''
import urllib
import xml.etree.ElementTree as ET
address = raw_input('Enter location: ')
if len(address) < 1 : address = 'http://python-data.dr-chuck.net/comments_288504.xml'
print 'Retrieving ', address
page = urllib.urlopen(address)
data = page.read()
print 'Retrieved ' , len(data), ' characters'
tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
counts = []
for comment in comments:
	counts.append(int(comment.find('count').text))
print 'Count :', len(counts)
print 'Sum   :', sum(counts)
