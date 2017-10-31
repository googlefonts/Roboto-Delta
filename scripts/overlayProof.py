from fontTools.pens.cocoaPen import CocoaPen
from AppKit import NSBezierPath
from fontParts.world import OpenFont

fontA = OpenFont("Roboto-Regular.ufo", showInterface=False)
fontB = OpenFont("../src/RobotoDelta-Regular.ufo", showInterface=False)

def drawGlyph(pen, glyph):
    save()
    stroke(None)
    fill(0)
    pen.path = NSBezierPath.bezierPath()
    glyph.draw(pen)
    drawPath(pen.path)
    restore()
    
def drawOutline(pen, glyph, color, s):
    save()
    strokeWidth(1/s)
    stroke(*color)
    fill(None)
    pen.path = NSBezierPath.bezierPath()
    glyph.draw(pen)
    drawPath(pen.path)
    restore()

def drawMetrics(glyph, color, s=1):
    save()
    fill(None)
    stroke(*color)
    strokeWidth(1/s)
    parent = glyph.getParent()
    rect(0, parent.info.descender, glyph.width, parent.info.ascender-parent.info.descender)
    line((0, 0), (glyph.width, 0))
    line((0, parent.info.xHeight), (glyph.width, parent.info.xHeight))
    line((0, parent.info.capHeight), (glyph.width, parent.info.capHeight))
    restore()
    
w, h = 1440, 900
s = 0.25
red = (1, 0, 0)
blue = (0, 0, 1)
margin = 50

#glyphSet = ["A", "B", "C"]
glyphSet = fontB.glyphOrder

for glyphName in glyphSet:
    
    if glyphName not in fontA or glyphName not in fontB:
        continue
    
    glyphA = fontA[glyphName]
    glyphB = fontB[glyphName]
    
    if len(glyphB) == 0:
        continue
    
    glyphA.decompose()
    glyphB.decompose()
    
    penA = CocoaPen(fontA)
    penB = CocoaPen(fontB)

    nameA = " ".join([fontA.info.familyName, fontA.info.styleName])
    nameB = " ".join([fontB.info.familyName, fontB.info.styleName])

    widthDiff = glyphB.width-glyphA.width
    yoffset = abs(min(glyphA.getParent().info.descender, glyphB.getParent().info.descender))

    newPage(w, h)
    save()
    translate(margin, height()-margin)
    fontSize(12)
    text(nameA+"\n"+glyphName, (0, 0))
    translate(margin+glyphA.width*s)
    text(nameB+"\n"+glyphName, (0, 0))
    translate(margin+glyphB.width*s)
    fs = FormattedString(txt="Width ")
    fs.append(str(glyphA.width)+" ", fill=red)
    fs.append(str(glyphB.width)+" ", fill=blue)
    fs.append(str(widthDiff), fill=0)
    text(fs, (0, 0))
    restore()

    save()
    scale(s)

    translate(margin/s, margin/s+yoffset)
    drawMetrics(glyphA, red, s)
    drawOutline(penA, glyphA, red, s)

    translate(glyphA.width+margin/s)
    drawMetrics(glyphB, blue, s)
    drawOutline(penB, glyphB, blue, s)

    translate(glyphB.width+margin/s)
    drawMetrics(glyphA, red, s)
    drawOutline(penA, glyphA, red, s)

    translate(-widthDiff/2, 0)
    drawMetrics(glyphB, blue, s)
    drawOutline(penB, glyphB, blue, s)
    
    restore()

    newPage(w, h)
    save()
    translate(margin, height()-margin)
    fontSize(12)
    text(nameA+"\n"+glyphName, (0, 0))
    translate(margin+glyphA.width*s)
    text(nameB+"\n"+glyphName, (0, 0))
    restore()

    save()
    scale(s)

    translate(margin/s, margin/s+yoffset)
    drawGlyph(penA, glyphA)

    translate(glyphA.width+margin/s)
    drawGlyph(penB, glyphB)

    restore()

saveImage(["overlayProof.pdf"])

