#!/usr/bin/env python
#-*- coding: utf-8 -*

from SimpleWebSocketServer2 import WebSocket, SimpleWebSocketServer2
from GameBuilder import Player, Game
import ipdb, time, json
import sys
import signal

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

servermaxwait = {}
SERVERMAXWAIT= 0.015
servermaxwait[0] = SERVERMAXWAIT
servermaxwaitafterconnexion = 1
# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)
game = Game()


class SimpleConnexion(WebSocket):
    def handleMessage(self):
        #ipdb.set_trace()
        address = self.address
        player = game.getPlayerByAddress(address[0],address[1])
        message = self.data.encode('ascii', 'replace').split('//')
        player.receivedData = True
        if message[0] == 'angle' : 
          #ipdb.set_trace(frame=None)
          player.angle = message[1]
        if message[0] == 'connected' :
          print self.address, 'connection client'
        if message[0] == 'globalView' :
          player.isGlobalView = True
          #ipdb.set_trace(frame=None)
          #player.client.sendMessage(unicode(json.dumps(game.getMapSize())))
          #print 'globalView'       

    def handleConnected(self):
       #ipdb.set_trace()
       servermaxwait[0] = servermaxwaitafterconnexion
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
      #signal.setitimer(signal.ITIMER_REAL,servermaxwait[0])
      try: 
         server.serveforever()
         #print 'forever'
      except TimeoutException:
         #print 'serverstep is waiting for too long... servermaxwait :', servermaxwait
         continue # continue the for loop if function A takes more than 5 second
      else :
         signal.alarm(0)
   if servermaxwait[0] == servermaxwaitafterconnexion :
      servermaxwait[0] = SERVERMAXWAIT
   game.step()

   clients = game.getClients()
   players = game.getPlayerList()

   for client in clients:
      client.sendMessage(game.getJsonObjects())
   return time.time() - timeStep


server = SimpleWebSocketServer2('', 5627, SimpleConnexion)
iteration = 0
framesTime = 0
#ipdb.set_trace()
while 1 :
   frameTime = serverStep(server, iteration)
   framesTime += frameTime
   iteration += 1
   #print '-',frameTime
   if iteration % 250 == 0 :
      t = framesTime/250
      print ' average fps = ', (1/t)
      framesTime = 0