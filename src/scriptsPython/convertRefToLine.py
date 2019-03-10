import sys

# Script supplementaire : sert a transformer le wsj_0010_sample.pos.ref pour etre utilise avec evaluate.py

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
	else :
		print "Usage : python convertRefToLine.py <file.ref> (Genere un fichier ayant pour nom <file.ref>.converted)"
