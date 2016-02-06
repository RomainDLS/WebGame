from SimpleWebSocketServer2 import WebSocket, SimpleWebSocketServer2
import ipdb, time
import sys

clients = []
addressTmp = []
dataTmp = []
message = ''

class SimpleConnexion(WebSocket):
    def handleMessage(self):
        addressTmp.append(self.address)
        dataTmp.append(self.data.encode('ascii', 'replace'))
        message = "Address: %s - %d, Message: %s" % (self.address[0], self.address[1],dataTmp)
        print(message)
        ipdb.set_trace()

    def handleConnected(self):
       print self.address, 'connected'
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

def serverStep(server):
   timeStep = time.time()
   server.serveforever()
   ipdb.set_trace()
   print "ServerStep %s" % message
   for client in clients:
      #ipdb.set_trace()
      if len(addressTmp) > 0:
         if(client.address[1] == addressTmp[0][1]):
            if(len(dataTmp) > 0):
               client.data = dataTmp[0]
               dataTmp.remove(dataTmp[0])
            addressTmp.remove(addressTmp[0])
   return time.time() - timeStep


server = SimpleWebSocketServer2('', 5627, SimpleConnexion)
iteration = 0
#ipdb.set_trace()
while 1 :
   serverStep(server)
   iteration += 1
   if(iteration%10==0):
      for client in clients:
          if client.data != "":
             print client.address
             print client.data.decode("utf-8")