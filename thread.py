import threading
import time

exitFlag = 0

class MyThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run (self):
		print('starting :' + self.name)
		print_time(self.name, self.counter, 5)
		print('exiting ' + self.name)

def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print('{}:{}'.format(threadName, time.ctime(time.time())))
		counter -= 1

t1 = MyThread(1, "t1", 1)
t2 = MyThread(2, "t2", 2)


t1.start()
t2.start()


t1.join()
t2.join()

print('exiting the main thread')