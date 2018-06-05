from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
from mutatorMath.ufo.document import DesignSpaceDocumentWriter, DesignSpaceDocumentReader

path = u"/Users/david/Documents/Typefaces/Venture/sources/MeritBadge_extra.designspace"
doc = DesignSpaceDocumentReader(path, ufoVersion=2)
doc.process(makeGlyphs=True, makeKerning=True, makeInfo=True)
print 'done'