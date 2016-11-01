
class CLI:
	""" Terminal UI for application.
	"""

	def __init__(self, lfx):

		self.luriflix = lfx

		# Main operation loop
		print("Luriflix -- type h or help for help")
		while True:
			command = raw_input(' >> ').split()
			
			operation = command[0]
			arguments = command[1:]

			if operation in ["s", "scan"]:
				files = lfx.scan(arguments)
				print(files)
				
			elif operation in ["h", "help"]:
				print("Scan:")
				print("[scan, s] [suffix] [suffix] ...")