import xml.etree.ElementTree as ET
import sys

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	sentence = ""
	
	if argc > 1 and (argv[1].endswith(".xml") or argv[1].endswith(".conll")) :
		# Partie disambiguated.xml
		if argv[1].endswith(".xml") :
			tree = ET.parse(argv[1])
			root = tree.getroot()
			
			for child in root :
				lemma = child.find("lemma").text
				macro = child.find("micro").text
				sentence = sentence + lemma + "_" + macro + " "
		
		# Partie conll
		elif argv[1].endswith(".conll") :
			f = open(argv[1], "r")
			for line in f.readlines() :
				if line != "\n" :
					words = line.split("\t")
					sentence = sentence + words[1] + "_" + words[4] + " "
			f.close()
		
		print(sentence)
	
	else :
		print "Usage : ex3.py <file>.disambiguated.xml or ex3.py <file>.conll"
