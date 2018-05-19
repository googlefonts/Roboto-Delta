from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
from mutatorMath.ufo.document import DesignSpaceDocumentWriter, DesignSpaceDocumentReader

path = u"/Users/david/Documents/Type_Network/Roboto-Delta/src/_RobotoDelta-newMasters.designspace"
doc = DesignSpaceDocumentReader(path, ufoVersion=2)
doc.process(makeGlyphs=True, makeKerning=True, makeInfo=True)
print 'done'