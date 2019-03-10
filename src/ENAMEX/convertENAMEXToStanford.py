import sys
import re

def convertENAMEXToEntities(inputFile) :
	text = ""
	
	enamTag = re.compile("<ENAMEX TYPE=\"(.*?)\".*?>(.*?)</ENAMEX>")
	for line in inputFile.readlines() :
		entities = enamTag.findall(line)
		for entity in entities :
			sentence = ""
			words = entity[1].split(" ")
			for word in words :
				sentence = sentence + word + "_" + entity[0] + " "
			text = text + sentence
	
	return text

if __name__ == "__main__" :
	argv = sys.argv
	argc = len(argv)
	
	if argc > 2 :
		inputFile = open(argv[1], "r")
		outputFile = open(argv[2], "w")
		
		outputFile.write(convertENAMEXToEntities(inputFile))
		
		inputFile.close()
		outputFile.close()
	else :
		print "Usage : python convertENAMEXToEntites <inpuFile> <outputFile>"
