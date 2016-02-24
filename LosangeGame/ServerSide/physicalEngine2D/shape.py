#!/usr/bin/env python
#-*- coding: utf-8 -*

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
	def __init__(self, linkedPoints, angle = 0):
		self._linkedPoints = linkedPoints
		self._nbPoints = len(linkedPoints)
		self._centroid = self.getCentroid()
		self._angle = float(angle)

	def getCentroid(self):
		sumX = 0
		sumY = 0
		nbP = self._nbPoints
		for i in range (0, nbP):
			sumX += self._linkedPoints[i][0]
			sumY += self._linkedPoints[i][1]
		return (sumX/nbP, sumY/nbP)

	def rotate(self, angle, center = None):
		self._angle += angle
		if self._angle >= 360 :
			self._angle = self._angle % 360
		nbP = self._nbPoints
		if center is None:
			center = self.centroid
		#try optimized for
		for i in range (0, nbP):
			point = self._linkedPoints[i]
			self._linkedPoints[i] = self._rotatePoint(point, center, angle)

	def _rotatePoint (self, Point, Center, Angle):
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

	def setPosition(self, x, y):
		#ipdb.set_trace()
		dx = self._centroid[0] - x
		dy = self._centroid[1] - y
		for i in range (0, self._nbPoints) :
			self._linkedPoints[i] = (self._linkedPoints[i][0] + dx, self._linkedPoints[i][1] + dy)
		self._centroid = (x, y)

	def angle():
	    doc = "The angle property."
	    def fget(self):
	        return self._angle
	    def fset(self, value, center = None):
	    	rotationToDo = float(value) - float(self._angle)
	    	self.rotate(rotationToDo, center)
	        self._angle = float(value)
	    return locals()
	angle = property(**angle())

	def x():
	    doc = "The x property."
	    def fget(self):
	        return self._centroid[0]
	    return locals()
	x = property(**x())

	def y():
	    doc = "The y property."
	    def fget(self):
	        return self._centroid[1]
	    return locals()
	y = property(**y())

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
	    	if type(value) is not list:
	    		raise Exception("type of linkedPoints is not list")
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
		linkedPoints = []
		linkedPoints.append((x,y))
		linkedPoints.append((x + width, y))
		linkedPoints.append((x + width,y + height))
		linkedPoints.append((x,y + height))
		self._x = x
		self._y = y
		self._width = width
		self._height = height
		Shape.__init__(self, linkedPoints)

	def width():
	    doc = "The width property."
	    def fget(self):
	        return self._width
	    return locals()
	width = property(**width())

	def height():
	    doc = "The height property."
	    def fget(self):
	        return self._height
	    return locals()
	height = property(**height())

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

class Ellipse(Shape):
	def __init__(self, x, y, r, wX, wY, angle = 0):
		self._r = r
		self._wX = wX
		self._wY = wY
		linkedPoints = []
		for i in range (0, 360, CIRCLE_DRAWING_PRECISION):
			pointX = x + wX * r * math.cos(math.radians(i))
			pointY = y + wY * r * math.sin(math.radians(i))
			linkedPoints.append((int(round(pointX)), int(round(pointY))))
		Shape.__init__(self, linkedPoints, angle)

	def wX():
	    doc = "The wX property."
	    def fget(self):
	        return self._wX
	    return locals()
	wX = property(**wX())

	def wY():
	    doc = "The wY property."
	    def fget(self):
	        return self._wY
	    return locals()
	wY = property(**wY())

	def r():
	    doc = "The r property."
	    def fget(self):
	        return self._r
	    return locals()
	r = property(**r())

class Circle(Ellipse):
	def __init__(self, x, y, r):
		Ellipse.__init__(self, x, y, r, 1, 1)