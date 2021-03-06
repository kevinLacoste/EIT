import sys
import re

def convertENAMEXToEntities(inputFile) :
	text = ""
	
	enamTag = re.compile("<ENAMEX TYPE=\"(.*?)\".*?>(.*?)</ENAMEX>")
	supprTag = re.compile("<.*?>")
	addTag = re.compile("(?P<word>[^\s|]+)")
	for line in inputFile.readlines() :
		entities = enamTag.findall(line)
		line = enamTag.sub("||| ", line)
		line = supprTag.sub("", line)
		line = addTag.sub("\g<word>/O", line)
		for entity in entities :
			sentence = ""
			words = entity[1].split(" ")
			for word in words :
				sentence = sentence + word + "/" + entity[0] + " "
			line = re.sub("\|\|\|", sentence, line, 1)
		text = text + line
	
	text = re.sub(" +", " ", text)
	
	words = text.split(" ")
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
