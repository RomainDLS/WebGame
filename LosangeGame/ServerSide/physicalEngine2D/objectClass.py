#    ----> X
#  |
#  |
#  v
#  Y


class Object(object):
	def __init__(self, x, y, objectName, objectId):
		self._x = x
		self._y = y
		self._name = objectName
		self._id = objectId

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
	    def fset(self, value):
	        self._x = value
	    return locals()
	x = property(**x())

	def y():
	    doc = "The y property."
	    def fget(self):
	        return self._y
	    def fset(self, value):
	        self._y = value
	    return locals()
	y = property(**y())
	

class staticObject(Object):
	def __init__(self, x, y, objectName, objectId):
		Object.__init__(x,y,objectName,objectId)

	def updatePosition(self, x, y):
		self._x = x
		self._y = y


class dynamicObject(Object):
	def __init__(self, x, y, objectName, objectId):
		self._speedX = 0
		self._speedY = 0
		self._accelerationX = 0
		self._accelerationY = 0
		Object.__init__(x,y,objectName,objectId)


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

	def x():
	    doc = "The x property."
	    def fget(self):
	        return self._x
	    def fset(self, value):
	        self._x = value
	    return locals()
	x = property(**x())

	def y():
	    doc = "The y property."
	    def fget(self):
	        return self._y
	    def fset(self, value):
	        self._y = value
	    return locals()
	y = property(**y())
