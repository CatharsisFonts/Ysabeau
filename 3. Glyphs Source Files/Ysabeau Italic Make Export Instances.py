#MenuTitle: Ysabeau Italic Make Export Instances
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters in the .glyphs file."""

import GlyphsApp

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


