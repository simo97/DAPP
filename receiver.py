import socket

UDP_PORT = 5005
UDP_IP = '127.0.0.1'

print('ready to receive')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	print("receve a message" + data)
