#MenuTitle: Ysabeau Italic Make Export Instances
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters in the .glyphs file."""

import GlyphsApp

Font = Glyphs.font

all01names = [ g.name for g in Font.glyphs if (g.name.find(".ss01") > 0) ]
all02names = [ g.name for g in Font.glyphs if (g.name.find(".ss02") > 0) ]
all03names = [ g.name for g in Font.glyphs if (g.name.find(".ss03") > 0) ]
allBGRnames = [ g.name for g in Font.glyphs if (g.name.find(".loclBGR") > 0) ]
allLFnames = [ g.name for g in Font.glyphs if (g.name.find(".lf") > 0) ]

badones = [ name for name in all02names if (name.replace(".ss02",".ss01") in all01names) ]
for b in badones: all02names.remove( b )

renameGlyphs1 = [ "%s=%s" % ( x, x.replace(".ss01","") ) for x in all01names ]
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(".ss02","") ) for x in all02names ]
renameGlyphs3 = [ "%s=%s" % ( x, x.replace(".ss03","") ) for x in all03names ]
renameGlyphs4 = [ "%s=%s" % ( x, x.replace(".loclBGR","") ) for x in allBGRnames ]
renameGlyphs5 = [ "%s=%s" % ( x, x.replace(".lf","") ) for x in allLFGlyphNames ]


#decomposeGlyphs = all01names + allLFGlyphNames
decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	if thisInstance.familyName.endswith("Infant"):
		print(thisInstance.familyName + " " + thisInstance.name)
		del(thisInstance.customParameters["Rename Glyphs"])
		thisInstance.customParameters["Rename Glyphs"] = renameGlyphs1 + \
			renameGlyphs2 + renameGlyphs3 + renameGlyphs4 + renameGlyphs5
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


