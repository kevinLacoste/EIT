import xml.etree.ElementTree as ET
import sys

class specificEntity :
	def __init__(self, name, entityType):
		self.name = name
		self.entityType = entityType
		self.count = 1

def extractEntities(inputText) :
	entities = dict()
	
	nbWords = 0
	maxLength = 25
	for line in inputText :
		element = line.split("\t")
		if element[0] != "\n" and element[0] != "\r\n" and element[5] != "_" :
			# Reglage de la longueur maximale
			if len(element[1]) > maxLength :
				maxLength = len(element[1])
			if len(element[5]) > maxLength :
				maxLength = len(element[5])
			
			# Recuperation du tag dans les entites nommees
			if element[1] not in entities.keys() :
				entities[element[1]] = specificEntity(element[1], element[5])
			else :
				entities[element[1]].count = entities[element[1]].count + 1
			
		# Incrementation du nombre de mots
		nbWords = nbWords + 1
	
	entities["|nbWords|"] = nbWords
	entities["|maxLength|"] = maxLength
	
	return entities

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	
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
		
		inputFile.close()
	else :
		print "Usage : python limaEntitiesExtractor.py <file>.conll"
