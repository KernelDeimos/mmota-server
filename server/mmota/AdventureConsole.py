class AdventureConsole:
	def __init__(self, req):
		self.req = req

	async def run(self):
		while self.req.check_active():
			data = ""
			try:
				data = await self.req.wait_input()
			except:
				print("Listener is dead")
				return
			output = ''.join(data + "... " for x in range(5))
			self.req.send(output)
