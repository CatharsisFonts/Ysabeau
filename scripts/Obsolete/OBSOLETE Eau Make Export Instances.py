#MenuTitle: Eau de Garamond Make Export Instances
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
		
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in all02names ]
renameGlyphsParameterKey = "Rename Glyphs"

suffix = ".lf"
allLFGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs3 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allLFGlyphNames ]


decomposeGlyphs = all01names + all02names + allLFGlyphNames

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.endswith("Infant"):
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs1 + renameGlyphs2 + renameGlyphs3, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["ss01", "ss02", "lnum"], "Remove Features" )
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )


# Text
Font = Glyphs.font

suffix = ".ss02"
all02names = [ g.name for g in Font.glyphs if (g.name.find(suffix) > 0) ]
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in all02names ]
renameGlyphsParameterKey = "Rename Glyphs"

decomposeGlyphs = all02names

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.endswith("Text"):
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs2, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["ss02"], "Remove Features" )
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )


# Smallcaps
Font = Glyphs.font

allSCnames = [ g.name for g in Font.glyphs if (g.name.find(".sc") > 0) ]
renameSC = [ "%s=%s" % ( x, x.replace(".sc","") ) for x in allSCnames ]

decomposeGlyphs = allSCnames

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.endswith("SC"):
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameSC, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["liga","dlig","smcp","c2sc"], "Remove Features" )
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )
	