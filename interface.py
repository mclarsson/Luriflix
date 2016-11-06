
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

			elif operation == "ls":
				# Show list of application files
				if len(lfx.files) > 0:
					titles = lfx.property_titles
					if titles[0] != '#':
						titles.insert(0, '#')
					table_data = [titles] # first list in table is headers
					a = 1
					for file in lfx.files:
						row = [a]
						for title in titles[1:]:
							if title in file.properties:
								row.append(file.properties[title])
							else:
								row.append("")

						table_data.append(row)
						a += 1

					table = AsciiTable(table_data)
					print table.table
				else:
					print("No files registered")

			elif operation == "save":
				# Save
				lfx.save()

			elif operation == "scan":
				# Scan directory 
				lfx.scan(arguments[0])

			elif operation == "edit":
				# Edits property of file (example: edit 1 Title Lord Of The Rings)
				index = int(arguments[0]) - 1
				attr = arguments[1]
				value = " ".join(arguments[2:])
				lfx.files[index].properties[attr] = value

			elif operation == "play":
				# Open movie
				index = int(arguments[0]) - 1
				file = lfx.files[index].properties['Source'] + "\\" + lfx.files[index].properties['File']
				lfx.run(file)
				
			elif operation == "sv":
				# Save
				lfx.save()

			elif operation == "sc":
				# Scan directory 
				lfx.scan(arguments[0])
