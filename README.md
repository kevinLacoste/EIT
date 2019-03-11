Projet TAL - EIT

Les ressources fournies avec le projet sont disponibles dans le dossier Ressources.
Le dossier src contient quant à lui les scripts et les fichiers générés durant le projet, c'est à dire :
-- Les scripts python, classés par partie du projet et exercice, et fournis avec les fichiers sur lesquels ils sont censés fonctionner
-- Les tables de traduction pour respectivement les parties II,III et V du projet

Scripts disponibles :
-- limaEntitiesExtractor.py : ce script prend en entrée un fichier .conll et permet d'afficher la liste des entités nommées sous ce format :
	Entité nommée	Type	Nombre d’occurrences	Proportion dans le texte (%)
	
	Usage : python limaEntitiesExtractor.py <inputFile>.conll <outputFile>
	
-- syntaxicAnalyzer.py : ce script prend en entrée un fichier .conll ou .disambiguated.xml et transcrit son contenu sous forme de texte avec comme suffixe _TAG, TAG étant le tag de l'analyse syntaxique pour le token concerné.
	Usage : python syntaxicAnalyser.py <file>.disambiguated.xml <outputFile> 
	Usage : python syntaxicAnalyser.py <file>.conll <outputFile>
	
	
-- translateToUniv.py : ce script sert à traduire les tags de la PTB ou Penn Tree Bank vers les tags universels. Il utilise la table de traduction POSTags_PTB_Universal.txt
	Usage : python translateToUniv.py <table> <file>

-- convertRefToLine.py : un script annexe permettant de formatter wsj_0010_sample.txt.pos.ref de manière à pouvoir l'utiliser avec evaluate.py
	Usage : python convertRefToLine.py <file.ref> <outputFile>
	
-- stanfordEntitiesExtractor.py : ce script sert à extraire les entités nommées provenant de l'outil de reconnaissance d'entités de l'université de Stanford de la même façon que limaEntitiesExtractor.py
	Usage : python stanfordEntitiesExtractor.py <inputFile> <outputFile>
	
-- convertENAMEXToStanford.py : ce script prend en entrée la référence ENAMEX fournie (formal-tst.NE.key.04oct95_small.ne) et la traduit en liste d'entités nommées de Stanford de manière à pouvoir être comparée. La mise en forme peut être à refaire (sauts de lignes)
	Usage : python convertENAMEXToEntites <inpuFile> <outputFile>
	
-- translateLIMAEntToStanfordEnt.py : ce script permet de traduire un fichier .conll provenant de LIMA en liste d'entités nommées Stanford. Il necessite la table POSTags_LIMAEnt_StanfordEnt.txt .
	Usage : python translateLIMAEntToStanfordEnt.py <table for LIMA to Stanford> <file>.conll <outputFile>
	
Tables : 
-- POSTags_PTB_Universal.txt : table traduisant les tags PTB (Penn Tree Bank) vers les tags universels
-- POSTags_LIMAEnt_StanfordEnt.txt : table permettant la traduction des types d'entités nommées d'un fichier .conll (LIMA) vers les types d'entités nommées Stanford

