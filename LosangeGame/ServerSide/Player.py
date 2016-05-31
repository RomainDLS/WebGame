#!/usr/bin/env python
#-*- coding: utf-8 -*

import ipdb, time, json
import physicalEngine2D as p

class Player:
	def __init__(self, client, isGlobalView = False):
		self._isGlobalView = isGlobalView
		self._addressIp = client.address[0]
		self._addressClient = client.address[1]
		self._id = None
		self._client = client 
		self._angle = 0
		self._receivedData = False
		self._screenSizeX = 0
		self._screenSizeY = 0
		self._statut = "alive"

	def click(self):
		# ipdb.set_trace(frame=None)
		print "player %d click" %(self._addressClient)

	def setScreenSize(self, screenSizeX, screenSizeY):
		self._screenSizeX = int(float(screenSizeX))
		self._screenSizeY = int(float(screenSizeY))

	def angle(self, angle):
		self._angle = angle

	def id():
	    doc = "The id property."
	    def fget(self):
	        return self._id
	    def fset(self, value):
	    	if self._id is None :
		        self._id = value
	    return locals()
	id = property(**id())

	def statut():
	    doc = "The statut property."
	    def fget(self):
	        return self._statut
	    def fset(self, value):
	        self._statut = value
	    return locals()
	statut = property(**statut())

	def shapeId():
	    doc = "The shapeId property."
	    def fget(self):
	        return self._shapeId
	    def fset(self, value):
	        self._shapeId = value
	    return locals()
	shapeId = property(**shapeId())

	def screenSizeX():
	    doc = "The screenSizeX property."
	    def fget(self):
	        return self._screenSizeX
	    return locals()
	screenSizeX = property(**screenSizeX())

	def screenSizeY():
	    doc = "The screenSizeY property."
	    def fget(self):
	        return self._screenSizeY
	    return locals()
	screenSizeY = property(**screenSizeY())

	def isGlobalView():
	    doc = "The isGlobalView property."
	    def fget(self):
	        return self._isGlobalView
	    def fset(self, value):
	        self._isGlobalView = value
	    return locals()
	isGlobalView = property(**isGlobalView())

	def receivedData():
	    doc = "The receivedData property."
	    def fget(self):
	        return self._receivedData
	    def fset(self, value):
	        self._receivedData = value
	    return locals()
	receivedData = property(**receivedData())

	def angle():
	    doc = "The angle property."
	    def fget(self):
	        return self._angle
	    def fset(self, value):
	        self._angle = value
	    return locals()
	angle = property(**angle())

	def client():
	    doc = "The client property."
	    def fget(self):
	        return self._client
	    return locals()
	client = property(**client())

	def addressClient():
	    doc = "The addressClient property."
	    def fget(self):
	        return self._addressClient
	    return locals()
	addressClient = property(**addressClient())

	def addressIp():
	    doc = "The addressIp property."
	    def fget(self):
	        return self._addressIp
	    return locals()
	addressIp = property(**addressIp())

class GlobalView(Player):
	def __init__(self, client):
		Player.__init__(self,client,True)