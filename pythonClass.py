'''
Scroll to the bottom for more information
'''

#!/bin/python

print "This is a python class example"


# Class definitions here #
class Monkey():

	def jump(self):
		print "I can't jump, sorry. I am lazy"

	def run(self):
		print "I can run very fast"


class Chimpanzee(Monkey):

	def jump(self):
		print "Voila, Je sui d'appelle Chimpanzee, I can jump fast"
		
	def shout(self):
		print "I also shout aloud, you'll go deaf mind you!"


class Orangutan(Monkey):
	def smart(self):
		print "I am smart, I know how to use tools \
		       I sometime bite my scientists :P "	


# Using the class #

mm = Monkey() 
mm.jump()
mm.run()

cc = Chimpanzee()
cc.jump()
cc.shout()

po = Orangutan()
po.smart()

'''
A test program for Inheritance, Chimpanzee inherits the monkey
'''

