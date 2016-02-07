import ipdb

class Player:
	def __init__(self, client):
		self._addressIp = client.address[0]
		self._addressClient = client.address[1]
		self._client = client 
		self._angle = 0

	def angle(self, angle):
		self._angle = angle

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

	def angle():
	    doc = "The angle property."
	    def fget(self):
	        return self._angle
	    def fset(self, value):
	        self._angle = value
	    def fdel(self):
	        del self._angle
	    return locals()
	angle = property(**angle())

class Game:
	def __init__(self):
		self._playerList = []

	def append(self, player):
		self._playerList.append(player)

	def remove(self, player):
		self._playerList.remove(player)

	def getPlayerByAddress(self, ip, clientNumber):
		if len(self._playerList) > 0:
			for player in self._playerList :
				if(player.addressIp == ip and player.addressClient == clientNumber) :
					return player
		return None

	def getPlayerList(self):
		return self._playerList