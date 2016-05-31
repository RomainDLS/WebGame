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
import math

def CollisionHandlerFunction(object1, object2):
	"""
          Called when collision is detected.
    """
	pass

class CollisionManager(object):
	def __init__(self, CollisionHandler = None):
		self._collisionList = []
		self._oldCollisionList = []
		self._newCollisionList = []
		self._numberOfCollisions = 0
		self.collisionHandler = CollisionHandler

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
					if self._isCollisioned(obj,objectCible):
						if self.collisionHandler is not None :
							self.collisionHandler(obj, objectCible)
						else :
							self._addNewCollision(obj, objectCible)
					# ipdb.set_trace(frame=None)
					# print 'probable collision : ' + obj.name + ' - ' + objectCible.name + " number : " + str(self._numberOfCollisions)

	def _isCollisioned(self, object1, object2):
		if type(object1.shape) is not Ellipse and type(object2.shape) is not Ellipse :
			return self.SAT(object1.shape.linkedPoints,object2.shape.linkedPoints)
		else :
			# handle ellipses objects
			ipdb.set_trace(frame=None)

	def SAT(self, shape1, shape2):
		vectorList1 = self.getVectorList(shape1)
		vectorList2 = self.getVectorList(shape2)
		for vector in vectorList1 :
			normalVector = (-vector[1], vector[0])
			Overling = self.checkOverlapping(shape1, shape2, normalVector)
			if not Overling :
				return False
		for vector in vectorList2 :
			normalVector = (-vector[1], vector[0])
			Overling = self.checkOverlapping(shape1, shape2, normalVector)
			if not Overling :
				return False
		# ipdb.set_trace(frame=None)
		return True

	# check Overlapping following vector 
	def checkOverlapping(self, shape1, shape2, vector):
		firstValue = self.valueOnSeparatingAxis(shape1[0], shape2[0], vector)
		mini1 = firstValue
		maxi1 = firstValue
		for point in shape1 :
			value = self.valueOnSeparatingAxis(point, shape2[0], vector)
			if value < mini1 :
				mini1 = value
			if value > maxi1 :
				maxi1 = value
		firstValue = self.valueOnSeparatingAxis(shape2[0], shape2[0], vector)
		mini2 = firstValue
		maxi2 = firstValue
		for point in shape2 :
			value = self.valueOnSeparatingAxis(point, shape2[0], vector)
			if value < mini2 :
				mini2 = value
			if value > maxi2 :
				maxi2 = value
		if mini2 < mini1 < maxi2 or mini2 < maxi1 < maxi2 :
			return True
		else :
			return False

	def getVectorList(self, shape):
		vectorList = []
		i = 0
		for point in shape:
			if point is shape[-1]:
				vectorList.append((shape[0][0] - point[0],shape[0][1] - point[1]))
			else :
				vectorList.append((shape[i+1][0] - point[0],shape[i+1][1] -point[1]))
			i += 1
		return vectorList
	# retourne une valeur égale à la distance entre l'origin et l'image du point suivant le vecteur vector
	def valueOnSeparatingAxis(self, point, origin, vector):
		if point[0] > origin[0] :
			dX = point[0] - origin[0]
		else :
			dX = origin[0] - point[0]
		if point[1] > origin[1] :
			dY = point[1] - origin[1]
		else :
			dY = origin[1] - point[1]
		# D : distance point - origin
		distanceOP = math.sqrt(dX**2 + dY**2)
		# Vecteur origin -> point
		vectorOP = ((point[0] - origin[0]),(point[1] - origin[1]))
		# Angle : Point - Origin - vector
		arcAngleOPV = self._getArcAngle(vectorOP, vector)

		return (distanceOP * arcAngleOPV)

	# We can get the angle of to vectors v1 & v2 by doing : math.acos(self._getCosAngle(v1,v2))
	def _getArcAngle(self, v1, v2):
		x1 = v1[0]
		x2 = v2[0]
		y1 = v1[1]
		y2 = v2[1]
		if (x1*x2 + y1*y2) != 0:
			angle = (x1*x2 + y1*y2)/(math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2))
		else :
			angle = 0
		return angle

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