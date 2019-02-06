import lexer_calc
import shunting_yard
import ext


_input = input()
a = lexer_calc.format_input(_input)
print("This is formatted to cater for - ")
print(a)
b = lexer_calc.tokeniser(a)
print("Tokenised input")
print(b)
rpn = shunting_yard.shunting(b)
print("RPN of Tokenised" + " ")
print(rpn)
result = ext.make_tree(rpn)
print(ext.evaluate(result))



