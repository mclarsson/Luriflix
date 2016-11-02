
""" Module with interfaces. """

from terminaltables import AsciiTable

class TextUI:
	""" Terminal UI for application. Mainly for development """

	def __init__(self, lfx):

		# Main operation loop
		while True:

			command = raw_input(' >> ').split()
			
			operation = command[0]
			arguments = command[1:]

			if operation == "upd":
				# Update applications list of files
				
				lfx.update()

			elif operation == "ls":
				# Show list of application files
				
				files = lfx.files
				table_data = [['File']] # first list in table is headers

				for file in files:
					row = []
					row.append(file)
					table_data.append(row)


				table = AsciiTable(table_data)
				print table.table