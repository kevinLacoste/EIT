import sys

def createTranslationTable(translationFile) :
	translationTable = dict()
	
	for line in translationFile.readlines() :
		elems = line.split(" ")
		if len(elems) == 2 :
			translationTable[elems[0]] = elems[1].replace("\n", "").replace("\r", "")
	return translationTable

def writeEntitiesFromLIMAToStanford(inputFile, translationTable) :
	text = ""
	isLineJump = False
	
	for line in inputFile.readlines() :
		element = line.split("\t")
		if element[0] == "\n" or element[0] == "\r\n" :
			text = text[:len(text)-1] + "\n"
			isLineJump = True
		elif isLineJump :
			isLineJump = False
		elif element[5] in translationTable.keys() :
			words = element[1].split(" ")
			for word in words :
				text = text + word + "/" + translationTable[element[5]] + " "
		else :
			# Tag par defaut
			text = text + element[1] + "/O "
	
	return text

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	
	if argc > 3 and argv[2].endswith(".conll") :
		translationFile = open(argv[1], "r")
		inputFile = open(argv[2], "r")
		
		translationTable = createTranslationTable(translationFile)
		outputText = writeEntitiesFromLIMAToStanford(inputFile, translationTable)
		
		outputFile = open(argv[3], "w")
		outputFile.write(outputText)
		
		translationFile.close()
		inputFile.close()
		outputFile.close()
	else :
		print "Usage : python translateLIMAEntToStanfordEnt.py <table for LIMA to Stanford> <file>.conll <outputFile>"
