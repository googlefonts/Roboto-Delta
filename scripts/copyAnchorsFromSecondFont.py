f = CurrentFont()
src = AllFonts()[1]
for g in f:
    srcg = src[g.name]
    existing = []
    for a in g.anchors:
        existing.append(a.name)
    for a in srcg.anchors:
        g.appendAnchor(a.name, (a.x, a.y))