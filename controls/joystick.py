import pygame
import socket
import json
from time import sleep

pygame.init()

pygame.joystick.init()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PI_IP = "192.168.0.24"
PORT = 5000


j = pygame.joystick.Joystick(0)
j.init()
while True:
	pygame.event.pump()
	d = [j.get_axis(1), j.get_axis(3)]
	print(d)
	data = json.dumps({"l": d[0], "y": d[1]}).encode()
	sock.sendto(data, (PI_IP, PORT))
	sleep(0.05)

j.quit()
pygame.joystick.quit()
pygame.quit()
