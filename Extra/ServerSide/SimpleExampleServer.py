from SimpleWebSocketServer2 import WebSocket, SimpleWebSocketServer2
import pdb


clients = []
class SimpleChat(WebSocket):

    def handleMessage(self):
        pdb.set_trace()
        for client in clients:
          if client != self:
            client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
       print self.address, 'connected'
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       pdb.set_trace()
       clients.remove(self)
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

server = SimpleWebSocketServer2('', 5627, SimpleChat)
while 1 :
	server.serveforever()
