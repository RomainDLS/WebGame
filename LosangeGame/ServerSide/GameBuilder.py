#!/usr/bin/env python
#-*- coding: utf-8 -*

import ipdb, time, json
import physicalEngine2D as p
from Player import Player
import random


class Game:
	def __init__(self):
		self._playerList = []
		self._playerId = 0
		self._spawnPoints = []
		# self._spawnPoints.append((50,50))
		self._spawnPoints.append((100,215))
		# self._spawnPoints.append((200,200))
		self._gameProcessing = p.Engine(2000,1200, self.CollisionHandler)
		rectangle = self._gameProcessing.addNewObject("rectangle",False,p.Rectangle(50,50,100,100),None,"rectangle")
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
		self._setPlayerVelocity()
		self._gameProcessing.engineStep()
		return time.time() - timeStep

	def _setPlayerVelocity(self):
		for player in self._playerList:
			idPlayer = player.id
			if player.isGlobalView is False :
				playerObject = self._gameProcessing.getObjectbyId(idPlayer)
				# Calcul velocity to apply to shape
				# velocityToApply = playerObject.shape.angle - player.angle 
				# playerObject.velocity = velocityToApply
				playerObject.shape.angle = player.angle

	def append(self, player):
		# ipdb.set_trace()
		self._playerId += 1
		player.id = self._playerId
		playerShape = p.Shape([(30, 0), (60, 50), (30, 100), (0, 50)])
		spawnPoint = random.choice(self._spawnPoints)
		playerShape.setPosition(spawnPoint[0], spawnPoint[1])
		self._gameProcessing.addNewObject("player%d" % int(float(player.id)), False, playerShape, player.id, "Player")
		self._playerList.append(player)

	def remove(self, addressIp, addressClient):
		#ipdb.set_trace()
		for player in self._playerList :
			if player.addressIp == addressIp and player.addressClient :
				self._gameProcessing.deleteObject(player.id)
				self._playerList.remove(player)

	def getPlayerByAddress(self, ip, clientNumber):
		if len(self._playerList) > 0:
			for player in self._playerList :
				if(player.addressIp == ip and player.addressClient == clientNumber) :
					return player
		return None


	def getPlayerById(self, playerId):
		for player in self._playerList :
			if player.id == playerId :
				return player

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

		if player.isGlobalView is False : 
			playerInfo = {}
			playerInfo['positionX'] =  self._gameProcessing.getObjectbyId(player.id).shape.x
			playerInfo['positionY'] =  self._gameProcessing.getObjectbyId(player.id).shape.y
			objList.append(playerInfo)
		
		for obj in self._gameProcessing.objectList:
			if obj.id == player.id and player.isGlobalView is False :
				stepX = obj.shape.getCentroid()[0] - player.screenSizeX/2
				stepY = obj.shape.getCentroid()[1] - player.screenSizeY/2
				objList.append(obj.getJsonObject(stepX,stepY, player))
		for obj in self._gameProcessing.objectList:
			if obj.id != player.id :
				objList.append(obj.getJsonObject(stepX,stepY))

		return unicode(json.dumps(objList))

	def CollisionHandler(self, object1, object2):
		if object1.type == 'Player' :
			player = self.getPlayerById(object1.id)
			player.statut = "dead"
		if object2.type == 'Player' :
			player = self.getPlayerById(object2.id)
			player.statut = "dead"
