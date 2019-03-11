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
	for line in inputText :
		element = line.split("\t")
		if element[0] != "\n" and element[0] != "\r\n" and element[5] != "_" :
			# Recuperation du tag dans les entites nommees
			if element[1] not in entities.keys() :
				entities[element[1]] = specificEntity(element[1], element[5])
			else :
				entities[element[1]].count = entities[element[1]].count + 1
			
		# Incrementation du nombre de mots
		nbWords = nbWords + 1
	
	entities["|nbWords|"] = nbWords
	
	return entities

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	
	if argc > 2 and argv[1].endswith(".conll"):
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
	else :
		print "Usage : python limaEntitiesExtractor.py <inputFile>.conll <outputFile>"
