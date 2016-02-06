from SimpleWebSocketServer2 import WebSocket, SimpleWebSocketServer2
import ipdb


clients = []
class SimpleConnexion(WebSocket):

    def handleMessage(self):
        ipdb.set_trace()
        for client in clients:
          if client != self:
            client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
       print self.address, 'connected'
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       ipdb.set_trace()
       clients.remove(self)
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

server = SimpleWebSocketServer2('', 5627, SimpleConnexion)
iteration = 0
while 1 :
   ipdb.set_trace()
   iteration += 1
   server.serveforever()
   if(iteration%10==0):
      for client in clients:
          print client.address
          print client.data.decode("utf-8")
   