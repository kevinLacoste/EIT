import sys

def createTranslationTable(translationFile) :
	translationTable = dict()
	
	t_file = open(translationFile, "r")
	
	for line in t_file.readlines() :
		elems = line.split(" ")
		if len(elems) == 2 :
			translationTable[elems[0]] = elems[1].replace("\n", "").replace("\t", "")
	return translationTable

def switchTags (lines, translationTable) :
	text = ""
	transKeys = translationTable.keys()
	for line in lines :
		words = line.split(" ")
		for word in words :
			sub = word.split("_")
			# Cas ou le mot ne possede pas ce caractere
			if len(sub) == 1 :
				text = text + sub[0] + " "
			# Dans ce cas on verifie que le dernier element est un tag lexical
			else :
				tag = sub[len(sub)-1]
				for i in range(len(sub)) :
					if i < len(sub)-1 :
						text = text + sub[i] + "_"
					else :
						# Cas ou le dernier element est bien un tag lima
						if tag in transKeys :
							text = text + translationTable[tag]
						# Cas ou ce n'est pas un tag lima
						else :
							text = text + tag
						text = text + " "
	return text

if __name__ == "__main__" :
	argv = sys.argv
	argc = len(argv)
	if argc > 2 :
		# Creation des tables de conversion
		translationTableToUniv = createTranslationTable(argv[1])
		
		# Recuperation des fichiers a traiter
		inputFile = open(argv[2], "r")
		
		# Traitement de la reference
		text = switchTags(inputFile.readlines(), translationTableToUniv)
		
		# Stockage dans les fichiers de sortie
		outputName = argv[2] + ".univ"
		outputFile = open(outputName, "w")
		outputFile.write(text)
		
		# Fermeture de tous les fichiers
		inputFile.close()
		outputFile.close()
		
	else :
		print "Usage : python3 ex4.py <table> <file>"
