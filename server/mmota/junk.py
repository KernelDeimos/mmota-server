#!/usr/bin/python2

class TestConsole:
	def __init__(self, comm):
		self.comm = comm
	def run(self):
		while True:
			# Echo the back to the client
			data = await self.comm.wait_input()
			cur_thread = threading.currentThread()
			response = '%s: %s' % (cur_thread.getName(), data)

			try:
				await self.comm.send(response)
			except:
				print(cur_thread.getName() + " is offline.")
				break

			if ('%s' % data) == "exit":
				print(cur_thread.getName() + " quit.")
				break

			time.sleep(0.1)
