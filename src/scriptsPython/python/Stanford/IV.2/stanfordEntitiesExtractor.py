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
	maxLength = 25
	
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
			
			# Recherche de la longueur de trueWord
			if len(trueWord) > maxLength :
				maxLength = len(trueWord)
			
			nbWords = nbWords + 1
	
	entities["|nbWords|"] = nbWords
	entities["|maxLength|"] = maxLength
	return entities

if __name__ == "__main__" :
	argv = sys.argv
	argc = len(argv)
	if argc > 1 :
		inputFile = open(argv[1], "r")
		entities = extractEntities(inputFile.readlines())
		
		# Valeurs arbitraires
		nbWords = entities["|nbWords|"]
		maxLength = entities["|maxLength|"]
		
		# Suppression des valeurs au dessus
		entities.pop("|nbWords|", None)
		entities.pop("|maxLength|", None)
		
		# Marche parce qu'on traite de l'anglais
		keys = list(entities.keys())
		keys.sort(key=str.lower)
		
		print "Entite nommee", " "*(maxLength-13), "Type", " "*(maxLength-4), "Nb occurences   %(texte)"
		print ""
		
		for key in keys :
			entity = entities[key]
			nameLength = len(entity.name)
			typeLength = len(entity.entityType)
			print entity.name, " "*(maxLength-nameLength), entity.entityType, " "*(maxLength-typeLength+6), entity.count, " "*(8-len(str(entity.count))), round(100.0*entity.count/nbWords, 2), " %"
			
		print ""
		print "Nombre de mots dans le document : ", nbWords
	else :
		print "usage: python stanfordEntitiesExtractor.py <file>"
