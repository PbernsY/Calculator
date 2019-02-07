import shunting_yard
from lexer_calc import *
class ExpressionTree(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		if not self.left:
			return str(self.value)
		return "(" +  " ".join(str(self.value) + str(self.left) + str(self.right)) + ")"


OPERATORS = {

	"+" : int.__add__,
	"-" : int.__sub__,
	"*" : int.__mul__, 
	"/" : int.__floordiv__,
	"^" :int.__pow__
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
		if char not in OPERATORS:
			stack.append(ExpressionTree(char))
		else:
			expression = ExpressionTree(char)
			expression.right = stack.pop()
			expression.left = stack.pop()
			stack.append(expression)
	return stack.pop()

def evaluate(node):
    if not node.right and not node.left:
        return int(node.value)
    operator = OPERATORS[node.value]
    return operator(evaluate(node.left), (evaluate(node.right)))
