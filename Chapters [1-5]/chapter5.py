'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore
the number.
Enter the numbers from the book for problem 5.1 and Match the desired output as shown.  
'''
largest  = None
smallest = None
l = list()
while True:
    num      =  raw_input("Enter a number: ")
    if  num  == "done": 
    	break
    try:
        num  == int(num)
    except:
        print 'Invalid input'
        continue
    l.append(int(num))
    largest  = max(l)
    smallest = min(l)
print 'The maximum integer you gave as input is ',largest,'.'
print 'The minimun integer you gave as input is ',smallest,'.'
