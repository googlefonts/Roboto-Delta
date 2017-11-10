from defcon import Font
import os

src = "../src"

fonts = []
for directory in os.listdir(src):
    if directory.endswith(".ufo"):
        path = os.path.join(src, directory)
        fonts.append(Font(path))

base = fonts[0]
fonts = fonts[1:]

print "Default Master", base.path
print

for glyph in base:
    
    baseSegments = []
    for contour in glyph:
        for segment in contour.segments:
            baseSegments.append(segment)
    baseLen = [len(segment) for segment in baseSegments]
    
    baseAnchors = sorted([anchor.name for anchor in glyph.anchors])
        
    for font in fonts:
        
        if glyph.name not in font:
            continue
            
        otherGlyph = font[glyph.name]
        
        otherSegments = []
        for contour in otherGlyph:
            for segment in contour.segments:
                otherSegments.append(segment)
        otherLen = [len(segment) for segment in otherSegments]
        
        otherAnchors = sorted([anchor.name for anchor in otherGlyph.anchors])
        
        if baseLen != otherLen:
            print "!= segments", glyph.name, otherGlyph.getParent().info.styleName
        
        if baseAnchors != otherAnchors:
            print "!= anchors", glyph.name, otherGlyph.getParent().info.styleName
