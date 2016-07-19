#Create a dictionary that depicts the a-z and A-Z characters to their perspective ASCII values
d = {}
for ii in range(ord('A'),ord('z') + 1):
	d[chr(ii)] = ii
#now we have to remove some characters between Z and a
print d
import re
for key in d.keys():
	if not re.search('[a-zA-Z]',key):
		del d[key]
#and voila we have the desired dictionary
print d
