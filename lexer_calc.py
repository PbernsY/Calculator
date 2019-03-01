


class Token:
	def __init__(self, type, value = "Null"):
		self.type = type
		self.value = value


	def __str__(self):
		return 'Token({type}, {value})'.format(type = self.type, value = self.value)

	def __repr__(self):
		return self.__str__()


tokens = {
	"+" : ("PLUS","+"),
	"-" : ("MINUS", "-"),
	"/" : ("DIV", "/"),
	"*" : ("MUL", "*"),
	"(" : ("OPP", "("),
	")" : ("CLP", ")"),
	"^" : ("POW", "^")
}


bracks = [ "(", ")"]





class Token:
	def __init__(self, type, value = "Null"):
		self.type = type
		self.value = value


	def __str__(self):
		return 'Token({type}, {value})'.format(type = self.type, value = self.value)

	def __repr__(self):
		return self.__str__()


tokens = {
	"+" : ("PLUS","+"),
	"-" : ("MINUS", "-"),
	"/" : ("DIV", "/"),
	"*" : ("MUL", "*"),
	"(" : ("OPP", "("),
	")" : ("CLP", ")"),
	"^" : ("POW", "^")
}


bracks = [ "(", ")"]


def tokeniser(_input):
        tokenised = []
        i = 0
        if _input[0] == "-":
            tokenised.append(Token("INT", "-" + _input[1]))
            i = 2
        while i < len(_input):
            if _input[i] == " ":
                continue
            if _input[i] == "-":
                if _input[i - 1] not in tokens and _input[i + 1] not in tokens:
                    tokenised.append(Token("MINUS", "-"))
                    i += 1
                else:
                    if _input[i + 1] not in tokens:
                        tokenised.append(Token("INT", "-" + _input[i + 1]))
                        i += 2
                    else:
                        tokenised.append(Token("MINUS", "-"))
                        i += 1



            elif _input[i] in tokens:
                tokenised.append(Token(tokens[_input[i]][0],  tokens[_input[i]][1]))
                i += 1
            elif _input[i].isdigit():
                tokenised.append(Token("INT", _input[i]))
                i += 1
        return(tokenised)







