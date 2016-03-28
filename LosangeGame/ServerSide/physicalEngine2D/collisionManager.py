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

class CollisionManager(object):
	def __init__(self):
		self._collisionList = []
		self._oldCollisionList = []
		self._newCollisionList = []
		self._numberOfCollisions = 0

	def collisionDetection(self, objectCible, objectList, objectCount):
		# ipdb.set_trace(frame=None)
		objectBounds = objectCible.shape.bounds()
		# for key in objectList:
		for i in range (objectCount, len(objectList)):
			key = objectList.keys()[i]
			obj = objectList[key]
			if obj.name.split(':')[0] != 'bounds' and obj != objectCible : 
				bounds = obj.shape.bounds()
				check1 = bounds.minX <= objectBounds.maxX <= bounds.maxX
				check2 = bounds.minX <= objectBounds.minX <= bounds.maxX
				check3 = bounds.minY <= objectBounds.maxY <= bounds.maxY
				check4 = bounds.minY <= objectBounds.minY <= bounds.maxY
				check5 = objectBounds.minX <= bounds.maxX <= objectBounds.maxX
				check6 = objectBounds.minX <= bounds.minX <= objectBounds.maxX
				check7 = objectBounds.minY <= bounds.maxY <= objectBounds.maxY
				check8 = objectBounds.minY <= bounds.minY <= objectBounds.maxY
				if (check1 or check2 or check5 or check6) and (check3 or check4 or check7 or check8) :
					self._numberOfCollisions += 1
					self._addNewCollision(obj, objectCible)
					# ipdb.set_trace(frame=None)
					# print 'probable collision : ' + obj.name + ' - ' + objectCible.name + " number : " + str(self._numberOfCollisions)

	def reinitializeLists(self):
		self._oldCollisionList = list(self._collisionList)
		del self._collisionList[:]
		del self._newCollisionList[:]

	def _addNewCollision(self, object1, object2):
		# ipdb.set_trace(frame=None)
		collision = (object1,object2)
		self._collisionList.append(collision)
		isNew = True
		for oldCollision in self._oldCollisionList :
			if collision == oldCollision :
				isNew = False
		if isNew :
			self._newCollisionList.append(collision)

	def getEndOfCollisions(self):
		endOfCollisionsList = []
		for oldCollision in self._oldCollisionList :
			isEnded = True
			for collision in self._collisionList :
				if oldCollision == collision :
					isEnded = False
			if isEnded :
				endOfCollisionsList.append(oldCollision)
		return endOfCollisionsList

	def numberOfCollisions():
	    doc = "The numberOfCollisions property."
	    def fget(self):
	        return self._numberOfCollision
	    return locals()
	numberOfCollisions = property(**numberOfCollisions())

	def newCollisionList():
	    doc = "The newCollisionList property."
	    def fget(self):
	        return self._newCollisionList
	    return locals()
	newCollisionList = property(**newCollisionList())

	def collisionList():
	    doc = "The collisionList property."
	    def fget(self):
	        return self._collisionList
	    return locals()
	collisionList = property(**collisionList())