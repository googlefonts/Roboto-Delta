from itertools import product, izip
# http://stackoverflow.com/questions/5228158/cartesian-product-of-a-dictionary-of-lists
def my_product(dicts):
    return (dict(izip(dicts, x)) for x in product(*dicts.itervalues()))


segoe = installFont(u"../fonts/RobotoDelta-VF.ttf")

locations = {
    "wght": [100, 400, 900],
    "wdth": [75, 100, 125],
    "opsz": [8, 12, 36],
}

my_locations = []
for item in my_product(locations):
    my_locations.append(item)

characters = u"the quick brown fox jumps over the lazy dog"
   
m = 100
for loc in my_locations:
    newPage(1000, 500)
    fontSize(12)
    font("Menlo")
    text(str(loc), (50, 50))
    
    fontSize(36)
    font(segoe)
    fontVariations(**loc)
    textBox(characters.upper(), (m, m, width()-m*2, height()-m*2))
    textBox(characters, (m, m, width()-m*2, height()-m*3))
    textBox("0123456789", (m, m, width()-m*2, height()-m*4))

saveImage("27locations.pdf")