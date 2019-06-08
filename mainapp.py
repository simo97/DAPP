#!/usr/bin/python3

"""
Launch the main program and listen to incomming info and start a thread to send info

steps:
1- create a voting
2- register for voting
3- send vte
4- send the result
"""

import random
import socket, sys

from storage import Storage
from netservices import OutingService, InboundingService
from models import Voting


UDP_IP = "10.42.0.1"
UDP_PORT = 4002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
	
	try:
		sock.connect((UDP_IP, UDP_PORT))
	except Exception as e:
		print('la connexion a echouer')
		sys.exit()
	print("------------- ME = :" + Storage.NAME)
	# start a thread to listen the network here
	outBService = OutingService(sock)
	voting = Voting()

	voting.setName(str(random.randint(0, 20)))
	voting.setSender(Storage.NAME)
	voting.setOptions(list("apple", "banana", "cofee"))
	voting.setDefaultTime()

	outBService.create(voting)

	ibService = InboundingService(sock)
	ibService.start() # launch the thread here


if __name__ == '__main__':
	main()