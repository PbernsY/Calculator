class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def deqeue(self):
		return self.queue.pop(0)

	def is_empty(self):
		return True if not len(self.queue) else False
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
}

def isoperator(char):
	return char in "-+/*"
def shunting(_input):
	outq = Queue()
	op_stack = Stack()
	for char in _input:
		if char.isdigit():
			outq.enqueue(char)
		if isoperator(char):
			try:
				while (op_stack.peek() != "(") and ((PRECEDENCE[op_stack.peek()][0] > PRECEDENCE[char][0]) or ((PRECEDENCE[op_stack.peek()][0] == PRECEDENCE[char][0]) and
					PRECEDENCE[op_stack.peek()][1] == "left")):
					outq.enqueue(op_stack.pop())
				op_stack.push(char)
			except:
				op_stack.push(char)
			
		if char == "(":
			op_stack.push(char)
		if char == ")":
			while op_stack.peek() != "(":
				outq.enqueue(op_stack.pop())
			op_stack.pop()

	while not op_stack.is_empty():
		if op_stack.peek() in "()":
			raise ValueError("Incorrect Input")
		outq.enqueue(op_stack.pop())

	return outq





print(shunting("(3+(4 * 2))"))