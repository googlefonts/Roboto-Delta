import os
import subprocess
import shutil
import random
import fontTools
from fontTools.ttLib import TTFont

basePath = os.path.split(os.path.split(__file__)[0])[0]
sourcePath =  os.path.join(basePath, u"fonts/RobotoDelta-VF.ttf")
destPath = os.path.join(basePath, "src/master_ufo")

pathToFontToolsMutator = os.path.join(os.path.split(fontTools.__file__)[0], 'varLib/mutator.py')


locations = {
   'wghtmin': {
    'wght': 300
    },
}


for fontName, thisLocation in locations.items():
    location = thisLocation.copy()
    cmds = ['python', pathToFontToolsMutator, sourcePath]
    for k, v in location.items():
        cmds.append('%s=%s' %(k, v))
    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    tempPath = sourcePath.replace('.ttf', '-instance.ttf')
    print cmds
    f = TTFont(tempPath)
    f['name'].setName(fontName, 6, 1, 0, 0) # Macintosh
    f['name'].setName(fontName, 6, 3, 1, 0x409) # Windows
    f.save(os.path.join(destPath, fontName+'.ttf'))
    os.remove(tempPath)