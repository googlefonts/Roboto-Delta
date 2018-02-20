from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables._g_l_y_f import Glyph
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.varLib.mutator import instantiateVariableFont

# grade min
xopq = 64 #minimum=26, maximum=171, default=94
yopq = 48 #minimum=26, maximum=132, default=77

# grade max
#xopq = 124 #minimum=26, maximum=171, default=94
#yopq = 108 #minimum=26, maximum=132, default=77

xtramin = 210
xtramax = 513

path = u"../fonts/RobotoDelta-VF.ttf"

ttFont = TTFont(path)

glyphSet = ttFont.getGlyphSet()

data = {}
for key in glyphSet.keys():
	data[key] = {}

# DEFAULT
for key in glyphSet.keys():
	g = glyphSet[key]
	data[key]["default"] = g.width

# MAX
location = {"XOPQ": xopq, "YOPQ": yopq, "XTRA": xtramax}
maxfont = instantiateVariableFont(ttFont, location)
maxGlyphSet = maxfont.getGlyphSet()

for key in maxGlyphSet.keys():
	g = maxGlyphSet[key]
	data[key]["max"] = g.width

# MIN
location = {"XOPQ": xopq, "YOPQ": yopq, "XTRA": xtramin}
minfont = instantiateVariableFont(ttFont, location)
minGlyphSet = minfont.getGlyphSet()

for key in minGlyphSet.keys():
	g = minGlyphSet[key]
	data[key]["min"] = g.width

# GRADE
gradeFont = ttFont
glyf = gradeFont["glyf"]
#gradeFont["glyf"] = glyf = newTable("glyf")
#glyf.glyphOrder = ttFont.getGlyphOrder()
#glyf.glyphs = {}

for key, value in data.items():

	dflt, mn, mx = value["default"], value["min"], value["max"]
	try:
		f = 1.0 * (dflt-mn)/(mx-mn)
	except ZeroDivisionError:
		f = 0 # TEST THIS
	loc = (xtramax-xtramin)*f+xtramin

	location = {"XOPQ": xopq, "YOPQ": yopq, "XTRA": loc}
	
	tempFont = instantiateVariableFont(ttFont, location)
	tempglyph = tempFont.getGlyphSet()[key]
	
	glyf[key] = Glyph()
    	
	pen = TTGlyphPen(None)
	tempglyph.draw(pen)
	
	glyf[key] = pen.glyph()

"""
#print "Removing GX tables"
for tag in ('fvar','avar','gvar'):
	if tag in gradeFont:
		del gradeFont[tag]
"""

import os
TARGET_DIR = ""
fileName = "RobotoDelta-GRADmin.ttf"
gradeFont.save(os.path.join(TARGET_DIR, fileName))
