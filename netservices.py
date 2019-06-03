#!/usr/bin/python3

"""
what we need to do: launch 2 services (thread) one to listen the network and other one to 
send data over it
"""

import threading
import time
import socket
import random
import sys


UDP_IP = "10.42.0.1"
UDP_PORT = 4002
MESSAGE = "Hello, world!"


class OutingService(threading.Thread):
	"""
	responsible of sending data on the network
	"""
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.threadId = random.randint(0, 10)
		self.connexion = conn

	def register(self):
		pass

	def result(self, result):
		pass

	def run(self):
		"""
		read a text on the console and send it to the network
		"""
		while 1:
			message = input('votre message ici svp: ')
			self.connexion.send(message.encode('Utf-8'))


class InboundingService(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.threadId = random.randint(0, 10)
		self.connexion = conn

	def run(self):
		while True:
			message_recu = self.connexion.recv(1024).decode('Utf-8')
			
			print("Message recu " + message_recu)
			if not message_recu or message_recu.upper() == "FIN":
				break
		inboundngService.stop()
		print('inboudservice stopped')
		self.connexion.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.connect((UDP_IP, UDP_PORT))
except Exception as e:
	print('la connexion a echouer')
	sys.exit()

print('program launched')

outboundService = OutingService(sock)
inboundngService = InboundingService(sock)

outboundService.start()
inboundngService.start()