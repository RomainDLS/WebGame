#    ----> X
#  |
#  |
#  v
#  Y

from shape import *
import json

class Object(object):
	def __init__(self, objectName, objectId, shape):
		self._x = shape.x
		self._y = shape.y
		self._name = objectName
		self._id = objectId
		self._shape = shape

	def getJsonObject(self):
		jsonObject = {}
		jsonObject['name'] = self._name
		jsonObject['position'] = (self._shape.x,self._shape.y)
		#ipdb.set_trace()
		# Object is rectangle
		if type(self._shape) is Rectangle:
			jsonObject['angle'] = self._shape.angle
			jsonObject['type'] = "rectangle"
			jsonObject['params'] = (self._shape.width,self._shape.height)
		# Object is ellispe
		elif type(self._shape) is Ellipse or type(self._shape) is Circle:
			jsonObject['angle'] = self._shape.angle
			jsonObject['type'] = "ellipse"
			jsonObject['params'] = (self._shape.r,self._shape.wX,self._shape.wY)
		# Object is a complexe shape
		else :
			jsonObject['type'] = "complexe"
			jsonObject['params'] = self._shape.linkedPoints
		return jsonObject

	def setPosition(self, x, y):
		self._shape.setPosition(x,y)
		self._x = self._shape.x
		self._y = self._shape.y

	def rotate(self, angle, center = None):
		self._shape.rotate(angle, center)

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
	def __init__(self, objectName, objectId,shape):
		Object.__init__(self,objectName,objectId,shape)

class dynamicObject(Object):
	def __init__(self, objectName, objectId, shape):
		self._speedX = 0
		self._speedY = 0
		self._accelerationX = 0
		self._accelerationY = 0
		Object.__init__(self,objectName,objectId,shape)

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
	    def fdel(self):
	        del self._accelerationY
	    return locals()
	accelerationY = property(**accelerationY())