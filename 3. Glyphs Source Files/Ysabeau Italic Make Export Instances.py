#MenuTitle: Ysabeau Italic Make Export Instances
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters in the .glyphs file."""

import GlyphsApp


# Infant
Font = Glyphs.font

suffix = ".ss01"
all01names = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in all01names ]
renameGlyphsParameterKey = "Rename Glyphs"

forbidden = all01names
forbidden = [ x.replace(".ss01", ".ss02") for x in forbidden ]

suffix = ".ss02"
all02names = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]
good02names = all02names
for x in forbidden:
	if x in all02names: 
		good02names.remove(x)
		
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in good02names ]

suffix = ".ss03"
all03names = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]
good03names = all03names
for x in forbidden:
	if x in all03names: 
		good03names.remove(x)
		
renameGlyphs3 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in good03names ]


forbidden = all01names
forbidden = [ x.replace(".ss01", ".loclBGR") for x in forbidden ]

suffix = ".loclBGR"
allBGRnames = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]		
renameGlyphs4 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allBGRnames ]

suffix = ".lf"
allLFGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs5 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allLFGlyphNames ]

#decomposeGlyphs = all01names + allLFGlyphNames
decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	if thisInstance.familyName.endswith("Infant"):
		print(thisInstance.familyName + " " + thisInstance.name)
		del(thisInstance.customParameters["Rename Glyphs"])
		thisInstance.customParameters["Rename Glyphs"] = renameGlyphs1 + renameGlyphs2 + renameGlyphs3 + renameGlyphs4 + renameGlyphs5
		thisInstance.customParameters["Remove Features"] = ["ss01", "ss02", "lnum", "locl"]
		del(thisInstance.customParameters["Decompose Glyphs"])
		thisInstance.customParameters["Decompose Glyphs"] = decomposeGlyphs


# Office
Font = Glyphs.font

suffix = ".ss02"
all02names = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in all02names ]

suffix = ".tf"
allTFnames = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allTFnames ]

#decomposeGlyphs = all02names
decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	if thisInstance.familyName.endswith("Office"):
		print(thisInstance.familyName + " " + thisInstance.name)
		del(thisInstance.customParameters["Rename Glyphs"])
		thisInstance.customParameters["Rename Glyphs"] = renameGlyphs1 + renameGlyphs2
		thisInstance.customParameters["Remove Features"] = ["ss02", "tnum"]
		del(thisInstance.customParameters["Decompose Glyphs"])
		thisInstance.customParameters["Decompose Glyphs"] = decomposeGlyphs

