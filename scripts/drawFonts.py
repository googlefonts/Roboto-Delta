from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath
from defcon import Font
import string

fonts = [
    "../src/1-drawings/RobotoDelta-Regular.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmin-YOPQmin.ufo",
    "../src/1-drawings/test-XOPQmin.ufo",
    "../src/1-drawings/test-YOPQmin.ufo",
    "../src/1-drawings/RobotoDelta-XOPQmax-YOPQmax.ufo",
    "../src/1-drawings/test-XOPQmax.ufo",
    "../src/1-drawings/test-YOPQmax.ufo",
    ]

size(2000, 720)

translate(20, 20)
scale(0.05)

for path in reversed(fonts):
    
    f = Font(path)
    pen = CocoaPen(f)
    
    save()
    for char in string.uppercase.replace("WX", ""):

        pen.path = NSBezierPath.alloc().init()
        glyph = f[char]
        glyph.draw(pen)
        
        drawPath(pen.path)
        
        translate(glyph.width)
    restore()
    
    translate(0, 2000)