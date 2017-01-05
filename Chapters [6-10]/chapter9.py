'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest
number of mail messages. The program looks for 'From ' lines and takes the second word of those lines
as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = raw_input("Enter file: ")
if len(name) < 1 : 
    name = "mbox-short.txt"
dct      = {}
handle   = open(name , 'r')
for line in handle:
    if line.startswith('From ') and len(line) > 2:
        line = line.split()
        dct[line[1]] = dct.get(line[1] , 0) + 1
m        = dct.values()
m        = max(m)
print list(dct.keys())[list(dct.values()).index(m)] , m
