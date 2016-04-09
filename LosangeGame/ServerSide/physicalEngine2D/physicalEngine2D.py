#!/usr/bin/env python
#-*- coding: utf-8 -*

#    ----> X
#  |
#  |
#  v
#  Y

from object import staticObject, dynamicObject, Object
from map import Map
from collisionManager import CollisionManager
from shape import *
import ipdb

class Engine(object):
	def __init__(self, mapSizeX, mapSizeY):
		self._objectList = {}
		self._objectIdCount = 0
		self._map = Map(mapSizeX,mapSizeY)
		self._collisionManager = CollisionManager()

	def engineStep(self):
		# ipdb.set_trace()
		# self._drawBounds()
		self._collisionManager.reinitializeLists()
		i = 0
		for key in self._objectList:
			obj = self._objectList[key]
			if type(obj) is dynamicObject :
				obj.save()
				obj.updatePosition()
				self._collisionManager.collisionDetection(obj, self._objectList, i)
				# self._objectList[key] = obj.getBackup()
				# 	ipdb.set_trace(frame=None)
			i += 1

		newColList = self._collisionManager.newCollisionList
		endedColList = self._collisionManager.getEndOfCollisions()
		if newColList :
			print 'New Collisions : '
			print newColList
		if endedColList :
			print 'End Of Collisions : '
			print endedColList

	def _drawBounds(self):
		newBounds = []
		for key in self._objectList:
			obj = self._objectList[key]
			if obj.name.split(':')[0] != 'bounds' : 
				name = "bounds:%d" % obj.id
				bounds = obj.shape.bounds()
				shape = Rectangle(bounds.minX, bounds.minY, bounds.maxX - bounds.minX, bounds.maxY - bounds.minY)
				if self.getObjectbyName(name) is not None :
					self.getObjectbyName(name).shape = shape
				else :
					newbound = {}
					newbound['name'] = name
					newbound['shape'] = shape
					newBounds.append(newbound)
		for bounds in newBounds :
			self._objectIdCount += 1
			self.addNewObject(bounds['name'], True, bounds['shape'])

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

	def deleteObjectById(self, objectId):
		for key in self._objectList:
			if self._objectList[key]._id == objectId :
				toDel = key
				break
		del self._objectList[toDel]

	def deleteObject(self, objectId):
		try:
			del self._objectList[objectId]
			# ipdb.set_trace(frame=None)
			boundObjId = self.getObjectbyName(('bounds:%d' % int(float(objectId)))).id
			del self._objectList[boundObjId]
		except KeyError:
			pass

	def getObjectbyId(self, objectId):
		for key in self._objectList:
			if self._objectList[key]._id == objectId :
				return self._objectList[key]
		return None

	def getObjectbyName(self, objectName):
		for key in self._objectList:
			if self._objectList[key]._name == objectName :
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