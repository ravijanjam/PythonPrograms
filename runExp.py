#!/usr/bin/python

from random import randint

# Put into bins
arr1 = [] 
arr2 = [] 
nExp = 100
nType = 3
seq = []

def evtGen(nExp, nType):
	for i in range(1, nExp):

		t = randint(0, 1000)%nType
		seq.append(t);

		for j in range(1, nType):
			if t==nType:
				arr1.append(t)
		
evtGen(nExp, nType)

print '\n Total number of times experiment is run : ', nExp, "\n"
print seq, "length of the sequence: " ,len(seq)
#print arr1, '\n number of samples with value is 0', len(arr1), "\n"
#print arr2, '\n number of samples with value is 0', len(arr2), "\n"


