import re



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
}


tokenised = []
def tokeniser(_input):
	# regex works just fine, hacky 
	#tokens_ = re.findall(r"[\+\-\*\(\)/]|\d+", _input)
	
	for untokenised_chr in _input:
		if untokenised_chr == "":
			continue
		if untokenised_chr in "()":
			tokenised.append(untokenised_chr)
		elif untokenised_chr.isdigit():
			tokenised.append(Token("INT", int(untokenised_chr)))
		elif untokenised_chr in tokens:
			tokenised.append(Token(tokens[untokenised_chr][0], tokens[untokenised_chr][1]))
	return(tokenised)

