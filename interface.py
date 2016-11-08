
""" Module with interfaces. """

from terminaltables import AsciiTable
from Tkinter import *

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
				self.print_list(self.current_list, list(lfx.titles)) # Duplicate titles with list()

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

			index = 1
			for file in files:
				row = [index]
				for title in titles[1:]:
					if title in file.attributes:
						row.append(file.attributes[title])
					else:
						row.append("")

				table_data.append(row)
				index += 1

			table = AsciiTable(table_data)
			print table.table

class GUI:
	def __init__(self, lfx):

		self.lfx = lfx

		# List of all files
		self.complete_list = lfx.files

		# List of files found through search
		self.filtered_list = []

		# Currently active list of files
		self.current_list = self.complete_list

		# GUI stuff
		self.top = Tk()
		self.top.minsize(width=500, height=500)
		self.top.grid_columnconfigure(0, weight=1)
		self.top.grid_rowconfigure(1, weight=1)

		self.search_field = Entry(self.top, bd =5)
		self.search_field.grid(column=0, row=0, sticky='we', columnspan = 2)
		self.search_field.bind("<Key>", self.search_key_down)

		self.file_list = Listbox(self.top)
		self.list_files()
		self.file_list.grid(column=0, row=1, sticky='wesn')

		self.scrollbar = Scrollbar(self.top, command=self.file_list.yview)
		self.scrollbar.config(command=self.file_list.yview)
		self.file_list.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.grid(column=1, row=1, sticky='sn')

		self.top.mainloop()

	def search_key_down(self, key):
		value = self.search_field.get() + key.char
		self.filtered_list = self.lfx.filter(value.split())
		if len(self.filtered_list) == 0:
			self.current_list = self.complete_list
		else:
			self.current_list = self.filtered_list

		self.list_files()

	def list_files(self):
		# List of files
		self.file_list.delete(0, END)
		for file in self.current_list:
			self.file_list.insert(END, file.attributes['Title'])
