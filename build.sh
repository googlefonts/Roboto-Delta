# build the master_ttf_interpolatable from the master_ufo
fontmake -o ttf-interpolatable -m RobotoDelta.designspace --no-production-names
# build the variable font from the designspace
fonttools varLib RobotoDelta.designspace
# move the variable font to the fonts directory
mv RobotoDelta-VF.ttf fonts/RobotoDelta-VF.ttf