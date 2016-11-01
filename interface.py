
""" Module with interfaces. """

class TextUI:
	""" Terminal UI for application. Mainly for development
	"""

	def __init__(self, lfx):

		# Main operation loop
		while True:

			command = raw_input(' >> ').split()
			
			operation = command[0]
			arguments = command[1:]

			if operation == "upd":
				lfx.update()
			elif operation == "ls":
				files = lfx.files
				for file in files:
					print(file)