
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

			if operation == "q":
				# Exit program

				return None

			elif operation == "upd":
				# Update applications list of files
				
				lfx.update()

			elif operation == "ls":
				# Show list of application files
				
				if len(lfx.files) > 0:
					table_data = [lfx.files[0].property_titles] # first list in table is headers
					for file in lfx.files:
						row = [file.properties['File'], file.properties['Title']]
						table_data.append(row)

					table = AsciiTable(table_data)
					print table.table

				else:
					print("No files registered, enter upd to update")

			elif operation == "s":
				# Save
				
				lfx.save()