'''
Find the sum of all the integers in the text.
'''
import re
fh = open('regex_sum_288502.txt','r')
s = 0;
for line in fh:
	line = line.rstrip()
	x  = re.findall('[0-9]+',line) #or '\S*[0-9]\S*'
	if x == []:
		continue
	else:
		for q in x:
			s = s + int(q)
print s
