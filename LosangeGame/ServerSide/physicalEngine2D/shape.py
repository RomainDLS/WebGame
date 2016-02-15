from __future__ import division
import math
import ipdb

#  (X,Y)
#    ----> X
#  |
#  |
#  v
#  Y

CIRCLE_DRAWING_PRECISION = 24			#range from 1 to 90, smaller is morer precise

def sig(dx):
	if dx > 0 : return 1
	if dx == 0 : return 0
	if dx < 0 : return -1

class Shape(object):
	def __init__(self, linkedPoints):
		self._linkedPoints = linkedPoints
		self._nbPoints = len(linkedPoints)
		self._centroid = self.getCentroid()

	def getCentroid(self):
		sumX = 0
		sumY = 0
		nbP = self._nbPoints
		for i in range (0, nbP):
			sumX += self._linkedPoints[i][0]
			sumY += self._linkedPoints[i][1]
		return (sumX/nbP, sumY/nbP)

	def rotate(self, angle, center = None):
		nbP = self._nbPoints
		if center is None:
			center = self.centroid
		for i in range (0, nbP):
			point = self._linkedPoints[i]
			self._linkedPoints[i] = self.rotatePoint(point, center, angle)

	def rotatePoint (self, Point, Center, Angle):
		Angle = Angle*math.pi/180
		x = Point[0]
		y = Point[1]
		Cx = Center[0]
		Cy = Center[1]
		rotatedPointX = math.cos(Angle)*(x-Cx)-math.sin(Angle)*(y-Cy) + Cx
		rotatedPointY = math.sin(Angle)*(x-Cx)+math.cos(Angle)*(y-Cy) + Cy
		return (rotatedPointX,rotatedPointY)

	def getAngle(self, radius, width):
		return math.acos(width/radius) * 180 / math.pi

	def centroid():
	    doc = "The centroid property."
	    def fget(self):
	        return self._centroid
	    return locals()
	centroid = property(**centroid())

	def linkedPoints():
	    doc = "The linkedPoints property."
	    def fget(self):
	        return self._linkedPoints
	    def fset(self, value):
	    	if type(value) is not dict:
	    		raise Exception("type of linkedPoints is not dict")
	    	self._linkedPoints = value
	    return locals()

	def circleDrawingPrecision():
	    doc = "The circleDrawingPrecision property."
	    def fget(self):
	        return self._circleDrawingPrecision
	    def fset(self, value):
	    	if value > 90 or value < 0:
	    		raise Exception("circleDrawingPrecision : range from 1 to 90")
	        self._circleDrawingPrecision = value
	    return locals()
	circleDrawingPrecision = property(**circleDrawingPrecision())
	linkedPoints = property(**linkedPoints())

class Rectangle(Shape):
	def __init__(self, x, y, width, height):
		#ipdb.set_trace()
		linkedPoints = {}
		linkedPoints[0] = (x,y)
		linkedPoints[1] = (x + width, y)
		linkedPoints[2] = (x + width,y + height)
		linkedPoints[3] = (x,y + height)
		Shape.__init__(self, linkedPoints)

class Ellipse(Shape):
	def __init__(self, x, y, r, wX, wY):
		self._x = x
		self._y = y
		self._r = r
		linkedPoints = {}
		count = 0
		for i in range (0, 360, CIRCLE_DRAWING_PRECISION):
			pointX = x + wX * r * math.cos(math.radians(i))
			pointY = y + wY * r * math.sin(math.radians(i))
			linkedPoints[count] = (int(round(pointX)), int(round(pointY)))
			count += 1
		Shape.__init__(self, linkedPoints)

class Circle(Ellipse):
	def __init__(self, x, y, r):
		Ellipse.__init__(self, x, y, r, 1, 1)