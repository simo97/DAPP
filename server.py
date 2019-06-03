HOST = '10.42.0.1'
PORT = 4002


import sys, socket, threading


class ThreadClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connection = conn

	def run(self):
		nom = self.getName()
		while 1:
			msgClient = self.connection.recv(1024).decode('Utf-8')
			print(msgClient)
			if not msgClient or msgClient.upper() == "FIN":
				break
			message = msgClient

			# resend a tout le monde
			for key in conn_client:
				if key != nom:
					conn_client[key].send(message.encode('Utf-8'))

		self.connection.close()
		del conn_client[nom]
		print('client {} deconnecter'.format(nom))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.bind((HOST, PORT))
except socket.error:
	print('la connection socket a lddresse choisie a echoue')
	sys.exit()

print('serveur pret')
sock.listen(5)


conn_client = {}
while 1:
	connexion, adresse = sock.accept()

	th = ThreadClient(connexion)
	th.start()

	it = th.getName()
	conn_client[it] = connexion
	print('client {} connecter, adress IP {} et port {}'.format(it, it[0], it[1]))

	msg = 'envoyer vos messages'
	connexion.send(msg.encode('Utf-8'))