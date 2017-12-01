# FIXME anchors in intermediate masters are not kept when extracting the UFO from the variable font instance...

from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
from fontmake.font_project import FontProject
from fontTools.varLib import build
from fontTools.varLib.mutator import instantiateVariableFont
from defcon import Font
from robofab.world import OpenFont#, NewFont
from extractor import extractUFO
import os

# FIXME temp removal of mark and mkmk features with an empty class
class NoMarkFeatureWriter(object):
	def __init__(self, font):
		pass
		
	def write(self, doMark, doMkmk):
		return None
		
def buildDesignSpace(sources, instances, axes):
	
	doc = DesignSpaceDocument()
	
	for source in sources:
		s = SourceDescriptor()
		s.path = source["path"]
		s.name = source["name"]
		s.copyInfo = source["copyInfo"]
		s.location = source["location"]
		s.familyName = source["familyName"]
		s.styleName = source["styleName"]
		doc.addSource(s)
	
	for instance in instances:
		i = InstanceDescriptor()
		i.location = instance["location"]
		i.familyName = instance["familyName"]
		i.styleName = instance["styleName"]
		doc.addInstance(i)
	
	for axis in axes:
		a = AxisDescriptor()
		a.minimum = axis["minimum"]
		a.maximum = axis["maximum"]
		a.default = axis["default"]
		a.name = axis["name"]
		a.tag = axis["tag"]
		for languageCode, labelName in axis["labelNames"].items():
			a.labelNames[languageCode] = labelName
		a.map = axis["map"]
		doc.addAxis(a)
		
	return doc

def buildGlyphSet(dflt, fonts):
	# fill the glyph set with missing glyphs
	for font in fonts:
		for glyph in dflt:
			glyphName = glyph.name
			if glyphName not in font and glyphName not in composites:
				font.insertGlyph(glyph)
				font[glyphName].lib['com.typemytype.robofont.mark'] = [0, 0, 0, 0.25] # dark grey

def buildComposites(composites, fonts):
	# build the composites
	for font in fonts:
		for glyphName in composites.keys():
			font.newGlyph(glyphName)
			composite = font[glyphName]
			
			value = composites[glyphName]
			items = value.split("+")
			base = items[0]
			items = items[1:]
			
			baseGlyph = font[base]
			composite.width = baseGlyph.width
			composite.appendComponent(base)
			
			for item in items:
				baseName, anchorName = item.split("@")
				anchor = _anchor = None
				offset = (0, 0)
				for a in baseGlyph.anchors:
					if a.name == anchorName:
						anchor = a
				for a in font[baseName].anchors:
					if a.name == "_"+anchorName:
						_anchor = a
				if anchor is not None and _anchor is not None:
					x = anchor.x - _anchor.x
					y = anchor.y - _anchor.y
					offset = (x, y)
				composite.appendComponent(baseName, offset)
			composite.lib['com.typemytype.robofont.mark'] = [0, 0, 0, 0.5] # grey

def setGlyphOrder(glyphOrder, fonts):
	for font in fonts:
		font.lib['public.glyphOrder'] = glyphOrder

def saveMasters(fonts):
	# save in master_ufo directory
	for font in fonts:
		path = os.path.join("master_ufo", os.path.basename(font.path))
		font.save(path)

finder = lambda s: s.replace('master_ufo', 'master_ttf_interpolatable').replace('.ufo', '.ttf')

with open("RobotoDelta.enc") as enc:
	glyphOrder = enc.read().splitlines()

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

designSpacePath = "RobotoDelta.designspace"
familyName = "RobotoDelta"
default = "RobotoDelta-Regular.ufo"
src_dir = "1-drawings"

