from __future__ import division
#    ----> X
#  |
#  |
#  v
#  Y
import ipdb 

def sig(dx):
	if dx > 0 : return 1
	if dx == 0 : return 0
	if dx < 0 : return -1

class Shape(object):
	def __init__(self, pixelList):
		self._pixelList = pixelList

	def pixelList():
	    doc = "The pixelList property."
	    def fget(self):
	        return self._pixelList
	    def fset(self, value):
	        self._pixelList = value
	    return locals()
	pixelList = property(**pixelList())

class simpleShape(Shape):
	def __init__(self, linkedPoints):
		self._linkedPoints = linkedPoints
		pixelList = []
		for line in linkedPoints:
			pixelList.append(self.tryDrawLine(line))
		Shape.__init__(self, pixelList)

		def linkedPoints():
		    doc = "The linkedPoints property."
		    def fget(self):
		        return self._linkedPoints
		    def fset(self, value):
		        self._linkedPoints = value
		    return locals()
		linkedPoints = property(**linkedPoints())

	def newTryDrawLine(self, line):
		ipdb.set_trace()
		pixelList = []
		x0 = line[0][0]
		y0 = line[0][1]
		x1 = line[1][0]
		y1 = line[1][1]
		dx = x1 - x0
		dy = y1 - y0
		D = 2*dy - dx
		pixelList.append((x0,y0))
		y=y0
		if D > 0 :
			y = y + 1
			D -= (2*dx)
		for x in range (x0 + 1, x1 + sig(x1 - x0),sig(x1 - x0)) :
			pixelList.append((x,y))
			D += (2*dx)
			if D > 0 : 
				y += 1
				D -= 2*dx
		return pixelList
	
	def tryDrawLine(self, line):
		ipdb.set_trace()
		pixelList = []
		x0 = line[0][0]
		y0 = line[0][1]
		x1 = line[1][0]
		y1 = line[1][1]
		dx = x1 - x0
		dy = y1 - y0
		error = 0
		derror = abs(dx/dy)
		signDx = sig(dx)
		y = y0
		for x in range (x0,x1 + signDx,signDx) :
			pixelList.append((x,y))
			error = error + derror
			while error >= 0.5 :
				pixelList.append((x,y))
				y = y + sig(dy)
				error -= 1 	
		return pixelList

	def _drawLine(self, line):
		originX = line[0][0]
		originY = line[0][1]
		destinationX = line[1][0]
		destinationY = line[1][1]
		distanceX = destinationX - originX
		distanceY = destinationY - originY
		middleX = int(round(distanceX/2)) + originX
		middleY = int(round(distanceY/2)) + originY
		firstHalfLine = ((originX,originY),(middleX,middleY))
		secondHalfLine = ((destinationX,destinationY),(middleX,middleY))
		firstHalf = self._drawHalfLine(firstHalfLine)
		secondHalf = self._drawHalfLine(secondHalfLine)
		ipdb.set_trace()
		return firstHalf + secondHalf

	def _drawHalfLine(self, line):
		ipdb.set_trace()
		pixelList = []
		if(line[0][0] > line[1][0]):
			originX = line[1][0]
			originY = line[1][1]
			destinationX = line[0][0]
			destinationY = line[0][1]
		else :
			originX = line[0][0]
			originY = line[0][1]
			destinationX = line[1][0]
			destinationY = line[1][1]
		distanceX = destinationX - originX
		distanceY = destinationY - originY
		if distanceX == 0 or distanceY == 0 :			
			pixelList.append((originX,originY))
			return pixelList
		
		previousY = originY
		for x in range (originX, destinationX+1):
			y = originY + distanceY * (x - originX) / distanceX
			y = int(round(y))+1
			if(previousY>y):
				startY = y
				endY = previousY
			else :
				startY = previousY
				endY = y
			if (startY == endY) :
				pixelList.append((x,y))
			else : 
				for y in range (startY,endY):
					pixelList.append((x,y))
			previousY = y 
		return pixelList

class Rectangle(simpleShape):
	def __init__(self, width, height):
		#ipdb.set_trace()
		linkedPoints = []
		linkedPoints.append(((0,0),(width,0)))
		linkedPoints.append(((width,0),(width,height)))
		linkedPoints.append(((width,height),(0,height)))
		linkedPoints.append(((width,height),(0,0)))
		simpleShape.__init__(self, linkedPoints)