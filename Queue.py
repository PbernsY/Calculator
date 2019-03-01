'''class Node():
	def __init__(self):
		self.item = None
		self.next = None

class Stack():
	def __init__(self):
		self.top = None
	def isempty(self):
		return self.top == None
	def push(self, item):
		old = self.top
		self.top = Node()
		self.top.item = item
		self.top.next = old
	def pop(self):
		item = self.top.item
		self.top = self.top.next
		return item 
'''
from Stack import Stack
class Queue:
	def __init__(self):
		self.enq_stack = Stack()
		self.deq_stack = Stack()

	def enqueue(self, item):
		self.enq_stack.push(item)

	def isempty(self):
		return self.enq_stack.isempty() and self.deq_stack.isempty()
	def dequeue(self):
		if not self.deq_stack.isempty():
			return self.deq_stack.pop()
		else:
			if self.enq_stack:
				while not self.enq_stack.isempty():
					self.deq_stack.push(self.enq_stack.pop())
				return self.deq_stack.pop()
