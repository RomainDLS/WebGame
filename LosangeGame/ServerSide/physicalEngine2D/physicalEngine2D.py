#    ----> X
#  |
#  |
#  v
#  Y

from objectClass import staticObject, dynamicObject, Object
from mapClass import Map

class Engine(object):
	def __init__(self, mapSizeX, mapSizeY):
		self._objectList = []
		self._objectIdCount = 0
		self._map = Map(mapSizeX,mapSizeY)

	def addNewObject(self, objectName, isStatic):
		self._objectIdCount += 1
		if isStatic :
			newObject = staticObject(0,0, objectName, self._objectIdCount)
		else : 
			newObject = dynamicObject(0,0, objectName, self._objectIdCount)
		self._objectList.append(newObject)
		return self._objectIdCount

	def getOObjectbyId(self, objectId):
		for singleObject in self._objectList:
			if singleObject._id == objectId :
				return singleObject
		return None