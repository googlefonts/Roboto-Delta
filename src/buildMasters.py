"""
This script builds the 'master_ufo' fonts from the '1-drawings' fonts. 
It fills the glyph set based on the default master and creates all the composite accents.
"""

# TODO use fontParts instead of defcon
from defcon import Font
import os

# define the default master
default = "RobotoDelta-Regular.ufo"

# dictionary of glyph constructions used to build the composite accents
composites = {
	"Agrave": "A+grave@top",
	"Aacute": "A+acute@top",
	"Acircumflex": "A+circumflex@top",
	"Atilde": "A+tilde@top",
	"Adieresis": "A+dieresis@top",
	"Aring": "A+ring@top",
	"Ccedilla": "C+cedilla@bottom",
	"Egrave": "E+grave@top",
	"Eacute": "E+acute@top",
	"Ecircumflex": "E+circumflex@top",
	"Edieresis": "E+dieresis@top",
	"Igrave": "I+grave@top",
	"Iacute": "I+acute@top",
	"Icircumflex": "I+circumflex@top",
	"Idieresis": "I+dieresis@top",
	"Ntilde": "N+tilde@top",
	"Ograve": "O+grave@top",
	"Oacute": "O+acute@top",
	"Ocircumflex": "O+circumflex@top",
	"Otilde": "O+tilde@top",
	"Odieresis": "O+dieresis@top",
	"Ugrave": "U+grave@top",
	"Uacute": "U+acute@top",
	"Ucircumflex": "U+circumflex@top",
	"Udieresis": "U+dieresis@top",
	"Yacute": "Y+acute@top",
	"agrave": "a+grave@top",
	"aacute": "a+acute@top",
	"acircumflex": "a+circumflex@top",
	"atilde": "a+tilde@top",
	"adieresis": "a+dieresis@top",
	"aring": "a+ring@top",
	"ccedilla": "c+cedilla@bottom",
	"egrave": "e+grave@top",
	"eacute": "e+acute@top",
	"ecircumflex": "e+circumflex@top",
	"edieresis": "e+dieresis@top",
	"igrave": "dotlessi+grave@top",
	"iacute": "dotlessi+acute@top",
	"icircumflex": "dotlessi+circumflex@top",
	"idieresis": "dotlessi+dieresis@top",
	"ntilde": "n+tilde@top",
	"ograve": "o+grave@top",
	"oacute": "o+acute@top",
	"ocircumflex": "o+circumflex@top",
	"otilde": "o+tilde@top",
	"odieresis": "o+dieresis@top",
	"ugrave": "u+grave@top",
	"uacute": "u+acute@top",
	"ucircumflex": "u+circumflex@top",
	"udieresis": "u+dieresis@top",
	"yacute": "y+acute@top",
	"ydieresis": "y+dieresis@top",
}

src_dir = "1-drawings"
target_dir = "master_ufo"

masters = [directory for directory in os.listdir(src_dir) if directory.endswith(".ufo")]

# take the default out of the master list
if default in masters: masters.remove(default)

# load the default font
default_path = os.path.join(src_dir, default)
dflt = Font(default_path)

# load the font objects
fonts = []
for master in masters:
	path = os.path.join(src_dir, master)
	font = Font(path)
	fonts.append(font)

for font in fonts:
	
	# fill the glyph set with missing glyphs
	for glyph in dflt:
		
		glyphName = glyph.name
		
		if glyphName not in font and glyphName not in composites:
			font.insertGlyph(glyph)
			font[glyphName].lib['com.typemytype.robofont.mark'] = [0, 0, 0, 0.25] # dark grey
	
	# build the composites
	for glyphName in composites.keys():
		
		glyph = dflt[glyphName]
		
		if glyphName in composites.keys():
			font.newGlyph(glyphName)
			composite = font[glyphName]
			composite.width = glyph.width
			
			value = composites[glyphName]
			items = value.split("+")
			base = items[0]
			items = items[1:]
			
			component = composite.instantiateComponent()
			component.baseGlyph = base
			baseGlyph = font[base]
			composite.appendComponent(component)
			
			for item in items:
				baseName, anchorName = item.split("@")
				component = composite.instantiateComponent()
				component.baseGlyph = baseName
				anchor = _anchor = None
				for a in baseGlyph.anchors:
					if a["name"] == anchorName:
						anchor = a
				for a in font[baseName].anchors:
					if a["name"] == "_"+anchorName:
						_anchor = a
				if anchor and _anchor:
					x = anchor["x"] - _anchor["x"]
					y = anchor["y"] - _anchor["y"]
					component.move((x, y))
				composite.appendComponent(component)
			composite.lib['com.typemytype.robofont.mark'] = [0, 0, 0, 0.5] # grey
	
	# set the glyph order
	font.glyphOrder = dflt.glyphOrder
	
	# save in master_ufo directory
	path = os.path.join(target_dir, os.path.basename(font.path))
	font.save(path)

# save default in master_ufo directory
path = os.path.join(target_dir, os.path.basename(dflt.path))
dflt.save(path)