#!/usr/bin/env python
#-*- coding: utf-8 -*

class Bounds():
	def __init__(self, maxX, minX, maxY, minY):
		self._minX = minX
		self._maxX = maxX
		self._minY = minY
		self._maxY = maxY

	def reset(self):
		self.minX = 0
		self.maxX = 0
		self.minY = 0
		self.maxY = 0		

	def maxX():
	    doc = "The maxX property."
	    def fget(self):
	        return self._maxX
	    return locals()
	    def fset(self, value):
	        self._maxX = value
	    return locals()
	maxX = property(**maxX())

	def minX():
	    doc = "The minX property."
	    def fget(self):
	        return self._minX
	    def fset(self, value):
	        self._minX = value
	    return locals()
	minX = property(**minX())

	def maxY():
	    doc = "The maxY property."
	    def fget(self):
	        return self._maxY
	    def fset(self, value):
	        self._maxY = value
	    return locals()
	maxY = property(**maxY())

	def minY():
	    doc = "The minY property."
	    def fget(self):
	        return self._minY
	    def fset(self, value):
	        self._minY = value
	    return locals()
	minY = property(**minY())