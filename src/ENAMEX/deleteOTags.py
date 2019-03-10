import sys

def deleteOTags(inputFile) :
	text = ""
	
	for line in inputFile.readlines() :
		line = line.replace("\n", "").replace("\r\n", "")
		entities = line.split(" ")
		for entity in entities :
			words = entity.split("/")
			if len(words) > 1 and words[len(words)-1] != "O" :
				for i in range(len(words)) :
					if i == len(words)-1 :
						text = text[:len(text)-1] + "_" + words[i] + " "
					else :
						text = text + words[i] + "/"
			
	
	return text

if __name__ == "__main__" :
	argv = sys.argv
	argc = len(argv)
	
	if argc > 2 :
		inputFile = open(argv[1], "r")
		outputFile = open(argv[2], "w")
		
		outputFile.write(deleteOTags(inputFile))
		
		inputFile.close()
		outputFile.close()
	else :
		print "Usage : deleteOTags <inputFile> <outputFile>"
