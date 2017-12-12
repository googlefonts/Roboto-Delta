familyName = "RobotoDelta"
regular = OpenFont("../src/1-drawings/RobotoDelta-Regular.ufo", showUI=False)

xymax = OpenFont("../src/1-drawings/RobotoDelta-XOPQmax-YOPQmax.ufo", showUI=False)
xymin = OpenFont("../src/1-drawings/RobotoDelta-XOPQmin-YOPQmin.ufo", showUI=False)

x_min = NewFont(showUI=False)
x_min.info.familyName = familyName
x_min.info.styleName = "XOPQmin-i"
x_min.interpolate((1, 0), regular, xymin)
x_min.save("../src/1-drawings/RobotoDelta-XOPQmin-i.ufo")

x_max = NewFont(showUI=False)
x_max.info.familyName = familyName
x_max.info.styleName = "XOPQmax-i"
x_max.interpolate((1, 0), regular, xymax)
x_max.save("../src/1-drawings/RobotoDelta-XOPQmax-i.ufo")

y_min = NewFont(showUI=False)
y_min.info.familyName = familyName
y_min.info.styleName = "YOPQmin-i"
y_min.interpolate((0, 1), regular, xymin)
y_min.save("../src/1-drawings/RobotoDelta-YOPQmin-i.ufo")

y_max = NewFont(showUI=False)
y_max.info.familyName = familyName
y_max.info.styleName = "YOPQmax-i"
y_max.interpolate((0, 1), regular, xymax)
y_max.save("../src/1-drawings/RobotoDelta-YOPQmax-i.ufo")