sources = [
	dict(path="master_ufo/RobotoDelta-Regular.ufo", name="RobotoDelta-Regular.ufo", location=dict(XOPQ=94, YOPQ=77, XTRA=359, YTLC=514, YTUC=712, YTAS=750, YTDE=-203, YTAD=563, YTDD=0, UDLN=-49, wght=400, wdth=0, opsz=12, PWGT=0, PWDT=0, POPS=0, GRAD=0, YTRA=0,), styleName="Regular", familyName=familyName, copyInfo=True),	

	dict(path="master_ufo/RobotoDelta-XOPQmin.ufo", name="RobotoDelta-XOPQmin.ufo", location=dict(XOPQ=26), styleName="XOPQmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-XOPQmax.ufo", name="RobotoDelta-XOPQmax.ufo", location=dict(XOPQ=171), styleName="XOPQmax", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-YOPQmin.ufo", name="RobotoDelta-YOPQmin.ufo", location=dict(YOPQ=26), styleName="YOPQmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-YOPQmax.ufo", name="RobotoDelta-YOPQmax.ufo", location=dict(YOPQ=132), styleName="YOPQmax", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoDelta-XOPQmin-YOPQmin.ufo", name="RobotoDelta-XOPQmin-YOPQmin.ufo", location=dict(XOPQ=26, YOPQ=26), styleName="XOPQmin-YOPQmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-XOPQmax-YOPQmax.ufo", name="RobotoDelta-XOPQmax-YOPQmax.ufo", location=dict(XOPQ=171, YOPQ=132), styleName="XOPQmax-YOPQmax", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoDelta-XTRAmin.ufo", name="RobotoDelta-XTRAmin.ufo", location=dict(XTRA=210), styleName="XTRAmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-XTRAmax.ufo", name="RobotoDelta-XTRAmax.ufo", location=dict(XTRA=513), styleName="XTRAmax", familyName=familyName, copyInfo=False),
]

axes = [
	dict(minimum=210, maximum=513, default=359, name="XTRA", tag="XTRA", labelNames={"en": "XTRA"}, map=[]),
	dict(minimum=26, maximum=171, default=94, name="XOPQ", tag="XOPQ", labelNames={"en": "XOPQ"}, map=[]),
	dict(minimum=26, maximum=132, default=77, name="YOPQ", tag="YOPQ", labelNames={"en": "YOPQ"}, map=[]),
	dict(minimum=416, maximum=570, default=514, name="YTLC", tag="YTLC", labelNames={"en": "YTLC"}, map=[]),
	dict(minimum=528, maximum=760, default=712, name="YTUC", tag="YTUC", labelNames={"en": "YTUC"}, map=[]),
	dict(minimum=649, maximum=854, default=750, name="YTAS", tag="YTAS", labelNames={"en": "YTAS"}, map=[]),
	dict(minimum=-305, maximum=-98, default=-203, name="YTDE", tag="YTDE", labelNames={"en": "YTDE"}, map=[]),
	dict(minimum=460, maximum=600, default=563, name="YTAD", tag="YTAD", labelNames={"en": "YTAD"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTDD", tag="YTDD", labelNames={"en": "YTDD"}, map=[]),
	dict(minimum=-195, maximum=0, default=-49, name="UDLN", tag="UDLN", labelNames={"en": "UDLN"}, map=[]),
	dict(minimum=100, maximum=900, default=400, name="wght", tag="wght", labelNames={"en": "wght"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="wdth", tag="wdth", labelNames={"en": "wdth"}, map=[]),
	dict(minimum=8, maximum=36, default=12, name="opsz", tag="opsz", labelNames={"en": "opsz"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="PWGT", tag="PWGT", labelNames={"en": "PWGT"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="PWDT", tag="PWDT", labelNames={"en": "PWDT"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="POPS", tag="POPS", labelNames={"en": "POPS"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="GRAD", tag="GRAD", labelNames={"en": "GRAD"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTRA", tag="YTRA", labelNames={"en": "YTRA"}, map=[]),
]

instances = [
]

doc = buildDesignSpace(sources, instances, axes)
doc.write(designSpacePath)

# load the default font
default_path = os.path.join(src_dir, default)
dflt = OpenFont(default_path)

masters = [source.name for source in doc.sources]
# take the default out of the master list
masters.remove(default)

# load the font objects
fonts = {}
for master in masters:
	path = os.path.join(src_dir, master)
	font = OpenFont(path)
	fonts[master] = font
	
# interpolation
XOPQminYOPQmin = fonts["RobotoDelta-XOPQmin-YOPQmin.ufo"]
XOPQmaxYOPQmax = fonts["RobotoDelta-XOPQmax-YOPQmax.ufo"]
XOPQmin = fonts["RobotoDelta-XOPQmin.ufo"]
YOPQmin = fonts["RobotoDelta-YOPQmin.ufo"]
XOPQmax = fonts["RobotoDelta-XOPQmax.ufo"]
YOPQmax = fonts["RobotoDelta-YOPQmax.ufo"]

for glyphName in XOPQminYOPQmin.keys():
	if glyphName not in XOPQmin:
		glyph = XOPQmin.newGlyph(glyphName)
		glyph.interpolate((1, 0), dflt[glyphName], XOPQminYOPQmin[glyphName])
	if glyphName not in YOPQmin:
		glyph = YOPQmin.newGlyph(glyphName)
		glyph.interpolate((0, 1), dflt[glyphName], XOPQminYOPQmin[glyphName])
	if glyphName not in XOPQmax:
		glyph = XOPQmax.newGlyph(glyphName)
		glyph.interpolate((1, 0), dflt[glyphName], XOPQmaxYOPQmax[glyphName])
	if glyphName not in YOPQmax:
		glyph = YOPQmax.newGlyph(glyphName)
		glyph.interpolate((0, 1), dflt[glyphName], XOPQmaxYOPQmax[glyphName])

fonts = fonts.values()

buildGlyphSet(dflt, fonts)
allfonts = [dflt]+fonts

saveMasters(allfonts) # save in master_ufo
ufos = [font.path for font in allfonts]

project = FontProject()
project.run_from_ufos(
	ufos, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False, 
	mark_writer_class=NoMarkFeatureWriter) # FIXME use default mark_writer_class

# tmp vf
# extract instance and fill intermediate master
varfont, _, _ = build(designSpacePath, finder)
instance = instantiateVariableFont(varfont, dict(XOPQ=26, YOPQ=26, XTRA=210))
instance.save("instance.ttf")
tmp = Font()
extractUFO("instance.ttf", tmp)
tmp.save("instance.ufo", formatVersion=2)
tmp = OpenFont("instance.ufo")
font = OpenFont("1-drawings/RobotoDelta-XOPQmin-YOPQmin-XTRAmin.ufo")
buildGlyphSet(tmp, [font])

allfonts.append(font)

buildComposites(composites, allfonts)
setGlyphOrder(glyphOrder, allfonts)
saveMasters(allfonts) # save in master_ufo

# update design space
intermediates = [
	dict(path="master_ufo/RobotoDelta-XOPQmin-YOPQmin-XTRAmin.ufo", name="RobotoDelta-XOPQmin-YOPQmin-XTRAmin.ufo", location=dict(XOPQ=26, YOPQ=26, XTRA=210), styleName="XOPQmax-YOPQmax-XTRAmin", familyName=familyName, copyInfo=False),
	]
sources += intermediates

doc = buildDesignSpace(sources, instances, axes)
doc.write(designSpacePath)

for i in intermediates:
	ufos.append(i["path"])

project = FontProject()
project.run_from_ufos(
	ufos, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False, 
	mark_writer_class=NoMarkFeatureWriter) # FIXME use default mark_writer_class

outfile = "../fonts/RobotoDelta-VF.ttf"
varfont, _, _ = build(designSpacePath, finder)
varfont.save(outfile)

print "DONE"

"""

# --------------
# 4. Blending VF
# --------------

print "Blending..."

varfont, _, _ = build(designspace_filename, finder)

familyName = "RobotoDelta"
instancedir = "instances/"

locations = {
	'Regular': {
		# default
	},
	'opszmin': {
		'YOPQ': 84,
		'XOPQ': 100,
		'YTLC': 532,
		'XTRA': 384,
	},
	'opszmax': {
		'YOPQ': 64,
		'XOPQ': 78,
		'YTLC': 490,
		'XTRA': 332,
	},
	'wghtmin': {
		'YOPQ': 52,
		'XOPQ': 44,
		'YTLC': 514,
		'XTRA': 384,
	},
	'wghtmax': {
		'YOPQ': 104,
		'XOPQ': 140,
		'YTLC': 528,
		'XTRA': 284,
	},
	'opszmin-wghtmin': {
		'YOPQ': 58,
		'XOPQ': 50,
		'YTLC': 528,
		'XTRA': 396,
	},
	'opszmin-wghtmax': {
		'YOPQ': 100,
		'XOPQ': 132,
		'YTLC': 542,
		'XTRA': 330,
	},
	'opszmax-wghtmin': {
		'YOPQ': 26,
		'XOPQ': 26,
		'YTLC': 484,
		'XTRA': 368,
	},
	'opszmax-wghtmax': {
		'YOPQ': 110,
		'XOPQ': 156,
		'YTLC': 490,
		'XTRA': 210,
	},
}

for key, location in locations.items():
	instance = instantiateVariableFont(varfont, location)
	instancename = "%s-%s.ttf" % (familyName, key)
	instancepath = os.path.join(instancedir, instancename)
	instance.save(instancepath)


finder = lambda s: s.replace('master_ufo', 'master_ttf_interpolatable').replace('.ufo', '.ttf')
varfont, _, _ = build(designspace_filename, finder)
print "Saving variation font %s" % outfile
varfont.save(outfile)
print "DONE"

"""