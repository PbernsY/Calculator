import lexer_calc
import shunting_yard
import ext

while True:

	_input = input()
	if _input == "quit()":
		break
	b = lexer_calc.tokeniser(_input)
	print("Tokenised input {}".format(b))
	rpn = shunting_yard.shunting(b)
	print("RPN of Tokenised  {}".format(rpn))
	result = ext.make_tree(rpn)
	print("Result of {} is {}".format(b,ext.evaluate(result)))



