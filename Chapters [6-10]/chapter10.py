'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the
day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and
then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name);dct = {};
for line in handle:
    if line.startswith('From ') and len(line) > 3:
        line = line.split()
        time = line[-2].split(':')
        key  = time[0]
        dct[key] = dct.get(key , 0) + 1
dct1 = dct.items()
dct1.sort()
for item in dct1:
    print item[0], item[1]
