#!/usr/bin/env python
#-*- coding: utf-8 -*

#    ----> X
#  |
#  |
#  v
#  Y

class Map:
	def __init__(self,sizeX,sizeY):
		self._sizeX = sizeX
		self._sizeY = sizeY

	def sizeX():
	    doc = "The sizeX property."
	    def fget(self):
	        return self._sizeX
	    return locals()
	sizeX = property(**sizeX())

	def sizeY():
	    doc = "The sizeY property."
	    def fget(self):
	        return self._sizeY
	    return locals()
	sizeY = property(**sizeY())