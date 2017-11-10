a, b = AllFonts()

for glyph in a:
    
    bglyph = b[glyph.name]
    
    for i, contour in enumerate(glyph.contours):
        
        bcontour = bglyph[i]
        
        for j, point in enumerate(contour.points):

            bpoint = bcontour.points[j]
            
            x, y = point.x, point.y
            bx, by = bpoint.x, bpoint.y
            
            if x != bx and y != by:
                
                print glyph
                break
