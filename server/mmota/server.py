#!/usr/bin/python3
import asyncio
import websockets
import time

import threading

# from .junk import TestConsole

# class ClientCommunicator:
# 	def __init__(self, socket):
# 		self.socket = socket
# 	async def wait_input(self):
# 		websocket = self.socket
# 		print("< {}".format(data))
# 		data = await websocket.recv()
# 		return data
# 	async def send_input(self, data):
# 		print("> {}".format(data))
# 		self.socket.send(data)

class WebsocketRequest:
	def __init__(self, websocket):
		self.websocket = websocket
		messages = []

	async def handle_oputs(self):
		while True:
			print("sending...")
			await self.websocket.send("Hello")
			print("> {}".format("Hello"))
			time.sleep(10)

	async def handle_iputs(self):
		while True:
			try:
				print("receiving...")
				data = await self.websocket.recv()
				print("< {}".format(data))
				# self.messages.append(data)
			except:
				print("Listener is dead")

	async def run(self):

		loop = asyncio.new_event_loop()

		asyncio.set_event_loop(loop)
		asyncio.ensure_future(self.handle_iputs())
		asyncio.ensure_future(self.handle_oputs())
		
		loop.run_forever()
		# cc = ClientCommunicator(websocket)
		# tc = TestConsole(cc)
		# tc.run()
		# while True:
		# 	data = await websocket.recv()
		# 	messages.append(data)
		# 	print("< {}".format(name))

		# 	greeting = ''.join(name + "... " for x in range(5))
		# 	await websocket.send(greeting)
		# 	print("> {}".format(greeting))

		# 	time.sleep(0.1)

class WebsocketServer:
	def __init__(self, address):
		self.ip = address[0]
		self.port = address[1]


	async def hello(self, websocket, path):
		req = WebsocketRequest(websocket)
		await req.run()
		# while True:
		# 	name = await websocket.recv()
		# 	print("< {}".format(name))

		# 	greeting = ''.join(name + "... " for x in range(5))
		# 	await websocket.send(greeting)
		# 	print("> {}".format(greeting))

		# 	time.sleep(0.1)

	def run(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)

		start_server = websockets.serve(self.hello, self.ip, self.port)

		asyncio.get_event_loop().run_until_complete(start_server)
		asyncio.get_event_loop().run_forever()
