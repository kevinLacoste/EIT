import xml.etree.ElementTree as ET
import sys

class specificEntity :
	def __init__(self, name, entityType):
		self.name = name
		self.entityType = entityType
		self.count = 1

if __name__ == "__main__" :
	argc = len(sys.argv)
	argv = sys.argv
	
	if argc > 2 :
		nbWordsTree = ET.parse(argv[1])
		entitiesTree = ET.parse(argv[2])
		
		nbWords = len(nbWordsTree.getroot())
		root = entitiesTree.getroot()
		
		# Dictionnaries to store data
		entities = dict()
		maxLength = 0
		
		for child in root :
			string = child.find("string").text
			entType = child.find("type").text
			
			if len(string) > maxLength :
				maxLength = len(string)
			if len(entType) > maxLength :
				maxLength = len(entType)
			
			if string not in entities.keys() :
				entities[string] = specificEntity(string, entType)
			else :
				entities[string].count =  entities[string].count + 1
		
		if maxLength < 25 :
			maxLength = 25
		
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
		
	else :
		print "Usage : ex2.py <file>.disambiguated.xml <file>.se.xml"
