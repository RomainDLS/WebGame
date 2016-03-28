#!/usr/bin/env python
#-*- coding: utf-8 -*

import ipdb, time, json
import physicalEngine2D as p
from Player import Player
import random


class Game:
	def __init__(self):
		self._playerList = []
		self._spawnPoints = [(215,100),(100,215)]
		# self._spawnPoints = [(200,200)]
		self._gameProcessing = p.Engine(2000,1200)
		rectangle = self._gameProcessing.addNewObject("rectangle",False,p.Rectangle(50,50,100,100))
		rectangle.velocity = -1
		#circle = self._gameProcessing.addNewObject("circle",False, p.Ellipse(100, 100, 10, 1, 2, 0))
		# cShape = [(110, 100), (103, 119), (92, 112), (92, 88), (103, 81), (109, 92)]
		# cObj = self._gameProcessing.addNewObject("mistyc", False, p.Shape(cShape))
		# cObj.velocity = 1
		#ipdb.set_trace()

	def setPlayerToGlobalView(self, playerAddress):
		# ipdb.set_trace(frame=None)
		player = self.getPlayerByAddress(playerAddress[0], playerAddress[1])
		player.isGlobalView = True
		self._gameProcessing.deleteObjectById(playerAddress[1])
		del player

	def getClientInfo(self, clientId):
		clientInfo = {}
		clientInfo['type'] = 'clientInfo'
		clientInfo['clientId'] = clientId
		clientInfo['mapX'] = self._gameProcessing.map.sizeX
		clientInfo['mapY'] = self._gameProcessing.map.sizeY
		return clientInfo

	def step(self):
		# ipdb.set_trace(frame=None)
		timeStep = time.time()
		for player in self._playerList:
			idPlayer = player._addressClient
			if player.isGlobalView is False :
				self._gameProcessing.getObjectbyId(idPlayer).angle(player.angle)
		self._gameProcessing.engineStep()
		return time.time() - timeStep	

	def append(self, player):
		# ipdb.set_trace()
		playerShape = p.Shape([(30, 0), (60, 50), (30, 100), (0, 50)])
		spawnPoint = random.choice(self._spawnPoints)
		playerShape.setPosition(spawnPoint[0], spawnPoint[1])
		self._gameProcessing.addNewObject("player%d" % int(float(player.addressClient)), False, playerShape, player.addressClient)
		self._playerList.append(player)

	def remove(self, addressIp, addressClient):
		#ipdb.set_trace()
		for player in self._playerList :
			if player.addressIp == addressIp and player.addressClient :
				self._gameProcessing.deleteObject(player.addressClient)
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

	def getJsonObjects(self, playerAddress):
		player = self.getPlayerByAddress(playerAddress[0], playerAddress[1])
		stepX = 0
		stepY = 0

		objList = []
		# ipdb.set_trace(frame=None)

		if player.isGlobalView is False : 
			playerInfo = {}
			playerInfo['positionX'] =  self._gameProcessing.getObjectbyId(playerAddress[1]).shape.x
			playerInfo['positionY'] =  self._gameProcessing.getObjectbyId(playerAddress[1]).shape.y
			objList.append(playerInfo)
		
		for obj in self._gameProcessing.objectList:
			if obj.id == playerAddress[1] and player.isGlobalView is False :
				stepX = obj.shape.getCentroid()[0] - player.screenSizeX/2
				stepY = obj.shape.getCentroid()[1] - player.screenSizeY/2
				# objList.append(obj.getJsonObject(stepX,stepY))
		for obj in self._gameProcessing.objectList:
			if obj.id != playerAddress[1] :
				objList.append(obj.getJsonObject(stepX,stepY))

		return unicode(json.dumps(objList))