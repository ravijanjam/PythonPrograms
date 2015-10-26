''' SCROLL DOWN FOR MORE INFORMATION ON THIS CODE '''

#!/usr/bin/python

import threading, time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print "Starting " +  self.name
		print_time(self.name, self.counter, 5)
		print "Exiting " + self.name


def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print "%s: %s" % (threadName, time.ctime(time.time()))
		counter -= 1

# Create new threads
thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting main Thread"

'''

Purpose :
	Prints the date with a short delay from two threads.

To run this program at the command prompt do 
	python threadsPython2.py
'''
