'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt
'''
name = raw_input('Enter the name of the file: ')
if len(name) < 3 : name = 'words.txt'
fh = open(name,'r')
for line in fh:
	print line.upper().strip()
fh.close()
