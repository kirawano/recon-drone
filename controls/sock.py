import socket
import json
from motor import arcade

UDP_IP = "0.0.0.0"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	try:
		message = json.loads(data.decode())
		d = [-message.get("l", 0), -message.get("r", 0)]
		arcade(d)
	except json.JSONDecodeError:
		print("received malformed packet")

sock.close()
