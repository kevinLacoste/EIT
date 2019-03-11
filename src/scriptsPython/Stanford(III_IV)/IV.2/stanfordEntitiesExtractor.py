import sys

class specificEntity :
	def __init__(self, name, entityType):
		self.name = name
		self.entityType = entityType
		self.count = 1

def extractEntities(inputText) :
	# Table for extraction
	entities = dict()
	
	nbWords = 0
	
	for line in inputText :
		words = line.split(" ")
		for word in words :
			parts = word.split("/")
			trueWord = ""
			tag = parts[len(parts) - 1]
			if tag not in ["O", " ", "\n", "\t"] :
				for i in range(len(parts)) :
					if i == len(parts) - 2 :
						trueWord = trueWord + parts[i]
					elif i < len(parts) - 2 :
						trueWord = trueWord + parts[i]
				if trueWord not in entities.keys() :
					entities[trueWord] = specificEntity(trueWord, tag)
				else :
					entities[trueWord].count = entities[trueWord].count + 1
			nbWords = nbWords + 1
	
	entities["|nbWords|"] = nbWords
	return entities

if __name__ == "__main__" :
	argv = sys.argv
	argc = len(argv)
	if argc > 2 :
		inputFile = open(argv[1], "r")
		outputFile = open(argv[2], "w")
		entities = extractEntities(inputFile.readlines())
		
		# Valeurs arbitraires
		nbWords = entities["|nbWords|"]
		
		# Suppression des valeurs au dessus
		entities.pop("|nbWords|", None)
		
		# Marche parce qu'on traite de l'anglais
		keys = list(entities.keys())
		keys.sort(key=str.lower)
		
		for key in keys :
			entity = entities[key]
			outputFile.write(entity.name + "\t" + entity.entityType + "\t" + str(entity.count) + "\t" + str(round(100.0*entity.count/nbWords, 2)) + "\n")
		
		inputFile.close()
		outputFile.close()
	else :
		print "Usage : python stanfordEntitiesExtractor.py <inputFile> <outputFile>"
