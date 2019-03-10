import sys

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	
	if argc > 1 :
		inputFile = open(argv[1], "r")
		outputFile = open(argv[1] + ".converted", "w")
		for line in inputFile.readlines() :
			words = line.split("\t")
			for i in range(len(words)) :
				if i == len(words)-1 :
					outputFile.write("_" + words[i].replace("\n", "").replace("\r\n", "") + " ")
				else :
					outputFile.write(words[i])
		inputFile.close()
		outputFile.close()
