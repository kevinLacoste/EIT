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
	
	for line in inputFile.readlines() :
		element = line.split("\t")
		if element[0] == "\n" or element[0] == "\n" :
			text = text[:len(text)-1] + "\n"
		elif element[5] in translationTable.keys() :
			text = text + element[1] + "/" + translationTable[element[5]] + " "
		else :
			# Tag par defaut
			text = text + element[1] + "/O "
	
	return text

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	
	if argc > 2 and argv[2].endswith(".conll") :
		translationFile = open(argv[1], "r")
		inputFile = open(argv[2], "r")
		
		translationTable = createTranslationTable(translationFile)
		outputText = writeEntitiesFromLIMAToStanford(inputFile, translationTable)
		
		outputName = argv[2][:len(argv[2])-6] + ".output"
		outputFile = open(outputName, "w")
		outputFile.write(outputText)
		
		translationFile.close()
		inputFile.close()
		outputFile.close()
	else :
		print("Usage : python translateLIMAEntToStanfordEnt.py <table for LIMA to Stanford> <file>.conll")
