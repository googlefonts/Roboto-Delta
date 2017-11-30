import os

# --------------
# 1. DesignSpace
# --------------

print "Writing DesignSpace"

from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor

designSpacePath = "RobotoDelta.designspace"
familyName = "RobotoDelta"

sources = [
	# TODO update axis values
	dict(path="master_ufo/RobotoDelta-Regular.ufo", name="RobotoDelta-Regular.ufo", location=dict(XOPQ=94, YOPQ=77, XTRA=359, YTLC=514, YTUC=712, YTAS=750, YTDE=-203, YTAD=563, YTDD=0, UDLN=-49, wght=400, wdth=0, opsz=12, PWGT=0, PWDT=0, POPS=0, GRAD=0, YTRA=0,), styleName="Regular", familyName=familyName, copyInfo=True),	
	
	dict(path="master_ufo/RobotoDelta-XOPQmin-i.ufo", name="RobotoDelta-XOPQmin-i.ufo", location=dict(XOPQ=26), styleName="XOPQmin-i", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-XOPQmax-i.ufo", name="RobotoDelta-XOPQmax-i.ufo", location=dict(XOPQ=171), styleName="XOPQmax-i", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-YOPQmin-i.ufo", name="RobotoDelta-YOPQmin-i.ufo", location=dict(YOPQ=26), styleName="YOPQmin-i", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-YOPQmax-i.ufo", name="RobotoDelta-YOPQmax-i.ufo", location=dict(YOPQ=132), styleName="YOPQmax-i", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoDelta-XOPQmin-YOPQmin.ufo", name="RobotoDelta-XOPQmin-YOPQmin.ufo", location=dict(XOPQ=26, YOPQ=26), styleName="XOPQmin-YOPQmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-XOPQmax-YOPQmax.ufo", name="RobotoDelta-XOPQmax-YOPQmax.ufo", location=dict(XOPQ=171, YOPQ=132), styleName="XOPQmax-YOPQmax", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoDelta-XTRAmin.ufo", name="RobotoDelta-XTRAmin.ufo", location=dict(XTRA=210), styleName="XTRAmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoDelta-XTRAmax.ufo", name="RobotoDelta-XTRAmax.ufo", location=dict(XTRA=513), styleName="XTRAmax", familyName=familyName, copyInfo=False),	

	dict(path="master_ufo/RobotoDelta-XOPQmin-YOPQmin-XTRAmin.ufo", name="RobotoDelta-XOPQmin-YOPQmin-XTRAmin.ufo", location=dict(XOPQ=26, YOPQ=26, XTRA=210), styleName="XOPQmax-YOPQmax-XTRAmin", familyName=familyName, copyInfo=False),
	
	#dict(path="master_ufo/RobotoDelta-YTLCmin.ufo", name="RobotoDelta-YTLCmin.ufo", location=dict(YTLC=416), styleName="YTLCmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTLCmax.ufo", name="RobotoDelta-YTLCmax.ufo", location=dict(YTLC=570), styleName="YTLCmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTUCmin.ufo", name="RobotoDelta-YTUCmin.ufo", location=dict(YTUC=528), styleName="YTUCmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTUCmax.ufo", name="RobotoDelta-YTUCmax.ufo", location=dict(YTUC=760), styleName="YTUCmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTASmin.ufo", name="RobotoDelta-YTASmin.ufo", location=dict(YTAS=649), styleName="YTASmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTASmax.ufo", name="RobotoDelta-YTASmax.ufo", location=dict(YTAS=854), styleName="YTASmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTDEmin.ufo", name="RobotoDelta-YTDEmin.ufo", location=dict(YTDE=-305), styleName="YTDEmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTDEmax.ufo", name="RobotoDelta-YTDEmax.ufo", location=dict(YTDE=-98), styleName="YTDEmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTADmin.ufo", name="RobotoDelta-YTADmin.ufo", location=dict(YTAD=460), styleName="YTADmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTADmax.ufo", name="RobotoDelta-YTADmax.ufo", location=dict(YTAD=600), styleName="YTADmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTDDmin.ufo", name="RobotoDelta-YTDDmin.ufo", location=dict(YTDD=-1), styleName="YTDDmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTDDmax.ufo", name="RobotoDelta-YTDDmax.ufo", location=dict(YTDD=1), styleName="YTDDmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-UDLNmin.ufo", name="RobotoDelta-UDLNmin.ufo", location=dict(UDLN=-195), styleName="UDLNmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-UDLNmax.ufo", name="RobotoDelta-UDLNmax.ufo", location=dict(UDLN=0), styleName="UDLNmax", familyName=familyName, copyInfo=False),
	
	##dict(path="instances/RobotoDelta-wghtmin.ttf", name="RobotoDelta-wghtmin.ttf", location=dict(wght=100), styleName="wghtmin", familyName=familyName, copyInfo=False),
	##dict(path="instances/RobotoDelta-wghtmax.ttf", name="RobotoDelta-wghtmax.ttf", location=dict(wght=900), styleName="wghtmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-wdthmin.ufo", name="RobotoDelta-wdthmin.ufo", location=dict(wdth=-1), styleName="wdthmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-wdthmax.ufo", name="RobotoDelta-wdthmax.ufo", location=dict(wdth=1), styleName="wdthmax", familyName=familyName, copyInfo=False),
	##dict(path="instances/RobotoDelta-opszmin.ttf", name="RobotoDelta-opszmin.ttf", location=dict(opsz=8), styleName="opszmin", familyName=familyName, copyInfo=False),
	##dict(path="instances/RobotoDelta-opszmax.ttf", name="RobotoDelta-opszmax.ttf", location=dict(opsz=36), styleName="opszmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-PWGTmin.ufo", name="RobotoDelta-PWGTmin.ufo", location=dict(PWGT=-1), styleName="PWGTmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-PWGTmax.ufo", name="RobotoDelta-PWGTmax.ufo", location=dict(PWGT=1), styleName="PWGTmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-PWDTmin.ufo", name="RobotoDelta-PWDTmin.ufo", location=dict(PWDT=-1), styleName="PWDTmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-PWDTmax.ufo", name="RobotoDelta-PWDTmax.ufo", location=dict(PWDT=1), styleName="PWDTmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-POPSmin.ufo", name="RobotoDelta-POPSmin.ufo", location=dict(POPS=-1), styleName="POPSmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-POPSmax.ufo", name="RobotoDelta-POPSmax.ufo", location=dict(POPS=1), styleName="POPSmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-GRADmin.ufo", name="RobotoDelta-GRADmin.ufo", location=dict(GRAD=-1), styleName="GRADmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-GRADmax.ufo", name="RobotoDelta-GRADmax.ufo", location=dict(GRAD=1), styleName="GRADmax", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTRAmin.ufo", name="RobotoDelta-YTRAmin.ufo", location=dict(YTRA=-1), styleName="YTRAmin", familyName=familyName, copyInfo=False),
	#dict(path="master_ufo/RobotoDelta-YTRAmax.ufo", name="RobotoDelta-YTRAmax.ufo", location=dict(YTRA=1), styleName="YTRAmax", familyName=familyName, copyInfo=False),
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

doc.write(designSpacePath)

# --------------
# 2. Master UFOs
# --------------

print "Building master_ufo"

# TODO use fontParts instead of defcon
from defcon import Font

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
			
			value = composites[glyphName]
			items = value.split("+")
			base = items[0]
			items = items[1:]
			
			component = composite.instantiateComponent()
			component.baseGlyph = base
			baseGlyph = font[base]
			composite.width = baseGlyph.width
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

# --------------
# 3. Master TTFs
# --------------

print "Building master_ttf_interpolatable"

from fontmake.font_project import FontProject

ufos = []
for directory in os.listdir("master_ufo"):
    if directory.endswith(".ufo"):
        path = os.path.join("master_ufo", directory)
        ufos.append(path)
project = FontProject()
project.run_from_ufos(ufos, output=("ttf-interpolatable"), remove_overlaps=False, use_production_names=False) # FIXME this also build master_ttf and should not.

# --------------
# 4. Blending VF
# --------------

print "Blending..."

from fontTools.varLib import build
from fontTools.varLib.mutator import instantiateVariableFont

designspace_filename = "RobotoDelta.designspace"
finder = lambda s: s.replace('master_ufo', 'master_ttf_interpolatable').replace('.ufo', '.ttf')
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

outfile = "../fonts/RobotoDelta-VF.ttf"
finder = lambda s: s.replace('master_ufo', 'master_ttf_interpolatable').replace('.ufo', '.ttf')
varfont, _, _ = build(designspace_filename, finder)
print "Saving variation font %s" % outfile
varfont.save(outfile)
print "DONE"