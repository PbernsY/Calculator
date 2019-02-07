


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
	for untokenised_chr in _input:
		if untokenised_chr == "":
			continue
		#if untokenised_chr in "()":
		#	tokenised.append(untokenised_chr)
		elif untokenised_chr.isdigit():
			tokenised.append(Token("INT", int(untokenised_chr)))
		elif untokenised_chr in tokens:
			tokenised.append(Token(tokens[untokenised_chr][0], tokens[untokenised_chr][1]))
	return(tokenised)





def format_input(_string):
	output = []
	i = 0
	if  _string[0] == "-":
				output.append("0")
				output.append(_string[0])
				i += 1
	while i < len(_string):
		if _string[i] == " ":
			i += 1
			continue
		if _string[i] == "-":
			if _string[i - 1].isdigit() and not _string[i + 1] == "-":
				output.append(_string[i])
				i += 1
			if _string[i + 1] == "-":
				output.append("+")
				i += 2
			
			elif _string[i - 1] in tokens:
				output.append("0")
				output.append(_string[i])
				i += 1
		else:
			output.append(_string[i])
			i += 1
	return output


