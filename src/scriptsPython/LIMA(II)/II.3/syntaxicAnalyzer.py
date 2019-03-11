import xml.etree.ElementTree as ET
import sys

class token :
	def __init__(self, content, tag) :
		self.content = content
		self.tag = tag

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	sentence = ""
	
	if argc > 2 and (argv[1].endswith(".xml") or argv[1].endswith(".conll")) :
		# Partie disambiguated.xml
		if argv[1].endswith(".xml") :
			tree = ET.parse(argv[1])
			root = tree.getroot()
			children = dict()
			
			for child in root :
				position = child.get("position")
				lemma = child.find("lemma").text
				macro = child.find("micro").text
				children[position] = token(lemma, macro)
			
			for key, value in sorted(children.items(), key=lambda x: int(x[0])) :
				words = value.content.split(" ")
				for word  in words :
					sentence = sentence + word + "_" + value.tag + " "
		
		# Partie conll
		elif argv[1].endswith(".conll") :
			isLineJump = False
			
			f = open(argv[1], "r")
			for line in f.readlines() :
				if line != "\n" and not isLineJump :
					words = line.split("\t")
					bits = words[1].split(" ")
					for bit in bits :
						sentence = sentence + bit + "_" + words[4] + " "
				elif isLineJump :
					isLineJump = False
				else :
					sentence = sentence + "\n"
					isLineJump = True
			f.close()
		
		outputFile = open(argv[2], "w")
		outputFile.write(sentence)
		outputFile.close()
	
	else :
		print "Usage : python syntaxicAnalyser.py <file>.disambiguated.xml <outputFile> \nUsage : python syntaxicAnalyser.py <file>.conll <outputFile>"
