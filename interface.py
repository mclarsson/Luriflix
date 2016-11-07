
""" Module with interfaces. """

from terminaltables import AsciiTable

class TextUI:
	""" Terminal UI for application. Mainly for development """

	def __init__(self, lfx):

		# List of all files
		self.complete_list = lfx.files

		# List of files found through search
		self.filtered_list = []

		# Currently active list of files
		self.current_list = self.complete_list

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
				self.print_list(self.current_list, lfx.titles)

			elif operation == "save":
				# Save
				lfx.save()

			elif operation == "scan":
				# Scan directory 
				lfx.scan(arguments[0])
				self.complete_list = lfx.files

			elif operation == "edit":
				# Edits property of file (example: edit 1 Title Lord Of The Rings)
				index = int(arguments[0]) - 1
				attr = arguments[1]
				value = " ".join(arguments[2:])
				lfx.files[index].attributes[attr] = value

			elif operation == "play":
				# Open movie
				index = int(arguments[0]) - 1
				file = self.current_list[index].attributes['Source'] + "\\" + self.current_list[index].attributes['File']
				lfx.run(file)

			elif operation == "search":
				self.filtered_list = lfx.filter(arguments)
				self.current_list = self.filtered_list
				self.print_list(self.current_list, lfx.titles)

			elif operation == "csearch":
				# Cancel search and reset list
				self.current_list = self.complete_list
				

	def print_list(self, files, titles):

		if len(files) > 0:

			titles.insert(0, '#')
			table_data = [titles] # first list in table is headers

			a = 1
			for file in files:
				row = [a]
				for title in titles[1:]:
					if title in file.attributes:
						row.append(file.attributes[title])
					else:
						row.append("")

				table_data.append(row)
				a += 1

			table = AsciiTable(table_data)
			print table.table


