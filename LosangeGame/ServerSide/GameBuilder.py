#!/usr/bin/env python
#-*- coding: utf-8 -*

import ipdb, time, json
import physicalEngine2D as p

class Player:
	def __init__(self, client):
		self._isGlobalView = False
		self._addressIp = client.address[0]
		self._addressClient = client.address[1]
		self._client = client 
		self._angle = 0
		self._receivedData = False

	def angle(self, angle):
		self._angle = angle

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

class Game:
	def __init__(self):
		self._playerList = []
		self._gameProcessing = p.Engine(1000,600)
		rectangle = self._gameProcessing.addNewObject("rectangle",True,p.Rectangle(5,5,10,10))
		circle = self._gameProcessing.addNewObject("circle",False, p.Ellipse(50, 50, 10, 1, 2, 45))

	def step(self):
		timeStep = time.time()
		self._gameProcessing.objectList[1].rotate(2)
		return time.time() - timeStep	

	def append(self, player):
		#ipdb.set_trace()
		self._playerList.append(player)

	def remove(self, addressIp, addressClient):
		#ipdb.set_trace()
		for player in self._playerList :
			if player.addressIp == addressIp and player.addressClient :
				self._playerList.remove(player)

	def getPlayerByAddress(self, ip, clientNumber):
		if len(self._playerList) > 0:
			for player in self._playerList :
				if(player.addressIp == ip and player.addressClient == clientNumber) :
					return player
		return None

	def getPlayerList(self):
		return self._playerList

	def getClients(self):
		clientList = []
		#ipdb.set_trace()
		for player in self._playerList :
			clientList.append(player.client)
		return clientList

	def getObjects(self):
		return self._gameProcessing.objectList

	def getJsonObjects(self):
		objList = []
		for obj in self._gameProcessing.objectList:
			objList.append(obj.getJsonObject())
		return unicode(json.dumps(objList))