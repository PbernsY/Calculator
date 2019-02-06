import shunting_yard
from lexer_calc import *
class ExpressionTree(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.value) + str(self.left) + str(self.right)


OPERATORS = {

	"+" : int.__add__,
	"-" : int.__sub__,
	"*" : int.__mul__, 
	"/" : int.__floordiv__,
	} 

def is_operator(item):
	return item in OPERATORS

def inorder_traversal(item):
	if item:
		inorder_traversal(item.left)
		print(item.value),
		inorder_traversal(item.right)

def make_tree(POSTFIXNOTATION):
	stack = []
	for char in POSTFIXNOTATION:
		if not is_operator(char):
			_int = ExpressionTree(char)
			stack.append(_int)
		else:
			_int = ExpressionTree(char)
			child1 = stack.pop()
			child2 = stack.pop()
			_int.right = child1
			_int.left = child2
			stack.append(_int)
	_int = stack.pop()
	return _int

def evaluate(node):
	if not node.right and not node.left:
		return int(node.value)
	else:
		return OPERATORS[node.value](evaluate(node.left), (evaluate(node.right)))

