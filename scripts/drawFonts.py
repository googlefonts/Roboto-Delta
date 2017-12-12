from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath
from defcon import Font
import string

"""
fonts = [
    "../src/1-drawings/RobotoDelta-Regular.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmin-YOPQmin.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmin-i.ufo",
    "../src/1-drawings/RobotoDelta-YOPQmin-i.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmax-YOPQmax.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmax-i.ufo",
    "../src/1-drawings/RobotoDelta-YOPQmax-i.ufo",
    ]
"""

fonts = [
    "../src/1-drawings/RobotoDelta-XOPQmin-YOPQmin.ufo",
    "old-duovars/XOPQminYOPQmin.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmax-YOPQmax.ufo",
    "old-duovars/XOPQmaxYOPQmax.ufo",
    "../src/1-drawings/RobotoDelta-XTRAmin.ufo",
    "old-duovars/XTRAmin.ufo",
    ]

size(2100, 625)

translate(25, 25)
scale(0.05)

for path in reversed(fonts):
    
    f = Font(path)
    pen = CocoaPen(f)
    
    save()
    for char in string.uppercase:

        pen.path = NSBezierPath.alloc().init()
        glyph = f[char]
        glyph.draw(pen)
        
        drawPath(pen.path)
        
        translate(glyph.width)
    restore()
    
    translate(0, 2000)
saveImage(["drawFonts.pdf"])