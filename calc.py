import lexer_calc
import shunting_yard
import ext



while True:
	_input = input()
	if _input == "quit()":
		break
	else:
		a = lexer_calc.format_input(_input)
		print(a)
		b = lexer_calc.tokeniser(a)
		print(b)
		rpn = shunting_yard.shunting(b)
		print(rpn)
		result = ext.make_tree(rpn)



