#MenuTitle: Eau de Garamond Batch Generate Fonts
# -*- coding: utf-8 -*-
__doc__="""
Eau de Garamond Batch Generate Fonts.
"""


fileFolder = "~/Documents/Typography/EauDeGaramond/GitHub/3. Glyphs Source Files/"

otf_path = "~/Documents/Typography/EauDeGaramond/GitHub/2. OpenType Font Files/"
ttf_path = "~/Documents/Typography/EauDeGaramond/GitHub/1. TrueType Font Files/"

OTF_AutoHint = True
TTF_AutoHint = True
RemoveOverlap = True
UseSubroutines = True
UseProductionNames = True


import os

fileFolder = os.path.expanduser(fileFolder)
fileNames = os.listdir(fileFolder)

print fileNames

for fileName in fileNames:
	if os.path.splitext(fileName)[1] == ".glyphs":
		font = GSFont(os.path.join(fileFolder, fileName))
		print font.familyName
		for instance in font.instances:
			print "== Exporting OTF =="
			print instance.generate(Format = "OTF", FontPath = os.path.expanduser(otf_path), AutoHint = OTF_AutoHint, RemoveOverlap = RemoveOverlap, UseSubroutines = UseSubroutines, UseProductionNames = UseProductionNames)
		print
		for instance in font.instances:
			print "== Exporting TTF =="
			print instance.generate(Format = "TTF", FontPath = os.path.expanduser(ttf_path), AutoHint = TTF_AutoHint, RemoveOverlap = RemoveOverlap, UseProductionNames = UseProductionNames)
		print
		#for instance in font.instances:
		#	print "== Exporting WOFF =="
		#	print instance.generate(Format = "WOFF", FontPath = os.path.expanduser(web_path), AutoHint = TTF_AutoHint, RemoveOverlap = RemoveOverlap, UseSubroutines = UseSubroutines, UseProductionNames = UseProductionNames)
		#print