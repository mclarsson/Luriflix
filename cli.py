
class CLI:
	""" Terminal UI for application.
	"""

	def __init__(self):

		# Main operation loop
		while True:
			command = raw_input(' >> ')
			print(command)