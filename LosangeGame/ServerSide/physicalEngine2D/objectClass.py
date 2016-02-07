#    ----> X
#  |
#  |
#  v
#  Y


class Object:
	def __init__(self, x, y, objectName, objectId):
		self._x = x
		self._y = y

class staticObject(Object):

class dynamicObject(Object):
	def __init__(self, x, y, objectName, objectId):
		self._x = x
		self._y = y
		self._speedX = 0
		self._speedY = 0
		self._accelerationX = 0
		self._accelerationY = 0

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
