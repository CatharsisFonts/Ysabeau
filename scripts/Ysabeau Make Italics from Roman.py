#MenuTitle: Ysabeau Make Italics from Roman
# -*- coding: utf-8 -*-
"""Copies all common glyphs from Ysabeau Black to Ysabeau Black Italic"""

import GlyphsApp



print("Warning: This script requires both Ysabeau and Ysabeau Italics to be open.")
print

Fonts = Glyphs.fonts

YRoman = [f for f in Fonts if (os.path.basename(f.filepath) == "YsabeauRoman.glyphs")]
if YRoman: YRoman = YRoman[0] 
else: print("Error: Ysabeau Roman not open.")

YItalic = [f for f in Fonts if (os.path.basename(f.filepath) == "YsabeauItalic.glyphs")]
if YItalic: YItalic = YItalic[0] 
else: print("Error: Ysabeau Italic not open.")

BlackRoman = [m.id for m in YRoman.masters if (m.name == "Black")][0]
BlackItalic = [m.id for m in YItalic.masters if (m.name == "Black")][0]

RomanGlyphs = YRoman.glyphs
ItalicGlyphs = YItalic.glyphs

for i in ItalicGlyphs:
	matches = [g for g in RomanGlyphs if (g.name == i.name)]
	if matches:
		r = matches[0]
		print(r)
		i.layers[BlackItalic] = r.layers[BlackRoman]

print("Done.")
