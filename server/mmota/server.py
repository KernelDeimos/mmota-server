#!/usr/bin/python3
import asyncio
import websockets
import time

import threading

from .AdventureConsole import AdventureConsole

class WebsocketRequest:
	def __init__(self, websocket):
		self.websocket = websocket
		self.active = True

		# Store input messages from user
		self.inputs   = []
		# Queue output messages here
		self.messages = []

		# Input checking interval
		self.inputChkI = 1000 / 20.0 # 20 Hz
		# Output queue interval
		self.ouputChkI = 1000 / 20.0 # 20 Hz

	def check_active(self):
		return self.active

	async def wait_input(self):
		print("Waiting...")
		try:
			data = await self.websocket.recv()
			print("< {}".format(data))
			return data
		except:
			print("Listener is dead")
			return None

	async def send(self, out):
		await self.websocket.send(out)

	async def run_adventure_console(self):
		print("Running adventure console...")
		cons = AdventureConsole(self)
		await cons.run()

	async def run(self):

		loop = asyncio.new_event_loop()

		asyncio.set_event_loop(loop)
		asyncio.ensure_future(self.run_adventure_console())
		
		loop.run_forever()

class WebsocketServer:
	def __init__(self, address):
		self.ip = address[0]
		self.port = address[1]


	async def hello(self, websocket, path):
		req = WebsocketRequest(websocket)
		await req.run()

	def run(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)

		start_server = websockets.serve(self.hello, self.ip, self.port)

		asyncio.get_event_loop().run_until_complete(start_server)
		asyncio.get_event_loop().run_forever()
