import re
fh = open('regex_sum_288502.txt')
s = 0;w = [];
for line in fh:
	line = line.rstrip()
	x  = re.findall('\S*[0-9]\S*',line)
	if x == []:
		continue
	else:
		for q in x:
			s = s + int(q)
print s
