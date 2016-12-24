#Author: Abheek Gulati
#For: NJIT class CS 656

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	print "recieved message: ", data
	data = data.upper()
	print "addr: ", addr
	print "data: ", data
	sock.sendto(data, addr)
