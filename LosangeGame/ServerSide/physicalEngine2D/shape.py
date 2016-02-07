#    ----> X
#  |
#  |
#  v
#  Y

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
			pixelList.append(self._drawLine(line))
		Shape.__init__(self, pixelList)
			

	def _drawLine(self, line):
		pixelList = []
		originX = line[0][0]
		originY = line[0][1]
		destinationX = line[1][0]
		destinationY = line[1][1]
		distanceX = destinationX - originX
		distanceY = destinationY - originY
		for x in range (originX, destinationX):
			y = originY + distanceY * (x - originX) / distanceX
			pixelList.append((x,y))
		return pixelList

class Rectangle(simpleShape):
	def __init__(self, width, height):
		linkedPoints = []
		linkedPoints.append(((0,0),(width,0)))
		linkedPoints.append(((width,0),(width,height)))
		linkedPoints.append(((width,height),(0,height)))
		linkedPoints.append(((width,height),(0,0)))
		simpleShape.__init__(self, linkedPoints)