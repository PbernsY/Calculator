from multiprocessing import *
def sayhi():
	print "Hi from process", current_process().pid


def procex():
	print "HI from process", current_process().pid, (parent process)
	otherproc = Process(target = sayhi, args = ())

	otherproc.start()