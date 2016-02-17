from SimpleWebSocketServer2 import WebSocket, SimpleWebSocketServer2
from GameBuilder import Player, Game
import ipdb, time
import sys

clients = []
addressTmp = []
dataTmp = []
message = ''
game = Game()


class SimpleConnexion(WebSocket):
    def handleMessage(self):
        ipdb.set_trace()
        address = self.address
        player = game.getPlayerByAddress(address[0],address[1])
        message = self.data.encode('ascii', 'replace').split('//')
        if message[0] == 'angle' :
          player.angle = message[1]
        if message[0] == 'connected' :
          print self.address, 'connected'

    def handleConnected(self):
       #ipdb.set_trace()
       newPlayer = Player(self)
       game.append(newPlayer)
       print self.address, 'connected'
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       game.remove(game.getPlayerByAddress(self.address))
       clients.remove(self)
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

def serverStep(server, stepNumber):
   timeStep = time.time()
   server.serveforever()
   #ipdb.set_trace()
   clients = game.getClients()
   print "ServerStep %s" % message
   if stepNumber % 30 == 0 :
     for client in clients:
        client.sendMessage(game.getObjects())
   return time.time() - timeStep


server = SimpleWebSocketServer2('', 5627, SimpleConnexion)
iteration = 0
#ipdb.set_trace()
while 1 :
   serverStep(server, iteration)
   iteration += 1