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
import ipdb

class Engine(object):
	def __init__(self, mapSizeX, mapSizeY):
		self._objectList = {}
		self._objectIdCount = 0
		self._map = Map(mapSizeX,mapSizeY)

	def engineStep(self):
		#ipdb.set_trace()
		for key in self._objectList:
			obj = self._objectList[key]
			if type(obj) is dynamicObject :
				obj.updatePosition()

	def addNewObject(self, objectName, isStatic, shape, objectId=None):
		if objectId is None :
			self._objectIdCount += 1
			objectId = self._objectIdCount
		if isStatic :
			newObject = staticObject(objectName, objectId, shape)
		else : 
			newObject = dynamicObject(objectName, objectId, shape)
		self._objectList[objectId] = (newObject)
		return newObject

	def deleteObject(self, objectId):
		try:
			del self._objectList[objectId]
		except KeyError:
			pass

	def getObjectbyId(self, objectId):
		for key in self._objectList:
			if self._objectList[key]._id == objectId :
				return self._objectList[key]
		return None

	def objectList():
	    doc = "The objectList property."
	    def fget(self):
	    	objList = []
	    	for key in self._objectList:
	    		objList.append(self._objectList[key])
	        return objList
	    return locals()
	objectList = property(**objectList())

	def objectDict():
	    doc = "The objectDict property."
	    def fget(self):
	        return self._objectList
	    return locals()
	objectDict = property(**objectDict())

	def map():
	    doc = "The map property."
	    def fget(self):
	        return self._map
	    return locals()
	map = property(**map())