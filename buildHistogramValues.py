''' SCROLL DOWN FOR MORE INFORMATION ON THIS CODE '''

#!/bin/usr/python

import random

rnList = [random.randrange(1, 100, 1) for _ in range(100)]


print "The list of random numbers are as shown below: "
print rnList

''' Count the number of times a value in the list occurs '''
# Reads the 100 values from the list sequentially
for i in range(100):
	print rnList[i], "occurs ", rnList.count(i), "times"


'''
Purpose :
	Generates 100 random values, adds them to a list and prints out the number of times each value occured

To run this program at the command prompt do 
	python threadsPython2.py
'''
