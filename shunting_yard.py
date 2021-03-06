class Token:
	def __init__(self, type, value = "Null"):
		self.type = type
		self.value = value


	def __str__(self):
		return 'Token({type}, {value})'.format(type = self.type, value = self.value)

	def __repr__(self):
		return self.__str__()
class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def deqeue(self):
		return self.queue.pop(0)

	def is_empty(self):
		return True if not len(self.queue) else False

	def __iter__(self):
		yield from self.queue
	def __str__(self):
		out = [str(x) for x in self.queue]
		return str(out)



class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1] if self.stack else False
	def is_empty(self):
		return len(self.stack) == 0

		








PRECEDENCE = {
		"+" : (2, "left"),
		"*" : (3, "left"),
		"-" : (2, "left"),
		"/" : (2, "left"),
		"^" : (4, "right")
}

def isoperator(char):
	return char in "-+/*^"
def shunting(_input):
	outq = Queue()
	op_stack = Stack()
	for char in _input:
		if char.value == "(":
			op_stack.push(char.value)
		if char.value == ")":
			while op_stack.peek() != "(":
				outq.enqueue(op_stack.pop())
			op_stack.pop()

		if char.type == "INT":
			outq.enqueue(int(char.value))
		if isoperator((str(char.value))):
			try:
				while (op_stack.peek() != "(") and ((PRECEDENCE[op_stack.peek()][0] > PRECEDENCE[char.value][0]) or ((PRECEDENCE[op_stack.peek()][0] == PRECEDENCE[char.value][0]) and
					PRECEDENCE[op_stack.peek()][1] == "left")):
					outq.enqueue(op_stack.pop())
				op_stack.push(char.value)
			except:
				op_stack.push(char.value)
			
		

	while not op_stack.is_empty():
		if op_stack.peek() in "()":
			raise ValueError("Incorrect Input")
		outq.enqueue(op_stack.pop())
	return outq








