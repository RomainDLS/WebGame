#    ----> X
#  |
#  |
#  v
#  Y


class Engine:
	def __init__(self, mapSizeX, mapSizeY):
		self._objectList = []
		self._objectIdCount = 0
		self._map = Map(mapSizeX,mapSizeY)

	def addNewObject(self, objectName, isStatic):
		newObject = Object(, y, objectName, objectId)
