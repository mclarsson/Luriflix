
class CLI:
	""" Terminal UI for application.
	"""

	def __init__(self, lfx):

		self.luriflix = lfx

		# Main operation loop
		while True:
			command = raw_input(' >> ').split()
			
			operation = command[0]
			arguments = command[1:]

			if operation == "scan":
				lfx.scan(arguments)
