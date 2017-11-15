glyphSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

from defcon import Font
import os

src = "../src/1-drawings"

fonts = []
for directory in os.listdir(src):
    if directory.endswith(".ufo"):
        path = os.path.join(src, directory)
        fonts.append(Font(path))

base = fonts[0]
fonts = fonts[1:]

print "Default Master", base.path
print "..."

for font in fonts:

    for glyphName in glyphSet:
    
        glyph = base[glyphName]
            
        if glyphName not in font:
            continue
            
        otherGlyph = font[glyphName]
        
        if glyph.leftMargin != otherGlyph.leftMargin:
            print font.info.styleName, glyphName, "LEFT", glyph.leftMargin - otherGlyph.leftMargin
        if glyph.rightMargin != otherGlyph.rightMargin:
            print font.info.styleName, glyphName, "right", glyph.rightMargin - otherGlyph.rightMargin
    print
            