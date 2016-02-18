#!/usr/bin/env python
#-*- coding: utf-8 -*

#    ----> X
#  |
#  |
#  v
#  Y

from object import staticObject, dynamicObject, Object
from map import Map
from shape import *

class Engine(object):
	def __init__(self, mapSizeX, mapSizeY):
		self._objectList = []
		self._objectIdCount = 0
		self._map = Map(mapSizeX,mapSizeY)

	def addNewObject(self, objectName, isStatic, shape):
		self._objectIdCount += 1
		if isStatic :
			newObject = staticObject(objectName, self._objectIdCount, shape)
		else : 
			newObject = dynamicObject(objectName, self._objectIdCount, shape)
		self._objectList.append(newObject)
		return newObject

	def getObjectbyId(self, objectId):
		for singleObject in self._objectList:
			if singleObject._id == objectId :
				return singleObject
		return None

	def objectList():
	    doc = "The objectList property."
	    def fget(self):
	        return self._objectList
	    return locals()
	objectList = property(**objectList())

	def map():
	    doc = "The map property."
	    def fget(self):
	        return self._map
	    return locals()
	map = property(**map())