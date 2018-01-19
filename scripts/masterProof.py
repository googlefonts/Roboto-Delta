from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath
from defcon import Font
import os

master_dir = "../src/1-drawings"
master_dir = "../src/master_ufo"

ufos = [
	"RobotoDelta-Regular.ufo",
	
	"RobotoDelta-XOPQmin.ufo",
	"RobotoDelta-XOPQmax.ufo",
	"RobotoDelta-YOPQmin.ufo",
	"RobotoDelta-YOPQmax.ufo",
	"RobotoDelta-XOPQmin-YOPQmin.ufo",
	"RobotoDelta-XOPQmax-YOPQmax.ufo",
	
	"RobotoDelta-XTRAmin.ufo",
	"RobotoDelta-XTRAmax.ufo",
	"RobotoDelta-XOPQmin-YOPQmin-XTRAmin.ufo",
	"RobotoDelta-XOPQmin-YOPQmin-XTRAmax.ufo",

	"RobotoDelta-wghtmin.ufo",
	"RobotoDelta-wghtmax.ufo",

	"RobotoDelta-wdthmin.ufo",
	"RobotoDelta-wdthmax.ufo",
	
	"RobotoDelta-opszmin.ufo",
	"RobotoDelta-opszmax.ufo",

	"RobotoDelta-YTASmin.ufo",
	"RobotoDelta-YTASmax.ufo",
	
	"RobotoDelta-YTDEmin.ufo",
	"RobotoDelta-YTDEmax.ufo",

	"RobotoDelta-YTLCmin.ufo",
	"RobotoDelta-YTLCmax.ufo",

	"RobotoDelta-YTUCmin.ufo",
	"RobotoDelta-YTUCmax.ufo",
	
	"RobotoDelta-YTRAmin.ufo",
	"RobotoDelta-YTRAmax.ufo",
	
	"RobotoDelta-YTADmin.ufo",
	"RobotoDelta-YTADmax.ufo",

	"RobotoDelta-YTDDmin.ufo",
	"RobotoDelta-YTDDmax.ufo",
	
	"RobotoDelta-UDLNmin.ufo",
	"RobotoDelta-UDLNmax.ufo",
	
	"RobotoDelta-GRADmin.ufo",
	"RobotoDelta-GRADmax.ufo",
]

m = 100
c = 50
for ufo in ufos:
    newPage(1000, 1000)
    fontobject = Font(os.path.join(master_dir, ufo))
    pen = CocoaPen(fontobject)
    x = m
    fontSize(12)
    font("Menlo")
    text(ufo, (x, m))
    translate(m, height()-m)
    save()
    for glyphName in fontobject.glyphOrder:
        if glyphName in fontobject:
            glyph = fontobject[glyphName]
            pen.path = NSBezierPath.bezierPath()    
            glyph.draw(pen)
            save()
            scale(0.015)
            drawPath(pen.path)
            restore()
            translate(c)
            x += c
        if x >= width()-m:
            restore()
            x = m
            translate(0, -c)
            save()
    restore()
			#if glyph.unicode:
			#	char = unichr(glyph.unicode)
			#	print "<div>%s</div>" % char