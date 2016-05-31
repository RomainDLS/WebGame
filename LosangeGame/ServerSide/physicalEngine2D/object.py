#!/usr/bin/env python
#-*- coding: utf-8 -*

#    ----> X
#  |
#  |
#  v
#  Y

from shape import *
from bound import *
import json

class Object(object):
	def __init__(self, objectName, objectId, shape, ObjectType=None):
		self._type = ObjectType
		self._x = shape.x
		self._y = shape.y
		self._name = objectName
		self._id = objectId
		self._shape = shape
		self._isSaved = False
		self._savedObject = self

	def getJsonObject(self, stepX = 0, stepY = 0, player = None):
		jsonObject = {}
		jsonObject['name'] = self._name
		jsonObject['id'] = self._id
		jsonObject['position'] = (self._shape.x - stepX, self._shape.y - stepY)
		#ipdb.set_trace()
		# Object is rectangle
		if type(self._shape) is Rectangle:
			jsonObject['angle'] = self._shape.angle
			jsonObject['type'] = "rectangle"
			jsonObject['params'] = (self._shape.width, self._shape.height)
		# Object is ellispe
		elif type(self._shape) is Ellipse or type(self._shape) is Circle:
			jsonObject['angle'] = self._shape.angle
			jsonObject['type'] = "ellipse"
			jsonObject['params'] = (self._shape.r, self._shape.wX, self._shape.wY)
		# Object is a complexe shape
		else :
			if player is not None :
				jsonObject['statut'] = player.statut
			jsonObject['type'] = "complexe"
			# ipdb.set_trace(frame=None)
			shapeTmp = self._shape
			xTmp = self._shape.x
			yTmp = self._shape.y
			shapeTmp.setPosition(self._shape.x - stepX, self._shape.y - stepY)
			jsonObject['params'] = list(shapeTmp.linkedPoints)
			shapeTmp.setPosition(xTmp, yTmp)
		return jsonObject

	def save(self):
		self._savedObject = Object(self._name, self._id, self._shape)
		self._isSaved = True

	def getBackup(self):
		if self._isSaved is True :
			return self._savedObject

	def setPosition(self, x, y):
		self._shape.setPosition(x,y)
		self._x = self._shape.x
		self._y = self._shape.y

	def rotate(self, angle, center = None):
		self._shape.rotate(angle, center)

	def angle(self, angle):
		self._shape.angle = angle

	def type():
	    doc = "The type property."
	    def fget(self):
	        return self._type
	    def fset(self, value):
	        self._type = value
	    return locals()
	type = property(**type())

	def shape():
	    doc = "The shape property."
	    def fget(self):
	        return self._shape
	    def fset(self, value):
	        self._shape = value
	    return locals()
	shape = property(**shape())

	def name():
	    doc = "The name property."
	    def fget(self):
	        return self._name
	    def fset(self, value):
	        self._name = value
	    return locals()
	name = property(**name())

	def id():
	    doc = "The id property."
	    def fget(self):
	        return self._id
	    return locals()
	id = property(**id())

	def x():
	    doc = "The x property."
	    def fget(self):
	        return self._x
	    return locals()
	x = property(**x())

	def y():
	    doc = "The y property."
	    def fget(self):
	        return self._y
	    return locals()
	y = property(**y())
	

class staticObject(Object):
	def __init__(self, objectName, objectId, shape, ObjectType=None):
		Object.__init__(self,objectName,objectId,shape,ObjectType)

class dynamicObject(Object):
	def __init__(self, objectName, objectId, shape, ObjectType):
		self._speedX = 0
		self._speedY = 0
		self._accelerationX = 0
		self._accelerationY = 0
		self._velocity = 0
		Object.__init__(self,objectName,objectId,shape,ObjectType)

	def updatePosition(self):
		self._x += self._speedX
		self._y += self._speedY
		if self._speedX != 0 or self._speedY != 0:
			self.setPosition(self._x, self._y)
		self._speedX += self._accelerationX
		self._speedY += self._accelerationY
		if self._velocity != 0 :
			self.rotate(self._velocity)

	def speedX():
	    doc = "The speedX property."
	    def fget(self):
	        return self._speedX
	    def fset(self, value):
	        self._speedX = value
	    return locals()
	speedX = property(**speedX())

	def speedY():
	    doc = "The speedY property."
	    def fget(self):
	        return self._speedY
	    def fset(self, value):
	        self._speedY = value
	    return locals()
	speedY = property(**speedY())

	def accelerationX():
	    doc = "The accelerationX property."
	    def fget(self):
	        return self._accelerationX
	    def fset(self, value):
	        self._accelerationX = value
	    return locals()
	accelerationX = property(**accelerationX())

	def accelerationY():
	    doc = "The accelerationY property."
	    def fget(self):
	        return self._accelerationY
	    def fset(self, value):
	        self._accelerationY = value
	    return locals()
	accelerationY = property(**accelerationY())

	def velocity():
	    doc = "The velocity property."
	    def fget(self):
	        return self._velocity
	    def fset(self, value):
	        self._velocity = value
	    return locals()
	velocity = property(**velocity())