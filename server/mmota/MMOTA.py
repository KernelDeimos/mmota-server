#!/usr/bin/python3

from .server import WebsocketServer

class MMOTA:
	def __init__(self):
		print("test")
	def main(self):
		import socket
		import threading
		import time

		address = ('localhost', 26231)
		server = WebsocketServer(address)
		
		t = threading.Thread(target=server.run)
		t.setDaemon(True) # don't hang on exit
		t.start()
		print('Server loop running in thread: ' + str(t.getName()))

		input()
