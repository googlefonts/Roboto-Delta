from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
import os

designSpacePath = "RobotoDelta.designspace"
familyName = "RobotoDelta"

sources = [
	dict(path="src/master_ufo/RobotoDelta-Regular.ufo", name="RobotoDelta-Regular.ufo", location=dict(XTRA=0, XOPQ=0, YOPQ=0, YTLC=0, YTUC=0, YTAS=0, YTDE=0, YTAD=0, YTDD=0, UDLN=0, wght=0, wdth=0, opsz=0, PWGT=0, PWDT=0, POPS=0, GRAD=0, YTRA=0,), styleName="Regular", familyName=familyName, copyInfo=True),	
	dict(path="src/master_ufo/RobotoDelta-XTRAmin.ufo", name="RobotoDelta-XTRAmin.ufo", location=dict(XTRA=-1), styleName="XTRAmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-XTRAmax.ufo", name="RobotoDelta-XTRAmax.ufo", location=dict(XTRA=1), styleName="XTRAmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-XOPQmin.ufo", name="RobotoDelta-XOPQmin.ufo", location=dict(XOPQ=-1), styleName="XOPQmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-XOPQmax.ufo", name="RobotoDelta-XOPQmax.ufo", location=dict(XOPQ=1), styleName="XOPQmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YOPQmin.ufo", name="RobotoDelta-YOPQmin.ufo", location=dict(YOPQ=-1), styleName="YOPQmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YOPQmax.ufo", name="RobotoDelta-YOPQmax.ufo", location=dict(YOPQ=1), styleName="YOPQmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTLCmin.ufo", name="RobotoDelta-YTLCmin.ufo", location=dict(YTLC=-1), styleName="YTLCmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTLCmax.ufo", name="RobotoDelta-YTLCmax.ufo", location=dict(YTLC=1), styleName="YTLCmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTUCmin.ufo", name="RobotoDelta-YTUCmin.ufo", location=dict(YTUC=-1), styleName="YTUCmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTUCmax.ufo", name="RobotoDelta-YTUCmax.ufo", location=dict(YTUC=1), styleName="YTUCmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTASmin.ufo", name="RobotoDelta-YTASmin.ufo", location=dict(YTAS=-1), styleName="YTASmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTASmax.ufo", name="RobotoDelta-YTASmax.ufo", location=dict(YTAS=1), styleName="YTASmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTDEmin.ufo", name="RobotoDelta-YTDEmin.ufo", location=dict(YTDE=-1), styleName="YTDEmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTDEmax.ufo", name="RobotoDelta-YTDEmax.ufo", location=dict(YTDE=1), styleName="YTDEmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTADmin.ufo", name="RobotoDelta-YTADmin.ufo", location=dict(YTAD=-1), styleName="YTADmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTADmax.ufo", name="RobotoDelta-YTADmax.ufo", location=dict(YTAD=1), styleName="YTADmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTDDmin.ufo", name="RobotoDelta-YTDDmin.ufo", location=dict(YTDD=-1), styleName="YTDDmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-YTDDmax.ufo", name="RobotoDelta-YTDDmax.ufo", location=dict(YTDD=1), styleName="YTDDmax", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-UDLNmin.ufo", name="RobotoDelta-UDLNmin.ufo", location=dict(UDLN=-1), styleName="UDLNmin", familyName=familyName, copyInfo=False),
	dict(path="src/master_ufo/RobotoDelta-UDLNmax.ufo", name="RobotoDelta-UDLNmax.ufo", location=dict(UDLN=1), styleName="UDLNmax", familyName=familyName, copyInfo=False),
	
	#dict(path="src/master_ufo/RobotoDelta-wghtmin.ufo", name="RobotoDelta-wghtmin.ufo", location=dict(wght=-1), styleName="wghtmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-wghtmax.ufo", name="RobotoDelta-wghtmax.ufo", location=dict(wght=1), styleName="wghtmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-wdthmin.ufo", name="RobotoDelta-wdthmin.ufo", location=dict(wdth=-1), styleName="wdthmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-wdthmax.ufo", name="RobotoDelta-wdthmax.ufo", location=dict(wdth=1), styleName="wdthmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-opszmin.ufo", name="RobotoDelta-opszmin.ufo", location=dict(opsz=-1), styleName="opszmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-opszmax.ufo", name="RobotoDelta-opszmax.ufo", location=dict(opsz=1), styleName="opszmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-PWGTmin.ufo", name="RobotoDelta-PWGTmin.ufo", location=dict(PWGT=-1), styleName="PWGTmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-PWGTmax.ufo", name="RobotoDelta-PWGTmax.ufo", location=dict(PWGT=1), styleName="PWGTmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-PWDTmin.ufo", name="RobotoDelta-PWDTmin.ufo", location=dict(PWDT=-1), styleName="PWDTmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-PWDTmax.ufo", name="RobotoDelta-PWDTmax.ufo", location=dict(PWDT=1), styleName="PWDTmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-POPSmin.ufo", name="RobotoDelta-POPSmin.ufo", location=dict(POPS=-1), styleName="POPSmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-POPSmax.ufo", name="RobotoDelta-POPSmax.ufo", location=dict(POPS=1), styleName="POPSmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-GRADmin.ufo", name="RobotoDelta-GRADmin.ufo", location=dict(GRAD=-1), styleName="GRADmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-GRADmax.ufo", name="RobotoDelta-GRADmax.ufo", location=dict(GRAD=1), styleName="GRADmax", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-YTRAmin.ufo", name="RobotoDelta-YTRAmin.ufo", location=dict(YTRA=-1), styleName="YTRAmin", familyName=familyName, copyInfo=False),
	#dict(path="src/master_ufo/RobotoDelta-YTRAmax.ufo", name="RobotoDelta-YTRAmax.ufo", location=dict(YTRA=1), styleName="YTRAmax", familyName=familyName, copyInfo=False),
]
axes = [
	dict(minimum=-1, maximum=1, default=0, name="XTRA", tag="XTRA", labelNames={"en": "XTRA"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="XOPQ", tag="XOPQ", labelNames={"en": "XOPQ"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YOPQ", tag="YOPQ", labelNames={"en": "YOPQ"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTLC", tag="YTLC", labelNames={"en": "YTLC"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTUC", tag="YTUC", labelNames={"en": "YTUC"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTAS", tag="YTAS", labelNames={"en": "YTAS"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTDE", tag="YTDE", labelNames={"en": "YTDE"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTAD", tag="YTAD", labelNames={"en": "YTAD"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTDD", tag="YTDD", labelNames={"en": "YTDD"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="UDLN", tag="UDLN", labelNames={"en": "UDLN"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="wght", tag="wght", labelNames={"en": "wght"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="wdth", tag="wdth", labelNames={"en": "wdth"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="opsz", tag="opsz", labelNames={"en": "opsz"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="PWGT", tag="PWGT", labelNames={"en": "PWGT"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="PWDT", tag="PWDT", labelNames={"en": "PWDT"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="POPS", tag="POPS", labelNames={"en": "POPS"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="GRAD", tag="GRAD", labelNames={"en": "GRAD"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="YTRA", tag="YTRA", labelNames={"en": "YTRA"}, map=[]),
]

instances = [
]

#for source in sources:
#	instances.append(dict(location=source["location"], styleName=source["styleName"], familyName=source["familyName"]))

### 

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

#doc.checkAxes()

#doc.checkDefault()

doc.write(designSpacePath)
