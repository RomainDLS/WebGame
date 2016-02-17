from SimpleWebSocketServer2 import WebSocket, SimpleWebSocketServer2
from GameBuilder import Player, Game
import ipdb, time
import sys

game = Game()


class SimpleConnexion(WebSocket):
    def handleMessage(self):
        #ipdb.set_trace()
        address = self.address
        player = game.getPlayerByAddress(address[0],address[1])
        message = self.data.encode('ascii', 'replace').split('//')
        player.receivedData = True
        if message[0] == 'angle' :
          player.angle = message[1]
        if message[0] == 'connected' :
          print self.address, 'connection client'

    def handleConnected(self):
       #ipdb.set_trace()
       newPlayer = Player(self)
       game.append(newPlayer)
       print self.address, 'connection server'

    def handleClose(self):
       #ipdb.set_trace()
       address = self.address
       game.remove(address[0],address[1])
       print self.address, 'closed'

def playersAllReceivedData():
   #ipdb.set_trace()
   if game.getPlayerList() == [] :
      return True
   for player in game.getPlayerList() :
      if player.receivedData is False :
         return True
   for player in game.getPlayerList():
      player.receivedData = False
   return False

def serverStep(server, stepNumber):
   timeStep = time.time()
   while playersAllReceivedData() :
      server.serveforever()
   game.step()

   clients = game.getClients()
   players = game.getPlayerList()

   for client in clients:
      client.sendMessage(game.getJsonObjects())
   return time.time() - timeStep


server = SimpleWebSocketServer2('', 5627, SimpleConnexion)
iteration = 0
#ipdb.set_trace()
while 1 :
   frameTime = serverStep(server, iteration)
   iteration += 1
   if iteration % 100 == 0 :
      print frameTime